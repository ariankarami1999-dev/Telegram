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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-efSmCELSIEbI1PRvIlWvGDBZJzOTGtA3m0Eb0MPLKTEYKxtvfkjCnJi0eV0uOAJGEobWTeI0vu9AAMpr-5-ot_7-UrUMWhgPDf3cEAOS8_vD4tCaZDhEPT3PkYJazOllt7CkmcjgYw0Y1tn1xOowcXfae9mLe0FystExkQv4yhkyQ3ZeK3hyN9eAe-uJUdjPn-vTkgEqhjB_-ip678nOUbKqkfiWqz5mqiO3qVhe0Hhdjj6_AiR77neLbDC6d0uOWrTz9pCtjxyj3V3pHW5jzU35FYH6ogxOLh01wcFhu5v4SErzicibNfxoh_zH5dLuq-5NMRNpMGvptT8kyo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpWKK1f6GSdx1XJYF6aT0hQmPwc12h1RS9u4c8-F-oCfckATc-AbLIo1g-1lSj1YbYnqLQn3NosFT-rtYTcQUqL6miPxg_TE-uxT6MEWOxB2wsgkMllbHGPHRduExqRsz-hkX63JKWvVHm_Jd2YeT_90fzVVIlGOftOKEkqBzj87KPPyBG2HeeEBE8xWv3nxIocGYAnzZQxHLbQkqL5bLxs8aZCHVczdFSCJW5-XiHv_6jABE7sNZiA2HA5ehl8xhy2MpR3a_S68Qt_4BNwkxdJnVOSsK7bGQZpavb6UFQaAOxWrFjo1rtVtjyuyN1bgQvhDGAAF9Rie3o6wx-5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQbr2QQISjVSia5hYpUZ8i9fYCdVLkSDje6yu5sne8rOE7svuV4afU3gQ-vIYkZ1LCPriPDcIPjLBQf6jP-rX1gvroTzLceNsmGaW9cyYvG7W3CNxGO6GHpL_zn1VMQ8xsLHtTeunRwcMvAW_B8ssGdpuMDRBhR8KFgNwT8pAdBRXJcXmTPNXMe6l_xg7OeyLg6M0FMNfGmiaZ5SrXzwAY0D783h2D0dfiUdar57sRIbVgVBvLFJ9_buGsu35IcbDRB6Cl0gJmVjduyLcB0XOoFL5xpZvpcAhXjNRAc7TW4AvzLZJ-k4x5y_5k1KX5ULDQUri7V1Ag1XInH93CvuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=OpX6kknpm8Iya1C5V_GxOT6drTYayt8Wstx5lDoLeF22SZtQb2lCWU9eczABtMOw3LWnprG76ZtNXpDjLnbGLqd_45Mj_4ixLjT3EkQxSl2j-BaYit4zT3_U6DPtSuEblTlIfXPBkMHnGNVltkqVy6xlaNOpWLCs22cU2UG235DCFVbMWAE97XROUDMDmVEr2v8BU_ovYR7XbjAs9cGpxapVErCsNpckehCiGfPebAHvQq4KqqU0Hs2AVeOEVmg3NCwM1tXmJeZcqaKnRv2h06vi8pg4wLN7KfO7FWUXG0svtYfOx4B--TSgbht6YR2vQFN84kqYzHcab7Sfqg3zRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=OpX6kknpm8Iya1C5V_GxOT6drTYayt8Wstx5lDoLeF22SZtQb2lCWU9eczABtMOw3LWnprG76ZtNXpDjLnbGLqd_45Mj_4ixLjT3EkQxSl2j-BaYit4zT3_U6DPtSuEblTlIfXPBkMHnGNVltkqVy6xlaNOpWLCs22cU2UG235DCFVbMWAE97XROUDMDmVEr2v8BU_ovYR7XbjAs9cGpxapVErCsNpckehCiGfPebAHvQq4KqqU0Hs2AVeOEVmg3NCwM1tXmJeZcqaKnRv2h06vi8pg4wLN7KfO7FWUXG0svtYfOx4B--TSgbht6YR2vQFN84kqYzHcab7Sfqg3zRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQE3Cq2IarY8X-_Ou6fz_-qdBGWOOAVF32SgEn3wpQ7GxdTW9gJJMpVsTqkxf4WfRWLsiIC47_6L4dqaTawOmQ0EA_R6CvyqrgXe_0V6178I_-cWEtPwoPZ2qb3Do0qZ0xwmnFgG74TyLte6p3amF0VGUX5xff88KckCTAZwVwIdr6bNlBDONk98nNenh5ynX8fDU_RH5_5JMtLMGqjZX7znw2kWW5mnExr9dycuYTt3lEgX5PL0EbeUFsQ2o4oMmC_JI8rZ8Jv_5cWTImMpBaEelpQa28fYWLWiOKmpk_YpBh7lwD1kAwiWoq0BQeWL0lwESN2nkNvTWwPSIX__Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=jAJVcfXBT69KbdbVbT30XqbGQTPblApv8jmJPaq2MuzmDneoe-2c2PSDBKt-s__a_zq0xz6a7cnlNNGOpPBpZAUQfw2_FhkmAzadGpKbvHzIofLdchLJJ11prlUaRdcTjl3Dm8ZZ6Ty_R1YhWv0XwAiRyy6aI8uFMiJ4zYQJ21jnu2hOG0uKG_XKSSFuQg0TH1rGRD7BgBgBVJmb7z6gXBYtVBvQwFP1AaZRa0oR6kENKHRb6Oi-HZKEcrToSe0KScC1Rkb5iHXdBXtDGArTnULb4KASPFWrBYJhdzZ0SycFwwHQi9R55Qvq8KukgeoLYk_pP0i435onmHfSvM8jWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=jAJVcfXBT69KbdbVbT30XqbGQTPblApv8jmJPaq2MuzmDneoe-2c2PSDBKt-s__a_zq0xz6a7cnlNNGOpPBpZAUQfw2_FhkmAzadGpKbvHzIofLdchLJJ11prlUaRdcTjl3Dm8ZZ6Ty_R1YhWv0XwAiRyy6aI8uFMiJ4zYQJ21jnu2hOG0uKG_XKSSFuQg0TH1rGRD7BgBgBVJmb7z6gXBYtVBvQwFP1AaZRa0oR6kENKHRb6Oi-HZKEcrToSe0KScC1Rkb5iHXdBXtDGArTnULb4KASPFWrBYJhdzZ0SycFwwHQi9R55Qvq8KukgeoLYk_pP0i435onmHfSvM8jWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxKSWjSmIZRGZCkiIdztiiXPmw7MI6TsWnzLxX_AJEyaXn6s1X9kzMjbMn30_ayUlpX43jgOi2hKsaylIDAERPdR9wiSz5wIZY5ruhOBz29lqEnvQ8OJA3QE3xoOOn07hJ7aPaXAstfulhyboeoyMGoOar8LOWvMcfcxoR66Axqafd-J0EBZkLg8Tgqglw7jCnAyFzoOgDi0j_ZqkFDps8E3JXU0zNqWCiK4fh1l6htJhQKhgNfpm6bWuusQnRQwpD1aIG4rIAakmimFuyal57AGRH7BjzW98Pm2p6etv_0cHru_OKew9GdlilnK61ISD1nMQic1SZi4rPobpk4Usw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=i2cePFwMNwWAoBTXsjaJSrSyUO2LHWL6UCtFDZj_qpD1S8MpHHymOqrQTJQUrl7hZ0Fq9sW-UsgwrGfbDqkWYOPpcBEIw2AGvZTCQO94mTCumSEK1gPMztWo5HNvyDDg3Mf8yoG_wAgdIvvf-EfdL026wf4bIHQr16Eax4w7R9HCTUnFWp7WOveUneBOuGR82AYI8zVfvRBdd__asNm9eSEQuLsdE0rbCzVMFcfMynsnD7PB9ohyfNCgcvAzaeufDzg5s-Mf0-Hy8YDhCSie4tshZKas-0ztLm2rOSedG0ZWcW85sfMCAQUAoDRpNTPNKzKSUOG-GZ7LkTkCcA8ChA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=i2cePFwMNwWAoBTXsjaJSrSyUO2LHWL6UCtFDZj_qpD1S8MpHHymOqrQTJQUrl7hZ0Fq9sW-UsgwrGfbDqkWYOPpcBEIw2AGvZTCQO94mTCumSEK1gPMztWo5HNvyDDg3Mf8yoG_wAgdIvvf-EfdL026wf4bIHQr16Eax4w7R9HCTUnFWp7WOveUneBOuGR82AYI8zVfvRBdd__asNm9eSEQuLsdE0rbCzVMFcfMynsnD7PB9ohyfNCgcvAzaeufDzg5s-Mf0-Hy8YDhCSie4tshZKas-0ztLm2rOSedG0ZWcW85sfMCAQUAoDRpNTPNKzKSUOG-GZ7LkTkCcA8ChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoeSXsrBu2SwGXH3CORN6LJT0I3HJVRsecWcRwDcuwmM61kuIpJwmCsIjqY_HyhsP1NJARCH8-KbqoEC-QP_vzZ9umDgIGA0tXN2HBENxtpeLYltrkJYjq6_IxA6nn_qtHFjEvSZzE6Y4M_0qHPlI6AjztP6GeT02hGMCIix1MV91ceXI96bxKc1Z27gUAaPMkjjdMTAopFVNlQP5WuG--5w7imM3ZMlztQlSZUQg0O2IKUdu0qBSpNlkPakRKReK4gbVtMYS_ZcZDvNUdnQ0KGAu62YoM-bC0Quyox9YqjMKgFnmEWPj0DagW65aLGvxFdiFAoCXVBzZbLGdhOqUeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoeSXsrBu2SwGXH3CORN6LJT0I3HJVRsecWcRwDcuwmM61kuIpJwmCsIjqY_HyhsP1NJARCH8-KbqoEC-QP_vzZ9umDgIGA0tXN2HBENxtpeLYltrkJYjq6_IxA6nn_qtHFjEvSZzE6Y4M_0qHPlI6AjztP6GeT02hGMCIix1MV91ceXI96bxKc1Z27gUAaPMkjjdMTAopFVNlQP5WuG--5w7imM3ZMlztQlSZUQg0O2IKUdu0qBSpNlkPakRKReK4gbVtMYS_ZcZDvNUdnQ0KGAu62YoM-bC0Quyox9YqjMKgFnmEWPj0DagW65aLGvxFdiFAoCXVBzZbLGdhOqUeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQlqSADDudZDr2N-RkA7eaojGehR1i2Lx3mb6TZ8DeYP1HFTT9qNmNXgvS464_1WlIBBSgStUa_QNzaiRwl6-QZMtIeWKzBqvlqOcWVhOe1WsEe2BLiRK9hvWHr3O58npfT2M9FdFD8Y7caU5EXpv6TYyo4Y0vKj5Un_q6AZb_WIqxb2U4AesCXIT3q9Qry47VnFkM_xFbhfx4CgboOG8MIRzjMVnmOig7x8wYq2Ba8hdapniN9XwJCzdVMxkKNIqOvffxFMrqTESsFi4ptGdmMKneWbOR_5qd4jHJVMcU0GcoCHKaJl4vDgX_8m5iImIwpz8-x160hqdiLYEV8ZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Fw2mz7cubEnkPn7pzOQxOw7MOzFYNlLXQEYUadc1I_pQhb7MknJAtFlJNMuTKaB0JlWWrT20H8yEL2XId0U8kSDX7VsenAUJ7zARIVzQ50IPW-P6feHCLio4EdrGd7YP70L4ObHnFkORIandYmcEPT9JCBPw1xce1lODbeCAh-tQay1wIR9WgppQxRT03gcC5XN19xodmNOUJDGTWRUAKLuMwYPwfVB0tS3un9Kw8zQsNl_ptBahjvbtFhnq_dc-s004lR0LOJ7f-UwuT11LePUlOJKtUur174oJyfJ4ud8fbl3fMDmq-o65xbl9CDyibnplomB00pCtBdfJ7Z3BEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Fw2mz7cubEnkPn7pzOQxOw7MOzFYNlLXQEYUadc1I_pQhb7MknJAtFlJNMuTKaB0JlWWrT20H8yEL2XId0U8kSDX7VsenAUJ7zARIVzQ50IPW-P6feHCLio4EdrGd7YP70L4ObHnFkORIandYmcEPT9JCBPw1xce1lODbeCAh-tQay1wIR9WgppQxRT03gcC5XN19xodmNOUJDGTWRUAKLuMwYPwfVB0tS3un9Kw8zQsNl_ptBahjvbtFhnq_dc-s004lR0LOJ7f-UwuT11LePUlOJKtUur174oJyfJ4ud8fbl3fMDmq-o65xbl9CDyibnplomB00pCtBdfJ7Z3BEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8opU_9kQPkWAtFQdr0Uqjf0hWVkvX5wylE9q9xx56-9Q50MpfOvya_-HzZaCqckBC6w63-jhbRq6UHhjXFObHp9hDbU0FT4bY3a4T1LS-NIXG_LtdxhTU_bDdz50M5hwsT-sjfPPT1lf_iOqGDAKHW4vjznLhJnXMKQ5T92Rel1OxWsQdVfMY_KBszVaSaKmTzcSImANlDUqK-J3hpInzTKcZ_rSejEMZxDNSldR4rI8At2ngztHQ7Wbh7L62Qd3hfIXpSUoNA__GQmb6QYAco-vzY9fXOl4tf6J04E-RaoznUKuk6Wu5ATmxf6sncbgyWSnBy-oj93mUAHs3zOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=tjKHlegFI376Uhf5PuZhxd3KMPTPEvW8eRBLkdX07n-JB-tHvm0hz0otejfTreUjUWBT-eVfOdGvxMgruqNhcR0G2nXSr-mTsSxrcLHHMTBNweKK_ETjHRmNXDfYVi9T8T4cJ_jJYMH056aJhawdP7bvVXNcSBGU1YvZMM8ERhQmqZKifDRSFyfZBpajcu8VuhV47zJE0bLOGXuGQExQYvgh5AgiamFbcLOx5Yl6sNzt_mTPnyoESc3-GSUD9YkV2kmcapAYbXrhIce2UHA3aWPzHi_e5R5EnJyCbafKHCVt_mG42deNEGwjFwZ4Jikwj4x6FZpdHvE0964AY7IfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=tjKHlegFI376Uhf5PuZhxd3KMPTPEvW8eRBLkdX07n-JB-tHvm0hz0otejfTreUjUWBT-eVfOdGvxMgruqNhcR0G2nXSr-mTsSxrcLHHMTBNweKK_ETjHRmNXDfYVi9T8T4cJ_jJYMH056aJhawdP7bvVXNcSBGU1YvZMM8ERhQmqZKifDRSFyfZBpajcu8VuhV47zJE0bLOGXuGQExQYvgh5AgiamFbcLOx5Yl6sNzt_mTPnyoESc3-GSUD9YkV2kmcapAYbXrhIce2UHA3aWPzHi_e5R5EnJyCbafKHCVt_mG42deNEGwjFwZ4Jikwj4x6FZpdHvE0964AY7IfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lWSldFXcULycTu3WFD_3dNN4pS0Q4lmhUd8itfcvOwsG22UJGIy-W6A-vue_bANKACOxUlkdjMS6YcY1Dq5H4aMoyj3KVsk787lFKQLuBTk5eYUPyX5TvQab0xBUXhppvxpAGVwylJz1t0ye_18BQ-zPJIJ07SRIh9f54NbKBBTKwXuJpxbjKFwIGmnCOsw5qjhDcd9VnfXLdkcnYjgRwZNCmb-rlYgG8_knlCBJyo0WD07ihodMjys1LD8veB8BGQdxAMnpNVzlXA2Z0rgRvuzqDTracBD6ESaYpIG8MssrCmZmjh8UU1EUDyao2kt-DbK2fGYJ4VHOEKgIgziKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lWSldFXcULycTu3WFD_3dNN4pS0Q4lmhUd8itfcvOwsG22UJGIy-W6A-vue_bANKACOxUlkdjMS6YcY1Dq5H4aMoyj3KVsk787lFKQLuBTk5eYUPyX5TvQab0xBUXhppvxpAGVwylJz1t0ye_18BQ-zPJIJ07SRIh9f54NbKBBTKwXuJpxbjKFwIGmnCOsw5qjhDcd9VnfXLdkcnYjgRwZNCmb-rlYgG8_knlCBJyo0WD07ihodMjys1LD8veB8BGQdxAMnpNVzlXA2Z0rgRvuzqDTracBD6ESaYpIG8MssrCmZmjh8UU1EUDyao2kt-DbK2fGYJ4VHOEKgIgziKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=h6dkVZ6lc01YXaxYV5WjntUAqLg0DzhOZwYwG2XkP-9wOTJBTFeCac0ze-TbwLbVSeJhNYOK0i5ohuJjC5Ot8OyXMYz4pb3dg5G4HA8fpPBFEApXT_INT0hkmuElTRbNXFXXKp8h_EFQNRyNjWRO-LjsK5iSdo_XZ71RGRDEKuWbxvJvOn1l6nxXxiixu78c6xwDP3Y8z6cxqfzqv_uL_NoXs3s_iDkNpTEiEiW7hU9RiBDsu8yXTKEhBntUr6IuHlUITdlzgRXYHDU45x10pWQgtIcr-5B_bkbN-S1KmBGJ9azactHIeyBuMJXiLiNRi2rbOiHfEFUk_WMm8LdJxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=h6dkVZ6lc01YXaxYV5WjntUAqLg0DzhOZwYwG2XkP-9wOTJBTFeCac0ze-TbwLbVSeJhNYOK0i5ohuJjC5Ot8OyXMYz4pb3dg5G4HA8fpPBFEApXT_INT0hkmuElTRbNXFXXKp8h_EFQNRyNjWRO-LjsK5iSdo_XZ71RGRDEKuWbxvJvOn1l6nxXxiixu78c6xwDP3Y8z6cxqfzqv_uL_NoXs3s_iDkNpTEiEiW7hU9RiBDsu8yXTKEhBntUr6IuHlUITdlzgRXYHDU45x10pWQgtIcr-5B_bkbN-S1KmBGJ9azactHIeyBuMJXiLiNRi2rbOiHfEFUk_WMm8LdJxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=vbr73_kVSZ5aqKfc2uLBqNLzsVxIXxdDMkMLisQzxJyQAx0MTjjMEibSxI91nJpHTl55OmHIBxOwHxxjAsuj8DPfelWxSPouosHAlhral0SbGMEoK4ZKAQh8-I5mOjb8eUFFKUC6PzNEjx1OkgUr5Tb1-FPQcOoEglF6EsPe1lvGLBElXsz3zTjJ1efgT_xnHfQ2R97jyVCyBT6p8GAERuPxRKeRahbkdlM4RFbfrvE1f8dRnPWwlz5yM7Vb9IcQ7SZvi9ndVIkeKP-x_eAOPSQxU3wdhVtiTU-kXkMQ2qQBYV5QNBO5AlqZkjG7bqOXa-E4FqjNxRl49Z5jDN36gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=vbr73_kVSZ5aqKfc2uLBqNLzsVxIXxdDMkMLisQzxJyQAx0MTjjMEibSxI91nJpHTl55OmHIBxOwHxxjAsuj8DPfelWxSPouosHAlhral0SbGMEoK4ZKAQh8-I5mOjb8eUFFKUC6PzNEjx1OkgUr5Tb1-FPQcOoEglF6EsPe1lvGLBElXsz3zTjJ1efgT_xnHfQ2R97jyVCyBT6p8GAERuPxRKeRahbkdlM4RFbfrvE1f8dRnPWwlz5yM7Vb9IcQ7SZvi9ndVIkeKP-x_eAOPSQxU3wdhVtiTU-kXkMQ2qQBYV5QNBO5AlqZkjG7bqOXa-E4FqjNxRl49Z5jDN36gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=W45Iec8c5lEX6d_af52O723gpH04SDzKOfqh5MzEeSQ9pZTROiOrjC_H_TBlh_ULQfleqQOWFn3XfB_tmUmI86cgyvoVe_R8KgzZkUdajRgGM4SAkXbKAWskDa3t-kIN-f29tZGstb6AHpJ7Fvz1sidSISsbKa2xITwsLBHHuJomqY5n_AJJ9n7P7Xq_RrwOhstzQ3rjGlu6kGx5P8Y_XVAkWmPocNwpW8QwPIhSo1QBpwXTe6l2gINfIS4JFuXoMMra3Scuri-Wz97FkfsBpGH_OPUYFPcdU7THRKCXBgo8FRCL8TMXrPDNwYosbnMbYnEP_uK6CwD_jK6qZkcBZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=W45Iec8c5lEX6d_af52O723gpH04SDzKOfqh5MzEeSQ9pZTROiOrjC_H_TBlh_ULQfleqQOWFn3XfB_tmUmI86cgyvoVe_R8KgzZkUdajRgGM4SAkXbKAWskDa3t-kIN-f29tZGstb6AHpJ7Fvz1sidSISsbKa2xITwsLBHHuJomqY5n_AJJ9n7P7Xq_RrwOhstzQ3rjGlu6kGx5P8Y_XVAkWmPocNwpW8QwPIhSo1QBpwXTe6l2gINfIS4JFuXoMMra3Scuri-Wz97FkfsBpGH_OPUYFPcdU7THRKCXBgo8FRCL8TMXrPDNwYosbnMbYnEP_uK6CwD_jK6qZkcBZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwUEIjqMKQK4utbmUSBlkAMxwrhTX3zigKcGauwWRBCCOAb4BiI8GgGXx346UIbgoHJodyxz6tkcxR9-LJUgTczZeZDL5VvcgLWObWXzHdp4lLqLFC5A-291q6bxhryqkVgjoAg4xhhxutHFNd2fkz3Se36c8em6CepCpfvVr06B0C5CY6qAZbZzYUb5ABWfjz-PBIOR1e0eKJsHymdjzRoHefU4mmDmQhIiXv54vDVHXIZEOycSzsDDH1BVpojtq1Ip-IHlAsBe0CJrBTxHn_Pllose4CuQ1F2Cer-cptHpDaXW-r5exnxsufVIsc6tELd4J_CkIGmNBMGwi6mSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGDN-oIUxANf7KygaaEevDrdpt-2-9urpR52WCUoNb0ouoF18VxTulncLteRK94qohuDdWQwgvT8IWoCEg98TpkzVHQAziB-Mx8VR_NCDofrhIvxqglEJvkXWlzVZ3L0CYeomtoNFUFKuno9ndqUV3YbvdkZHpodVSj2iEf0RXBfPSHjsEv_NuKHBd7FyYKetov5luEz_6e5BacEvBQjB0b0Wgn9VBD7AU6jA3dWXwb6pl5yoVDD8hZnrekvjKpHK2lMNqOTrf6nIXYYXXRHpeusdQRITSuYW1hN7MwBBav77GvdmTRfH-37UtsTPyfyDCNSaVHmZW8jcZ5ICqDITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcMP18iXTDpuVrf7KRFaJYuhHf3ALEoEkTeV79cKM_mLSHi6e3FL7x7-NrTpFRVvBQo_jmRS2jPbxDP0aj4mrZdwins6jvt8t1kAsScfQRRY27JMb11Xqpu_Zx-9DZPrRzxfB6zx4882Appj0XouB4Nout1CxXvKBznvqQXnaIzI4C8CZGK-115MHtiEkPZ4KWmpE_YDtnW6uKTNmMa3dWVz_NuXjUCKo7alUwrbt-dJmDBGp-GnKDg2EhcCv74-rM1zcLT2MhFGSEOfFPHrBMKHukroWZOoQvPSmpVu3U23N8sOUXXgpqEEM8sjIvQMII2i4Gs9txj0vQuLG0-Evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=aGn8rJD-FOuR_nqiZ4YQAVYrqKwCFTl_uJcHFYVlKDvEyPVzeiM9GySPJkq0AUItmuCiestMGBMPiPL94a-gfBpYu5nEesOVv7BIV7FogKhK-TcTmXir3QMwg2axC-gJcGhjBbHyYdTnimAjEsNPIML_IKYKs87cF_z1JVOEgO3MF6-b-rncNOs7zH1WKFV5z5ce7oXjYUm9wcknoTROalBZnsDY816pWfonzQtQU1_ok5FqOsq1MZ2RRAM8B_Sh-254YI_9PfAJYQ_AZ36SW4HN5iIaWkllkectiK5DF1NaosLwNuNgs8NuEn9rjidu-O12ccwhfDzopPZEL3xB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=aGn8rJD-FOuR_nqiZ4YQAVYrqKwCFTl_uJcHFYVlKDvEyPVzeiM9GySPJkq0AUItmuCiestMGBMPiPL94a-gfBpYu5nEesOVv7BIV7FogKhK-TcTmXir3QMwg2axC-gJcGhjBbHyYdTnimAjEsNPIML_IKYKs87cF_z1JVOEgO3MF6-b-rncNOs7zH1WKFV5z5ce7oXjYUm9wcknoTROalBZnsDY816pWfonzQtQU1_ok5FqOsq1MZ2RRAM8B_Sh-254YI_9PfAJYQ_AZ36SW4HN5iIaWkllkectiK5DF1NaosLwNuNgs8NuEn9rjidu-O12ccwhfDzopPZEL3xB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGi4zExjhU4QR9Hu8AtAWrOkm4OdyktBcnVnpC4wqU1Afn5dlvKskdHOON88K3OM2Op5afi9-vVGsUXZkdnQQgVf8I5nev-kXWcKyebOXsPayP-uhQaaONNvBAEXW8rRrL7ZR0qj5b5LVhFlltFsyA1KNIg9oXFe2vjvKWOJ9eCctzg6fz3nAqZHybt7HPoGpg_Lp4pwDMDET7x7Z688a_S1Cm2TJpkfP4C1zHmVrGUYof6UxtEee62pAPEgmJHFB3MIxqQZ1mlX7OnG3XmxTx86jN_OWqn6Cl0VYi3X_3rkfkGtAJWf6Upt0zRjcYxf-fctOBb6EvNupaRwbNiEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=UXmyCv3hziQnEliBaj79b-FTh1t6F51ITcpjq1hd1VDC4ixfIHFbFArQ0iu2pnXysZlRGmnNjsZwx9S9HzX76Tf3X5lfP-xIHu1QxvzjbJCuiGPCDEfIyf86PXPXJObJdxj2v_nDipYZ3TZHxlSnxQLa6W8hwunK9EovNKqpuNqsbY2tSH5hpSLdeEgc426se7AgqBA8Q_fG-3e2-e4CGC0sr7hCpKY-rITgRspssh12BsGd8P0Y5jhE9CKS4Dht2hTGshU3vGCZNNsw8omfDFFJSzQotG5kNLOQTe58P9vO58qWvGanZEPAZr2Al3Y05kY1Frl7_6BvR8hewlThNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=UXmyCv3hziQnEliBaj79b-FTh1t6F51ITcpjq1hd1VDC4ixfIHFbFArQ0iu2pnXysZlRGmnNjsZwx9S9HzX76Tf3X5lfP-xIHu1QxvzjbJCuiGPCDEfIyf86PXPXJObJdxj2v_nDipYZ3TZHxlSnxQLa6W8hwunK9EovNKqpuNqsbY2tSH5hpSLdeEgc426se7AgqBA8Q_fG-3e2-e4CGC0sr7hCpKY-rITgRspssh12BsGd8P0Y5jhE9CKS4Dht2hTGshU3vGCZNNsw8omfDFFJSzQotG5kNLOQTe58P9vO58qWvGanZEPAZr2Al3Y05kY1Frl7_6BvR8hewlThNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY2wSzEFwDMTa45YMS8zRRL87FzRsgEv4JrASlahMiZQSyUt9PWwTkV4hprxLghOfZUV9_dSR5htwwDTOp82qdIslu5toIMo8d1BwktEEoseWlZl16GxNAXnrjauKEH8t0-HJ2i3wBQbjidTTvdz0YquwOanh06tP4tCXymjhzn0PZZe29xEqmNMUsLgD-HeniM5imUagv9bq9X5aBG4fEk3iXY0MW6mQhmiIhmxvmfNs9qQNIeT6fxkWpgfE8aDZPj96w3Y22T2G9xbHbhSCCiBXmB9fbCEml70vPFn5vI2YFVbbNdD0JbgpO7sCLVXlJN-1EwOoCDPUOb3Q_sG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c44iTYujp4e4Sy-BjBCb9SD6AcPJzepaFD4ukYy2wy9WBygvDm1F9C5rUPTZhQz2Y_zZQ_b80Fx74F5BlsCFw4Anvl4n-GNLYLJM2CF8VK5E6BAlInVqtpGxvUboh7jKlefvdfENPlFCup1vgxF-xBy7ysMALC_2WMDm1QDedn1ctY4c6m5OYo0iR9VFXlDpiSGzqr2vMsmuGMkxdMCb9mXCsIkUXaHupoMdXI_-qti3AwxYoaT2KknuLoRotYHYny5zyfsiJNPg7AqXPyk7U8ltzI2paoetXHDJdCrxYW8N0NvUMZhlwBR5v0FBgc3jlrpymZj6OHVaeBQIaH9vSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=fOjYYVgUgxSKRS5zq9LxTJO3Sks6rjEzlnQYYc6OhvejVsui355dcI6V8z66cEPROGKiEEWXvMs5GPsfqUhduxIucZ86GcP0p6_Z6KSUspuVRtVTHl4XiowFfwpSi09xUbYCinXUXh81iHdgVQam-rLZ7VGry0oHtCJtvx-zZBOwjzyGpatbewotVEE22Fsd-sg5j4xBVs2Pg6DZ1cV9C35iAOQEDKIg-kaJ4jjc8s_LR63jreGt9Xmx4Xxj_MH54SQykYaUvX3Uhp8VrxIMERbht6Gz2mY_nM6OKkt28L7l80ovdduZzor84sHO8hhXCuqqbSweuPWCKMc4O-cCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=fOjYYVgUgxSKRS5zq9LxTJO3Sks6rjEzlnQYYc6OhvejVsui355dcI6V8z66cEPROGKiEEWXvMs5GPsfqUhduxIucZ86GcP0p6_Z6KSUspuVRtVTHl4XiowFfwpSi09xUbYCinXUXh81iHdgVQam-rLZ7VGry0oHtCJtvx-zZBOwjzyGpatbewotVEE22Fsd-sg5j4xBVs2Pg6DZ1cV9C35iAOQEDKIg-kaJ4jjc8s_LR63jreGt9Xmx4Xxj_MH54SQykYaUvX3Uhp8VrxIMERbht6Gz2mY_nM6OKkt28L7l80ovdduZzor84sHO8hhXCuqqbSweuPWCKMc4O-cCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWLd7934maRppZ8VFLf7uwEw74wQdGCEo7jFpNMvYUh0yvCMTnuigu5DlO_DFkQmDO6T1kTpIfjmPjKZgvWk-RjDoOzIGLQlnLYfaFTLlnrQ5pm1QVMcH0h13AYM9M4_XdujCrHT8absRwqXbMfc7zyP_JmfeFrIZliQk9t8f-T4Zmb5LtznZyd8SOlkVXz__NMGb6PSY6GrtcEuwufttjuyn09UsInAdcYY-r54EvdZ3e4HjntnQ_9jLdYW_NM-w2uQ8wu5e3jd1Z616pNyeGjWfUwkDb4G0Y1EDCy0Gne1ijxCmDsXCxipr0YwiHiCnBYYPNCJuUiOzSKESTfqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgXf3a0KeD3cRKvhhywuABw-c2HT9b1o-gM8AnQxhlfzv6la-KCp5-BJ_BNPnngaH5Wbo0q4jAHdH3dI0l8lWiwbiR83z0zxxSEfznDJNTfRX3yrPqXGOm8P27epqY_4CtjC8dSYbQfues7P70iZkCqhBbJDQU1nugNb_yip9gN02XvL9HVlKpyolHukh43FAqCNIHsPlVLDA4m366DaP3pD09O7pOF1STU_XMdnjcoko_ds2HoiF52DZvASn73Y2XVhAkFlCcrDT9MXb76bB0FB2EKOzRYMKrzEWZCAFIafWuxa68NM9-jCZ0G3HqLxMxJsuTuq4EznDMZUkcxHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4sbofNPLcAa_dD7ky2uJLRKznLnc33n-AjMySaYMjBbf3F7zblzyvzodfCesKHtH9jF3efL47RoZ7KbYnZGY8ZsIlYSxkzUue4Sy5Q5DEVNTr8n4Oedie6wRknOr31iMUcJfAE562-dNE6G3Pkh9YJbYo1hcv93cXKDNCM0gjcN3oUlUTAmPaw2o7wH926Eze_akwvEXGQt0j-5k3A09egh-TZ1YZA4oDf4zN6HQy4cD4Dp5JcELVs_-RPD9hPA937rSZeHHeQ4wVyr0BqPvzqizq5N86V3LnNfRTu-9hpT9YObTmmjEj2iRjtPiitCr0Y5Rp7wHUbR-zUxL8jJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACrcBvGvfCfjId8fEd0SDCL0JROWQrHqq3KMl6g2_LsV5Mecj9_gAY4dKt2qKeltk2IBQaBxQbSVzyFwn5kNHksOi6jlloFw3Ie10bJRDkMDxkT7nFVurq45cQVXalP-2DqHgaOPWK88gwqoiOl8iWfF-402kR3C_aX4U0ujZxFGNttYO1o322h3ILMgrwRc2QnmPhFMJdjYMI60dYgMTektGy3s_hthF3_7VQFIXDhUpxLUEEptEHEBt3FgDZ-glQraITRXoVgxf0ZEIbFReeWwTTIsXrI4BUTyh9WAOfoCTMVhjRhjHKMMXzZ3bSbTgUbqIRBSSskeq_RTkf0NFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnwDtd669YDUyESPstRiq3O9TkU00_MGqm8_t9W3Vpxt2xCNZH3Hf7wN1jbzyEGpt_GlVDsaHbKi0rssJ12NXyL_hmWb3NHTLN4sBqSadI8WJlkWIKBgf_yM7Oi3bW6nNwLr1VWF8xY-auycF_CVqbJL-yrIOkFjxg872ZH3DswksVIB4vkbwYYdMCHE6AG8F8O0IbzglfIBmJgVsGYnceVK96E_nc6PpD1X-4zIa3kNYpnkBPbtL4qeUxSGyo_I-2DO-htAaxQJWnBF7KZx8qH-RaPvFgOLsGSBMwrFUuuvh95yqeqjJ8VSDV5QaC-pUShaqnRGfRV29JE0KCPYKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7erLBi2GGSZW6gn12YxbKEVaSLBV-Ws6u6CAU14ASkerCpVT4UAvHpZi8c_PaDSChesJMYl9XrDLTr2gzEadIsxwY4RgCypo_bNABFAIUyIxlcY7I6epGA0rXEJwocpXGkqloW1LCkJGOxn8jEpr4f5pG4SEFluQoe2L8V0mC4WzltTVKIhEZcKomU7tBF8zw9CFxNpJFVamzbTOVl0pDTC-VWxmPhyQrKOTNBQYB85PzH8uC7Ko_0qCP4wUUGB-BnaQPS9dwS9_nEPztJ3ctH0R6EiWfJySCZHhfNwupsiErbDyOI-37A_3DRngsxV_H5ZHGUf27v-XXfN3EXayw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=aKi5NepPKNhHwwtuHdn8kPwaOcA5sw2fEPLoXkhmGiG46BJM4LUBPZTQr9me6CrcqjQjRjlRU-3GxrAMYJpZJNhRaWsu5ADEpB_iHbwiiYCRBg98rzGyRelocqFO0AetLFdEj7Tb6hyp0ZGsMZEIqRsvzsZ9XL6p9Na0cIC37MxHF4vbONZ9hDh_zYg0kIKnaJ0KDYn0Gdyw8rJRg6NQ1cBkZPQ7RitGOWCxi1RP_CKtNHSK9jLsVWgP8dgtjsVAFB2UKkNvuq9LO_p_uxnMSM5ezagDpVIQxqq2mTbGU94_jieQC_4femyykhWlacRFgUxnpeY9qQDr2qr1-8fvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=aKi5NepPKNhHwwtuHdn8kPwaOcA5sw2fEPLoXkhmGiG46BJM4LUBPZTQr9me6CrcqjQjRjlRU-3GxrAMYJpZJNhRaWsu5ADEpB_iHbwiiYCRBg98rzGyRelocqFO0AetLFdEj7Tb6hyp0ZGsMZEIqRsvzsZ9XL6p9Na0cIC37MxHF4vbONZ9hDh_zYg0kIKnaJ0KDYn0Gdyw8rJRg6NQ1cBkZPQ7RitGOWCxi1RP_CKtNHSK9jLsVWgP8dgtjsVAFB2UKkNvuq9LO_p_uxnMSM5ezagDpVIQxqq2mTbGU94_jieQC_4femyykhWlacRFgUxnpeY9qQDr2qr1-8fvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG-dkNZ4qog07-O0sMW4R1TVCNls8Sj0mmUf1gdQHnuCSxStsZLhToUbm-ZVGN_OY0p0g36lIoiic16oKgFCnTczHLmgHkvvq3FMi6uNsTyhSa5CvM5S7sSstMRDnZ_G8hKgfxu1AYQqu4uu6SPqz4l1IXe6ksIdyNbypGC8H0J-doKKeF0-7YEHiMkGm6NSilMypZ7ovmaUoYSIoUVxWtawuexlpK38G8SB1wYCVrShRU-1DD1SlyToCQf-53dazm_ybmqBCEMo_bnbAwaGLZ_NuXI2dL2B3kAPXPXaawvcRFiJhqx4pbhekUEeBrjZ3KZwA72ZWgJXtnCPM8ZLSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=phO3D-bEkV8EJxrDxIPTvPWwBdLKSOoKD4NkStu94tw4l2YPj9MXpNZqnMdmV1YFtKmD2ZcbBH-8Z7X-5ycLfVoSHpLiAfI56M1HzPylzrJ1TW3qOaAQagwszl4d1UPQCVGc5MlGRQvheaedWidR4zsK7gli-EUdfr7fssQqJZ3e6vGk_L0x-43WlunrDhGiUgWiuQVByiN63nTaHjcg7Uxhp5mVI5tS-FB85wEz0oIy6Yf_rnLbTPPrgfV3J-4EQSdsw2sBNqUD3nQPcf5F2NX-BhRem22xI3dxVp-6AfIxLDRXyVnRAgOwb-ObQijUmadaHKPEwZZDbVQwNnZ2SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=phO3D-bEkV8EJxrDxIPTvPWwBdLKSOoKD4NkStu94tw4l2YPj9MXpNZqnMdmV1YFtKmD2ZcbBH-8Z7X-5ycLfVoSHpLiAfI56M1HzPylzrJ1TW3qOaAQagwszl4d1UPQCVGc5MlGRQvheaedWidR4zsK7gli-EUdfr7fssQqJZ3e6vGk_L0x-43WlunrDhGiUgWiuQVByiN63nTaHjcg7Uxhp5mVI5tS-FB85wEz0oIy6Yf_rnLbTPPrgfV3J-4EQSdsw2sBNqUD3nQPcf5F2NX-BhRem22xI3dxVp-6AfIxLDRXyVnRAgOwb-ObQijUmadaHKPEwZZDbVQwNnZ2SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=pS-AqjAkh7zRlXCCgG1mC5uMz7ay_cl2EDCwePAYBWxLZK82L7pZDTxFr3f5-Dpf4P5JhpASZpteumwizGlB_boJSl92lZAIlAz2tVp-HcmRTIjCsqpYQVcIG3e003FaL8k_9gBPtD3hb-LqTjc0NUHtqWonN29bYXp6i6YOSNMwkmDkJRG3vk7ScRmATRu3nOCs02gvS86dUEwynYw4i-MBPPG59SCvsLiB0Pm4e9IZ_4CtescemB9tOgLW3rByhYrKSdYB6sVogpgJ6R2aDuQKW5NoI0KNUPu-RRGXfvecanjRcoT1X8yYmYG79A4rWm4cZV19qifDL3kcrE9Mrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=pS-AqjAkh7zRlXCCgG1mC5uMz7ay_cl2EDCwePAYBWxLZK82L7pZDTxFr3f5-Dpf4P5JhpASZpteumwizGlB_boJSl92lZAIlAz2tVp-HcmRTIjCsqpYQVcIG3e003FaL8k_9gBPtD3hb-LqTjc0NUHtqWonN29bYXp6i6YOSNMwkmDkJRG3vk7ScRmATRu3nOCs02gvS86dUEwynYw4i-MBPPG59SCvsLiB0Pm4e9IZ_4CtescemB9tOgLW3rByhYrKSdYB6sVogpgJ6R2aDuQKW5NoI0KNUPu-RRGXfvecanjRcoT1X8yYmYG79A4rWm4cZV19qifDL3kcrE9Mrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAw_obK03Lwdg-oAWF_kxGGBuuZfgXqE4rtSjWlsvfeHuc23513QoqkBdOgtDJJUeQ-259TUc9OLoENsp46o-IPc--PUJyjn3gUec4t4o7IcT1MxG7d0WcNtTHwhEOdm1AORo9xG6hKuh8PknAmxH1rocBxim7th9qUruZv20IrLSEvDQ5TSjogx6NWVWnBm7x94qtdC7o0YlyNjWfxDcLvVEpk6_l2YXwTE4Yse1V2-ZZeONokC09t-sehdJ6OrvC7Urk6HnHBc4cqcdISNydeeUEnbYfN9YjE14sQB25QqEjms_2L-3UzI8q8WSoc0vikCj4S4JgodEDbG9wV8Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=rlTptHcZ7BPI8gYUIaed9EpwxsotWVztK4Ai7JcKigcM7JuU-ozskzAmOdRA-Elvoa6JvHYzxP91fdNArQl1xDbbxliG2NwsinVqTW1LSmWVRUJQ8XzqZ5PQKO5o0YlyIVXQInDn2_LlDbKys86Jgx-XFi9kUQuw7vJ5RkEbMhaA0_PpmiyruE0thIIgcwvL5vPnZ8m9B6ce7401221Kk2SG8TPjZMJ0vvoesfRjVJgr3kKPTlGvzoLeVu0aQHxyFDIK-6FcidXW_tTAQVpiJxzhB0tSUVCh73saaPVwclWedLyYiigP3khDKDQkD5Ngzx6j97wkCH_70O2WdWQT0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=rlTptHcZ7BPI8gYUIaed9EpwxsotWVztK4Ai7JcKigcM7JuU-ozskzAmOdRA-Elvoa6JvHYzxP91fdNArQl1xDbbxliG2NwsinVqTW1LSmWVRUJQ8XzqZ5PQKO5o0YlyIVXQInDn2_LlDbKys86Jgx-XFi9kUQuw7vJ5RkEbMhaA0_PpmiyruE0thIIgcwvL5vPnZ8m9B6ce7401221Kk2SG8TPjZMJ0vvoesfRjVJgr3kKPTlGvzoLeVu0aQHxyFDIK-6FcidXW_tTAQVpiJxzhB0tSUVCh73saaPVwclWedLyYiigP3khDKDQkD5Ngzx6j97wkCH_70O2WdWQT0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWIO4AFCRwtMIZ_xgcnEml9t8attMyqb4a4RLHh7MwDTiIu7_LM1R45mL5tt1qMmFyfBwF0cceZUj5_DSD59ZZARPSTdEeohX_tQkpn_VkxLn6-OS-51T7252U2X663toFRqY_89V8U4eIaE9evLcFhUE9oyNCfgtcYo_LIin9Hk75fajX3SHwPf9YR38DRr3ka6cFcAkVvFlyftm6PARliOJADrVGRJNnSOPL0eGv7tV3FC1Gc3q9IK4_-qfcGy8hWP_flLse62QCmN7y1SMD8P4-C92ZTJVJjv6z-D66OKdLg2hYVmnyTH2p3ZX-HD0_3gNL-V8XgHCBKQglTU2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtG7N-kJ3ThO28lloyUDgblxUhuKbU-SQPGzMLQjUmsyucszoeYe4nYM4Lw9FSJ6fp3fgtVfzXQryJl6ztWEhRBJCLMHA4APS_guMr0fX5UDT0Shc3dUVc3DkmpLH-vZipFSkD7u4UryZId-5g6bmiKp47SouykkHY_4TwWdwo3WMdeGgPd9qp08JSsPzx3Uhksf6apZAUAVzr1SPREKWvrt9zTzP5Wp6910Pgho29xcXdy_p0up_Rejt2R4Hm6tHCWfEqfXc3QrJGaeM1pYhss8BhGrFOZiiiMp3ek_3HwodYFs4eFpPi5IRA9ExT8La2yoXUiRZhDMcIA-ZIGz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BStf23lZB3e15kgcs8g_sgbHscpYgIZFVu0D3YHSQyREQLTiaPw07FB_HnzYBdvt3ny0uEam7QIjWEwlIRjeglrSZXYY8V_TEsrjF1Id9YW3mPhrLugRiXfxt9aQDgcQo3HYPvehCss9LWS5V1s0K1lR_9WJAIwHCq032Tuw49KRqYe8epUfpNmIZuvOPHl3LSQ-viFdLm8YwCflrzp5qADOZhoJM-z-pX--hE0f8E6WiOQ6gi49bINIIBhHZVHZtw467Su7jKmOg-Uxzz3qd1cEEEy6ggVVf0ffFlBKA85NDBrSXjvCnon1ZJeRsbzjfiFGfDWMoOp6FqsFn3s4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ2erk8MwtWK7a0YIlhslBF9LbcdQ-0OafrQNYKxhygREnb9Z3MRuElVSRujgkC8Mx4oAtfXZHkHbbVApAzWu1aIqTV46D2FurzyvmkxVpOJn9wgSixchx5OZ-zo9sYqUWYGK6ze9wDNCP-Ouim1ilqimahyPacWqM8BDvXm0wXbno1fgU82ozhaysVaTcDD28xEJl0gdWS01ZkqnvCsJ4x37fRAh8S_woC_pe4-PjsVF8A2UuyfjRSJHIUh2DVD3UKFDwtaCdna7KGSGSTTS7D93L_pNRPl040q_2qIPN7cHex5B4-ZsI5yDWdqiuvX6u8YuvV-ilTY7u3D2Ko57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv5z5fyBwvAWMuOQruvk_m6SvwzLnowFmXovFJoqpyjYg-U7gp7uPAa02Sqo2YvTgh8nEd8HGj6A95cba2SzmhIWC2OUqecMqZkeDFXYlMLEzcdin478WxzPtaWUxybMo95ijidInzSpTrsQLOBQufAY7REEXaldC-jeO2hJBux8Gxkr2kV_nKDYFocN8xF5RBHVQBkqm79UUykpKvK8fkFQOZYB9_C45GBcT12tDyNNVMbMEn4cLKtn6AfIRUhxUzEmRrEUJvrOWSBIXPYW9xNsR6S9cF0G6Y-r1iKVHUmsl7F5R4uG1BOCkx83a3cKXu1_WwVlwXCQ6NM4jeJ42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmUJjdxi-1Cg-NZc__hm0SJR9hIiUk3rCh0_tLdo8232GbggEgYcKtdcaEtbHbMzd8_xxyG2oSDgQu80LuOPgcV0OILdALplR25lgJWMkhakoGoNjfwKALQKTbBTW8EyFx2o0ios0d7Nkf6qdN3uwqtn1tssHHanV1rnCwGvzn-GhR9Pq9zZ3agyQP5lf_UuMi324kOPNmMy1x6ZuwVdDSzaEbKeG1RvmXsljQE0GgESq7oqQPfc0z-cva2p6Oc7f9fI2tmax7rDmXc55J6Op2R6oanZPxnSD7cYq67Hp2H-LhWhtJYHKQyantOz8Beoq1BckHKC-0JP5KcdknHwWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=SL8K2UGH6Eg3x06V8MAoNRGpQI7UsyTyf59ZgaifGlrhaHzVoB1xVqcuosSJy56q3y_-c-wG4u3xyAjrt70SvkZ2npCWI0vGUmj0Yznl1krqtdUyaK48OEVeBxwvsb4nYhIxuq930pdD2fN16_ttzCFplDYRAx71IDJEwD8gSjCSYjj4F4oiqjk8HVDTcFrVvk3uV0yA7E7LTd5s-JDticscxAIIKMXVSJKDqopjIAb9ELHyCfc4bbwEnzRsVxvTz4nyVGGBBXrAl8N_0_zEELXK8_qD-757M0bHLPVYMbnxk-TfL4uGJhuYn4WPZDONZazR9Ul4qxV0girETwAqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=SL8K2UGH6Eg3x06V8MAoNRGpQI7UsyTyf59ZgaifGlrhaHzVoB1xVqcuosSJy56q3y_-c-wG4u3xyAjrt70SvkZ2npCWI0vGUmj0Yznl1krqtdUyaK48OEVeBxwvsb4nYhIxuq930pdD2fN16_ttzCFplDYRAx71IDJEwD8gSjCSYjj4F4oiqjk8HVDTcFrVvk3uV0yA7E7LTd5s-JDticscxAIIKMXVSJKDqopjIAb9ELHyCfc4bbwEnzRsVxvTz4nyVGGBBXrAl8N_0_zEELXK8_qD-757M0bHLPVYMbnxk-TfL4uGJhuYn4WPZDONZazR9Ul4qxV0girETwAqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=FDAiUP46i7K7_hkArgVgwgJDmZwgsU9o9yf7s1mP_TC0rtw0FSTdVW1uKF-l-80_cgweBHEgxkZ152z5ILCW5yZOnM9zLXlqhwPMYCXp5tU1TTT85Nq0KBDMBziJh_lJ5S6ABhpy7MCRA7WuRMqSqhRRasl6xtnj63hG9dYt0SVD2W_Pp8MCi7D_WCBX_I6-v7qMAp7TcZ6RRKQ-KPJKrcheoFPalK2m4e2hSB1Wvi-p32MA6Z94wEzDV-ku1d7pWHxuwCflst0jH9pfn6VkPzYpIStwCDuo4tPSVsUY3fWjNbyhHgYXkM2tfivsZFY5cmTa4ErV_V9FGX-jPhgZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=FDAiUP46i7K7_hkArgVgwgJDmZwgsU9o9yf7s1mP_TC0rtw0FSTdVW1uKF-l-80_cgweBHEgxkZ152z5ILCW5yZOnM9zLXlqhwPMYCXp5tU1TTT85Nq0KBDMBziJh_lJ5S6ABhpy7MCRA7WuRMqSqhRRasl6xtnj63hG9dYt0SVD2W_Pp8MCi7D_WCBX_I6-v7qMAp7TcZ6RRKQ-KPJKrcheoFPalK2m4e2hSB1Wvi-p32MA6Z94wEzDV-ku1d7pWHxuwCflst0jH9pfn6VkPzYpIStwCDuo4tPSVsUY3fWjNbyhHgYXkM2tfivsZFY5cmTa4ErV_V9FGX-jPhgZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=lY36Zhl9bxCP00nV-f4JxjM0fFSVn1L1UT9ivxRO3ONwIM0l7NW3m7RvXf7q6btkHoja9h-hfO2Gy8h3Q2w2mTF2K6N77cLWMGpTmivo9owALuzKjRJDFCJzB1InhHyLHo4zJZwSZaDPSTbKdKer8ZgwDSzajfn1ufnWjrWUeSC8b2q5eQ-v86Acpl0LDqFfmukvkzm91sBLS1sXQMbc-79SVD6ZL4yeWpzEsoMlgpQAnP5rldITY-YbEPKyTJELB0EYsqtjucYDHnv0UiXEnL1_T0sMIDqmx3XMbGKc8BPZNPt3nTPnQ0BQ4lYvqR4O2Ldj7G4MWw3XOoPP09uEow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=lY36Zhl9bxCP00nV-f4JxjM0fFSVn1L1UT9ivxRO3ONwIM0l7NW3m7RvXf7q6btkHoja9h-hfO2Gy8h3Q2w2mTF2K6N77cLWMGpTmivo9owALuzKjRJDFCJzB1InhHyLHo4zJZwSZaDPSTbKdKer8ZgwDSzajfn1ufnWjrWUeSC8b2q5eQ-v86Acpl0LDqFfmukvkzm91sBLS1sXQMbc-79SVD6ZL4yeWpzEsoMlgpQAnP5rldITY-YbEPKyTJELB0EYsqtjucYDHnv0UiXEnL1_T0sMIDqmx3XMbGKc8BPZNPt3nTPnQ0BQ4lYvqR4O2Ldj7G4MWw3XOoPP09uEow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=Jc8gL0ofAXaXsOqMlRE7JWt1Yhj8IjcBh0KBpR2BToHWIzrsQ7k7Awj9fnlh3hTXwePKAo5ZrKMZHdWOYdIGUrPBceOG_xEYslnr2AynQQYHSKQtLmu112sjsA_Gi-4ctd60k0ru2fF7D5V5m81jdT4_mm0J-Fdu7UKYfgCdkF9YAzzjaIV4fVJS1rtmi8176MjEGLh5je5RLy0S-1jXqLniz0CsYYxrJPztJfIqdOJIlJOUz8fAmnAdDGctHwwm45K5O0sRQzPguStW3lUOa7Vny9l48U0xioGf0oeGqXz3oPpK74mNz68nUW8QDgtR0GHpr8PqqwFAVx0hB4ClRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=Jc8gL0ofAXaXsOqMlRE7JWt1Yhj8IjcBh0KBpR2BToHWIzrsQ7k7Awj9fnlh3hTXwePKAo5ZrKMZHdWOYdIGUrPBceOG_xEYslnr2AynQQYHSKQtLmu112sjsA_Gi-4ctd60k0ru2fF7D5V5m81jdT4_mm0J-Fdu7UKYfgCdkF9YAzzjaIV4fVJS1rtmi8176MjEGLh5je5RLy0S-1jXqLniz0CsYYxrJPztJfIqdOJIlJOUz8fAmnAdDGctHwwm45K5O0sRQzPguStW3lUOa7Vny9l48U0xioGf0oeGqXz3oPpK74mNz68nUW8QDgtR0GHpr8PqqwFAVx0hB4ClRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6Gbm7TXg66IRmy8fUtpmpad0sXpsuPgZSRASFvpR1_vVDnmVGYU9_J7R1RpiP3f1nOavZ47ZQjV0WsLzcfWufySYEJBCiBsIoPcivsfCagXzZEguiNJLkCcDDMU9wU6ZfAGNVojncut6R8ymb8Y9frJrHEAVQmd-gs7lJE7hD2kMNA3EG5Jw00_ZT56y1eQ7ZInbHuFhz9RSUrwhTAiP5--TWDIMUUQ_F8lXvwmMIFmVnTb-jf75bbuvwH3nNOArnfucnEHajQejSyImU2h6lihq5NLYChMPW3H5o-VTsvAi05XOTIF5_zuUQKXk0IwKGRb3QbxDzmWw4CqtnpHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Jnuj1x3vsGpMcm05XOp6ofHvir6Mw1WwzOgxB4ognTjLHwZmCY3ZKLDeHBJAAEXu2_4pYsYKVWtzZG18SqZn1iqyYwcHLJvPjKrsC9-pvzkJheAH6uXHpmJskmp3DD8oCIQYyDEqK58I8wy_9CWc2AjhCwt4XbqjNPai5IW6E4LRMBRLYvK_dSO-TUR90OHq8V9jdZYtnRhSFcBqsnNf5HpF16_BvPwY3LnTp0QLNX0BYTjr9TeSyaRImBlDj1GZg3ImXFqKFlSdXGcM0wC150YtAcMYo3EIuJjnUAWfXDydDESYH71wjh1yn_T_GFG17EBvsLDn-D_lRsA_lrgGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Jnuj1x3vsGpMcm05XOp6ofHvir6Mw1WwzOgxB4ognTjLHwZmCY3ZKLDeHBJAAEXu2_4pYsYKVWtzZG18SqZn1iqyYwcHLJvPjKrsC9-pvzkJheAH6uXHpmJskmp3DD8oCIQYyDEqK58I8wy_9CWc2AjhCwt4XbqjNPai5IW6E4LRMBRLYvK_dSO-TUR90OHq8V9jdZYtnRhSFcBqsnNf5HpF16_BvPwY3LnTp0QLNX0BYTjr9TeSyaRImBlDj1GZg3ImXFqKFlSdXGcM0wC150YtAcMYo3EIuJjnUAWfXDydDESYH71wjh1yn_T_GFG17EBvsLDn-D_lRsA_lrgGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8KJ-8poI8NjwdZ7jTZleTwnmqyN9uS1y-Cs8lZuAr6vo9OqZXKmHd1l7yIqtRhrWbdRQE--sbG7cN6c_JE6UxHhExoBP8W1adL8GEsZzYsFJ6plSgjxVuF6-B_Lf0g5lohjVbnlW5VL08Lcswo6Q7RNNbNU3Y6QbMm7AMAmDhrUWKw7iolQgIeFAa9B0b5d9XmQ9uWDk20_GVeRoVv_6_V8-cSrsS-3LTZTg0IPUPueYG5XQsEiZd6aOWHAp9VjfgGbLxJ3gzYo5a_yeKtbb6-sS86garagz_2NH20e-HLJxIAu_UOWObR-txwIoINqQzlF0E5YUOGHrsYQpm66Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=vR94hCoYnJWIcs4j5jk-B0pDe7jf-kGbQHpTo3i9AmYvGqIx4Fh76xxbp-CBy70ymjSmQLG38UgAxuIZUIJ1LfqGGB3pdYq9UDiT8XMzukJrt-oXo9pgUQ2yKgEn2MXr8Ilto1Pzpin91XakGUtuw7Mb0IX8VsCSeZp0EgVHkotHbTitt8HRUzkpybe7y5oRqKIfVygtt4ZJwiR-sp0uoyyEsTA12MSz9CpSrVT7xg6q7yKxY38DfEZ297YVoWY-wwBoUDEZGAc8as4Kfc7w_ZYcNwLRjUjgCaTbWlYvA7aeLSNy-KJP_SnLocC_8kWOabYhyJLC3_E1dB3D60N-XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=vR94hCoYnJWIcs4j5jk-B0pDe7jf-kGbQHpTo3i9AmYvGqIx4Fh76xxbp-CBy70ymjSmQLG38UgAxuIZUIJ1LfqGGB3pdYq9UDiT8XMzukJrt-oXo9pgUQ2yKgEn2MXr8Ilto1Pzpin91XakGUtuw7Mb0IX8VsCSeZp0EgVHkotHbTitt8HRUzkpybe7y5oRqKIfVygtt4ZJwiR-sp0uoyyEsTA12MSz9CpSrVT7xg6q7yKxY38DfEZ297YVoWY-wwBoUDEZGAc8as4Kfc7w_ZYcNwLRjUjgCaTbWlYvA7aeLSNy-KJP_SnLocC_8kWOabYhyJLC3_E1dB3D60N-XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=p6wCavqy4Z94WkmU6F7rsHdMulI8Qk-5qHNLuXU5h6vgPkSiFJCyGItB_yVE_lXPXjM5EcvrsXdDt12AlItEtfFStkJASwfAkHiTZwYtuWrOQFHTbSLFjc9OpaOrafM7mkphFfK_NatEjvyx1Xdp15hhjFfUrR8ngZp0Loj2MFJrvMvTCCmPX0jv6SlzKBwdWTBO4KYUEOpwWi76HEBgGJm-UfLT4kJGtSKu68uFB5VHsbDsU2nKCjja6TZZKZdV1J_UN1AKGSGU6dGSKHlquR6w42jgq5g6fRKYFqLncq6CaAHLFECVMGkK75N8cUIdCoA6qIyaYs2K0k-AADbPaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=p6wCavqy4Z94WkmU6F7rsHdMulI8Qk-5qHNLuXU5h6vgPkSiFJCyGItB_yVE_lXPXjM5EcvrsXdDt12AlItEtfFStkJASwfAkHiTZwYtuWrOQFHTbSLFjc9OpaOrafM7mkphFfK_NatEjvyx1Xdp15hhjFfUrR8ngZp0Loj2MFJrvMvTCCmPX0jv6SlzKBwdWTBO4KYUEOpwWi76HEBgGJm-UfLT4kJGtSKu68uFB5VHsbDsU2nKCjja6TZZKZdV1J_UN1AKGSGU6dGSKHlquR6w42jgq5g6fRKYFqLncq6CaAHLFECVMGkK75N8cUIdCoA6qIyaYs2K0k-AADbPaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=mNSlG_3NJJTpaSLKUwI3seMh--j1fcnkFl19kDac2xv-uKdX7OA7ekXewGR-Pgc2zcVf6p9gKEphkkTQJmFgV3KCk5JpQnkcWLJGF-39QlJuKB8bHnbA_iq4nnOlflQpNvXVyzvsANrMX5O_5CbE40BaFPNIGwHPT3ZjnmNbGv2edJ3stUBhOjQPrfAGlLr0gr5P8KgfLqBWdmucHqluBB8ppFG8HvHYeGfbYoOCoU-evBBTYbLIaUXrjjhYS83gDxkw_JJR8SWUXwcA6WP3mezsYKuZ7s4VZ0Z7zX8XMN8Diz85y73A6sNVE8f6KmS4cvzGpvXqrIGvEZ5f71xlPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=mNSlG_3NJJTpaSLKUwI3seMh--j1fcnkFl19kDac2xv-uKdX7OA7ekXewGR-Pgc2zcVf6p9gKEphkkTQJmFgV3KCk5JpQnkcWLJGF-39QlJuKB8bHnbA_iq4nnOlflQpNvXVyzvsANrMX5O_5CbE40BaFPNIGwHPT3ZjnmNbGv2edJ3stUBhOjQPrfAGlLr0gr5P8KgfLqBWdmucHqluBB8ppFG8HvHYeGfbYoOCoU-evBBTYbLIaUXrjjhYS83gDxkw_JJR8SWUXwcA6WP3mezsYKuZ7s4VZ0Z7zX8XMN8Diz85y73A6sNVE8f6KmS4cvzGpvXqrIGvEZ5f71xlPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=unBuLtfic9IKnZ2nUeaolBXvdN5WdUwl72Rt6yXqHgD6fESeoXVWNdnY90yQEjDTZebdTcNB8JJ0I30ZrZBgY1ceRiXwO3wgZ8X8sjJ9EP8A0_oEiBmYxkaN8_-V73IFgo-4-NFUhxjel6KZDgi8YXOB1uMspc2U08ACIcXGy4FQ_Yvd69bOtVsBIDu8aKRToBym93IMILSpDTVxa3Q4NOSljazkoJoZgJ_jjMf_4EDi10PPU2P-UY1m1dZqyih40oKMej8IlklD5T-pOpPfTZyXrvcKbiZPqkUvbMPPQxkgoZH3C0SONsHtfe49a4SYWMWR8v0GcTsfF9LyjfFk5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=unBuLtfic9IKnZ2nUeaolBXvdN5WdUwl72Rt6yXqHgD6fESeoXVWNdnY90yQEjDTZebdTcNB8JJ0I30ZrZBgY1ceRiXwO3wgZ8X8sjJ9EP8A0_oEiBmYxkaN8_-V73IFgo-4-NFUhxjel6KZDgi8YXOB1uMspc2U08ACIcXGy4FQ_Yvd69bOtVsBIDu8aKRToBym93IMILSpDTVxa3Q4NOSljazkoJoZgJ_jjMf_4EDi10PPU2P-UY1m1dZqyih40oKMej8IlklD5T-pOpPfTZyXrvcKbiZPqkUvbMPPQxkgoZH3C0SONsHtfe49a4SYWMWR8v0GcTsfF9LyjfFk5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=m21qHUuL4QQ3O9RzrF6DoMJ48i9A-OwzRaocu6E8MUsVDD1FFWazYRNScrxAFViXT5uYAIn1-_mpmVxXK-tzW0U8p_yMzSzvNCYPWK07lALq0ghzAg8cQJn4oAtNDvLShAxh0fpF2DJDZccRrXUwvfmW5-MAHllaMSDXEuAODKNPBylk5GAitGInFL6544IWDNLU64FTMaNVJlL-CT5BecC1WrGyoUZbnjQL1PU5c5spoL6WK2mdOc2gUFu4pDo2KmkkKnLYHvw7ePxkAfM9syPonUqFbNVZBnq8s37_Sbbe3ZXZ9FvPJDwQonFRs-Vw7pB-FMwUuA3u7qdjsrW6iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=m21qHUuL4QQ3O9RzrF6DoMJ48i9A-OwzRaocu6E8MUsVDD1FFWazYRNScrxAFViXT5uYAIn1-_mpmVxXK-tzW0U8p_yMzSzvNCYPWK07lALq0ghzAg8cQJn4oAtNDvLShAxh0fpF2DJDZccRrXUwvfmW5-MAHllaMSDXEuAODKNPBylk5GAitGInFL6544IWDNLU64FTMaNVJlL-CT5BecC1WrGyoUZbnjQL1PU5c5spoL6WK2mdOc2gUFu4pDo2KmkkKnLYHvw7ePxkAfM9syPonUqFbNVZBnq8s37_Sbbe3ZXZ9FvPJDwQonFRs-Vw7pB-FMwUuA3u7qdjsrW6iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=HBWT2Omc4O-5yx3Drnn3rfFqtL_-EzGjtFzOIZUbzST1rAaipx3IaKkmFyurApOFXcDw_nuRVTmaEGm0eVm_HjQHrTKMDSdSD7D0LEwKx3PyEUXrJJzWTYvbrOQ_wQW5SbB2N9-zeSGp15Z_NQqQ1rX0AtbNfqDGzoiXiuzBE_3lXqfNKb_j6222KTx4jrpnLdxnk3I3F1cofknlYlEu4e7q9Zgiblit8Intvw8gXGTjaPJiKCQ2d5YHyM724BOvVUFzDNkvzzGZTMKxMcj06T_tmq2e3mc4cXf9AIQ76LhzuGLo3deA9pR9MjhUUzwRWgZ4mzypUNpJs5AKKPQtvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=HBWT2Omc4O-5yx3Drnn3rfFqtL_-EzGjtFzOIZUbzST1rAaipx3IaKkmFyurApOFXcDw_nuRVTmaEGm0eVm_HjQHrTKMDSdSD7D0LEwKx3PyEUXrJJzWTYvbrOQ_wQW5SbB2N9-zeSGp15Z_NQqQ1rX0AtbNfqDGzoiXiuzBE_3lXqfNKb_j6222KTx4jrpnLdxnk3I3F1cofknlYlEu4e7q9Zgiblit8Intvw8gXGTjaPJiKCQ2d5YHyM724BOvVUFzDNkvzzGZTMKxMcj06T_tmq2e3mc4cXf9AIQ76LhzuGLo3deA9pR9MjhUUzwRWgZ4mzypUNpJs5AKKPQtvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=E_8DjvUX3GRtpL8fF8nPX3eOHKtevXiVHBPUR_K63bYX1DsO_shos8GNWeHae1PQm8yVWoKhsU5qn7BeyBpzjlYm_5ZBsKDY6LnzXUadY19wAAMI1l7-QXtoz8FONe0d7-AlIcdpCxHvqvHaX20aQ_3mAYpW9h4YwNpQ0d4jo-QEqTw3-hwl2DLqjuopdwVxowGoXzM005RWEYOhMVRfEBWWaKDzJwIs4fJI-L7ahqsKIyoUu0EoRck_HNdPOdnXMUUia8Wo1He_KNavIcXiLX2UrjUro0pL__Y3EomxIb-Qw12N-BrvcBeXs3a0K20nvFYzM9ryS-ZXto24y1b_8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=E_8DjvUX3GRtpL8fF8nPX3eOHKtevXiVHBPUR_K63bYX1DsO_shos8GNWeHae1PQm8yVWoKhsU5qn7BeyBpzjlYm_5ZBsKDY6LnzXUadY19wAAMI1l7-QXtoz8FONe0d7-AlIcdpCxHvqvHaX20aQ_3mAYpW9h4YwNpQ0d4jo-QEqTw3-hwl2DLqjuopdwVxowGoXzM005RWEYOhMVRfEBWWaKDzJwIs4fJI-L7ahqsKIyoUu0EoRck_HNdPOdnXMUUia8Wo1He_KNavIcXiLX2UrjUro0pL__Y3EomxIb-Qw12N-BrvcBeXs3a0K20nvFYzM9ryS-ZXto24y1b_8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADcnd8ikNLpnye4JH61qWOtDYalkmjNi0r7cvdLgDgCnE-YzQcz7vDfS4tt67usVOUq33vBFgWp28mLQsVOQ3G9MZZ0VMk2bks7GZRsqZ6rr3_Y_wRcSnXZoAhy2tYeCmiPHY_ogKc_CpO_aOWJ8GOiOcQ37EBOGWqh6Ammhl5p3CYEDmHMSdPmFNH2Uj8T3aTyx9V-Yju-E3b-HpR3UazQET4ishaYZd70PHKnUcDgQq4S4-O4dV5Yk5OvyiF6wv3ubMp2PFAvvOb64R7FJ4q002YJ9QfPAK-ETqXmuaXj7LhS9r51NzPpQXYNiuqv4S4LOq59j2wyXLpZG74RTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtcEKgmk7iDANyVV51MDZh-wwViKhSr3UmysIPI-FZuwlQRqD6FyxX--QQZDcLBhbnxf9-tzU6dvWqG5Y7CXpOKSpOwwWb5qMAz0n6ltegBlWTIeLfF3oNZNwlVx865hBiMkaMI9HPXyShmTiwglx6G7ing_reSvS2kAH46RlzdtWHBkVxzGmBQ7q5uLE5nAXHr6h8S32VAqYS0oOiEAok8b7PFHR3WuCHyNpm96ChvuJg88Ed2e_pAxVHO3j0cWi744zIOKP7HK1fjAdOPQ0cUa6R4bCbgzDEbVAmeLAHAXYIkUvQN7i37AIdD4bY9tA3dxyjVU0sb2uhONLMndHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=boBdorjx5XvGBHPtAIiHl0U07EYjFXCNpu7HN5LV1kJNT2nN6gM38IqusH8JXLy9qGNO5iJeTaoVTctZK84i03f-1JvERPV22JzAZcscG7rztQtq7aeGnusit-yozFDLkxYuJqtT8vwS4N5KinsC4K5QuRk6YbRcT564DGGTGvBxANXD_kVtSKeTGkvNSx3FUX7EVHGEsR4Sr6SoeTBkhf-gn9aJdqUdJ3DzJNm8Gd3KExI-OX-q9lmn0NOYd0FOLmzox1FyXkSfPFlRlt8EW9MOd6Qvz5yBAJNwB5XzGHFMpMhChZ6p6fcBSFQi0UksZIWmHxQ9wV8C2eZni19JWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=boBdorjx5XvGBHPtAIiHl0U07EYjFXCNpu7HN5LV1kJNT2nN6gM38IqusH8JXLy9qGNO5iJeTaoVTctZK84i03f-1JvERPV22JzAZcscG7rztQtq7aeGnusit-yozFDLkxYuJqtT8vwS4N5KinsC4K5QuRk6YbRcT564DGGTGvBxANXD_kVtSKeTGkvNSx3FUX7EVHGEsR4Sr6SoeTBkhf-gn9aJdqUdJ3DzJNm8Gd3KExI-OX-q9lmn0NOYd0FOLmzox1FyXkSfPFlRlt8EW9MOd6Qvz5yBAJNwB5XzGHFMpMhChZ6p6fcBSFQi0UksZIWmHxQ9wV8C2eZni19JWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHU3vuTB5Nc-2fE1Y30iQfrgHTG0No4HT7rUUOjdX07XRXLF1N50lsfx6-mq9KO3jzwH6ncIHAyvejh5Bjr-Oo7lH-iy_-mUTS3nxG5jjfLeFy-apfISQ8hJSVwH8duqrzPRegsbcT3L5ZGy0FFKPE-FNh6ZSpOdeqwnFpGfeurAdC9l9-MzFD3p9E3rBZEp5EgeIFv_F8bDheAutjDMDzN1I_yIwDaIvoz9iAZWBgo4gXybgGaN1QoOSolc35W5niP1OXjV2l8CPfDveZYCTowartPeVF20K_1Fn5guIPanBBaMt76uyVFhJE-rjHS_bwIIuU6WDbMj8enThVemQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
