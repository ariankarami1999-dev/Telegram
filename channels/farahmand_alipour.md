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
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUD9wU7-hVaeg9IOUTIckMwFDkbt3kh5NfRMt1ENq_iAc9yY4l1FEKWlMNFWWrgtn3RfZAEMDh_H61Y-Enso851R5MvpXCcZhojogz6EFN3aq-OmaU5frwqwQmJ3oHl0SwTA-R_RrvfmX97OqCylYP-IaSFVtEiQjaZkfIsU7h3rkXQewqQ1Oi1bRVWREakvhd-Q4OcPiSqOoQha4Nv-ZlEBYgwNZVyDDpi8KQzvrxC5xMqsiP-24shU8Ib5XIKIypJZc9SNQo-o4cRJqiaz7D-WN9L7akJILv3KkN1euT8HWNz4cw9I-cWkV-gOCuQjZB8QEDH2XEu7T4dw1gaO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-efSmCELSIEbI1PRvIlWvGDBZJzOTGtA3m0Eb0MPLKTEYKxtvfkjCnJi0eV0uOAJGEobWTeI0vu9AAMpr-5-ot_7-UrUMWhgPDf3cEAOS8_vD4tCaZDhEPT3PkYJazOllt7CkmcjgYw0Y1tn1xOowcXfae9mLe0FystExkQv4yhkyQ3ZeK3hyN9eAe-uJUdjPn-vTkgEqhjB_-ip678nOUbKqkfiWqz5mqiO3qVhe0Hhdjj6_AiR77neLbDC6d0uOWrTz9pCtjxyj3V3pHW5jzU35FYH6ogxOLh01wcFhu5v4SErzicibNfxoh_zH5dLuq-5NMRNpMGvptT8kyo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpWKK1f6GSdx1XJYF6aT0hQmPwc12h1RS9u4c8-F-oCfckATc-AbLIo1g-1lSj1YbYnqLQn3NosFT-rtYTcQUqL6miPxg_TE-uxT6MEWOxB2wsgkMllbHGPHRduExqRsz-hkX63JKWvVHm_Jd2YeT_90fzVVIlGOftOKEkqBzj87KPPyBG2HeeEBE8xWv3nxIocGYAnzZQxHLbQkqL5bLxs8aZCHVczdFSCJW5-XiHv_6jABE7sNZiA2HA5ehl8xhy2MpR3a_S68Qt_4BNwkxdJnVOSsK7bGQZpavb6UFQaAOxWrFjo1rtVtjyuyN1bgQvhDGAAF9Rie3o6wx-5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPy2jJ5Cq7i9JUca9W2Xr1fXDWZnm_qIoV9W0XcfUcOObVB2riQYjUXFL1_ukLZD2bF2DISU8OjWylGuqXmvQsPSw1wNj4pqFoGrd6XrqLGOQHKYQeM4pxxLOTm6zHMyhe9wpgG_M0WbsCFufQ4uFk5g8M-hBIZSdsVmVsz7038XTlWrUGLlUs6RRkXuzI0lSF-tG7qplQqn2afoLn7tleil-Mi-lSeH9Q14-_SNApuUK6po_tzs4wiYFDYfWXaE04B99sETIjbXVz--rDM5xVEo2_3OxzeNPqZSDlNKhNNZKs7tpKnHHAfcYpoBaJDmHOV0iFt6CAra-1scFC8MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=tOJDyK6jPuOAfuEOB6JVPUVCQZ8-OlBJUexSOmWWqKR23wsX3qmtulijdWdjj-tMU9AE9KCXNEouqETx82qhUI56uEqLYq8FEV1BxTtk4xV8Wn0StBEUrb5xm9OEewXuT91H_OE2WOWTEq1SnlGpGMcoZYtRADdVx8nmCfzLJabUT210a0QkZ6xuvlCOoGZfOJQ-YhsHQLOs8vF8ZDPcbz9WSTGxxDXRyaZZyzbElDvgpdqK6i1x5ziC-iwsvUoA7uhrGj2SCkpIBxrmjwimcGmXkOn59DbsauYBpS6D30Y6ntfukI6jof3JxXWNnbP-kG4FofgCiHw1QK6nFI1-FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=tOJDyK6jPuOAfuEOB6JVPUVCQZ8-OlBJUexSOmWWqKR23wsX3qmtulijdWdjj-tMU9AE9KCXNEouqETx82qhUI56uEqLYq8FEV1BxTtk4xV8Wn0StBEUrb5xm9OEewXuT91H_OE2WOWTEq1SnlGpGMcoZYtRADdVx8nmCfzLJabUT210a0QkZ6xuvlCOoGZfOJQ-YhsHQLOs8vF8ZDPcbz9WSTGxxDXRyaZZyzbElDvgpdqK6i1x5ziC-iwsvUoA7uhrGj2SCkpIBxrmjwimcGmXkOn59DbsauYBpS6D30Y6ntfukI6jof3JxXWNnbP-kG4FofgCiHw1QK6nFI1-FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXjVESp0C-hGI8O2YE8KtDa2QYbVeB4c1p7LLnLHjGq95JrU0RGKc4OUkIPQvxHmGirf7Wx5C8yJB7hp0XWsxL3-07xEmQPowtHdQRqY1SVjJW8uU6zRY230KUDcJxkPWB-ihyX3ROiJl-qBZt4_VILvwp953RwwyrMHJQishGp0Wf8ZQW_6veLW-WFkZgVgFiGODR2YIehcXAHFRI1OfZPB79_utZ8lP3qeVzuCa-vPQ5Q8rVnnCklarZ7ba9LZbtyTn1mD9GUq5YPa5erHZiRwum5in1VZwxu0EpYJXx31AJYqNjXbXrl1Yc-deIuUAB205al-M_uOltXPcaenug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=Y-7KJrsas56OKx3iaEGmdaTBNO6cJsQ32yFxBwp0X5wtJG30bMlxfUQB-1-8TWO6BxijUj9_hpPpwHDIGs091x8WeQyI4JrY12PZmsqwZKxIrsJtigd9xHyFwS9fsbY1UJgygdRP2AwlFTBWWQAX48bv7N-SsvnTdAFJzllwMYpx8QgQ1qt_QF3BbbPDN95diJooCzYMIP-7ErSWfEa2b4CeY0lh77ET7P8YroGN8TxiDcxSKS2F9NxudIM92ehQ5Bf4k3iq1SQD99PQv49ILGXq5vqzcxPZbiKwWwp9HLa-WhjoVQz2Yj6d40xQ7H2YZO8yrGI5s7VReOM97WVmDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=Y-7KJrsas56OKx3iaEGmdaTBNO6cJsQ32yFxBwp0X5wtJG30bMlxfUQB-1-8TWO6BxijUj9_hpPpwHDIGs091x8WeQyI4JrY12PZmsqwZKxIrsJtigd9xHyFwS9fsbY1UJgygdRP2AwlFTBWWQAX48bv7N-SsvnTdAFJzllwMYpx8QgQ1qt_QF3BbbPDN95diJooCzYMIP-7ErSWfEa2b4CeY0lh77ET7P8YroGN8TxiDcxSKS2F9NxudIM92ehQ5Bf4k3iq1SQD99PQv49ILGXq5vqzcxPZbiKwWwp9HLa-WhjoVQz2Yj6d40xQ7H2YZO8yrGI5s7VReOM97WVmDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUx-emAn6iqBwKdg-oh1rnhRICrHIRTisRUxyQDMi7LYC3HK8CSvs0xGVmC5yfZ3qX7wUYvoNaxdPyHQM6ERc-NHtYDvl5PXHg3uH1ZPi29QseecQH6jnZRdc7Ejqf1_4DTSXLQ2TMuDp3zlgGUZ1NLhMuCuTeHGbaQx2RzhA2br71kE_3UmL789tgWBO8qtJvGsOPB94BAgL6J89hgRwMGYUVYsLbDURGH23reBM39txo4UDS7qXUBXspqm5CX5FMzeBnGdj9XoyCfagn26OtB7oT-llYv0ynGFn6Kw_hju993yGlFciNv9GVwL5LwV_JbdD_eUkENrxBDUEb5LTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=eGW4Z1oETN3FXLsXjmfxSD8rF9VPvD8M4L1gLOcAZO5WryODF2gFNgzRYtYcMsyL3FAAJxqPOzjFwANOb2ihAIqwScTWfOIWuldKnX1TxypU4gek2ig7niMSJsT9zgJIirxxT2NAmUNCETt7ox4l_d2qUte4gK6PsAMUf4tTBVoLkC0d0naingxgcRy491DH7PWXZVAAKRWziGe1_CuPAZkdWqXQYQsoG1ZFCphYCdyEUwqEA-Y41XUJfifpedUejNS6sQnZRQkf9ZVCV6QZJIUl3ot2C1xcxTXjvM4QGLAol970wXkdFX2x31uLQM9TtN1T_qf-vmdkybC31xFx5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=eGW4Z1oETN3FXLsXjmfxSD8rF9VPvD8M4L1gLOcAZO5WryODF2gFNgzRYtYcMsyL3FAAJxqPOzjFwANOb2ihAIqwScTWfOIWuldKnX1TxypU4gek2ig7niMSJsT9zgJIirxxT2NAmUNCETt7ox4l_d2qUte4gK6PsAMUf4tTBVoLkC0d0naingxgcRy491DH7PWXZVAAKRWziGe1_CuPAZkdWqXQYQsoG1ZFCphYCdyEUwqEA-Y41XUJfifpedUejNS6sQnZRQkf9ZVCV6QZJIUl3ot2C1xcxTXjvM4QGLAol970wXkdFX2x31uLQM9TtN1T_qf-vmdkybC31xFx5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqqR5bjsYGxw1tQE1elKRBEDz8LanK6vSZPfrAVUcBfUDo6QPHpXXhzEJGf3Pu5xhBZ7c0XPVnX445e6IhyycDESGadPYVOnzWywtSQr7PBEVa3ORvNk5R3mbUBhVYXVi9bE02sIJbRXxBFkZ54PRefyFA8xEEzkPvfXuyZp0duP5FWOmTAMtbH4VqiXmqNwzvKdYR57QdmpNsg7Gm_nzI5i410A3rV3-6h4Q3509z0aGxM4wZHGup4k5h8qID6gIbpe5etWICUK2OnVeajM5kTLPGKIBkAO0oEIYZm8zWnOmL9FSOht0-6yX5Kjt9Jdk9qc4WXq8OfAvHpfhxheCFEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqqR5bjsYGxw1tQE1elKRBEDz8LanK6vSZPfrAVUcBfUDo6QPHpXXhzEJGf3Pu5xhBZ7c0XPVnX445e6IhyycDESGadPYVOnzWywtSQr7PBEVa3ORvNk5R3mbUBhVYXVi9bE02sIJbRXxBFkZ54PRefyFA8xEEzkPvfXuyZp0duP5FWOmTAMtbH4VqiXmqNwzvKdYR57QdmpNsg7Gm_nzI5i410A3rV3-6h4Q3509z0aGxM4wZHGup4k5h8qID6gIbpe5etWICUK2OnVeajM5kTLPGKIBkAO0oEIYZm8zWnOmL9FSOht0-6yX5Kjt9Jdk9qc4WXq8OfAvHpfhxheCFEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKIf-At8eY-2tmPESmpAEudqUYePgX4b8GljkYAehkSppegehvTMZYkK1_GfpcQICpLb9wNtt1eRh6bhohxhu7qoa9gMqgfKk4fYewyip7gftkk8vISxZozib1CrbQfy8uXEjxoN08TlK4v_MlOF0yNkaK8YFEh5TCVdEQDCnDBM0yTtN07Jj4jAmpB3rC0J9OmQle98DHkM-4ELInHV9AwLh90l8k0SzYksvY1vzFv1_B_GeTwMvN3kVmAL5yD-oiv072I9xODaT86u9U--gzxch6XHLleJowy64MH1WejFZYt8uFlvPS5Dcd2rx8HUUcmu4_lt5F5imTaGRz0onw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=mYsRd6GOgSwFoCS_wFe-agarn5fIp_-kOuzEu7A9lJZfNaynEYdd7hWaAAUJ2Y_ppKPtenbmtDdaThypG1xSpKWsVOQY093OIIntMYl0Elohhk4QgRgrZydOBqj5PpkqddkN3T44QOob82hSx9ALjXD6pFp0zh2IsOXllAuCPdeWR2UyHKLBkPVLt-X7YsPDD7TRBMM4n4aZg6s6d1d14Pm9YcajLXteyZ6pSdrNLcZAlVwcyJMPB6h107tYSC15pqTMoCtUENnqvgjC3QIr2IprFqobnK9lzpUH5ir-dcvme8JfvWb0etE_0aaunLA7eUq2h_oQbLfqaid1x9Xugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=mYsRd6GOgSwFoCS_wFe-agarn5fIp_-kOuzEu7A9lJZfNaynEYdd7hWaAAUJ2Y_ppKPtenbmtDdaThypG1xSpKWsVOQY093OIIntMYl0Elohhk4QgRgrZydOBqj5PpkqddkN3T44QOob82hSx9ALjXD6pFp0zh2IsOXllAuCPdeWR2UyHKLBkPVLt-X7YsPDD7TRBMM4n4aZg6s6d1d14Pm9YcajLXteyZ6pSdrNLcZAlVwcyJMPB6h107tYSC15pqTMoCtUENnqvgjC3QIr2IprFqobnK9lzpUH5ir-dcvme8JfvWb0etE_0aaunLA7eUq2h_oQbLfqaid1x9Xugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=YLcT67zfWGLuAEZsDK4S63-YumKdUzJtvIsYf07FpJIZ02VuzvdO2_VSvF1gnybc74YDyYFqZigSL_fLpH9abXpfIU01lXOv9PGkomu1FuaQM5vOs4Qo8a_wcRJoZnzSgS4wRDBN5k7ix6D_tStfDlu39seGxCW0fkWhu4znvKHLQW4KltpXc1oA_v0GheyWA116HPCCPmoccJaCvd4pYx0FU57n8Ay5oTIed27SLup4ViuPSV9B7ekhTWq5sF2KnYGr24QexMyl77fEW5vCmvKPmADwx5BDRP5H0iubJRm03EMAgrDvpbL812Orrv6Ujme5MWraVVRfR3Q4JNQsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=YLcT67zfWGLuAEZsDK4S63-YumKdUzJtvIsYf07FpJIZ02VuzvdO2_VSvF1gnybc74YDyYFqZigSL_fLpH9abXpfIU01lXOv9PGkomu1FuaQM5vOs4Qo8a_wcRJoZnzSgS4wRDBN5k7ix6D_tStfDlu39seGxCW0fkWhu4znvKHLQW4KltpXc1oA_v0GheyWA116HPCCPmoccJaCvd4pYx0FU57n8Ay5oTIed27SLup4ViuPSV9B7ekhTWq5sF2KnYGr24QexMyl77fEW5vCmvKPmADwx5BDRP5H0iubJRm03EMAgrDvpbL812Orrv6Ujme5MWraVVRfR3Q4JNQsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj-cCi_9hfIlrG60HUz2rWcMaMwKT6A7FBAPki2aRZrpPEeKHr-xsY3b3S4TK01Hvk1_YZWJeijpQZombzhw5Tfe2fyY8vZ04a1bi2-6ulnqyO38fdrq-ao7XQZiLCsVFoHhqTmhxd_24b7b2rQ89maN0zTK9GVbkN3GUcWXeLALNeQkPAJ830bkS_Bbbgl8fYi2AIrbQa579OqoQfC6YmFsE1LHnv0oTOGqlC6yBf8uSKZpcsqUDlVFHJIVHPPbBuOTErmETgcFEptZQlIYctoKSFQJIyDZ_h-7tfoW8gVu2m00sEDYSeFIpvANBB86WXk47DBYOO9QAcfbYzbkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=GPAfgZG5kar-zPowiZYc2QqM4jnrwrZFxMS8aFf71bc_zsxHM3CyhI-_Wl1M18z5U_B7EIn7rGiJNQ8Ud_oy9Mzog-ro92KAk_O3BUKsc5lKq8biyayOPeg2vTPW5HYyP73dtXYji2eJ3yW255fr_YvfIrwEXpwjmVnmNO1I_Mm-fCMVEyn-XPgh1CB8xQ_6_JmSOrJ1TK9saYcECXGHoGTVmNtCOFUg26TOV3IS4bIh-I_IocrVoIv5bWju1MC9XqIf5aUUHBdn0bITHiZW_ScaGmjyiiwA_byJ2D86b6uie0xPbKRpMa90P-Pw61YQVztl1NYet3-OJtvsFHK1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=GPAfgZG5kar-zPowiZYc2QqM4jnrwrZFxMS8aFf71bc_zsxHM3CyhI-_Wl1M18z5U_B7EIn7rGiJNQ8Ud_oy9Mzog-ro92KAk_O3BUKsc5lKq8biyayOPeg2vTPW5HYyP73dtXYji2eJ3yW255fr_YvfIrwEXpwjmVnmNO1I_Mm-fCMVEyn-XPgh1CB8xQ_6_JmSOrJ1TK9saYcECXGHoGTVmNtCOFUg26TOV3IS4bIh-I_IocrVoIv5bWju1MC9XqIf5aUUHBdn0bITHiZW_ScaGmjyiiwA_byJ2D86b6uie0xPbKRpMa90P-Pw61YQVztl1NYet3-OJtvsFHK1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=anR1WHJ2xMr4breofkViPst_aEpKoX_8np9AYnUuh_cPhORec9XACW3k4OKB0g4X8THxYGFMTfekZnfKU9CbrJFAnOkKpRzCLRSMYIdrddk-S0sQgA2u-IoTx5Q4rThrf9YJAM3a_pHGZD-Q--oU3hN2x58VjS3m9awdMLvM7nobeBowaCdvof_URcqTbnJfXWL9oBcWozBUWb5xA2AAHqlLifWUOlfzlbztFD4pWqKsjXDJdrCY45kotlttePMa7symBsboQGr1opih9NGH5RE0JZXOvoAKjvbRP4HAOUKnEeArkzWGEuFZeRFrGFAoj2n02lHRoMpuT_c18GBL4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=anR1WHJ2xMr4breofkViPst_aEpKoX_8np9AYnUuh_cPhORec9XACW3k4OKB0g4X8THxYGFMTfekZnfKU9CbrJFAnOkKpRzCLRSMYIdrddk-S0sQgA2u-IoTx5Q4rThrf9YJAM3a_pHGZD-Q--oU3hN2x58VjS3m9awdMLvM7nobeBowaCdvof_URcqTbnJfXWL9oBcWozBUWb5xA2AAHqlLifWUOlfzlbztFD4pWqKsjXDJdrCY45kotlttePMa7symBsboQGr1opih9NGH5RE0JZXOvoAKjvbRP4HAOUKnEeArkzWGEuFZeRFrGFAoj2n02lHRoMpuT_c18GBL4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=Z8bwjepYkKEbo0QuL12UKQ5-BrCgys0ofRIRKan-wrgX8gzF_9_1lPhyjqTx8GIlRddOUMsHl00V8vp3-LenMNmulNEa5Q6dstMmUiUrONHlurHraOWIN3O0rNRuU7f0_hTLeopuN74_p6kE8RmY33lQKJV9sDpHZ-cWo56lRnOxpfVUbtCH35Ey1LaTj54tWZWl8jYE-lTOWpCn97lDRhUZ2M40fV8d1DE8ZcfEmZ-vFxJFTgQhVR66cWMyymAhiykHCFD4jljG8cB7rOzRPyCKg0lQ5Xw-7xLjgR_mxnYs633LAaXHZG5Db06UkDNfyY5aYQJyv2eIsc-EIUNdqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=Z8bwjepYkKEbo0QuL12UKQ5-BrCgys0ofRIRKan-wrgX8gzF_9_1lPhyjqTx8GIlRddOUMsHl00V8vp3-LenMNmulNEa5Q6dstMmUiUrONHlurHraOWIN3O0rNRuU7f0_hTLeopuN74_p6kE8RmY33lQKJV9sDpHZ-cWo56lRnOxpfVUbtCH35Ey1LaTj54tWZWl8jYE-lTOWpCn97lDRhUZ2M40fV8d1DE8ZcfEmZ-vFxJFTgQhVR66cWMyymAhiykHCFD4jljG8cB7rOzRPyCKg0lQ5Xw-7xLjgR_mxnYs633LAaXHZG5Db06UkDNfyY5aYQJyv2eIsc-EIUNdqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=RaUqyIHzcwp16FUIjZreqlGqI3rhCzh42EgmLmQjdWWQpkBSWrQq0qqAGDAkGPNgWv4cFCAB_1GoRS9jIKYd4K9f9AnZIylfZIGhTzp0SzoDKc_BDRCtSIMn4TWJ3u-OzaoFP3LsAPpf6miP2wrwqYgqcZHMTklyvfXHsCjtgQGtQsK3gQILsNfd8Q2770eRMi9UXq_jZ5qThHAL84RCDlaWkinMYCFpAs_9ace2Q_MvSC5pBb87nYiJE9j9QRcu8RBcNvZuw9J24DXeGNPFPd9QXtHigVZfnq1c6tKGnR-Olj6GnGth6J1UBPjsLlFvUxRBPW-L5dUFeoyG7fYMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=RaUqyIHzcwp16FUIjZreqlGqI3rhCzh42EgmLmQjdWWQpkBSWrQq0qqAGDAkGPNgWv4cFCAB_1GoRS9jIKYd4K9f9AnZIylfZIGhTzp0SzoDKc_BDRCtSIMn4TWJ3u-OzaoFP3LsAPpf6miP2wrwqYgqcZHMTklyvfXHsCjtgQGtQsK3gQILsNfd8Q2770eRMi9UXq_jZ5qThHAL84RCDlaWkinMYCFpAs_9ace2Q_MvSC5pBb87nYiJE9j9QRcu8RBcNvZuw9J24DXeGNPFPd9QXtHigVZfnq1c6tKGnR-Olj6GnGth6J1UBPjsLlFvUxRBPW-L5dUFeoyG7fYMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=r2EH6SNexzQdcwO3tGI1iiaua4qWkCoPOW077fYqb10cCXaZDxxJKX1SfSScMbdVTkMQPtxU_ukd_sJJlSV-8VgehDPpTEWHG_ucSC8UJYfl8TNUwZALPa7utsmfDbkrkkhQk9EktbsZ4bc2oHyYBKOMykjnteuB5poBT67Z0tmU8bo8kKGVtjdh7SNgoGSDN1osmszIB4r6FBpA7rg9MUi-Uc_SDKgg6gI_FpXvO5sksY6AY5b-YcJh8m0NnLZ2wZTeGe0GkBKccc27dwzZiFu0j2YmWlUKI3Q9rdrhkfluNIQM1YZys7iLQ7Yyd2gK2nZDTsx7TNw-yWScaY51XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=r2EH6SNexzQdcwO3tGI1iiaua4qWkCoPOW077fYqb10cCXaZDxxJKX1SfSScMbdVTkMQPtxU_ukd_sJJlSV-8VgehDPpTEWHG_ucSC8UJYfl8TNUwZALPa7utsmfDbkrkkhQk9EktbsZ4bc2oHyYBKOMykjnteuB5poBT67Z0tmU8bo8kKGVtjdh7SNgoGSDN1osmszIB4r6FBpA7rg9MUi-Uc_SDKgg6gI_FpXvO5sksY6AY5b-YcJh8m0NnLZ2wZTeGe0GkBKccc27dwzZiFu0j2YmWlUKI3Q9rdrhkfluNIQM1YZys7iLQ7Yyd2gK2nZDTsx7TNw-yWScaY51XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuayxNApshf0fjgjhU8x2J_uWIo38uMJd_J4LKOm9dTDfS9WcqFOYEDmYZ0jKwyUAcbK4EYrI1o1OIT_3EY3xxu77-qs7KBUPucCrqN7tz3mKJgyUY6_5Re97-9zmI9EdueKG3LD9EqNhDKgaafcWwnEEaqSkSvmmbAo0ETOdVO93R_mX6_-Fg5h-79i6bUqSkB2ZW4QUtgHJYLtnusQKGTvkrdbKdtdHAzXt1c2O41YDzVJ_uDaKqgk7Y15ZwpwWVcZl0WjZaZKgZdsTZ7fMs46BkvkkBI75zXbCxcymYQmrcyE7LFLOKebSodWV0d4CqC58V_88E1dcwKzdnVNAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg_fQ_hnMMupaOdgZvf_5CMLX3DRNFgOLei9jo3KPCeaNKTACmpk5h00kjxfxXzY2J_tQD2TKbr78K_xsb-0osiC2a5a9aUkeZvnoyM95VSs-m_VQfVpz0jhKBFngG5g-CB7vVOe6misnahBSO530WjNkmBtJdiJ4ZtdRNxqJ_cSS5a6Y2Ddkd6YybFD703KZAQDNqRzP7mvOBPZO6gsbPn775N0Lu_LPbHpoiciAntoZMVNJ0t9A9QF2YEA_BFmIFy5SxxsCDrcy-9FTA90I3quNfHpWd-ycnH4ZXaNG_pJrZAoQqRvUZY_B4CBUtT98QKsmzxtyfyyiWE1hN6EoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTGOKEeO9b3SNFTqJIbsnRZWyCntPjHlyqSRjN5jnKC3Bys5-3-CAN8U2hj373Bipj2AzD3ntBNEj9R_bZjuNd2hiuLJfU6g6EaID8lvIFt0wixAM03Oc84oS_N_IA9Bv_uxPveurDbfWi0DZKeYK9eJDz2MVluFqhAG8gdQEaJIZ-jas9-YcLve0WdMy895MzfRPmRa-NP6SnUzJTW70wmCH5-MTY2FrxjkKjDvv6iulrg195lwlsJSosCJv7wyZHMzBakuNryPTmX81qQ26VnDrt3Ah6yc0ngRFvoBd5KWDY1-xs4k4K-WLQdc3ImBvZNnIVyfoW-ikjzCpDTgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Yf-HpGKRyGQiHdZLJ0Zdyi0D9gvwNe9_mlUr_SNB8OdOi-FxYkiFR11T1UGg_PdqALH_TYy2e4l70VFvJtcSTKEeH_0lw_eJq5QTEJC8eekG--zb5EtM0NC24Lm-267bN9r8BXK4utE_NQ2_5rz_spGo-QXKS0a5aoJMGuKFJWs8_GUycgU8NyCmnwsbkWBxlbpIpoGYxHxnLnxOPMUwwXLAbIQ7U8l3QTdEte7R73DAe8mnvXwnoPD8xwJ2TkMGZvscVgjjGds-tyMCU55NI7FxMLyHQosAPv-ohndXTn0HoFYlET4JaKVJnJeZxkdO4T9u9va132Gh0Orcl8hOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Yf-HpGKRyGQiHdZLJ0Zdyi0D9gvwNe9_mlUr_SNB8OdOi-FxYkiFR11T1UGg_PdqALH_TYy2e4l70VFvJtcSTKEeH_0lw_eJq5QTEJC8eekG--zb5EtM0NC24Lm-267bN9r8BXK4utE_NQ2_5rz_spGo-QXKS0a5aoJMGuKFJWs8_GUycgU8NyCmnwsbkWBxlbpIpoGYxHxnLnxOPMUwwXLAbIQ7U8l3QTdEte7R73DAe8mnvXwnoPD8xwJ2TkMGZvscVgjjGds-tyMCU55NI7FxMLyHQosAPv-ohndXTn0HoFYlET4JaKVJnJeZxkdO4T9u9va132Gh0Orcl8hOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpaGfh6UZ0P2CELioUMjDZVTjF3kikqYkgXmDnYuyJU-HWMlrOAXfY1ovZtzVcd6T55kp6VlQy8JC2I0fcKXyh4HGLP7wA2SaRw9bDk19uGIreSVblHWlj1r9HtItsv9NY0_fjjTg-fNKRcs9a6QhQ9ebIvD3V2m3NkOO5G1ih2KDVzCGniyMy6NhuGb4hPxlBpPEdvn6AfY-A7ft2qBXJ6bUU4ZvY7EzyJFGjETNwoqI9V8Cyy7T_LY4GmueoGJjpvXud-r-UuFfHbucpgJ3gsyHcCJN8UXcDWvqrAoDGaGUs_apAGVtfowzb9WrIVxvU0V1BuBnmC49hXRoO6fcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=rj2Nv7HziKdD7SDVoMK38CpNRZeY2VcQlvmtsorDxHNSWjq32QlKqi57JWZMpzlflgjhe1pEXNqdDEqIPKZguPUIy0FGjjKet6O6YL_IMgIr3I_pTUGqqCDqEu8x6lH5c67LdaM5ZPZdlPE8_nZumXsK6V7MUwuPTCMQrZ0lMwvM9hXFqNe1mhntb0eku-6SdKexhpOOgWv6dHe4ec-6oZ9eGoxyNDgTqEGCflea2jq-1_-UoywxTqITHQkHAqQxjvkHoEPftfAHEDg3pB-ipmt_iwYtVKBtjd2LZkaiGAYGb_T507wavHrFx3LrbBkPQlQ_4iFQZjO_naohAsBtEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=rj2Nv7HziKdD7SDVoMK38CpNRZeY2VcQlvmtsorDxHNSWjq32QlKqi57JWZMpzlflgjhe1pEXNqdDEqIPKZguPUIy0FGjjKet6O6YL_IMgIr3I_pTUGqqCDqEu8x6lH5c67LdaM5ZPZdlPE8_nZumXsK6V7MUwuPTCMQrZ0lMwvM9hXFqNe1mhntb0eku-6SdKexhpOOgWv6dHe4ec-6oZ9eGoxyNDgTqEGCflea2jq-1_-UoywxTqITHQkHAqQxjvkHoEPftfAHEDg3pB-ipmt_iwYtVKBtjd2LZkaiGAYGb_T507wavHrFx3LrbBkPQlQ_4iFQZjO_naohAsBtEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmMh1dKqC0b6NHttq52wgXr2yF6BD530g_cds2pZyWcOOBMrdsw51tTCWs47GoFUW3Ldlp1VND64KTRqhtsr7uQn9IsoFm2JFz_emHCfa9FIQMEe0eOP2VB5wRETFhmGaCfY6CffrGCfn71Jlw-038tRJYptkgulnFkwwsShWh_krK7geqh4k-EfHdnpvy9sKNjQjqdY7etS_SJgSB7oMBvqAe1lzkDngIsbNgvbSMKY1Eu3FpTwz1Pn1pHhmh2n_eVmqYJjldeLsoyXxTeZ9E9qphUpPzxx9RUrWRegRfZnKOIoKxMPxUrekh0mdJnZRo49K5myTrXTz3Xg9ZCrvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRA1L4zsTxtpnpmPIaRmSETzgVa06RHwOokSj-0cU1tXeJXEYt_rHmZZFZ6g0PBhiKA4Tg9tZqPm6DWKWJ-9ry3FYFvnP2pfr9_B4rfjRJSPOVowMZNYofaNtH-bhLilj3XSjlAJLVX51J8jMaZd9TUsGg4N0lc0bmutM8jO_qHp-OOSlmnUn7Sym3v-xKOBVZZdEr7Va8tfJkyP7bwV-P9_QBRyIQQq92Tl2FRilSzjM5Derz8n7zEYPlVAJv6tnVUClNJGYlAN7bHegQX1k2tJBG9hcWPaDqJLFTI7Zf5PblpzIEAAy-g8bJ_eQt92SyM0GtmAydrqE0NFW2s6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=q0FWH9NXDsWGheRaJQk5IPieCyvMiz8VMh8fdmsjForP_8-qDu97cM7Mv9osad7hb3jCl6YRXKK8jgsS9riuJT9EFUCMeM4_MkvCIOygAqYTLz02ubkuz_ddq2JcIt-IEvMMxrP5LB1_VHjWTujEZsjnMEzB4LlMpUhHzHHIu3il9o_IIrQOqD1VTEj6dWPsHbuAhnQhjUurpZL5m4Llbakd9cWRUZjRrDbxd9qz4TeO20XRfhEou1LSgbDMCkj7nQcmjdmD8niD7mWHUjTM1UefggwL4f4MpmUdBEgh0ByAueCjRAT5J1i-hAgKHnmYULQHY-UvgtPvMdoh6VIujQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=q0FWH9NXDsWGheRaJQk5IPieCyvMiz8VMh8fdmsjForP_8-qDu97cM7Mv9osad7hb3jCl6YRXKK8jgsS9riuJT9EFUCMeM4_MkvCIOygAqYTLz02ubkuz_ddq2JcIt-IEvMMxrP5LB1_VHjWTujEZsjnMEzB4LlMpUhHzHHIu3il9o_IIrQOqD1VTEj6dWPsHbuAhnQhjUurpZL5m4Llbakd9cWRUZjRrDbxd9qz4TeO20XRfhEou1LSgbDMCkj7nQcmjdmD8niD7mWHUjTM1UefggwL4f4MpmUdBEgh0ByAueCjRAT5J1i-hAgKHnmYULQHY-UvgtPvMdoh6VIujQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEte3p_QJhoZVZ4gnCIcDmNCDAelZY9ADM8dN8xVXEuDEp_2UFtojPbgtP1TeeO_ZRmScMxahw8j8RhKAmKubAcGHqcl7Am5qwuZwXqfjU0_xOx_BhkjHd3CX21XDq0ySJjr-BvBop9Sq4Jf0lVZY8fWDCcPJCY6Sk10kzeP4DLINr4sCBeUsEKKdCw3-g1o4yTCLCheT2bAdymK4tCOKngms2kbkH6TZAy39XWTUFFNFGXms1OEwlrWLjBarDCP5V7fW1eaX-rCsGlgL58JGW_6xV0pav93j0BLIyrqeF6lhs0o9tg1RyJLGIFQa3dswQJotvcF9TEW-gihMGuPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSAJGTD8fQ6VYk_zOdgz6OvBqfmYbcbvV0Nzxrxjuyv137uQ6_q200FucvFoy-C5ekMarCcUj4iPEFauBQqUXXeT7mGVrLH-4lzq39g2pyCuVPhkgVNTe_F_DNgg9n4tpCQtHmLAZdX_mydfMNny0sFuPnpq6nAAPQhFSVFGquqb0HVbBZombsvubxnaq5OAqM39Y8MBEA4Yz-iK9W_PbOOMuYDp74MlGE5JrHsYAfeXfmGYwSDv_AfMB5lb5N2CU1DBmDQNV0CwROBD8Ad48lI-cYf2fJlCR63psyO4tgCcX8tI6Bm4R5z3IPU1j4_i7p-jsnHbjXyK5otEboNt8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm4VOnWi9A5a3GkL0WvszB3ma8CGRg1XK4kHedp4__nXKcU-wvWw94DzMnn_WVubwvK8WT_RWJ19bh6dPwF4TKZ_m2e35_wFUO22zpKjniU8PmoDoj6Eei3DxdvICPIK-V7NmY3ecoXHQX2QIgoadrGMMZ7vlbMBlgYoH_ybHK4NGTAzsESJqNU8jZa7H9-ms6pUgpez6iXlkgZL8yZ6Lb_Cc2IF4G71sEwjvOqvNs9J_FYSsHU6zLDxxgxADpcSmgpjDyWy4gCacVb9z6VxOB0HReiwZv5aw5A4_Crta3k7iHsIY_eHNCbZLR21zlc1dI8bvGS9W_cY6H4PuZDqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPLRF9GZrYMNyyOqVdLelG3TpxdGNmh5hvMN6_7aXbtAEBPPLw43MDGY7fl8DYx7WcaSO0I9lFN5WXQlydM8PEnZeENgtIirr0EY7ouwul21L2SPewUS0m6o6qvHVtIZ9YZr8DTyjwzkFp5eBaToL2I9tnCLbrzvUN-_3-oWoptb5oNZPZBqp9ui_zAEDVnQ_OKGSO-rAavzBgMx2BtM93BRk_VpfmIlxvdRdCJqw8bvbA-FrEJwIuy8HSo0YgoCXmrqgGU26HlXteVfoidgW3atkJDqN5ISr3FP4eVHGMFTff6EJ7XvesuIlXDxQ1nClUhsYMDyUuRkO0n3mQaG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtVwnLAofCK57MylHua8gOIUAhIw0V-sq8MLcEQodXNn975sC91DJhTbBkxQ4HYa0DTvlPVcQNoErJx7EBhtDZ4AXa4C5A8PMimzcsl3DKwLrXe9ON8ixZe3nhIy04IDTFUSrzD_WCyFYtZmWDtTA2oUuCVbHuqMMDU0K-3GIzbo-sobefTU7bZYZisbqaj9zXA8v3FGqWwuM0rLsA15gEg3Dg0v59nnKXiSJ9mVNFH3kNRZ34GIX8hPv4c4HiPbJot-pf1QYIFLyZWOUGy9Z6YhABeagvw2gm-VBzypkvEeFvglCtHogGgVRTulT6h6BU0_AFqnc7VJ_lOkSIGhrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTPljLTv6l8PAagud-t66LE5F_UESeJ6l-coOB-8KS3_qTAkBVLAiO-2QNIv3s6flAJ7V9nm6HaTMr4l45DiN5cxRqThJID5d6mvDsiFDo68L_tJ7kF25kn8Q8GRKdKUneFEvymOP14f1FOrtzRpDmjV-JKf6ejCxXv7CGKNmn8fbgvJTeuqLAKPyATlodTEu9dlodC3h_V9G45rKWQom4AN6910D4MmVRk3W7ChTUIHNfKs7IsR9BoJ6YNLpb7h4K2TEUugDlUdTIuTW0yoAlDmszYjpJDmr29mENVNMZE-1nszrOAOAKkww2wkWTNXOnX-5vXYIweNxRPGnRwogA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=YwwAK0_JeRUE3aqQ4hr4uqZ0C7GXRadAhslynhN0hlEIjcbMUDfYWyfA6tYa4mrL00P6czGpBgBnrB5E6j_xp3R7H59SaDmI_OBKGPuaFIPPRjxbrKEEdInkihqMVuDvaClv4rGKpoDDs-nRuP0txALraGCmEKr_1Fw5XTQ97yHYWtM4AtcgSe-bvV6it5sFrCmqmiN9tX0X8eB47_RxU0kpE7KEtzBWebxWQDoiXn-384p9KBJ11kXtFqftoOfFfu1KXB3wpMDb5egfipnkOS8yH-46tNUe2AioTVdAqXZ43XyEOQHTo5QbBiKdewXitXG-qp-MyYZvHQz-7E4FIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=YwwAK0_JeRUE3aqQ4hr4uqZ0C7GXRadAhslynhN0hlEIjcbMUDfYWyfA6tYa4mrL00P6czGpBgBnrB5E6j_xp3R7H59SaDmI_OBKGPuaFIPPRjxbrKEEdInkihqMVuDvaClv4rGKpoDDs-nRuP0txALraGCmEKr_1Fw5XTQ97yHYWtM4AtcgSe-bvV6it5sFrCmqmiN9tX0X8eB47_RxU0kpE7KEtzBWebxWQDoiXn-384p9KBJ11kXtFqftoOfFfu1KXB3wpMDb5egfipnkOS8yH-46tNUe2AioTVdAqXZ43XyEOQHTo5QbBiKdewXitXG-qp-MyYZvHQz-7E4FIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXjepqiQlEFRGJMwrlJgnNdzyek4HJOPQGmIWur8VlO3jyOJaiBB7wgvniJP55hd1mog5gVAKKKx0OxTnb7Wx8rDNxMS-Lhs9_e75a7Njn5XouhXbVDWnFn7-k1oTtVr4OyvUM23KmcObve1OzIpSMnt5q5z02SmmmnJgYqR7IbLSKWa01bYJsr-377dDr6Rz2d1oaeQv4zSh8NzpsGWoAtoQqzp3MYFmy_uNfPZ2uvOOwuQnbzaJXrwcXRQaf0U6hMR_DXYCVrShRT5bJL0Z61RHIYArOm89wCwm25nt54JzUgDMlwWyZ2ZKbAPFN0j7KU2hSFSZ57iXtrcYZgq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=FVUKA7Do7q9rlf54ycURQSBqpEk8Q5pUO-snStfmFXUMJnHYTzj_I9Tw-9g-TE4XXpY-KIxXuE7uoqJmcaZjrxPmwSybKq7x3BH3uWGq3W8OmVD7vm3Nvzeaw81iL5ggPcpERYdKE4mSd0XmkWlZ3Oks0uA-BwJGkqgIK-9giXWEaGdeD7WCGomba4-0NcM9p54OFXfcsOpeQJzyIyHGf3RT2OfFHNsbgFyuLS-0PEy-BQeasgNBZK1aJk0vK2ziljwfPFU6-JgZ9WvKpxjPVlv0TxIpxuXU9tWJBQT92_VYW5m07oCoEpu7b9BQ1QnAvsY7fMfmyJPxgNSGa5n5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=FVUKA7Do7q9rlf54ycURQSBqpEk8Q5pUO-snStfmFXUMJnHYTzj_I9Tw-9g-TE4XXpY-KIxXuE7uoqJmcaZjrxPmwSybKq7x3BH3uWGq3W8OmVD7vm3Nvzeaw81iL5ggPcpERYdKE4mSd0XmkWlZ3Oks0uA-BwJGkqgIK-9giXWEaGdeD7WCGomba4-0NcM9p54OFXfcsOpeQJzyIyHGf3RT2OfFHNsbgFyuLS-0PEy-BQeasgNBZK1aJk0vK2ziljwfPFU6-JgZ9WvKpxjPVlv0TxIpxuXU9tWJBQT92_VYW5m07oCoEpu7b9BQ1QnAvsY7fMfmyJPxgNSGa5n5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=mKlbkVYKuMJluAlEMrAGdRuuQR0DMVxP61VLNXq855Emq10NdMFpjsQq2CV8nKCzJ_SMJWx0RbQQ4MsZWjhOnebYIhhBr1jttgPoogiJ5ewF4KadqPN7ZyuxNFZZJVOPFtgIx46WBg5caqTu83HfGvvUJRm0wtNP6fXVj7L9lvWPH54x7CIF1qgEiNWgO0BzSrlbybU2DZhY0gauCNpNECtUz6zbjrXFs3UxH0Zj-39xyH4RTHESKWKKELuVZGeeURz7fYxOXai8BOSknfPGTCK0VjmX6Q6DtZFXjYki6yraz9TdIqwJcrEDdnhdFXaTniGilQJw9v925dIr-qrWqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=mKlbkVYKuMJluAlEMrAGdRuuQR0DMVxP61VLNXq855Emq10NdMFpjsQq2CV8nKCzJ_SMJWx0RbQQ4MsZWjhOnebYIhhBr1jttgPoogiJ5ewF4KadqPN7ZyuxNFZZJVOPFtgIx46WBg5caqTu83HfGvvUJRm0wtNP6fXVj7L9lvWPH54x7CIF1qgEiNWgO0BzSrlbybU2DZhY0gauCNpNECtUz6zbjrXFs3UxH0Zj-39xyH4RTHESKWKKELuVZGeeURz7fYxOXai8BOSknfPGTCK0VjmX6Q6DtZFXjYki6yraz9TdIqwJcrEDdnhdFXaTniGilQJw9v925dIr-qrWqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syN3BcjlOXIS16rLHvNenrpY79YuUMuHDTw_XtIJYeVt1vmBPbhGLVRpJFcOFw16oaZuCFW_mrv27RuF436rnFrWlZXVzs9diCPqiXsAcFek_5q-YOdC7XaI4Fq87vKkAqLJm3u_aLNxQexwB2b1cfmX2FFoewWGqSrd9YbslBiqvIIxKAv7Gg8tjTt-4LBFByghiQpg83ngsOxX6gv_4IlbJlKX2BtSBCN1bO6mCpdLsxbgmf5zWkuTg6DXVmYM1860xCmBOxqg09VOKa7mMBrMXOnOzr0hjfYVb5IOPYjn3TP0MGoVA6Vgmd9u2q2D4W8iODpZ4LbMDiehb_I5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Y4b_EKudfPxCQJ-P6hqDEyzA7rHIICYfI0LjrmMsYT4nv-NhrsgljK8XSo4YQw_2IWxp255eaSen6VhbLjy-1drlkNFOEyX4TgD_7v9kmMRxnyyS9Y1tXMX35fpN0T2tOhG8rDP8m0tNvE33EIuzhxeFQTX7VsESt0LekLP1rFbmIGcMo1VmmgQVsTs8vphV6hbq9IJ36LmsUv8TvYPHOxtpqKz-Oq-7wWJXicT54nwkhBSyIxGk5qkCwpDZQ1LtwEc_kGltrA1bFqVX5eiCY-Vd0B7j2pOMjtzcdkTVUdMj7Nn4-oXGaQd0SDBbcTec2T2PsiRbEsnBXaaIuRDOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Y4b_EKudfPxCQJ-P6hqDEyzA7rHIICYfI0LjrmMsYT4nv-NhrsgljK8XSo4YQw_2IWxp255eaSen6VhbLjy-1drlkNFOEyX4TgD_7v9kmMRxnyyS9Y1tXMX35fpN0T2tOhG8rDP8m0tNvE33EIuzhxeFQTX7VsESt0LekLP1rFbmIGcMo1VmmgQVsTs8vphV6hbq9IJ36LmsUv8TvYPHOxtpqKz-Oq-7wWJXicT54nwkhBSyIxGk5qkCwpDZQ1LtwEc_kGltrA1bFqVX5eiCY-Vd0B7j2pOMjtzcdkTVUdMj7Nn4-oXGaQd0SDBbcTec2T2PsiRbEsnBXaaIuRDOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbcZCIlxGK5xxFWIvzn70a4pnmdl4KSBroIn2inzuA0RBW2h4mxEDSe7FIJBmJNC-c2ZjkM0DPq7T143im4mQb7xQicg1CUtbzgsd_awm9i4Apbo2Gn-S3jrl7b5ndMniHqQDlzj76UR3BIiUeTA9DmlKbBi3cMwqfKxuSS1TDSLUtpCnD_mVvDTDrCEeFZk6vLa-Bigd10Ss5RtTSJ0MnQma_RZ2E48dT1v0DXkUKJK0Ez82e9luIrTgEjUwcLOnZHNhwTFDHcG9Wt8nGsUbmBY0_FSxOAnFpmdLpEYoGgbD4Q4uYaeysX7fvl6pnZA4dUpyAkHoC4ssjgcI9x-bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so8wjFld5veI-3IeOeYdGNOKUzM5kLxxNqlDVv9CVyDXenOTOLswdffAXdwL3ArRdPlIWwQ7hTifNFicEv3GdXuE8RW95JDSlff4kexbuvhWRUrZ7o-M9MiVRWBnHzDClC2_WMX6TzjLPGoJdW3OGhkfgiforphC8QWHKwRA9J-fAwXSWVqwSWqw76ppW9rmBWcbjOGOE2M0_aZ1HZkGnmoLr-akwSJQgMx-3j7LzjICLDF0tdVUNgfGzO_HJ-W6c4ZrQy2MMt-BnP1zaTfpqpxSSK7n9JPc8bkEyjV6kovBD-ffHjxc_gk0UkJxXlVnPz0fxoBxIEH48QMW9l2ysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWbNDNY75NUAifLVHiBZClSGwKKaeVS2kaTD97dKclf-c-sDtT3uV4u36mNcYIgJYDufdDeUghyvXqILer6JuiLuL3oXZY_HW_xJsWqQklDdvVVmn78YVp-T4nN9V5Pc5_UzuOyUr83k22_LBW7SrF0si7rZ6360rvDJXJFU6e1eL2BTNqv5IQPuk6WphYRHT1sovlz8pxOBVavwFMoPEi2LBgd8E031n6eM89R1Lyi7eRfibOLi3IxSgRbUiUL60Op-P8bqRVPgpHUDBQIzLioST3V9HKeF9ww7SSIch4mPmLC6lXW07LTkaTKtszj7dTY13gyfktru--Bl0gIFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m16BiNU5uiHeiqM0cPaEu6elZ0QcSP9kokt374DcUw9mjiwZC8GpWLQUwW_W6z8B_hZWjGMLUi_oM0NyiEUCMnGPDowaS982sLT9JjlvijHKx2wI0l0CtNZG9d5v-f4En_RR3q7O2iDhQyjw_MR-pquXKi-mFY_HxP3C3u_X6j5miJaUt8Oc0kH30h1aA7g2kiw17Igws9nYVAmucMUDAl6l8EAQEWFpON2HWLeEubzLCSlrByHTKr2VnabI3WZy84muXVoKSGR65kY4sCbwvNsGxZtvG7loBlcXxaPsoahiMtTajlsfV2jkQ36DZl1iEYACm4WOw0pnn8PNn219TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb0pXR641hESPDKzyGpCFxNz7biEuF4ySEELLdFoN2I8NZsPES7GRzaLDzO11JSiB46mxJ3IcbuXvaWgDF06xVrG2vo35AYfBwuCWXCkraoJ--DleKp1D7WicsKQmsubvSx_G4hi_YbwCpzjQTJL2E2hH_TDprpF5G4Qz1e7VUfWF7Qkf7LWt9-UgTL5_dB2LGSXT1GcRmhbVsi3sO9J_JUsXq3Xiadrfus0ctcB4botbxxKbdaSXxr6WzqmoLmXoMpYJLD63nnTeMfwO-yr4P1qnGLb5-LO53j4owP-HC4Ydr0kemPrgJeE78DuDUe6CfpFHIAhE16dyNOUDHSucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUKBludMLO6RrFJFtmGoVjL-hT0qZLUj5-XOPBIUcnUFu7AxUyKSCbLwqRg1gl96_HiM6p9hvlqoLw2Iq_kM0SUAj4lk7gqHwooeu7QjdFZK384M9oCBrbcDCMgYlm5m12wZxWw-qJ9ScersRpQsa-X7K5BsEut10cKUBMCo14LMhSUMm2S1kRx7pUwQDP2UOvgOMlwsx6RTlWOSF6KRp0fX8OtUJHZWWcyWS8Au0LrWACfjoeUEUgWCM_Fyczrwbs47WJllPk-mISlUxAHP8AoJ_mpQld-nS3YgK065GhYSBUInbRhHftr-EwQSq9VwDHxLNxmOCVyaIoaedAE3NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=vKe3HJkbsoOLDF7QkncACpRi_qTTDrhOzasdU5O2e5fHUm6Q8oFQN3Shi1zUyIs_MQ8gqV-AEfDjvyXW-Q9fFdVfqG61ZFuktRKvobz5nq8NSRKvKq-nX8V6MBXToKg3ya4Dyx0GLWbWJHhW470XV6KEvKUmSY-skzIEwrILrvwsmlsA5SUQnQE8Z3ViGMKKJyuD9JJzNcTZ-tZwGerQqdW2WWLW1q4EvE5Iz4QBot4bHQcnB1NceKydSgaIvW6yU8p2ks-iP8F6B68LAT0BMaPJnf9JF8xmFidytLog2U2z6MtwRi-hDqN6ll03f6IVG6oWhT5a6JnXEHJUGBwdLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=vKe3HJkbsoOLDF7QkncACpRi_qTTDrhOzasdU5O2e5fHUm6Q8oFQN3Shi1zUyIs_MQ8gqV-AEfDjvyXW-Q9fFdVfqG61ZFuktRKvobz5nq8NSRKvKq-nX8V6MBXToKg3ya4Dyx0GLWbWJHhW470XV6KEvKUmSY-skzIEwrILrvwsmlsA5SUQnQE8Z3ViGMKKJyuD9JJzNcTZ-tZwGerQqdW2WWLW1q4EvE5Iz4QBot4bHQcnB1NceKydSgaIvW6yU8p2ks-iP8F6B68LAT0BMaPJnf9JF8xmFidytLog2U2z6MtwRi-hDqN6ll03f6IVG6oWhT5a6JnXEHJUGBwdLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=I9kApW3VT_jkRm1Mrk1CRPSDr7gojs2bsJx6ulpY76Y3Rx6wgQ4alKwUz6MGotNjISxgPIIzDZjVHfcri1PW64HvycH81PRi9PlScs6mMZg9oj9ObDGMqH97UsZfItbJmjXpCa8-HMGMSVNs1AtTU5HGjPfi40kXnlFXKfdI9sBUIrcHkBtf9wupdqvz-C-atXtSMRlN8Pd1wLKw89vgOOAwWV66B247IcLYc5jq0NYhFCiFFxla8MMGaCpAQeFPalXl5U6HJ6hqcL5wUq19kmX1UYg3p9aQfrwW_iBDYnjh-LYolSr3JLKG29eSwtEKMSUFjSePMl55x5iqc2rQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=I9kApW3VT_jkRm1Mrk1CRPSDr7gojs2bsJx6ulpY76Y3Rx6wgQ4alKwUz6MGotNjISxgPIIzDZjVHfcri1PW64HvycH81PRi9PlScs6mMZg9oj9ObDGMqH97UsZfItbJmjXpCa8-HMGMSVNs1AtTU5HGjPfi40kXnlFXKfdI9sBUIrcHkBtf9wupdqvz-C-atXtSMRlN8Pd1wLKw89vgOOAwWV66B247IcLYc5jq0NYhFCiFFxla8MMGaCpAQeFPalXl5U6HJ6hqcL5wUq19kmX1UYg3p9aQfrwW_iBDYnjh-LYolSr3JLKG29eSwtEKMSUFjSePMl55x5iqc2rQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=GwwNRq2YoZ2DwzRRmUEhICE1ZTnZnmxkbzu5MVooTuH0oIMtmA50jniDkMQz5KON1eiOI98nDopW2ONLysoEhODQGtNINSS5EMTlhdLfrE4yD-W8Cr-fpvYYVz9uz6dH2qI7iUj5Lj-19U9NQwPsej5c8eUrKgQl0_J0n8cf8w3CNIwuzslyn7tGP6GfdTZ4Y0n11BOYZx57x4WcaCjZAJqebSuUaHH95dbuVOeDQLGAW0Tm8SdUQ9xPMzjg1UK-g5M6jy94BPzEUspzUhI2qDYPXcDxmJOexwdyf3ryQVVaDQgZAHnCen8k7L7QOi0J0kPiX8SVLC3TtU-DlkWFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=GwwNRq2YoZ2DwzRRmUEhICE1ZTnZnmxkbzu5MVooTuH0oIMtmA50jniDkMQz5KON1eiOI98nDopW2ONLysoEhODQGtNINSS5EMTlhdLfrE4yD-W8Cr-fpvYYVz9uz6dH2qI7iUj5Lj-19U9NQwPsej5c8eUrKgQl0_J0n8cf8w3CNIwuzslyn7tGP6GfdTZ4Y0n11BOYZx57x4WcaCjZAJqebSuUaHH95dbuVOeDQLGAW0Tm8SdUQ9xPMzjg1UK-g5M6jy94BPzEUspzUhI2qDYPXcDxmJOexwdyf3ryQVVaDQgZAHnCen8k7L7QOi0J0kPiX8SVLC3TtU-DlkWFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=Xl_InjE-keBrtryCvhukswQDHTFhNh60QHKKLJeR25XYMEOruu39GTo9MvQrTcIFqoP-jrybxRjV3yewVvwpO5KIbCweOR4nQLco3FX7Zw1K_Q9y0vF5t3WKPHaB1IXx-zfbP2tTUCmUBwhkBldfKkc0wsI20tkrMDk8G_YQh_4Fi7YK7KjIOAx8cZT1hRPCq2TRpWbN0l6hgvH2V1-vd4glt6GXWas3JXy3tksEET3ddiXOgapLcjq1j5EscrKNksd3LP9kSG7L4nTHwPrZ_pjtSg82-KSBRa9je_rAuWe0Z6uJi-5FKhz5FdEqh4uShjlGFfLa489_5OamVbCOaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=Xl_InjE-keBrtryCvhukswQDHTFhNh60QHKKLJeR25XYMEOruu39GTo9MvQrTcIFqoP-jrybxRjV3yewVvwpO5KIbCweOR4nQLco3FX7Zw1K_Q9y0vF5t3WKPHaB1IXx-zfbP2tTUCmUBwhkBldfKkc0wsI20tkrMDk8G_YQh_4Fi7YK7KjIOAx8cZT1hRPCq2TRpWbN0l6hgvH2V1-vd4glt6GXWas3JXy3tksEET3ddiXOgapLcjq1j5EscrKNksd3LP9kSG7L4nTHwPrZ_pjtSg82-KSBRa9je_rAuWe0Z6uJi-5FKhz5FdEqh4uShjlGFfLa489_5OamVbCOaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuKx1VnZDRFhQFTSU5QRRBPP043HJwfmAdzStSuHiJF5-7JT2KofUhsQcv_mu5ks-kxMDIFPGcx5zXeQVtN2ifZffNixnDgopJw9iquo9rRYreRl6AQeDZIqHTYSbk31mJ-m6v1rAsxdXW8Ms2gNWLyYNUE5mUDaclFUFMkhd6Lri5DARqD5X3o7D4BjLdNzYaEobY01UuhMgLrNW1i3DeTJUYtSkAKU64SOUYymPRkX7VNjSYFXxJZ8X59Jf5JvuB3taIeQHj5GBgqD3xo4onCQYtRo8Be3ZG3QMoWG_QjVmNBqwPht8_Sxnj9r0BzPP-uEthgedBPPHGcb5mkyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=VdRZuO_SpIG2KR0gfmMoSURjJoWpuDolmdLLi8UHYZP5Evv-RT7zZ5l5vGjuDXh0ImPEZHv17RrR5ZLYlkUy4v5Zr5c6Euzd4dGrWL8Qe008-YGDfzqXb6v38yX8zWvmtEMsErlamRESF_0qQGW59T5WyIHN1qeLhnlADkmegj1bEWoPD-atitxedLfHuICoKL_hJE5Y1tIYIwKdJkjoPkQm_O10AmB95YPlWUPHH5dSv97F-iT_HCjBZcCVuSTXsFBamSvoUZQd0vHVWcR_jYnHXGxGIewGk6AqbgLPdmCGoS1knfj6DF_nX7kVwH6DnxYyQ-1z4LrHG8WqxD3h5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=VdRZuO_SpIG2KR0gfmMoSURjJoWpuDolmdLLi8UHYZP5Evv-RT7zZ5l5vGjuDXh0ImPEZHv17RrR5ZLYlkUy4v5Zr5c6Euzd4dGrWL8Qe008-YGDfzqXb6v38yX8zWvmtEMsErlamRESF_0qQGW59T5WyIHN1qeLhnlADkmegj1bEWoPD-atitxedLfHuICoKL_hJE5Y1tIYIwKdJkjoPkQm_O10AmB95YPlWUPHH5dSv97F-iT_HCjBZcCVuSTXsFBamSvoUZQd0vHVWcR_jYnHXGxGIewGk6AqbgLPdmCGoS1knfj6DF_nX7kVwH6DnxYyQ-1z4LrHG8WqxD3h5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnWwdNQ--WZ5AZf5eLhHpF-31PJXnpt_RyMr5gvXVzElNeAxRVAObzy92HXnJOXALvlTiz1NTdhOaw67-VlW1rKkcrm1feY4hXubNb1TJl-sIHco6bg9B62N6fynY_HGmrphHAtvE5cE4lxZJLRNC3obcwmoOmln8sAA11UOaWNzBAIZX_QWjoUGzfiG-7x0s8VnbtQdsOntI8hWoazZBDGBqbb6-NiywQGE6T98qzjtaU-5d8Tzkor3qi9heP9gfihokqGi8nB3eoQu_hVEj8sJQrFRquacRlZk4ysdmOhgQk01cpmYHDxV-SyyGq2ZFH4d2qkUOAFk210iT_OLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=JPtCTgJeUuwoxgKPVHzwyUhTZNI-FC3fQL4VncWK3A9GU3MFVYrrM-zN-DipeFP4k3TSpMQxzzj4P1SwLlT2YEB0QS4NCluscraVElhwFyJCLBQ5U3XxsP43YEV9j0pYuRaz7eyXorv77PAXzJCj3fB1TTYhbaOErvNPFvMmoiE3qZfYgusELEJ9f4oQXvnXEQFUCCZb4fAH4JE3F6Kd_aDNKdRbAedmzvDRK62MZINi3I-DP6s2ctVyJ6TAEb1SRiLtev8MPQzNobAh_Qge0vCGW5NcERFIcBOShgY34uN-1oVFrvAQioMT09mCFLIz-lL8Dnq8NMbrIU0rdE0CuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=JPtCTgJeUuwoxgKPVHzwyUhTZNI-FC3fQL4VncWK3A9GU3MFVYrrM-zN-DipeFP4k3TSpMQxzzj4P1SwLlT2YEB0QS4NCluscraVElhwFyJCLBQ5U3XxsP43YEV9j0pYuRaz7eyXorv77PAXzJCj3fB1TTYhbaOErvNPFvMmoiE3qZfYgusELEJ9f4oQXvnXEQFUCCZb4fAH4JE3F6Kd_aDNKdRbAedmzvDRK62MZINi3I-DP6s2ctVyJ6TAEb1SRiLtev8MPQzNobAh_Qge0vCGW5NcERFIcBOShgY34uN-1oVFrvAQioMT09mCFLIz-lL8Dnq8NMbrIU0rdE0CuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=FvNifkqQ5pcjb9z_I_o1NEesIHCU1InXR1l73QE5dDBpB0q9maSFEoBHYDToHkp65QCyRGTzs-CRzDQwS05mvgsoGGF-ZaK8JMxkAUwCFi1Chzuu5nLeEx1CDk-pKDDXIP10LnmqOdQjyNk480lbpWAbM6K5UDc8OGJ4ymuN_c6eNfLcZHEJcW3dP4bt3lE2aSrdLQ5BoPcnCINgxiiBLiIVgPzDnfnJm4817wieeSIqlBfYcWJKF767kf8DJR3nN8-xJtsFQ-DDxQ760CqQKaDJFBlB9MziR38mYOZGtI6JCMGobufwmppUSOfKICY_c4VLRStDbYWfETvMNC_yEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=FvNifkqQ5pcjb9z_I_o1NEesIHCU1InXR1l73QE5dDBpB0q9maSFEoBHYDToHkp65QCyRGTzs-CRzDQwS05mvgsoGGF-ZaK8JMxkAUwCFi1Chzuu5nLeEx1CDk-pKDDXIP10LnmqOdQjyNk480lbpWAbM6K5UDc8OGJ4ymuN_c6eNfLcZHEJcW3dP4bt3lE2aSrdLQ5BoPcnCINgxiiBLiIVgPzDnfnJm4817wieeSIqlBfYcWJKF767kf8DJR3nN8-xJtsFQ-DDxQ760CqQKaDJFBlB9MziR38mYOZGtI6JCMGobufwmppUSOfKICY_c4VLRStDbYWfETvMNC_yEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=QoX1rsCSEZevq95nAjomkL59FE_Qrw9FenwgCSg1bB9xcXqdUWZRGIcnmhx5xRWm2_vyQXFo9lQQZgDUDaHxnuJVyELID84-sJzAVBGHXhx3_yu5gEHvPwhqe3zneXslxWKVL8Ucbs9zli8CnS-nxMwapZzLVY0ZV9qc8ftNy7FnWu3o1EcvfgTPkdkuTYfB9RKSzqmJTaQI8FLqRg0GlZxw3mVpid9gXH9eiiBbWDbbkt_7STDekMTMItwYY4g4HGkO2uesWpwUB25KUFiPidVTjSsQoS-Z-uv52LaApw7h_m-wVUylhDFucpcfHUfBqls62ihG2MJEVTFvuc4vdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=QoX1rsCSEZevq95nAjomkL59FE_Qrw9FenwgCSg1bB9xcXqdUWZRGIcnmhx5xRWm2_vyQXFo9lQQZgDUDaHxnuJVyELID84-sJzAVBGHXhx3_yu5gEHvPwhqe3zneXslxWKVL8Ucbs9zli8CnS-nxMwapZzLVY0ZV9qc8ftNy7FnWu3o1EcvfgTPkdkuTYfB9RKSzqmJTaQI8FLqRg0GlZxw3mVpid9gXH9eiiBbWDbbkt_7STDekMTMItwYY4g4HGkO2uesWpwUB25KUFiPidVTjSsQoS-Z-uv52LaApw7h_m-wVUylhDFucpcfHUfBqls62ihG2MJEVTFvuc4vdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=jMWIpufVNZQM7S2orApR7mAUW8TbudRlfPazbb96-Y_SVop-QYSakjLDHkR7a7uJ_dUQvJT1dYfvWHamj4glb74hhL9JC-y81vNHMmRFl5A3SP6WYe4SPR_Bm6-KHbQdZoBomxJI1MdBsVG-48RPyM4sRnIq6Avju-eZxnUCz9345XjLqAgympWcgPM3c0BEd29BT15wUNbT9WP9TsLriW2QlFsXXf7T_pwwlTynnh-RfCgdmifgOKDKz7z10RmsHMNnjsFRXpvKtU39_STUlX5h1cMe6KExsExdWy98ZuQYU3ORukEswidE9ghPqmIHl6TGg-6i0bujtNG6lbxWAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=jMWIpufVNZQM7S2orApR7mAUW8TbudRlfPazbb96-Y_SVop-QYSakjLDHkR7a7uJ_dUQvJT1dYfvWHamj4glb74hhL9JC-y81vNHMmRFl5A3SP6WYe4SPR_Bm6-KHbQdZoBomxJI1MdBsVG-48RPyM4sRnIq6Avju-eZxnUCz9345XjLqAgympWcgPM3c0BEd29BT15wUNbT9WP9TsLriW2QlFsXXf7T_pwwlTynnh-RfCgdmifgOKDKz7z10RmsHMNnjsFRXpvKtU39_STUlX5h1cMe6KExsExdWy98ZuQYU3ORukEswidE9ghPqmIHl6TGg-6i0bujtNG6lbxWAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=YF-zaTaTf945UHHL9rpmubfqCP2Do_S5Kt5VuDFVZ6U-pGuLrDEILQtwq5JIp_quYFY23nzr9j_GF8Q0xHc9DU3LpT3xMX8OvreuAMNZ7yoG8i-cmgiIB6oxVAwYgVkkp4vF8eRyde6LnNahfxvitpphFKkXkcQJs6Lz6zOXwA53OtHpm8-WbM7HNGLA6O08mkccNnI5hDQKv3TXCiLgNR_MMr3SQ9jogqozzoTKtA6kirvtec0SFlRTSEQfUjfwBqmcAiTXqR3eBmtr99xCBS0mPU-_g2XfmUWvA4FchqY5HwYIhB4I1WOBWo34TIVGQqZWy1JtRw3g3o06sxT6GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=YF-zaTaTf945UHHL9rpmubfqCP2Do_S5Kt5VuDFVZ6U-pGuLrDEILQtwq5JIp_quYFY23nzr9j_GF8Q0xHc9DU3LpT3xMX8OvreuAMNZ7yoG8i-cmgiIB6oxVAwYgVkkp4vF8eRyde6LnNahfxvitpphFKkXkcQJs6Lz6zOXwA53OtHpm8-WbM7HNGLA6O08mkccNnI5hDQKv3TXCiLgNR_MMr3SQ9jogqozzoTKtA6kirvtec0SFlRTSEQfUjfwBqmcAiTXqR3eBmtr99xCBS0mPU-_g2XfmUWvA4FchqY5HwYIhB4I1WOBWo34TIVGQqZWy1JtRw3g3o06sxT6GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=Azs0751CzWs-HSBByehfGbgJpg8jD5g953qMmz-rOexvW0FjHn3HRrxblrOUEakvvIW199jgJ76wLc7VvLig2BNFyvXBS5YKJwX-ZNsOJPStQusKTxQ8Sie82zic3vP66iAYi7sAiLqWFxZYABOmkEoYENqEKDKFg-MdZDtaNNqXXTDs1tOCuJlfzNB_kPXH_b8j_SPU50zv4XTufyr9YNBhpvw0vKKxGECVP_N-LL7tzj-Ksjn-HDjtfCuuReM3dHEtbJu_ODijTuoP76GGXDu8AXgaVWX_mLdXez4mfN6aNcp7eC6fkmOi7jTlhvUwFMxwaxnbIhJuwHCxeseC9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=Azs0751CzWs-HSBByehfGbgJpg8jD5g953qMmz-rOexvW0FjHn3HRrxblrOUEakvvIW199jgJ76wLc7VvLig2BNFyvXBS5YKJwX-ZNsOJPStQusKTxQ8Sie82zic3vP66iAYi7sAiLqWFxZYABOmkEoYENqEKDKFg-MdZDtaNNqXXTDs1tOCuJlfzNB_kPXH_b8j_SPU50zv4XTufyr9YNBhpvw0vKKxGECVP_N-LL7tzj-Ksjn-HDjtfCuuReM3dHEtbJu_ODijTuoP76GGXDu8AXgaVWX_mLdXez4mfN6aNcp7eC6fkmOi7jTlhvUwFMxwaxnbIhJuwHCxeseC9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=H1CAkt6-7Zr0k2Hgs7bgXTgc0E4vJnC5JBj-0XUFlopaMWLdOe8gdDSjxhI6AQ65leJbl1kUvRE6Im50GwV1Iez-1ke4-cHZZNc6KRy5XiBQHSZ4id12MTzHhJ6bM8CuwBFAJK9WkguSzInoiTpgpJxnBXvQBkE6xSVydqCJNRRm_StqCi4AMvvvgVT2aom9t8jeEpfxOJMS8w8qWVTyetv_gpT9za6gx8oNyKyIUUCRhryfI9y1eA2rcX8_j6zBfPtIhIfJzzrDBiQLZ0pBCAG9AtSmcS9ngUEq7B1u7pSP7nHXc1A3hKWJUHHN3ecwDQE0F6yfEbTVSIPChX-pzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=H1CAkt6-7Zr0k2Hgs7bgXTgc0E4vJnC5JBj-0XUFlopaMWLdOe8gdDSjxhI6AQ65leJbl1kUvRE6Im50GwV1Iez-1ke4-cHZZNc6KRy5XiBQHSZ4id12MTzHhJ6bM8CuwBFAJK9WkguSzInoiTpgpJxnBXvQBkE6xSVydqCJNRRm_StqCi4AMvvvgVT2aom9t8jeEpfxOJMS8w8qWVTyetv_gpT9za6gx8oNyKyIUUCRhryfI9y1eA2rcX8_j6zBfPtIhIfJzzrDBiQLZ0pBCAG9AtSmcS9ngUEq7B1u7pSP7nHXc1A3hKWJUHHN3ecwDQE0F6yfEbTVSIPChX-pzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyVs5FJzuw2B6rlH9xFHT8zdoRN9AZSOoY05mpr20eJf99KFy-6HvlMmaiTq48Igv8c-wSYN0CLRTVOYJYLro0e4tcP5KKCPg1hZnlmInGiTT9UYCXqDMZO0-SeryavOotqj8AFhFmWaryp3xsWgLX0Iat9ga6CQZ9xkqiTLF0qRlDekknZLeWTgiWpU7Hi0irbOVJieudUBl4wlTwEvf2YyCaCVXKwFbrg3wpKrVrJwybLhaanRpPVg1QJPQw86u7Zv0-hPDyh3-M1vhHfLKn5wbLgX-cg7Jg9C8HfTzeTdwmrqvoxdGbcVsGw2I5t4yp3-47qEoOw1Ngm2D3ZmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CupcZeTsCXgupZxB_dYmGh58wC8WKHMiKGMURfTlZZ0NGJ6L3KYsNN0TFgmtfAmhwMQGYdRV5fJ2z6oZ_S0thHX322Ur6X06d4e17oGWVGrd5PFdEUfVLZQ3EhaR1o863FrcD8aGYaF5mHIQL3e-q3NVSn9ldvXECV0L_mt32rbPiqEyfRUgaty1tjkD_0eY95kvsZEgfSZw0do4Z92W7PgalNmbtyE-azhlHnIPXuP7jujecN8uYklfxUWoPViusUBr9XxBqWvYOt2IYFvfQv70FQ6as2Xpc7NY-webkWkZnm0ebXmFGZ6DU_c_XJUwsM5AGRWl3A_IQTnmNNOc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
