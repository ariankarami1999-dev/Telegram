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
<img src="https://cdn4.telesco.pe/file/aibW0XWmIedKeK7QSHF5vDgrC57olmi-GKin54nZBnT1VkfmwB56OZYuM5CJcSBwX-YSbtFUFxvayF-TenjiFRiYBZFsibEQh1Kf3cfat9D7nInFNB6Jx4Bl8HXB7xm7ghmv_NPrba_9kdMg88RDWlcVjFItAtsvqInLCNLgJ1TUsq9fIoKYeiDpRNYwfgFMpfSp_Ec_JytvfbZZJSK6ZLHpYfBF0gDmJfmrbPZvuz8J_Wb_LoEhdBFG4Siu2j1039MR6wAgmz-Ls8EXMr3iUHbYGn007fCm2XVGXX0TIIL1TYUgwbv2OaayTQL1JnmgCeLq9eNzxpAVhJol5roM6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 916K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-123503">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نتانیاهو در جریان بازدید از مرز شمالی: نیروهای ما از رودخانه لیتانی عبور کرده و مناطق فرماندهی مشرف به مرز را در کنترل خود دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/123503" target="_blank">📅 17:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: محاصره دریایی را یا با مذاکره یا با اقدام مستقیم می‌شکنیم؛ اگر درگیری ادامه پیدا کند، بعد سومی از قدرت را آشکار می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/123502" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e60b7eea.mp4?token=DMGu091q0GNC0q4ohFURE5tO_Wla5NWjqgPiCtduacicXu_NU7HYXlZIHlNjBC1uo5R9-xMlHcrjyUfqWbI_K6n84T2SP9wR5KacNCzMfBMrETLAf1OQrXD41wihry2q9lyh1-7j_inJFrige4n95cWm6FIM624FIs90MKIU9XdRy6RjRZiau450LV4eEk1wKISH9942eN5B1_ruGg2KqstU1gE1qT4dvMFFWwGFcRG7CIH1iTk9IRyIbrQ8B7A3r6jFC061Ubvj4Xuc1k_PGsjS6dRzFdGhAvuCJ4IFqkwxLCESFfMRyPLujlPl2S7u7mX7bn-kccNbz03wZ9ykvSfQw24cOhpTWAgzZRc8iY-eaYw2v4DK0Xxkaio8oxGNwlWV0_A3D46foT_2VtDqxs5l6ozasEO7h_61eTXAVQsXcpsEWsw73cmD4qfAZqwOTnwjdzLvtPL7G5XXkHiR7mCb_7rTG4BpdbabaMRtz_y1LY2YmHXifGobh33qouMiEZDjR4aUwsZooyYSTD_CM7f7zoBmN5R9Hpp4K0YymlMCf3E-uLVH7-83a2xwtNJUxR8eeVRqnVdZg7dS2EM63gOy9Ykx0mOJlRDIlVgJNuJ5-pfxAOykKK4FzlTiAesbxKuXeezdLcmZgSfCKWyoPCXUIajB9pItUBJ_hCgkF0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e60b7eea.mp4?token=DMGu091q0GNC0q4ohFURE5tO_Wla5NWjqgPiCtduacicXu_NU7HYXlZIHlNjBC1uo5R9-xMlHcrjyUfqWbI_K6n84T2SP9wR5KacNCzMfBMrETLAf1OQrXD41wihry2q9lyh1-7j_inJFrige4n95cWm6FIM624FIs90MKIU9XdRy6RjRZiau450LV4eEk1wKISH9942eN5B1_ruGg2KqstU1gE1qT4dvMFFWwGFcRG7CIH1iTk9IRyIbrQ8B7A3r6jFC061Ubvj4Xuc1k_PGsjS6dRzFdGhAvuCJ4IFqkwxLCESFfMRyPLujlPl2S7u7mX7bn-kccNbz03wZ9ykvSfQw24cOhpTWAgzZRc8iY-eaYw2v4DK0Xxkaio8oxGNwlWV0_A3D46foT_2VtDqxs5l6ozasEO7h_61eTXAVQsXcpsEWsw73cmD4qfAZqwOTnwjdzLvtPL7G5XXkHiR7mCb_7rTG4BpdbabaMRtz_y1LY2YmHXifGobh33qouMiEZDjR4aUwsZooyYSTD_CM7f7zoBmN5R9Hpp4K0YymlMCf3E-uLVH7-83a2xwtNJUxR8eeVRqnVdZg7dS2EM63gOy9Ykx0mOJlRDIlVgJNuJ5-pfxAOykKK4FzlTiAesbxKuXeezdLcmZgSfCKWyoPCXUIajB9pItUBJ_hCgkF0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل نتانیاهو تأیید کرد که نیروهای تیپ ۳۶ ارتش اسرائیل از رود لیطانی عبور کرده و به سمت نقاط استراتژیک جنوب لبنان پیش رفته‌اند. او اظهار داشت: «نیروهای ما از لیطانی عبور کردند، به زمین‌های مسلط پیش رفتند و در بیروت، بقاع و در سراسر جبهه عملیات انجام می‌دهند و به شدت به حزب‌الله ضربه می‌زنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/123501" target="_blank">📅 17:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123500">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a0v045F46eNz5qN_8JKOp66LdSFrujKTU_LI__IfFzmcs1hlxizUREZB4Ji5Ix2COrJjig8iAK7wHCPq_4c7e0xplxQCKp5a05_Gt7PuF0xpdGXMqabUrXaWzQwQJVPHM1GeYSF2zHo8gTn0swuALTrOKpjnqwJCYXWs19GAhI2ZPzVjOZOo59jCBE4ovl6qftiP6Kb1_lXQGUz0lV0fgM1N3En7o30TbFPRq1VJ44tOzaabmVGCgvkG2nXRKHY1TjBcJTjP0ZJQ1tmuWJorQXhH5d6EIqVTXr2RGPPkz2SoiW-MchmKjkPh0b7Nt_jK9AvSwArzyCYwb8XwP7bgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">CRYPTO SNIPER
〰️
همین  شات ها کافین که همه چیو ثابت کنن
✅
برآیند خوبی هم تو معاملات دارن
✅
و اینم بگم رکورد هایه کامنیوتی فارسی دستشه کارشونم با شفافیت کامل هست هم گروه باز هم نظرسنجی هفتگی درباره فعالیت
✅
ما هم تاییدش میکنیم
لینک :
https://t.me/+vlymyfKFnUo5MjI8</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123500" target="_blank">📅 17:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123499">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee0c5b006.mp4?token=r_zK3I55-azPA00vXmZtT0tjhMRmomJn-27YIe49P20a7t4vGAehW551gdq7mQZQ2sADbf3rA6Wj8FBPdWoj5lOaNrqROWEWe2ZxCRT3h8rSdd50q5w_iyJE5JxyeZ1rKjo4uOUeFiJ8HdgdlCjLBUW9uD8Ezzqg-cHnFoEup5aFkgHaPaDUFp3pjCk0J5DKAtacrC4bxg8hR0M3jGn5vhKKvWwYCfdjYVBKGWE2uPrc6Vna1eB38FOgKMIASOSFnLUh7mPhG_r8Owbxurcx9jvf1GNgeJ78goIxTxJKwzZLHT4ZpYJtZfaHw1Zdf5c6FJrh75faOhNZ6zCEEVHSVxa4exguSQmgcAJgBJE99NUQplet6aZjCa5ySzJPaEUwYwq_K__JgC30foaykWhdJRAVYYFrked17rixa-L5L6exlLQAMKZejMaXiCCo5ipHkR5rFv3ZqYknNO8NYho6HFFB0cZC6BqQUEX-YU6AMM0QrfhJ7x4k6mrv5AiY7GqFJRWVhXICol3y7zpfe-7ZQI_KXslHcjGRNtlURfICv94zD4RgpxPMt0xRbrjB6LUnS-ooJI1iV4CTpmJXir0jcQ-Eg1kvyHLl9ijdS5DVoUwW3lci5vj5z4qSUZWH5L-z6RXYiQJpbWjurymK-Beh6Ij_EBpMhAvKhVtA-Jyg-LU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee0c5b006.mp4?token=r_zK3I55-azPA00vXmZtT0tjhMRmomJn-27YIe49P20a7t4vGAehW551gdq7mQZQ2sADbf3rA6Wj8FBPdWoj5lOaNrqROWEWe2ZxCRT3h8rSdd50q5w_iyJE5JxyeZ1rKjo4uOUeFiJ8HdgdlCjLBUW9uD8Ezzqg-cHnFoEup5aFkgHaPaDUFp3pjCk0J5DKAtacrC4bxg8hR0M3jGn5vhKKvWwYCfdjYVBKGWE2uPrc6Vna1eB38FOgKMIASOSFnLUh7mPhG_r8Owbxurcx9jvf1GNgeJ78goIxTxJKwzZLHT4ZpYJtZfaHw1Zdf5c6FJrh75faOhNZ6zCEEVHSVxa4exguSQmgcAJgBJE99NUQplet6aZjCa5ySzJPaEUwYwq_K__JgC30foaykWhdJRAVYYFrked17rixa-L5L6exlLQAMKZejMaXiCCo5ipHkR5rFv3ZqYknNO8NYho6HFFB0cZC6BqQUEX-YU6AMM0QrfhJ7x4k6mrv5AiY7GqFJRWVhXICol3y7zpfe-7ZQI_KXslHcjGRNtlURfICv94zD4RgpxPMt0xRbrjB6LUnS-ooJI1iV4CTpmJXir0jcQ-Eg1kvyHLl9ijdS5DVoUwW3lci5vj5z4qSUZWH5L-z6RXYiQJpbWjurymK-Beh6Ij_EBpMhAvKhVtA-Jyg-LU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: دوران بمب اتم گذشته است؛ الان با عملیات میکروبی و بیولوژیک می‌توان حملاتی انجام داد و مسئولیت آن را گردن نگرفت
🔴
می‌توان بمب چرک استفاده کرد
🔴
ممکن است شرایط به جایی برسد که به رویارویی هسته‌ای برسیم؛ باید اقدامات پیشگیرانه انجام داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123499" target="_blank">📅 16:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123498">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I08wII7dVOSKvqbNOBbfsMKOmE_Xkef6vzHkXwLImCEzORFvxHP4clwVCYhqmtZiHrnuW2TBHcc6EEFO9Ved3PEG2YgLwN7WHfLhU6aQTdIY7GzDYIbDsEDsIc27llQSYjOXqmhxSVZXG6KbLWikWbTTl-bW2rtvHzD7jU_FsOscmSMSub-u5TGsvBODyTcQeQKtfn9q2aRQw05CHA-w1_vLek4El-F-ob2xXlvh7v8I1X5ZCkqZFTxO4eMEJrfrCBiXTz1R1jiZ7eBuRcbKNHnugZjGkoNa1FSZNUYYRGh0dLGb9H7mnkztzRqE5AJceCPy1HfYqohUw0NBIFDGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید قالیباف : ۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123498" target="_blank">📅 16:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123497">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیروی زمینی ارتش اسرائیل به دروازه های شهر نبطیه، دومین شهر بزرگ جنوب لبنان رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123497" target="_blank">📅 16:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123496">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز درباره جزئیات توافق احتمالی ایران و آمریکا/ ۱ - آتش‌بس اولیه و پایان موقت خصومت‌ها
🔴
به نوشته نیویورک‌تایمز، یکی از محورهای اصلی پیش‌نویس، تعیین شرایطی شبیه پیمان عدم تجاوز میان واشنگتن و تهران است. واسطه‌ها می‌گویند انتظار می‌رود این توافق دارای یک مؤلفه منطقه‌ای نیز باشد؛ موضوعی که به گفته مقام‌های ایرانی و یکی از دیپلمات‌های آگاه، شامل توقف جنگ در لبنان هم می‌شود.
🔴
دو دیپلمات مطلع از آخرین شرایط گفته‌اند توافق اولیه، پایان خصومت‌ها را برای یک دوره ابتدایی ۶۰ روزه تعیین می‌کند و امکان مذاکره میان دو طرف برای تمدید آن را فراهم می‌سازد.
🔴
با این حال، مقام ایرانیِ مطلع از پیش‌نویس می‌گوید متن مورد بحث شامل «اعلام پایان جنگ» در همه جبهه‌ها، از جمله لبنان، برای کل مدت مذاکرات است. دو مقام ایرانی نیز گفته‌اند مفاد این یادداشت تفاهم صرفاً مربوط به دوره مذاکرات برای دستیابی به یک توافق گسترده‌تر و دائمی خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/123496" target="_blank">📅 15:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123495">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
یک منبع مطلع به تسنیم گفت: متن تفاهم‌نامه احتمالی هنوز نهایی نشده و متونی که رسانه‌های غربی منتشر کرده‌اند عاری از دقت است؛ متن طی چند روز گذشته تغییراتی داشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/123495" target="_blank">📅 15:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123494">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
الجزیره: اسرائیل بزرگترین مانع رسیدن ایران و آمریکا به توافق است
نورالدین الدغیر خبرنگار الجزیره در تهران:
🔴
به نظر می‌رسد که اسرائیل بخش بزرگی از موانع رسیدن به امضای توافق بین تهران و واشنگتن را تشکیل می‌دهد.
🔴
اطلاعات حاکی از آن است که نقش اسرائیل [در عدم امضای توافق] پیچیده و چندوجهی است و فقط به بحث لبنان ختم نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123494" target="_blank">📅 15:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123493">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران با سرعت بسیار بالا داره توان موشکی خودش رو بازسازی میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123493" target="_blank">📅 15:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123492">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از مقامات:
ترامپ به مشاورانش گفته است که برای تصمیم‌گیری در مورد امضای توافق احتمالی با تهران به چند روز زمان نیاز دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123492" target="_blank">📅 15:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123491">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvsPLSMBmV0FW4RtPeBVUe7LmYIyaGauKpdY-eGtSbd2QVlmeefuz1HJBSHulDC3q2uvpuxYuWKYovGqhXzwVv7btxOS4QzGKe3biv-4m6KrzeEH1suoGV-nKq3POkdtBNb03VaK_rp_At6I-WTLqVG4XeAp4_1NBbpEqMYD7WhvY57gnu5QUJRQnXCXNKkchdnQXXIu6N9xCPF2wSVZrUxw-vMJO84OhU79gKd9RefRVPtSMpuWvqDXTAajWHJQMHji2nFRijek7h7Pz-WvGbmXUnqwcioapSDhYsxS9YUGoA721CHjkaZOI2U6Q0HwRD28mcAPEy7YqYtndSS0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز ملی مشاورین املاکه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123491" target="_blank">📅 15:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123490">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
حمله حمید رسایی به مجتبی خامنه‌ای با داستانی از پسر نوح
‼️
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123490" target="_blank">📅 15:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123489">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjAtVJL97mhurJLa61JZ34mYKsBNMnGZ5If2YQmF8VJGIfhRn0ISNOlZmBI-x-9SJT54g11zKJ7gLaPsolAN7COrxtYddcXXosZ6-anyVciymPC-h7IsL6XVUXdSbqCteZhcb5xWk9jYfaYsa8bfBin31-5tPMVUhWaOUnDrK_9hJ_ZLuiqLN1AjyIoQfiBNLKRfACNvxgvb_wZpvzKUbI60eX6TLcldvIg1hOmOr23s8yXjQyZt2DA2999loBBz6gLxBTNfIFGgLtlFKxj6UATojK51LYO_yWRw34mRNUY_ZL9_M1BR2dnluoTvgtYIGvdXYCBPfY2HGXnIL2N_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام‌جمعه کرج: موشک، آبادانی میاره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123489" target="_blank">📅 15:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123488">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نیویورک‌تایمز:
ویتکاف و کوشنر راه‌اندازی پروژه‌های ساختمانی در تهران و یک صندوق سرمایه‌گذاری را در صورت حصول توافق پیشنهاد کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/123488" target="_blank">📅 15:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بهترین سرعت با بهترین قیمت با God Vpn
🔵
تخفیف ویژه برای امروز فقط
✅
😍
10 گیگ فقط 210,000 تومن
😍
با استفاده از کد تخفیف  ((Fn)) متصل حتی در شرایط جنگی به خاطر اختصاصی بودن
✅
❤️
😍
کد تخفیف:  Fn  @GodVpnV2_Bot  برای نمایندگان پنل نمایندگی فعال میشه
👍
❤️
✅
تضمین بدون…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123487" target="_blank">📅 15:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123485">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ2-VnBCwnTjEKsFsiQWeoWqxZ6K-n6tcnucXjLdYVBtIcCKh1-3vUHbiu5V6SpBdSSA9rYu6kslcoicHFBZrH3x79uqTOGBEq7uRrnqXAaiCzyEH0LPGinGanHZfOeBd9sEOeDJvNZ9FyxCFYUbZ71ETlJm7M9Ox1GEtgCDtvt2gjghryxbp91VJKjmHqisdHbO9I44bw8nEhA1CNmBKo5vDd7hcQnGmF8jeWTU6bCkiPPblhIiXnfvMlqS7m0-KRzAJTFrsaH40neuXd2-L9xhM5wzwZJrgZPFvMnyQfKkFA6Phlodx0AcATyOrqY91EXGb42UiArsJdVUtd8CFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba50e8b61.mp4?token=HrItvY7WKYTuhoQL6uESxzM3o2Cs_0_MSIt0eUXw2rPVzSdmk2K2kk2X8lKRiPnZ_S5C0DsR9aim0PyLg7uc1yGpsLkTGTo12D9KTjyLjioDctK-9zA8X2H9HcC2JQeM-haroIBziSdqmjBoxsh3l7J5y9ByPbVb_b7SRhZcfWLWi0-iAwSa0LwbUPz8MNTX4OFflQEP4lxKUJQXeNdR26D5_BM2u_wozWPm0z9HLpNY1cSB7hFMchmCtEMlERupzQjgB0CT-E5MEm2576WoWaoNq-mvAOU5sL1J6HEfQTKsfhvdr1jIbQvVTRdJ-jb6-8mcY2EPToQTZdU7JQcqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba50e8b61.mp4?token=HrItvY7WKYTuhoQL6uESxzM3o2Cs_0_MSIt0eUXw2rPVzSdmk2K2kk2X8lKRiPnZ_S5C0DsR9aim0PyLg7uc1yGpsLkTGTo12D9KTjyLjioDctK-9zA8X2H9HcC2JQeM-haroIBziSdqmjBoxsh3l7J5y9ByPbVb_b7SRhZcfWLWi0-iAwSa0LwbUPz8MNTX4OFflQEP4lxKUJQXeNdR26D5_BM2u_wozWPm0z9HLpNY1cSB7hFMchmCtEMlERupzQjgB0CT-E5MEm2576WoWaoNq-mvAOU5sL1J6HEfQTKsfhvdr1jIbQvVTRdJ-jb6-8mcY2EPToQTZdU7JQcqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حوثی یمن ادعا می‌کنند که یک پهپاد MQ-9 ریپر آمریکا را در نزدیکی استان مارب سرنگون کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123485" target="_blank">📅 14:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123483">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نیروی دریایی سپاه : تو ۲۴ ساعت گذشته، ۲۴ تا کشتی با هماهنگی سپاه و وزارت خارجه از تنگه هرمز رد شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/123483" target="_blank">📅 14:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123482">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نیویورک‌تایمز: ایران شرط آغاز هرگونه مذاکره معنادار با دولت ترامپ را آزادسازی میلیاردها دلار از دارایی‌های مسدود شده خود اعلام کرده است.
🔴
تهران از یک شرط کوتاه نیامده؛ بدون دسترسی به این وجوه در بانک‌های خارجی، گفت‌وگویی شکل نخواهد گرفت. موضوعی که به «نقطه کور» توافق احتمالی تبدیل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123482" target="_blank">📅 14:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123481">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران با سرعت بسیار بالا داره توان موشکی خودش رو بازسازی میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123481" target="_blank">📅 14:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123480">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سیتنا: سهم IPV6 در اینترنت ایران همچنان نزدیک به صفر؛ بازگشت کامل به IPv4 فشار بر شبکه را افزایش داده است
🔴
بررسی داده‌های شبکه طی ۴۸ ساعت اخیر نشان می‌دهد سهم IPv6 در ترافیک اینترنت ایران همچنان بدون تغییر محسوس در محدوده نزدیک به صفر باقی مانده است؛ وضعیتی که به گفته کارشناسان، فشار مضاعفی بر زیرساخت IPv4 و سامانه‌های NAT وارد کرده و مانعی جدی برای رسیدن شبکه اینترنت کشور به پایداری کامل محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123480" target="_blank">📅 14:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123479">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDK8jSMt6bQL0CYzb9gFCmdKizwKm_UMVzhSowN_cUa_yY_lDjDTz5raCrZfXjECxLJIvNRsAoXiIt_jjtnEI8iiFkRJ2NWoYc8dTvsj9OmNGaS4z2-cy8osUjiezkPsHdw9zvnrYDrVFABeQ0s3bPUoma_hkKewb2vp_MFLaavc9qCnUBV2BBYvprnZIYYQdfVgAKJAM36Br4DdbZbmwKm2b7rGl7UhHhMdToPv-8IGqpXddHst8nfElLayu9YCAYUZPjq0gpvbgOBO0Vf86PZQX_OeLt1qIFO_YgK5mQ5w1-yjdYZ8uU39L6DL17Pk762-Q7BkHOdXZK1fS3yB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن تایمز: سیستم جدید یوتیوب برای شناسایی هوش مصنوعی؛ اعمال خودکار برچسب روی ویدیوهای افشانشده
🔴
طبق گزارش واشنگتن تایمز، از این پس از سازندگان ویدیو در یوتیوب خواسته می‌شود تا در طول فرآیند آپلود، استفاده یا عدم استفاده از هوش مصنوعی در تولید محتوای خود را مشخص کنند.
🔴
بر اساس این سیستم جدید، اگر یوتیوب استفاده از هوش مصنوعی را در ویدیویی تشخیص دهد که سازنده آن را فاش نکرده است، پلتفرم به طور خودکار برچسب مربوطه را روی ویدیو اعمال خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123479" target="_blank">📅 14:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123478">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co_8VMjqgrLw4CDXorqIFqT7GDOERA-NEloPpD0NIAZYGpNmmtxcG09rgxYpIUbp3X6i0AuR5Y38m3taBXnxBI0snoeaDPUs56vXhtCSXxuYUs5FpBl92KRSdYhqdZ35OO3Qypw0BY7De9gQ4uw9MPrs38s_iH1IBAXIykPOXFDr2-fZOZMwzvZdjWKFvLd1Jpiz__JCWuhFxQCZ2rtgCxUK0-sFtCRbCHNqiTonGNC4XFmUT4sdBklrXJ3HCYqaiXDG_dWpsqVwOwf2m3FLPSSRZnVpad6tCzkbY2RYh7Zqe6yfVoW_UeH_kkJ5SH6ZHUPsv8-RAYWwHt-rRpmK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123478" target="_blank">📅 14:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123477">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNso9FVU-eyJpfvEwMW0vWTM8yPebNKP5jWvLGkrtLkYeJchushr1sIW3zJk_PZh_Mte20dmceKekKKJ0Lk7CWhbJvEhMFIwYg-Mi3DryFtQD0aysRsruu_5rLn8MKnSyEB5phu0VT7Yx6zfb85y17EAoO-XQJDksn0oX8cq8RCltsRJcTK9xu8BtB72zB0w8vQtBp4wyusEGB0AKj_BqqoLZksMrlSNr1ejOes5FfSkWwqdOcA6pjyM_UcAgmwDOxnZUtDD496hvl-auvMNYaFWCik1yme4Z0T_oFntlEQ8IKj3u5ESPMBwQtr3BiXkXpM32mCZrWp7i0-8wNl5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر یوه‌مور الشافیق در جنوب لبنان هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/123477" target="_blank">📅 14:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123476">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTcH9l8xgveE061xs0BT4AxokmucT26uXYS08dfA8ZQd7mFa7e2OcbHgGRp0MVwI5wE3xQBLPIGHbfaAhxEaSe_EoWOn_VlWtakZfAXQxSUEiku4GvKVsgkgaBUc2eEEMHE4Z51XmpOjVtuiua-5GQUiLICxy279QXkwjpS7k7XUlpptE0Q9iJb2APU5fCRUWdyRp4Ox8g5xKG8abETqFV1C5FguGmfx9Guw0hlmOwz4CS8l5o0jjQsBB3uNiqJ1R8x8Th6r4WEvJosUYHrVYUYZyuST3g-CtORs6eeBeHCAUTQwBfKgPxBFdgwcILbD4sSEwS_AvXkCxxJnGmipPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: به قدرت ایرانی‌ها تعظیم کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123476" target="_blank">📅 13:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123475">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf3edc94f.mp4?token=QbKp64IMWOT78kdVai5AbbOp33Rvgn5Wpt2rFtZ-CNt3a4Qw_oh5lKTTOhTWo2odko3y4QbKR3r334dsopvoDv32OYRHHaYyOHiTWMWlknbvX5mhb_PQcVw-k7m9Ul1_aDY3G5kPShLdY-R_8lLYXbEFkWhbjuHIx46h0Baku3vkemdaG03AnQ43JE1G42cy84XQSgtCrMLN1-H_bGWxqFfBUr2tjw1uRjzIKJzTfQztpXp_ExqBcIJG5Zk1e6c00cVxpDvPrDTPgS34oEVF5XcKXlg6OTRAYOGRLzca8cnWFErTm_SftTGf9ZGinLIwFt3w_43daPT4xiyfryLmPIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf3edc94f.mp4?token=QbKp64IMWOT78kdVai5AbbOp33Rvgn5Wpt2rFtZ-CNt3a4Qw_oh5lKTTOhTWo2odko3y4QbKR3r334dsopvoDv32OYRHHaYyOHiTWMWlknbvX5mhb_PQcVw-k7m9Ul1_aDY3G5kPShLdY-R_8lLYXbEFkWhbjuHIx46h0Baku3vkemdaG03AnQ43JE1G42cy84XQSgtCrMLN1-H_bGWxqFfBUr2tjw1uRjzIKJzTfQztpXp_ExqBcIJG5Zk1e6c00cVxpDvPrDTPgS34oEVF5XcKXlg6OTRAYOGRLzca8cnWFErTm_SftTGf9ZGinLIwFt3w_43daPT4xiyfryLmPIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشتی‌ها در بخش عمان تنگهٔ هرمز، یکی پس از دیگری لنگر انداختند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123475" target="_blank">📅 13:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123474">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGDbDw_H23gBcc-yzQK_K7kJxbjBCMFdXIR4Te3mZ4eHu3GfnCQtT7gcOOZh9SFtANpwHAXpWqL2ygKjPNvcmZmU5Tcgvm_rze_w-60WDpt9Sg_GXSZXEnyl0CPQYbFFpDyhyE4bUw_QpxFW_UeN7wRdFUHabzDB6tA1H1B2CKP5_OZY6I6C_dqloiJU2PiVblMxlwdBVya06L1-23FxSm7jhR5j_sd46Vexd_4QBDlaubH5oXxr6RyZzgeUs9j9kq8GgjG07owJXIzn32LHZ4EKc0GCCg5YAHmBggwgKp_5ROklCD57nvUiHIrvtnnbPi3FKUnnNcNxQ3qKJVnmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس تحلیل نشریه اکونومیست، طرفین درگیر ممکن است بیش از هر زمان دیگری به یک توافق نزدیک شده باشند.
🔴
با این حال، این توافق جامع نخواهد بود و جنگ را برای همیشه پایان نخواهد داد.
🔴
این نشریه در ادامه توضیح می‌دهد که چگونه ملاحظات و بازی‌های سیاسی، عامل اصلی ارسال این پیام‌های ضدونقیض از سوی طرفین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123474" target="_blank">📅 13:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123473">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
کلش ریپورت به نقل از وال استریت ژورنال: وسواس شخصی پوتین؛ راه‌اندازی پروژه ۲۶ میلیارد دلاری برای افزایش طول عمر و مبارزه با پیری
🔴
طبق گزارش وال‌استریت ژورنال، ولادیمیر پوتین یک طرح ۲۶ میلیارد دلاری با حمایت دولت را برای تحقیق در زمینه افزایش طول عمر آغاز کرده است که گفته می‌شود ناشی از وسواس شخصی او با مسئله پیری است.
🔴
این پروژه کلان شامل حوزه‌های پیشرفته و جنجالی مانند چاپ زیستی اندام‌ها، پرورش اندام‌های انسانی در بدن خوک‌های کوچک، ژن‌درمانی و کرایوتراپی (سرما‌درمانی) می‌شود.
🔴
رهبری این پروژه حساس بر عهده دختر پوتین و یکی از متحدان نزدیک او قرار دارد.
🔴
با این حال، منتقدان بر این باورند که این طرح تا کنون دستاورد علمی معتبر و داوری‌شده‌ای نداشته و به نظر می‌رسد هدف از آن، بیشتر تأمین و هدایت بودجه‌های خاص باشد تا دست یافتن به نتایج واقعی علمی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/123473" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123472">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نیویورک تایمز: یکی از جدیدترین و شگفت‌انگیزترین عناصر پیش‌نویس توافق صلح ایران، یک صندوق سرمایه‌گذاری پیشنهادی برای ایران به مبلغ ۳۰۰ میلیارد دلار است.
🔴
ایران در ابتدا این موضوع را به عنوان غرامت برای خسارات جنگ (که آن را بین ۳۰۰ میلیارد تا ۱ تریلیون دلار تخمین می‌زند) مطرح کرد. طرف آمریکایی آن را به عنوان یک «صندوق سرمایه‌گذاری بین‌المللی» که به تسهیل آن کمک می‌کند، بازتعریف کرده است — یک چارچوب نرم‌تر که از کلمه غرامت اجتناب می‌کند.
🔴
به نظر می‌رسد این ایده از استیو ویتکوف و جرد کوشنر نشأت گرفته است که پروژه‌های املاک و مستغلات تهران و یک ابزار سرمایه‌گذاری گسترده‌تر را به عنوان شیرین‌کننده‌های معامله مطرح کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123472" target="_blank">📅 13:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123471">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خوش چشم تحلیلگر ارشد: الان دیگه بمب‌ هسته‌ای حرکت جالبی نیست؛ هرکی اینکارو کنه معلومه و میتونن بفهمن کار کی بوده. بنظرم تو این دوران فقط جنگ بیولوژیکی و میکروبی جوابه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123471" target="_blank">📅 13:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123470">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر علوم: امتحانات دانشجویان تحصیلات تکمیلی حضوری است/ کارشناسی، در انتظار تصمیم گیری نهایی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/123470" target="_blank">📅 13:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123469">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
الجزیره: مقامات عالیرتبه چین در نشست آسیایی با محوریت جنگ آمریکا علیه ایران غایب هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/123469" target="_blank">📅 12:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqQMTf9SX3aANTspFHvQhiwV1m6Lxx4uiyxrGqHUGGqijsGtzCQVX_SbOhI-iUD18p2DucVLZxBVzzMzPffhQHn8ijq_SLqHY7eAFQjevHT52Jd0SchZ0xvsLXD6QRXC7A-cTyUcVD4GNUg_nZuov71gAYINcvuLmySovstUoGDLCrKsayryQzxODsdSJpAkPaeIvlnSY8-kgrk3TzWkQ7VOmjTDqcZUxopioMumkClA6edplVbKkyH5HwkJAtF7H8U2NUnwppKDy9ZDxSvVyO6n6jrj2QmH-rI2c4gUpUVGl_c3l5h5Zepwv9UmYZXlVU2oPeAGBQU8C1gZu0JGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان بی سی: خشم ترامپ از عمان، «سوئیس خاورمیانه» را در کانون توجه قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123468" target="_blank">📅 12:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRCgmNfLUTIh31J2FOLw9XmgglR96tboKPb6sow2TCfX18dflJLoM2VslQwkzgcmh0HQ2_P5W0miuUIgCC5ukhM3Co-6fW2k-FUPU9OwwjempYz4i3QsPMdvwVRFdH7a7zXwvWNmFty67U6f4TcixurjK1HGouBR_rx8oXV_e77a4HoZ1TpvEPeLBsMUsExesTuAtnOPhaQw3N_CZvsZ795aAtoDms-fo1P-GtmT3uYq8X1lfqUJWOqM2-1tVzXv7GouvtqHzgAIdk00dw4P4sFeadrum9p4D9Wtxe9F__UO7xzxtbnFLSMcsYtxnRTQC-EyRxbi19uIn6sG1ecsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای جوزالم پست:  یک شرکت اسرائیلی دریافت که هکرهای گروه «آدابیل میناب»، مرتبط با وزارت اطلاعات ایران، در ماه مارس سیستم‌های حمل و نقل لس‌آنجلس را هک کرده و ۷۰۰ گیگابایت داده را به سرقت برده و عملیات پیش از جام جهانی فوتبال ۲۰۲۶ را مختل کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123467" target="_blank">📅 12:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123466">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu22n4cw_8k2LWJRwNo11h0Nn32Ju4Bn9ogrP9jakxoUYWsZU-ozfRydrqM6HLy4OGsyBeWRsb4fnRSTZgoA6g27W1y0LV-s8LVmwOs8vZrwcCb3Dv9AFLysUvolgrL1QarxR9_AMUZpKuGnlpKs7yoE_RjRIj9cpcJLAf3BkOOkhaZthAVui9d3iN0xpps_nw_7sXGn7G86nOb5LTRmNQ3GpkFh6rW36YQYguEN5EIyQDogpaBWfjWKCuHQUlslEGVsk3GxHKZEnF83HwT0IlaV3yxB12uMDPwyvfDffWpdz27uxmqkv0MnBqHsVQLokSPnfz1UonD_7F3JstTXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر ایالات متحده در ناتو: ما در کنار متحد ناتو خود، رومانی، ایستاده‌ایم و این تجاوز بی‌پروا به خاک آن را محکوم می‌کنیم. افکار ما با مجروحان در گالاتی است. ما از هر اینچ از خاک ناتو دفاع خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123466" target="_blank">📅 12:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123465">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
درحالی که هنوز مقامات ایران و آمریکا تاکنون درباره توافق احتمالی موضع‌گیری نکردند، برخی منابع پاکستانی از جمله «خبرگزاری رایت‌نو» مدعی شدند که «ایران و آمریکا اسلام آباد را برای امضای تفاهم‌نامه انتخاب کرده‌اند.»
🔴
بر اساس این ادعا، ایران ظرف ۳۰ روز تنگه هرمز را مین زدایی خواهد کرد. بنابر ادعای این گزارش، کاخ سفید این توافق را تأیید کرده است، در حالی که سی‌بی‌اس ادعا کرده که این توافق نهایی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123465" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123464">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ادعای معاون رئیس دفتر کاخ سفید در امور سیاست، استیون میلر: ایران امتیازات قابل توجه، مادی و چشمگیری به ایالات متحده داده است که تنها مدت کوتاهی پیش غیرممکن بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123464" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123463">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل: معاون فرمانده تیپ شهر غزه در شاخه نظامی جنبش حماس را ترور کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123463" target="_blank">📅 12:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123462">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رویترز: رئیس جمهور آمریکا در تلاش برای پایان دادن به جنگ با ایران، خود را در یک دوراهی می‌بیند.
🔴
او تحت فشار است تا تنگه هرمز را بازگشایی کند و قیمت بنزین را در کشورش کاهش دهد.
🔴
در عین حال، اگر امتیازی به تهران بدهد، ممکن است با واکنش شدید تندروهای ضد ایرانی در حزب جمهوری‌خواه مواجه شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123462" target="_blank">📅 12:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAyQISPRqJkdEhccsUMFl9d62tZvX2L2-IbOk5unbPdvd_HFWOe5Sz2hkBP71VrHybSYMrqPQvHutDWU-rK3nhzsFM-ntXwTCurpvXQ64sOM6Gpx3U8N1sTtSLcZaswkkrOaeu8R1L-TOL8edREAeIFRkU4No4a07Gh4JVSpctSVaiOyDTl7vnYkKDTt21FL5E0wHBd35mzUI_tptU7OKOBaNfDG0QWljgVBY9k9W8OOhRXUVcOEs-xWnzZEmN6_F38YhHJFPjplsqyDqpqsEAnbqH2pjlNhnQlNKF03jXfUtCkDa7eXu9h3l0LX03OHlNPOTJuuYwqdQsJG1k_SGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_hl6mfshzT_DZKRkM3kgLg8nLM5uYUbp_clkzyQwYroPU-g3ulFhz_nQWj9WBi6Tp7N_aiNZn93PX2BmNstTMMW-dvzXnYZ0ALIpgD7K7zeE-e5eEjseWm2CDbkfkQRAiA8vz4HTknpaeomxDtxsA9raXtFdJP84ZOkNOx0ZTwLHoLVRBKgQy8kIRY5w5-a1Q4nhepujeuJvm0dzC_2oJSATMrBpMUfE7MdAz-aDo0O3o1s6LNKJJ8DfdKnIPU0YeHzK-SsXKNks6JFLtdd3yC-Cj-ZKoGnrnL6f8ulllv7MrFh2XEnH4qP9UsTEqZWKmzXGupm_KQcfuww5SK3XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e86046fb.mp4?token=IJGaPeXZ79Krd71nMCCIWiNgYdvLhLL1uaBwebuZSskd-hUiJBfkERvHOUE4N6nwL37nnMYhQ4hdaGsQBBP-xe_sCwXVFlXAOFHWzSrcnjUvB3MHL0skE9H8Tyld-3lgXos9ZI4cGdFj1AK026mNMg_RBRtIOoFibm4RvSlbQmcDIzhjv2m7KaTZYB3mHJjTwszNBiPGsitL03KC6CRTBCydpZOgCWFE47VveyWnR7f8kyQk_C-bNkrmt4hBFywiJpNYwUdjcNhvFCKHG4LSY-4ie3PkCKVAY23F5yoTuM_npt5NU2fcY5sTzUI-NGPLUXNLCTcDoy11wEVrX3RUZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e86046fb.mp4?token=IJGaPeXZ79Krd71nMCCIWiNgYdvLhLL1uaBwebuZSskd-hUiJBfkERvHOUE4N6nwL37nnMYhQ4hdaGsQBBP-xe_sCwXVFlXAOFHWzSrcnjUvB3MHL0skE9H8Tyld-3lgXos9ZI4cGdFj1AK026mNMg_RBRtIOoFibm4RvSlbQmcDIzhjv2m7KaTZYB3mHJjTwszNBiPGsitL03KC6CRTBCydpZOgCWFE47VveyWnR7f8kyQk_C-bNkrmt4hBFywiJpNYwUdjcNhvFCKHG4LSY-4ie3PkCKVAY23F5yoTuM_npt5NU2fcY5sTzUI-NGPLUXNLCTcDoy11wEVrX3RUZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های صبح امروز ارتش اسرائیل به جنوب لبنان، صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/123458" target="_blank">📅 12:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل : ارتش اسرائیل خود را برای افزایش حملات هوایی و عملیات زمینی با استفاده از تاکتیک‌های یورش در خارج از خط زرد در لبنان آماده می‌‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123457" target="_blank">📅 12:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191d8e1a96.mp4?token=rhWC3c2Th5-arLD_3XeVIGXi8QRzZ1pyusa8Wcc4s1PMtInp5e5ostCAG7snjWJi9VsUhOmjE7fRI6R4r-sO-Ek2G_SJ6D279-xFNdvT_avFfm0b2BN-mwIFHVqbULdgg5ssuLrmhK90CyKynuTX3FTQZMCRwFaN3lDB6CPZ9BbqVJvV7Gk1HXEagLoXHJvVYadWneAeEJQwWKK8MybZUQWRslBFP6BO9KSl2-E82xSTFSivsopraK75AWxKbQaaGVsozADfR7mTDY1gLATe2woQcDxXTdOkOk7YzPLRB_JY-69E_7EAhvPdi7QNLmpOUJo2e8PBymM2IOWtLxxA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191d8e1a96.mp4?token=rhWC3c2Th5-arLD_3XeVIGXi8QRzZ1pyusa8Wcc4s1PMtInp5e5ostCAG7snjWJi9VsUhOmjE7fRI6R4r-sO-Ek2G_SJ6D279-xFNdvT_avFfm0b2BN-mwIFHVqbULdgg5ssuLrmhK90CyKynuTX3FTQZMCRwFaN3lDB6CPZ9BbqVJvV7Gk1HXEagLoXHJvVYadWneAeEJQwWKK8MybZUQWRslBFP6BO9KSl2-E82xSTFSivsopraK75AWxKbQaaGVsozADfR7mTDY1gLATe2woQcDxXTdOkOk7YzPLRB_JY-69E_7EAhvPdi7QNLmpOUJo2e8PBymM2IOWtLxxA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگزث در جمع سربازان آمریکایی:
"همانطور که رئیس جمهور در جلسه کابینه گفت... ایران یا می‌تواند با یک توافق از طریق مذاکره، کار را به روش درست انجام دهد - یا می‌تواند با شخص من در سمت چپ معامله کند. که اتفاقاً من بودم - اما این من نیستم. شماها هستید."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123456" target="_blank">📅 12:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f31aadf8.mp4?token=BKNO8SlYh0EoR486c0ZYmTZhyroSL6khCqnxuRxOCe8LnbvqLltpQLb2F3MHZil4m0m8Jm1Q0MYqRdeXcK_9IjJ6p6bkEZusM6pHtSyHYlDcYcKLSA5migx_Mk4om2QRqwqvi8flDbY98unP3i-RznZ0YFO_tBsNmCaYI9GYKrX-Cye--qJTHpQ9R1QECPCGSprAgWn2WCcmgeFIn1X-_Rr4lFJA6JrHsGmXJcuQb9agZneOiFTQw5PMvHQH69yJgErtTVOdyjapNkb_znLt2pwACc36FG10QoiXJ6pWK39c9fn8kr1w5Zf7hTerEsKfgVfYQTbhMf6SA-jLb2FJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f31aadf8.mp4?token=BKNO8SlYh0EoR486c0ZYmTZhyroSL6khCqnxuRxOCe8LnbvqLltpQLb2F3MHZil4m0m8Jm1Q0MYqRdeXcK_9IjJ6p6bkEZusM6pHtSyHYlDcYcKLSA5migx_Mk4om2QRqwqvi8flDbY98unP3i-RznZ0YFO_tBsNmCaYI9GYKrX-Cye--qJTHpQ9R1QECPCGSprAgWn2WCcmgeFIn1X-_Rr4lFJA6JrHsGmXJcuQb9agZneOiFTQw5PMvHQH69yJgErtTVOdyjapNkb_znLt2pwACc36FG10QoiXJ6pWK39c9fn8kr1w5Zf7hTerEsKfgVfYQTbhMf6SA-jLb2FJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورزشِ پیت هگست، تو سنگاپور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123455" target="_blank">📅 12:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ویدیوی حزب‌الله از هدف گرفتن دو تانک مرکاوا در جنوب لبنان با کوادکوپترهای انفجاری ابابیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123454" target="_blank">📅 12:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZeaVtBp2XqCIVj7FhQqYpy6L8tBkSo_uKsDu0XDm2KgGi72FLE4yF2tkTNlgSUZ1IcXGl5ImsqreHe9pmg18SbKWZfsrC8P45qtjKL0vj608NhLE9EFI7F5b9djGG3y_APlCthx4uHBXdB-gWXtvEU8lXYU7Y7oleErdjydXLYqzejCgvy4OJQaiz0u66BkVVzZHcW3Kh1s85m15e8Zjh58sWxLw_cGNrJi5IRAD9wCO79aAqny1CAkOqSuqHYhgoshI1CPbKUNs-KtwAk5djvUH8UaYPrM0PCbYjxa9jfyS5rRbCjSmfCGONfjiGEbceEXAg8DnMC5eblHZMLK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سرعت با بهترین قیمت با God Vpn
🔵
تخفیف ویژه برای امروز فقط
✅
😍
10 گیگ فقط 210,000 تومن
😍
با استفاده از کد تخفیف  ((Fn))
متصل حتی در شرایط جنگی به خاطر اختصاصی بودن
✅
❤️
😍
کد تخفیف:
Fn
@GodVpnV2_Bot
برای نمایندگان پنل نمایندگی فعال میشه
👍
❤️
✅
تضمین بدون قطعی
🌐
اتصال با تمامی دستگاه
🔻
🏪
پشتیبانی ۲۴ ساعته
✔️
دور زدن نت ملی
🔘
بالاترین سرعت با تمام اپراتورها
⭐
با کیفیت عالی و ضمانت بازگشت وجه
🌐
🌐
🌐
🌐
🌐
🌐
⭐️
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
جهت خرید کانفیگ اختصاصی در این ربات:
@GodVpnV2_Bot
ایدی کانال:
t.me/God_of_Vpn
پشتیبانی و خرید عمده:
@Mmkhh00
@Pc_V2ray</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123453" target="_blank">📅 11:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
اسحاق دار، وزیر امورخارجه پاکستان برای گفت‌وگو درباره مذاکرات ایران و آمریکا، وارد واشنگتن شد تا روبیو، همتای خود دیدار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123452" target="_blank">📅 11:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efcae5cf4.mp4?token=BVbhGXIeWJCN64048HrrWu-PreTTh6fsYVOicKOgTykguuoe9F7EAy3_2Ak3XYX9YMfdjKhtA3_LDLZ5-3G4ZBJNMAZRdgwsOUDpKPscZVjRW_PRjGYOBGF72wwW_Q18z7viuUommZsGyUoVXGwtnN5-mGqOmOLTQPoOBoTOqK3LyMyErBHL165qacb_X-F7sxM495_EC9EmHXOnIjqCalmN2IwlWAyomPeNy75wqTJho_EPC7BZf7lqHCullU3NKRfckXhmCWaYC4t3vvs9mW2aWzKWoZ39ZJm7DOzspQBZMM9EvATy8Nk3LUdpYv_LWFWR8j67M6E-fLoqM388Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efcae5cf4.mp4?token=BVbhGXIeWJCN64048HrrWu-PreTTh6fsYVOicKOgTykguuoe9F7EAy3_2Ak3XYX9YMfdjKhtA3_LDLZ5-3G4ZBJNMAZRdgwsOUDpKPscZVjRW_PRjGYOBGF72wwW_Q18z7viuUommZsGyUoVXGwtnN5-mGqOmOLTQPoOBoTOqK3LyMyErBHL165qacb_X-F7sxM495_EC9EmHXOnIjqCalmN2IwlWAyomPeNy75wqTJho_EPC7BZf7lqHCullU3NKRfckXhmCWaYC4t3vvs9mW2aWzKWoZ39ZJm7DOzspQBZMM9EvATy8Nk3LUdpYv_LWFWR8j67M6E-fLoqM388Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از عبور موشک های تاماهاوک از عراق در روز اول جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123451" target="_blank">📅 11:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123450">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjyU6kjBlVemdfnfCZB17cdLFURkPhPaApsLhWM-zxoOT57kJ9_-HF5UqErV8kWDrGg1Vq-Pt3wZbQGDvEKR-PqowjufGXJkcppZ3k0sayRTLMQ7di-SyqjeQDMN2ZCzfqQROHyERs7Syn6w1B8DV9GxKy18W-CDuFuQ8AvG5Kbq23juF4oC9jb6NWa95Ex0izrC4Z3I_fruK5VDUmbYgQa6b2JVniP351HHtj1be1dsnrEde7F4AUAJtcctGHhPkEfDi9GSZvu2T9iH1X0uKt446gmka_43BujPlIT-koHNNQ4G2Lo3Ji56Ik04DzubeVmaR_6MRRoAeCBER83oLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بسته بودن تنگه هرمز برای عربستان بد نشده، چون درآمدهای نفتیش قبل از این ماجراها ماهی ۱۸میلیارد دلار بود، اما بعد از جنگ به ۲۴میلیارد دلار رسیده
🔴
عربستان داره نفت بالای ۹۰دلار رو با خط لوله می‌بره دریای سرخ و از اون جا صادر می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123450" target="_blank">📅 11:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSA-65XMcsHlHTOdKF889nxFO-d5b95rQ11ikQBiSu4Vw2eoTiO9FHTbTx16oiHr50ECWmGCV6ARAdnDq3laWMw9HX37R1S4thzH2vaGF6qLcv9rOgJ7MCS3mF6PLBD5CPKWSeVI9U88BKM6PPE7GdDqKK7wyiKl9iGybGiKe6dJK3bSDc_tW0g2jSrbwt8Dfbo-nuYHfJxrGeYkPUh6F8qlZ96nd4etzlyl8TsxPt_aEWO79A3Ai0NPGRezzeScdMTBHAYRbpypAlLfX77d-7tLARoMj3Ir-iAqwLkCF5_u_ZxrlWgLqaI94bkRTa6pYUpAsCMtteNCbqqHZplSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdmA5H6vPGuJYSYpqRF80CUkl2i15K8Wgl5Nek5720aR0uWIjWiIWDvgFFcNt9uYylrLxabek4PRUqftpsLb9vcFg2fGqBGskWk1AH2uklHEEkfLP_mCEuAKYw_CJS53EMNXs_JK5MnFsXR1LwN22Mu4TTBcKlEkg7EzaMMiWYhU6TjjqXYeBshmdiueYtsgt4UT8vBsw6VQdUtW4Kh0EeSZEP-HTOuTO8cjmzvuIMtzpvm8iepq_A2iZWhsN6x97sybvlQdmM94mXrL-JmCN6rMb_li2o5r1-wKEP6XNC4XPLigW6HkEWYoLU_DWB6UspJavDTh5rfkXAuCeNBibg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل در جنوب لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123448" target="_blank">📅 11:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPIUoShKG3LCOWQMdNG1qMr7oPSxMramWbf4V7gE2nO-UCz_TorU7XBbFgap3ysn1DtCpQOaMpaBdyfG58kkMJbraJ9uW8nnJsLoH1dwUkWaOLjoLCJM2xSWzINo1Hu4fVEipT7NHO9p_TCo9zCYpqtWRQqN0EQ3qTBKEDYOYPBIqVMzwY1MajOGEdaQ9BdrkTBfQhCPQgM3qnmQXUKuz_kEKHOph87yRvFFuf9nRT04pxQLoMtb50kVmxLHbJPFitSP5om36Az0Thf9Z-zcQ6MskgNG7ZXYzzAh6JF5mPQ3tzAixsOWXRt5v-HvWWLDZn3unxGYuyLbO1sOqnKxtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
آمریکایی‌ها نیروهای بیگانه فضایی هم کمک گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123447" target="_blank">📅 11:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
حمله حمید رسایی به مجتبی خامنه‌ای با داستانی از پسر نوح
‼️
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123446" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iZyOBdiWJUNBXy5AS6cHdMHhtcQKr18GrVQO_W8c4IaA8zEBkgplU87Kq2QXUrUQzDdp-F2d_3hFTLStnnfpClk2Wfa-3gFcDVK5Mag21V89WCLXuy-RLn0TNuDJk6h3l9wvWGEdO4l4WTUp34PQC0zxC3qT38aSF8oYJhJBW_v3_zgWggdNSyFlnxlU7GQA1SWCbp_us08ZGeD8fTN-pZKB0VE1NBNJpOiJ3TpQOctNmcO6EzUFP29vy66xa_gcCS56LFth2D-5CafEBM9fvWz2iws5ANLh6P0uwCciK3yFVoMW5NdVp-Ehd9XSSIWMQT2h1w52Pc_wRD7oeC7eUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله حمید رسایی به مجتبی خامنه‌ای با داستانی از پسر نوح
‼️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123445" target="_blank">📅 11:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
دمای اهواز به ۴۸ درجه رسید و به عنوان گرم‌ترین مرکز استان ثبت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/123444" target="_blank">📅 11:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123443" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6af910a6c.mp4?token=Ro6k4jbkk-gFMjci6HUa6JaHn4aOc1hoCM6zRXQnjqRR6qNtL5tAoBWllbTQWIi3yvoB482JwsgCCm4VCOSheTLNX8rd3w5E15RzggHJMyKhvcMRp-boY06fF7qZt9DA-ImTK7bLgZakyK-kBW-m4stcA47bbh3zM0OJufLf0UKbqxqsV17AmX36lsj0qxh6CdKHllRrv0HIlEATzbB6X2V5g5ExAy3Wc0aB9tp0f8kKRTCf9TwyOxXf-INYuR-sBcd63H_15dIbsbxHWf3VNvDIp3iUiIe8WIevnT-1YAgShJsFKfn8JczNqCQ_CQvzRuhSWRZN3JkoMyPEwR99-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6af910a6c.mp4?token=Ro6k4jbkk-gFMjci6HUa6JaHn4aOc1hoCM6zRXQnjqRR6qNtL5tAoBWllbTQWIi3yvoB482JwsgCCm4VCOSheTLNX8rd3w5E15RzggHJMyKhvcMRp-boY06fF7qZt9DA-ImTK7bLgZakyK-kBW-m4stcA47bbh3zM0OJufLf0UKbqxqsV17AmX36lsj0qxh6CdKHllRrv0HIlEATzbB6X2V5g5ExAy3Wc0aB9tp0f8kKRTCf9TwyOxXf-INYuR-sBcd63H_15dIbsbxHWf3VNvDIp3iUiIe8WIevnT-1YAgShJsFKfn8JczNqCQ_CQvzRuhSWRZN3JkoMyPEwR99-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت یک بمب اسرائیلی از نمای نزدیک در جنگ رمضان
🔴
ترکش های این بمب بعد ترکیدن به صورت واضح معلوم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123442" target="_blank">📅 10:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کانال ۱۲ عبری: ارتش اسرائیل خود را برای افزایش حملات هوایی و عملیات زمینی با استفاده از تاکتیک‌های یورش در خارج از خط زرد در لبنان آماده می‌‌کند
🔴
نهاد امنیتی اسرائیل نگران است آمریکایی‌ها به‌زودی برای توقف حملات بر آن‌ها فشار وارد کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123441" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123440">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6561057fba.mp4?token=CRLRSIaVJd4fhUZlh1uxWzX5WU76uUM7am5x88ofZbRXlF1d6CGPxshwcyCEBJAmGvI0iAC_YvABerA59NFhKgd_BCb2pxGuWrKs7G-Ce7Zf-01E4FJ0KDE7tbfdnBLSVaZcbc5KErIT4k7STbT0YIaPKh33Jas0UwEO_baImrir5KJlbcNAbo5pKGvFd1InmLCGd4Ze_dGb8nEV4qT1xPDZC_VyGEJSR5xlwZUcPALzxw67HJEmvHARsvwSU4Lu555Xu2irabVFP0mU-F9LjM5hdGOVmHjJRBp9GBjfrWcjEdb1bSJm-rlPRA9xektPWytCsFUdOaWJozAnC4Lwgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6561057fba.mp4?token=CRLRSIaVJd4fhUZlh1uxWzX5WU76uUM7am5x88ofZbRXlF1d6CGPxshwcyCEBJAmGvI0iAC_YvABerA59NFhKgd_BCb2pxGuWrKs7G-Ce7Zf-01E4FJ0KDE7tbfdnBLSVaZcbc5KErIT4k7STbT0YIaPKh33Jas0UwEO_baImrir5KJlbcNAbo5pKGvFd1InmLCGd4Ze_dGb8nEV4qT1xPDZC_VyGEJSR5xlwZUcPALzxw67HJEmvHARsvwSU4Lu555Xu2irabVFP0mU-F9LjM5hdGOVmHjJRBp9GBjfrWcjEdb1bSJm-rlPRA9xektPWytCsFUdOaWJozAnC4Lwgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترافیک دریایی پشت تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123440" target="_blank">📅 10:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ایران تهدیدهای آمریکا علیه عمان را محکوم کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123439" target="_blank">📅 10:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: ایران قصد ندارد اورانیوم غنی شده خود را به کشور ثالث منتقل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123438" target="_blank">📅 10:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DSF7xi_TKNGRkSH8PLnjl3UkOzvOy6Pn7H1mggnR9f3m1BhiCci5MP0M-EkcxZPRMgvkGDtuMmEBrhITK8imLS2whk2YtjWBokaZR3MlNwQqjxyE0x_QeA8FdKwdzF4hRTQ4IgMeJdraH-SeFFMvctk0MSAzZA4mRcoPuQ0pGXB6TY_EGr782H-MfzwzKqaTUv0A0W1T7eBin1MV_TFqzmuYcQX4coRIofnrQy_Fp8cOyUPy1RzftWbynjQNYP6FPBzBWvljbaGi2hEu0VHpUsdqNzX-8_d5y28ka3R2KRn_9IZepE012rv6LtfTv113yoMGyrFsZ9eZmg2Q2aFUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qytOcVMpHZtDlTMpi0m8YyXwoUeXkuX000y57FdOdVyxDUFgcQHaMSP3ndcMfyXsSvQti9A5udKTRtRc17YATOcVEGektplhM9dXgJpdxxIo3dgjVB076SRmM0Nqz4QbfNCrpftGv2a4PUdHz7SyJ0-obZjJUDhP4sM8DbvTN3A6U87Ov2BOwMN0N5tTU3f2aVb_K6kPivXbGqYhabEOm_ZQEs0WmW_7jBtsw85HhqYrEPdsJvP3lK2jqvunCDnrGTVrdDkISQR7ItANE2lq4EBLFfueTEyQ29R_cJpw461X3HarOVnxPG5_Y37QVDsJrM2958dq1aXT6TUGcY-41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JgPPVF82XVpNdilZBWdVVQPZWWbbA_d_ssKcozCVb_dI3WDPbChWhqdaup6W0NGVTsnTsZt79l7jGeFtPdzEglxE9GNUFdUzrmrXgtvfn0IRTM7yUYINjkPifQ4D5-hK8qVHmk4dQD875Ln4OPKPQmf-5ASRDnpCrFfykBGASM2zRX2hTdchzxPe5wH3MZAYbPOyAjAmh34SXoliftf43xthbrnjtW5IzT6fJbpiHQn8_UY6MkFNkNj8X407v85Jostnxhpf-nfA-yqhbm4fJIO0u28AB66JOuzFMAkA9vauxjZHaRkk_KwDoLRSP3ehA4mYSfvUu4VoRQ_51_4dMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای منتشر شده توسط رویترز نشان می‌دهد که چین سکوی پرتاب عظیمی به مساحت هزاران کیلومتر مربع در نزدیکی انبارهای موشک‌های هسته‌ای خود در بیابان سین‌کیانگ در شمال غرب کشور ساخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123435" target="_blank">📅 10:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-6_yjlp_7sA06kEkpo7GRb9wS2jSZCIdgeGTBAn60NBjlzHq0UXnxkXR_02YYV-VvBV56kJMbYD6p2i90IryO8sF4rRBWeoHggB6MaK_CtF1fywPKC7VxZ6Gnbt9rLOoHfKcTg_eRe5d-1R58_j0Zr0Nr1U0wssCzdreu-6Zq2c5bAOB4Kyel_tVP60-0DCvRrlxIpVgYvYkgR3nXPst7wCJYk9-N6Lw9Tpyl8VZIzTy06foQHcQOwqEHekxLVMh-343es-anXZyIoAsG9JvVFp4WC6_qziUdhc_bJj3DfStE9rX7T__93YNE8Bb8suTva9zvHNp3JEJHDuGWlAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی انگلیس سطح تهدید در دریای عمان را از «بحرانی» به «شدید» کاهش داد، اما تأکید کرد که تنگه هرمز همچنان در بالاترین سطح هشدار یعنی «بحرانی» باقی مانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/123434" target="_blank">📅 10:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icYGpsIErVU3hWK5wpIuur8xLuGk1ahA3BAy2yguNgzvp4MKLyAqCCWsSiowIfcYfdnDdFOHNMTk1rt0REX1p__pAOHJB5v1-M6cRJyOioMNje8cFbDoI7jR5IlkjT9R3EavReN6ZIDADDF_tF-7cJ7N58VmyaahiiHHgEDhMPkAsJmz5ZRLSiBSz_1EqZZZ5epQ-8A-o3m1uZR3whajhWlRn_pBqAqqQXXl-ABv3myOJS_aLJTqIQd7Od-Q17XOmRP7PaOrVf8ID_fzFXMXzNXJNvfVOkqMYJWNAOwpgbRiRVGx6NY3SFpyaEWyWQacPV5trS6A5hYWdU_0kTxAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره:  رسانه‌های اسرائیلی: دولت اسرائیل وضعیت اضطراری در داخل کشور را تا ۱۶ ژوئن تمدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123433" target="_blank">📅 10:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
الجزیره: در ۷۲ ساعت گذشته چندین درگیری جزئی بین آمریکا و ایران رخ داده
🔴
درگیری‌ها به اندازه‌ای نیست که توافقی را که «در حال نزدیک شدن است» از مسیر خارج کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123432" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فارس: حدود یک سوم ذخایر طلای ایران به دلیل قدیمی بودن تجهیزات و روش‌های استخراج، همچنان زیر زمین دست‌نخورده باقی مانده و این مشکل باعث کاهش سالانه ۶.۶۴ تنی ظرفیت استخراج طلا در کشور شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123431" target="_blank">📅 10:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlA26G-aOyNC0VaM7mUNY4PDprZ2gOXctSvev-neU-T-ZmvybjfUfwqUx_hd-56XSKioYDRfDg_In_4KhEtt-EA5T6RK_WDWE0LKtjV6fWBAwPEdP8MeEdHaXZnt7-yjmdv3Ol4LFcQxBFdAy6cJ13eaduDzt7f7svZMepzm7XJCfA-mNwPU2t8K10sC7sWgZ23DvpJPEJ9KmtlFZzhZrFxlwM9t-6rwx9ytlXXi4gcnVGoRO6gzP8BxsqV9ImS_EJ_SECSgnYxpMw1qXlJxnOdB6KCwZC180p7tDSQ0-mIuda7411H1Ja-vrkmNsfa1rAzjLcHlZI7l2RAzbr2Bew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: قیمت نفت در پی انتشار گزارش‌ هایی مبنی بر توافق احتمالی آتش‌بس بین ایران و آمریکا، بیش از ۱ درصد کاهش یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123430" target="_blank">📅 10:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: ترجیح می‌دهم با ایران به توافق برسم، اما همه گزینه‌ها روی میز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123429" target="_blank">📅 10:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بر اساس گزارش الجزیره، با نزدیک شدن جنگ به ماه چهارم، سطحی از خوش‌بینی در کاخ سفید نسبت به نزدیک‌شدن به توافق با ایران وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123428" target="_blank">📅 09:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UOFM-A25UEfj_cbIc3OuJ_rNN9yBKitZQvQq2OsakHUlbfV6dD1ktoFHH66y8GYxZtzz-sAhEWDctmzPv1zFtgAvYk-conUcVFfximG74LFUY1GN9morVrwf6bU_YMwvdZkUQaE5H70JnLsSyDInYrMnO25HDAZ9XTUnp9YmqJK_yZNgHkWq6t7gYI6Pud0jSLcn2SHV5-f77O6j_rGG9fqDOh19r8M8YLR8OL6LT7C0VRIvYfdUbv3OB7BlE1-V5QLHFMkw4jK8BiSnLY3PoXaQlPaGG9leqVFw1oGII0QRq1-FnkIcw-52erQEzJuivvuhun_8n01yJNG8jiGo5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناتو: اوایل صبح امروز، یک ساختمان آپارتمانی در رومانی توسط یک پهپاد روسی هدف قرار گرفت
🔴
ما بی‌مبالاتی روسیه را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123427" target="_blank">📅 09:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس در گفتگو با ریانووستی: آمریکا باید در رفتار خود تجدیدنظر کند، در غیر این صورت موفقیتی در مذاکرات حاصل نخواهد شد.
🔴
آمریکا همواره بدعهدی‌ کرده است؛ مسبب شرایط امروز خود آمریکایی‌ها هستند.
🔴
آنچه امروز جمهوری ایران دنبال می‌کند، مدیریت هوشمند تنگه هرمز است.
🔴
اعمال کنترل و ترتیبات ایران در تنگه هرمز ماهیت دائمی دارد و بی تردید مقطعی نیست.
🔴
ایران قصد ندارد اورانیوم غنی شده خود را به کشور ثالث منتقل کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123426" target="_blank">📅 09:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزارت خارجه آمریکا هشت نهاد و هشت کشتی را به عنوان دارایی‌های ممنوعه برای حمل نفت یا محصولات پتروشیمی ایران معرفی و تحریم‌هایی علیه ۳ نهاد و ۱ فرد مرتبط با تجارت محصولات پتروشیمی با منشاء ایرانی اعمال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123425" target="_blank">📅 09:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=lkmZ2_LTmfaG5Wt9G517722xApS3XJf4VobB0i45v0STI-KExyT23gHl5ZIwzj_u7zGxQCYTvpaSWazlm7YpRiy9R42pjxjx_RtA4f5sJNv5v4Nuqav7QDyRW6vdr2d5fEjWLqzZm6PLQtmApDKulVYqVCrBUACN477UFcLDELNS_fm6Duh6cesMRuHDBw6d1V4f4QnMDd5e_Rn_gX5ak9j4HimW2CEqWPZJzk92ivBbvxmx3U2rSnjjiyLVYDfV2p2AnNbE5gtSjeEPYcxYVdHiK5AtALabOKrIVDOUaYe0Pp6Yvkaa16br3hyWuOyU-4TyFu5lsuHdqIr5nM5LCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=lkmZ2_LTmfaG5Wt9G517722xApS3XJf4VobB0i45v0STI-KExyT23gHl5ZIwzj_u7zGxQCYTvpaSWazlm7YpRiy9R42pjxjx_RtA4f5sJNv5v4Nuqav7QDyRW6vdr2d5fEjWLqzZm6PLQtmApDKulVYqVCrBUACN477UFcLDELNS_fm6Duh6cesMRuHDBw6d1V4f4QnMDd5e_Rn_gX5ak9j4HimW2CEqWPZJzk92ivBbvxmx3U2rSnjjiyLVYDfV2p2AnNbE5gtSjeEPYcxYVdHiK5AtALabOKrIVDOUaYe0Pp6Yvkaa16br3hyWuOyU-4TyFu5lsuHdqIr5nM5LCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
راکت غول‌پیکر مالک آمازون در سکوی پرتاب منفجر شد
🔴
راکت «نیو گلن» متعلق به شرکت فضایی جف بزوس (مؤسس آمازون)، در جریان یک آزمایش زمینی در پایگاه فضایی فلوریدا دچار انفجاری سهمگین شد.
🔴
این حادثه برنامه‌های فضایی آیندهٔ این شرکت را با تأخیر چندماهه مواجه خواهد کرد.
🔴
قرار است این راکت در آینده، ماهواره‌های اینترنتی شرکت آمازون را به مدار ببرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123424" target="_blank">📅 09:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae951ff3d.mp4?token=WzY-8tnCzFlqsVthiAYdsM8sym3MscIbiX_b2GFPwhH4uBnDsDFprNDGnd43BGL9CbuYsS5uqUWOC_Z4AusuUc4fDp1AopVP8YKF7CVi8uwE8sV9vetZWj5ul2he-WUnBNlbfeCKsMGbzptGGWMMtVKvUqT3QGS2hdl9LLvexKqom1NqpEh00R4wiBj_6cmUmiJ_nf444ghsXUXZkrcukUBMP6ukaMsaWY2uLhV3pjUZsSyPxOnMLP8NXQBdUe_UWJ04FmNmP8inT_KJkjD9zfbnDVYOLlT0n9yKV7jbLCuQymduvrFPea-pi9T5ptSZ1JMrkC-MbQXvjZHzpM9kXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae951ff3d.mp4?token=WzY-8tnCzFlqsVthiAYdsM8sym3MscIbiX_b2GFPwhH4uBnDsDFprNDGnd43BGL9CbuYsS5uqUWOC_Z4AusuUc4fDp1AopVP8YKF7CVi8uwE8sV9vetZWj5ul2he-WUnBNlbfeCKsMGbzptGGWMMtVKvUqT3QGS2hdl9LLvexKqom1NqpEh00R4wiBj_6cmUmiJ_nf444ghsXUXZkrcukUBMP6ukaMsaWY2uLhV3pjUZsSyPxOnMLP8NXQBdUe_UWJ04FmNmP8inT_KJkjD9zfbnDVYOLlT0n9yKV7jbLCuQymduvrFPea-pi9T5ptSZ1JMrkC-MbQXvjZHzpM9kXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: دستاوردهای ما علیه ایران قابل توجه بوده است
🔴
جی‌ دی ونس، معاون رئیس‌جمهور آمریکا: اگر به آنچه تاکنون به دست آورده‌ ایم نگاه کنید ،در صورتی که بتوانیم به یک توافق نهایی برسیم ،در حال بازگشایی تنگه هرمز هستیم.
🔴
ما پیش‌تر توان نظامی متعارف آنها( ایران) را به‌ شدت تضعیف کرده‌ ایم و در موقعیتی قرار داریم که میتوانیم برنامه هسته‌ ای‌ شان را به‌ طور قابل توجهی عقب بیندازیم،نه فقط در دوره این رئیس‌ جمهور، بلکه در بلندمدت.
🔴
این یک اتفاق بسیار، بسیار خوب برای مردم آمریکا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123423" target="_blank">📅 09:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803b57a4df.mp4?token=bfnr4Vr0ofy8GgJkKc_ZNEy2azbbuehepoU10d5gvAAtA1e4Q_3qMNbEevK5jxLEczGbGb_tXVrFg_FdXMiuG96SC2YYJwWoHR1fDwfo8SLKRHC3J-V1Jb8YZP9mV38KYyO-75kBs2RP-JKfoDoKIMP38jusrmMppQPvB7L26h_1pq9Wx0CIqieCupJxMMz3uXgoqlsgKb9SkIKM_UM06xtwSJsWD2aFKgz3uIDALnNY85ZQch26AJDZZ3LK-iItZy3oYJCrRt8Pu1w6Yv0tf7siimXf5rmnBvWZ8Q2BVGnfxMxJVcT1xQjewCpCyC_iDp23F-6fSD9f3oM-gMaIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803b57a4df.mp4?token=bfnr4Vr0ofy8GgJkKc_ZNEy2azbbuehepoU10d5gvAAtA1e4Q_3qMNbEevK5jxLEczGbGb_tXVrFg_FdXMiuG96SC2YYJwWoHR1fDwfo8SLKRHC3J-V1Jb8YZP9mV38KYyO-75kBs2RP-JKfoDoKIMP38jusrmMppQPvB7L26h_1pq9Wx0CIqieCupJxMMz3uXgoqlsgKb9SkIKM_UM06xtwSJsWD2aFKgz3uIDALnNY85ZQch26AJDZZ3LK-iItZy3oYJCrRt8Pu1w6Yv0tf7siimXf5rmnBvWZ8Q2BVGnfxMxJVcT1xQjewCpCyC_iDp23F-6fSD9f3oM-gMaIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی روسیه به حومه مرز اوکراین، ساختمانی مسکونی در شهر گالاتسی رومانی را هدف قرار داد و دو نفر راهی بیمارستان شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123422" target="_blank">📅 09:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت ارتباطات: داریم اینترنتو وصل میکنیم چون سه ماه قطع بوده ی کم طول می‌کشه ، صبور باشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123421" target="_blank">📅 09:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDbmFQLAHzwW5R4MbW9v2FtTr9vMMZ2csqnlDxxwY7srPJbGntlpBQJLsW-JSmz6W6AvOTch8xAOzA2owWcnHDrmu6TpEBdnAjLJuMp40hxBHsQxFaPQ4z_0hqJ2m2i_qABhXWxtVZoi6q1WIWTsMS4eX6J8tBXaBD8Gv8b73fe9zBUCjbZ5RhjKHvy4F4ClZLoKQzyDpaWpjRueB0EpN9Leoh27_8yGsDT2AIuGaagiFCX59F6aPSyRuLGfrz3g70QP3k1JF7X6LahY0X4yGcC6VEQlsdRwAYHA4rXSdXmZ02c6cNmcM5NBln11yuWDF0R0UeAQ_7wLO-hUIVNtOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید، نقشه پراکندگی حضور آدم فضایی هارو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/123420" target="_blank">📅 08:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Smbxr3bQ0qKDWvarGJOCAfB_ZXACi-36Hx2ziwU-rgr3TzOIwWKW0ji2Q8_NdLtW4AUl7WWEEqUpGgWpKwTlLnHncSuq6lsRkz3yCDCYkk16ruVSVNR9Ssvq7wSWLxnsLvnhV8_w8Ri0eP-modoBM24ZK67fdEbZwBUJLs_Wokncbc0vOCR_5djikF2yhT50a4XiUa2rICasfKcuK87xNKjzlficlqgMhHAc-P4n0Zbnu6y4WViBaehP9zPH9OJfVxBswcMQt06IB5ZIE0i_SEsfDgPmrgPTw8hkKGAN2Gwb7ePLwOVm0aCuMUde732D531L8L5sxyGvMoqVWI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: سیاست ایران گسترش همکاری با کشورهای مسلمان و همسایه در همه زمینه‌هاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/123419" target="_blank">📅 08:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOwe52Bdq6LVd81uj4yQJAl72TnRwhQ1mqWkI_bf7hqDXoEqgD47dpeH8QdqMMQt_zoS0qjKOiBt79P01n0vxAz7L1o0_TW1dA4mmomOZ-FPG76099pULFzGJZybFfzwmoBP5-8GUEl5_TGiOy0JXD6SMRyLCzf0tsdTnpp_gG-0VmkDQWsktZdwNpa7gw4YzocuixZtmOIOW6KC6O28WH6lDM5KMrU5HmBiTOFKAOthAyNHRptxNN_nr0Z4QLrZpNQ732MEjXNs8ia923b5JcXBlWL1nAauPEd5we_6ekv4W0fmheOMf9-7Rg39Eb7OhOxzcN1erDrAludlfT3sKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الحدث: وال استریت ژورنال به نقل از مقامات ایرانی: تهران نگران است که اسرائیل توافق با واشنگتن را از مسیر خود خارج کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/123418" target="_blank">📅 08:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
دی. ونس معاون ترامپ گفته دو کشور به هم نزدیک‌تر شده‌اند، اما هنوز توافق نهایی نشده.
🔴
هر بشکه نفت برنت به ۹۳.۳۶ دلار و نفت آمریکا به ۸۸.۲۷ دلار رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123417" target="_blank">📅 08:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سنتکام: هیچ هواگرد آمریکایی در نزدیکی بوشهر ساقط نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/123416" target="_blank">📅 08:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ونس: واشنگتن در مذاکرات با ایران «پیشرفت زیادی» داشته و معتقد است تهران «دست‌کم تا این لحظه، با حسن نیت در حال مذاکره است.»
🔴
ونس گفت: «ایرانی‌ها خواهان توافق هستند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/123415" target="_blank">📅 07:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e727e78c.mp4?token=SX-icqtH8T3ztnUmpLFb4rW_kWNV0Tj_v90ctLezcgl_tQHxe7vQlBd6tyvN5NBmHJqa03K6bDV-xyCAKuTeXjOiqR100d91wZwOK-aVGDhHZJa80lGpdvLoq1wvPz-uBtNQ0VKOss5xI8DsRFMafUBSh2qT7CcXsZG-zlcsGL_ikDGTU0nNCsAr_nz7Z0fIEawVRDPbDEEoGgeogpl-Li7gdRaSiF8JE4beh-E_TBFkzG1BNigD4yqVrCd7Y3E2ok7FpBzifkiYLfViSWNcanrlmzr878HHL0qP4e34Jtpr5E0mLc-UfBlowlPeVVKJRpYZ9qHTuVzdeUASfp5sww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e727e78c.mp4?token=SX-icqtH8T3ztnUmpLFb4rW_kWNV0Tj_v90ctLezcgl_tQHxe7vQlBd6tyvN5NBmHJqa03K6bDV-xyCAKuTeXjOiqR100d91wZwOK-aVGDhHZJa80lGpdvLoq1wvPz-uBtNQ0VKOss5xI8DsRFMafUBSh2qT7CcXsZG-zlcsGL_ikDGTU0nNCsAr_nz7Z0fIEawVRDPbDEEoGgeogpl-Li7gdRaSiF8JE4beh-E_TBFkzG1BNigD4yqVrCd7Y3E2ok7FpBzifkiYLfViSWNcanrlmzr878HHL0qP4e34Jtpr5E0mLc-UfBlowlPeVVKJRpYZ9qHTuVzdeUASfp5sww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون اول ترامپ :
- آمریکا الان تو موقعیتیه که بتونه برنامه هسته‌ای ایران رو متوقف کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/123414" target="_blank">📅 07:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بهترین سرعت با بهترین قیمت با God Vpn
🔵
تخفیف ویژه برای امشب فقط
✅
😍
10 گیگ فقط 280,000 تومن
😍
متصل حتی در شرایط جنگی به خاطر اختصاصی بودن
✅
❤️
😍
کانفیگ اقتصادی در ربات دوم 20 گیگ 290,000 تومن
😍
برای نمایندگان پنل نمایندگی فعال میشه
👍
❤️
✅
تضمین بدون قطعی
🌐
اتصال…</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/123413" target="_blank">📅 01:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVwIM-CtCi5bpG5xi7W0BmRcjDlsuq_ISCi0X_KaqDrXUarpaFBtWeqaSSlelu5OVvJoFCRMxOsqQ_nOXkVCIjqWcjfnkWtTT3_d5oYMDTUNul3Y3e4oPR9dlPtMwLSXIXW6coS5AN7wdguof0kjfWmWghc9o9Q7Px_YL4jg5_ULFpt7DY8HbNvfO505wnUAGFcPivv8LV_UaUj2Sn9TszQ7pbZbNUwYq-rwQisedX1q-aRkAGuMJSDYx-gcmjOXs8X8EDg0byRgDm19eTxUY5o6oGpFrimNAmbpcP21D4CvNQZmR1QNVvoE79VTR1-SXOYdKgqhDA_934ZFR28K4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سرعت با بهترین قیمت با God Vpn
🔵
تخفیف ویژه برای امشب فقط
✅
😍
10 گیگ فقط 280,000 تومن
😍
متصل حتی در شرایط جنگی به خاطر اختصاصی بودن
✅
❤️
😍
کانفیگ اقتصادی در ربات دوم 20 گیگ 290,000 تومن
😍
برای نمایندگان پنل نمایندگی فعال میشه
👍
❤️
✅
تضمین بدون قطعی
🌐
اتصال با تمامی دستگاه
🔻
🏪
پشتیبانی ۲۴ ساعته
✔️
دور زدن نت ملی
🔘
بالاترین سرعت با تمام اپراتورها
⭐
با کیفیت عالی و ضمانت بازگشت وجه
🌐
🌐
🌐
🌐
🌐
🌐
⭐️
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
جهت خرید کانفیگ اختصاصی در این ربات:
@GodVpnV2_Bot
خرید کانفیگ اقتصادی در این ربات:
@v2raypc1bot
ایدی کانال:
t.me/God_of_Vpn
پشتیبانی و خرید عمده:
@Mmkhh00
@Pc_V2ray</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/123412" target="_blank">📅 01:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123408">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRla0itbmmVcBFqq89CNtG8pXrjCsttbhoIlg6pJa9sSeQpVuNZRvEPu0MrSjF_jZj_HZe4ZRL98X7m6UECEXr8TP_RK63_1HQG1ScuwVi8Jq4qJLqwTzxmDyh1Z0_9xSsEvyctt4WHzPfIMLuiqnDvh8i1IiK2vJCjxNXhTBkyW_bkNy43Ih77MOPvv4bdEj2pa2H9SWuyNJUyqRVF5qLa_ApJwOarhzba9Y8HDrpCxhBj3R-UWRAwsSlQTT-ydixQ9YZNymxZeRQO_Yn8CtCNRNuju6D_GMQzV5DlmLKvnAN-EEy6H1YoFHztonv40yuVblJo3D7hFCMwyi5qkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnnYnzzfrF0BE7zdem2QW_L4f0oRcsm1YDr7CUPhdit2--p3r0kkZPxeS9RLqls9YAyTiEtqyhgjarMO-qPanryg_zwKrj-HJ11funqagGCIaUNEbO1FVWxB8ep_PtwiFuh-AlTnqA7495pv_SuAVNDD0dZHaMYuGK4N539fWKeKGY3YnisJo5UjKvK5k3psYzrSRQUU6q7gIRXOMm-laFWfAaACaKDRohlw2IObfbJerEPjDHhBLJOoE-naL53YkCEEVr3mRIlFX8nkpvufpcNrzLQ9Va-tOSDykFnmVJpUj57cIifQYuehvCs86Hr07CrUbHDLiEz4PzEeMQcwwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o53DAFKfS-0OLAaFR4D1kSfiAWpsIqUBgVCgZMwPt8_CAUdEwZSDqkzCFKZx5mBjnzyIfDCjqQLJpKPpBOGJf0eB1QmI0s54HstVF2QkDqVshATgV8v6Io00Wuoao4xqFXpgg0D_GxPpVxDjaeGfoYdfa2fFU04uueR0e94-N_ja3Ft_0UL_IPwfHk9pve6dBrwta9rS5glHayrriaT74w-ywZA8OB_7XBn2PokzxVbFclT3THYfQt9NxW10xolivdKgtIzVjDDffnq76f7mi23oKywfEscwwDqfjOK11cdo_FfVhSRQQq4L07Rl96bamFlKIKnrr1OchKGqmmIc1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb8eceea1.mp4?token=qUyQdb61bFQbT0jdoxBFCjH1ggvDsN-SdFU3ZNZq7MUVqOlsQ2eMAnLO-5kvFWwrL-yARwZaL_b_BvuSXlSadcN_ixCRpHdxd-0GExye_8e6pMj9xlsAVGf8EEpLyMbNrpbqAiWb0QU7Js2mV0e8UGrx_fg6SO9_mJHHVrJPz0L1G594Y1PvQbeFVkF_26GcPsuC5SC5MzwsongPpp7_Hb_LTIfuH07Hx1mEMkIfgOlcm_Vv1VAXT0cl61yGHv-FoDCaiPOPoasgBOG3UgNic9e6_E8oImWnhh0_1FPcT9RK858M7L6MFcFWwi-6n9luXa1w1AfiKEosBxHn-6DZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb8eceea1.mp4?token=qUyQdb61bFQbT0jdoxBFCjH1ggvDsN-SdFU3ZNZq7MUVqOlsQ2eMAnLO-5kvFWwrL-yARwZaL_b_BvuSXlSadcN_ixCRpHdxd-0GExye_8e6pMj9xlsAVGf8EEpLyMbNrpbqAiWb0QU7Js2mV0e8UGrx_fg6SO9_mJHHVrJPz0L1G594Y1PvQbeFVkF_26GcPsuC5SC5MzwsongPpp7_Hb_LTIfuH07Hx1mEMkIfgOlcm_Vv1VAXT0cl61yGHv-FoDCaiPOPoasgBOG3UgNic9e6_E8oImWnhh0_1FPcT9RK858M7L6MFcFWwi-6n9luXa1w1AfiKEosBxHn-6DZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های امشب ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/123408" target="_blank">📅 01:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123407">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ew6aRpIC36mNu5naPhSI6E5IE_Zfmq835MuZayNJzOwmNS4sesTWb8AW07snvrRVdcoZoE9frz1jmZ3fnCpzmeyIqW3drRl7jK2ND8tK-p6FNISrLqSrbha2gyEfh2qrn6ku4YtnCHneZ6XqczxHOZDCLFcC2W16rBRAKuq-5gsjdet-GFsXodR0_DaUTRy2aC6E-3Kj5V4qmPi-_rra_NPzRGct0RqxuXflFxW8gCCqMCBMBAxJUlf9u_f06rB1-qQwzj3dwChOEmUIHRoPCS0bejChyH83KBw5mj3V0sI5NP5hfrb8cJBYzHKbtADH9Pi55oCsT52wPkxNqEzK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از سال‌ها پُرشدگی سد کرج به 70 درصد رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/123407" target="_blank">📅 01:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123406">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLqNuGOn_lWqoJsEA6I95sG8fW7NSvg9xw9xJ5NQn1QSjqr_3ITDsyQkpnmMMnaFcOrwp0wB18N0kIC2NQAkBFvSf2YYY05rknVavHZkDegGvArYvwWWK5t8_OJv2hcKU33QketT4RGL8K2fERtOMRolsxIAwha9LmIQ35fAbFUu_OiZ4bHbymVJ6Y0xjOJ3OfrglUpSy2Iv9bskzk1MBGNKG-42CPcBUfxsC1SIh6ZVA3jhvhkGgnWG4qKt2FXRrTsZ0HYmS6qDVPx4uhdcEwqTnft_jOOh8rMbULCPo_UBOGS9D5bJpf0qid4ACxbgrW24ZLHbcXi-3ZNwomJnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست عجیب کاخ سفید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/123406" target="_blank">📅 01:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123405">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48cd5832a.mp4?token=iR8eo7rC4rSGSlfl9j9iX9gqTCGxguadRnTLWEFX2InpxLTJM1o9XYdgHTSGfDzf4h8L2bi838hJNdSbMCJZlUAXoNbnD3tEMQ2oaEvm8YWSs9spSuIE_Zn6E9WvcJ9tC7HOS3Ckk_BkdsF61DgqrGnfzmODAB9T8s_4xCeeiO9khWxYcxHdRLAg7Idg0TyNWHk3wogIBL7wkiUIFMNeuO-pGSy71baRp2Ko6Hxz3YMsfi_pi9ocrPeB1Ty5J4z3treIoj4-0hN7M2f588nl15hXAmf4xQznh-T1b2Nh3Ze-DDzHBFoA0-Dh83J7-M7JkRPO_FgwFa3QkH1_i7f2WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48cd5832a.mp4?token=iR8eo7rC4rSGSlfl9j9iX9gqTCGxguadRnTLWEFX2InpxLTJM1o9XYdgHTSGfDzf4h8L2bi838hJNdSbMCJZlUAXoNbnD3tEMQ2oaEvm8YWSs9spSuIE_Zn6E9WvcJ9tC7HOS3Ckk_BkdsF61DgqrGnfzmODAB9T8s_4xCeeiO9khWxYcxHdRLAg7Idg0TyNWHk3wogIBL7wkiUIFMNeuO-pGSy71baRp2Ko6Hxz3YMsfi_pi9ocrPeB1Ty5J4z3treIoj4-0hN7M2f588nl15hXAmf4xQznh-T1b2Nh3Ze-DDzHBFoA0-Dh83J7-M7JkRPO_FgwFa3QkH1_i7f2WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری که الجزیره از شدت خسارت حملات آمریکا به تاسیسات فولاد اصفهان منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/123405" target="_blank">📅 01:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123404">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
یادداشت تفاهم، حاصل جمعبندی مذاکرات در سطح دیپلماتیک است.
🔴
برای اجرایی شدن، نیاز به امضای مقامات عالی در تهران و واشنگتن دارد.
🔴
نیت توافق وجود دارد و انتظار می‌رود که از مرحله نیت به مرحله عمل منتقل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/123404" target="_blank">📅 00:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123403">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی آمریکا «سنتکام» شامگاه پنج‌شنبه هفتم خرداد ویدیویی از عملیات پروازی انجام شده از عرشه ناو هواپیمابر ابراهام لینکولن[USS Abraham Lincoln (CVN 72)] در جریان حرکت آن در دریای عرب و پشتیبانی از محاصره دریایی اعمال شده بر بنادر ایران، منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/123403" target="_blank">📅 00:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123402">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7CqwJ7dBOQAk1bedyx0WrFj_gE6luQxIcoWIcnPWLYPKorQa-Lbvy5fPr3rmVzybt9kH9Ycag5i82A7PqVWgfeEslA4uBXc5tkcpLc9HTk0ZdnwiYGYl83OlYnQDuPqPf0mHeE060Q4XxN4Nkw1MWXVlxrJ2KzTIeXugKQH38Bzn4JCQjjH6zq8FBQI6syLEVPvYE9u4BUK9YmKTV326iFbVoiUuXg-5iqlbwCsxBi0i-YiQqllpYC6IZJM24DDUTE8WxaQ7T5MkoerwUznU0RkdPX006qgEyMeo53-eJ4wlMPFZzZfSdDEoSZCKKla8O7Fz2lg2eZ2VHPno_nynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان:
به جلیلی گفتم توام بیا یه گوشه کارو بگیر کمک کن کشورو درست کنیم. گفت نه من فقط پیشنهاد میدم. گفتم پیشنهاد به چه دردم میخوره اخه. عمل میخوام. نخواستیم اصلا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/123402" target="_blank">📅 00:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123401">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T36CFdmvbQap0A_YqY4PP6xQWKwotYFKp4VCUEfvMT98krhVEwAPkh8g-cSDfKkHSo7-NWUiPtiokJKlUpqh2lqcD8WQS3b_XaP7a0bjKUY6sEl019dzvKo8849-O_xEYFmbegPYeT75pb1E-ckBCTjWM8XujLLCYAFx-dBsSEpH_4quzHl5jKl2Iu0lkYCqYKXomooCtvqTS2opFY0pDQnBmNZxMiyccXn4Hm-RWbf5HIdhoY8C8bETr86ak86BuusKJCmmjkbVEl7x8RAvqOipV-iE0J_kX7UI_DXmj3-InzBi0jJe8fDMaUR0vAZYTJdq0t-RJmzpRu5TRCj6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوخت رسان KC3 بریتانیا برفراز عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/123401" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123400">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot @NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط گیگی 25T
✅
@NetAazaadBot  @NetAazaadBot
🔥
یه…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/123400" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123399">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exZ7pdm81wXZAzSD1ib78pZSEqZEAUnn5fZqpg2oAbFYPY7NycT-G0Ykjcf9s3wlwD1ojIkEibgvYsmdxL2A6Ej0GvV6LybXE84YiCx9ui2p7yS0xo5RqD8y12X3enDaB5_vWb_q8lrGL03Z8f9HAMPpXD-CL0RXsUux5bz4XjfbXYRMMFV2xNfVmlrTJI-LMqbXSS9RjNmaBN6qRskq1WRJa102J1_66uD0PWK8qbj05qBJx_JmXwWvF8DLTNU7DK5bX-KOY9yg5qOn8mnQ41KY9T7aJoh9XhzK10ip4981DWnCHcad1TV6iRZ7_qI6Mqhf28hnKWRUYKOLw1SsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب
یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot
@NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط
گیگی 25T
✅
@NetAazaadBot
@NetAazaadBot
🔥
یه بار امتحان کن، خودت تفاوتشو حس می‌کنی
✅</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/123399" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123396">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln92nTtBD1DzGFmdd23_g_tzghar2i7E-JzJXp6HDrDQyLqqev82jNkSkWzanz7TnBx3LjnlFn0X6AeUHPH-C60lRMDyF-J7GROvutZnvVW4YD9lI_XxBFd0g_bvK9CHwtZoBRlcNKVPLofqS4JipW4Tb9RBtiTDTHGZgXM7AGiFev8R0D5zwM9OCYK5_LbBUgb5RtYl5hXCmQTMIuf5ORH0mfF41Uco1NPaD-55q21IiaGHOEXGUi13iu0ikC9pqYnUtLot5a94UqwdPteTPRp8pVp6Ay_YSGQCX_ks2QlAQvHla-hdJs3afxeZprRzLO_chGVNw-0mxgPXnOLrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یواش یواش برخی از اکانتهای امنیتی حذف جانشین سردار تنگسیری را دارن تایید میکنند در حمله دیشب آمریکا به بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/123396" target="_blank">📅 00:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123395">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJnbJrg37EIm4sJRR-SOe_lnouDA-L2jOsjPA9oBh_SqLLphfylvYLHNQGsrxYTJT43k42iCh31P-ZgNgqrxUYAyHr8eX2cHRRzg61dzqLCEV-4B_IMhQQPyiMrAZIpzF5B8eM94lq_PP6O9RjdD1EpdsTHATaSMEB-M8ngvMBOje1hxz0UvGfPjNbxftLgaDL1VINTxcrl9uGcdbqKLlD87wRW0eBzOE9WfaIgCj3sBdYErg1NyBbsrHZJ1-tyPitQQTcohRJoBOw_I8ckWItVIfyJYPub7nVXzmXTTcAcfwTfNoRh4e1gVUBA8F0feQK-g4TA5fSMlw3MUxxo5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
90 روز از ترور علی خامنه‌ای رهبر پیشین جمهوری اسلامی گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/123395" target="_blank">📅 00:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695242755a.mp4?token=a02YECsEilmHelM-KmQnz24DRzc5KujPmUQyZAFWhkEjo2lbxc-6E0jKcg_mzCcQsImANxt7HeuEX1teoX61Xx0o6WHV6zxBMwR9dTXwsSKJxSSeUIzHMrNAVhB6TwVhlfd3gat-Kq015ZfE8zGbgW6-3NIADisDDkqdmcpEJDc6Z8taEhSs-tXl0cyWVk11Xrnm0Ndns6i5vuPu4DujtC2dtrbo5xx5FIjP19sWjUiY_M3gd9dM1uHCcad9YGyC9ZPnD_KyRkWY3mqZo5dPiRa0_rcNAGezGcYygfMKtHFkHCC-pWUJYmBEuij-JmE0Q91ElVpaw_MxS7UqLotzhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695242755a.mp4?token=a02YECsEilmHelM-KmQnz24DRzc5KujPmUQyZAFWhkEjo2lbxc-6E0jKcg_mzCcQsImANxt7HeuEX1teoX61Xx0o6WHV6zxBMwR9dTXwsSKJxSSeUIzHMrNAVhB6TwVhlfd3gat-Kq015ZfE8zGbgW6-3NIADisDDkqdmcpEJDc6Z8taEhSs-tXl0cyWVk11Xrnm0Ndns6i5vuPu4DujtC2dtrbo5xx5FIjP19sWjUiY_M3gd9dM1uHCcad9YGyC9ZPnD_KyRkWY3mqZo5dPiRa0_rcNAGezGcYygfMKtHFkHCC-pWUJYmBEuij-JmE0Q91ElVpaw_MxS7UqLotzhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله به شرکت آسا پنجره کاشان، تصاویر از دوربین‌های مداربسته گرفته شده است
🔴
در حمله دوم که با شدت بیشتری انجام گرفت هیچ تصاویری موجود نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/123394" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6qFNNtSYh79U4u7YvJHtGB4q0lbPXIw0J2NkRswinlSLIEjzscjQSPlsVQMIZzh7wHSD7yeDOd6QqwM_hZ39cO36kW8X2we1S-DFXXJ1SWcVI9NZAQIwtfQegWpOsmZx_u3v8uSGKsUf3rRt0bHM2nvCHD0FaBbEHRZ8StiOfnIeXJOkik87kAjJAem44c8bzNsX6H-4v3RKKZLgv5d3YXF_iNLDgbKck4K5g8_E1jevQgJMPCkeoHe6phOMOQn0heTTlQQeyOGVLPP1NbNCBYPcyR5P_OfLxNfRNw3owtgkGk7JWqlGJed8xjvvEVe3Wfrlh3zDgqpQxIZo14enw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/se42T3PPrpb_J-mIyJlxB9DG_URW31-yM6YLQtAS7IYV17_9f3-9i8sI8yWq0mqfvlNOiq6TfWRaMJYUf-5ZUYG4vQOb5FVH6TD51dQa56iFihRlNrr1ftVtH0YzgJ4Lut7t-Oly8VCO2kd5d_5PEuPsr2wzTbSSwOWAC7IJMKK_5mjT0-I_EY63Af-yEUnTdouB2WIpsN3BcwQoRl5x6yF_Me3BdNy5OZZc9rsZd3rSYkLjcvdrS4Icrxwf22IjHTKs46fxGoMRbSBSykSGFoFotMDB4VRxUcDuVeWciTc9juKST6L7d4BQNEivMfKgoiiYSl7HVx9VCbJ1LQ3FCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDrVFylalz8KwN8o-J5IxkdP6fxKhcOHa8VEpgOaoKul3ZNYMLx0b3g9kOJMM0o_k2ndsC_UKK-8SDacYXT8dhB16rMBD4w2btFQIG9Fei5BOyQIvE8lermSjbMflGM4_QgLGwNsWG6nusOE58uKOQP5wbbqhcufV-5KkX7WE5YWgfrxT-vpjzqv-1ONtCR_e-5v7BtFN3hSyWXO11Z7DoTTjALDNR79J24HeCEg_yHB4t5nsAT7RK1jMSV1PuGFc9_mPpkAwXkfU2a-w1xTESvVRKr5dR2RvB6kAasaWuEfivEfPFPg9f1I7SW1pTm99FOFeL23xGdynMA29ht3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqAynM5omnJ4Iyio5OUq0Y4_DUXclrUMcsmApG8zhho3jaNiZ5qKCxQI8houlR6AbfCLFCneUeAQKe6yqfZegxNbWkFwz1Q6eEjjSlcbdhSuntfqWVHxgHw6Yaccu8s-zBFjaZS2axdhwyLG-yi2PUwR1lCwT_9gIdBCRKbPMo4P98wKT6JcE9QMrdGeOAgG-j_i6yMJs_oUVRifwVbwqUa35NOZmH4Rc7uFgWh-y9_NSuYY548uWLqrFKKbyFn1AzGq_Vnz_5idlPGiy-TVZgfRFrcVrxcq38BnjYPbkxkjdicKJJaHOLXp94FsH41jJnWA35ZeWnidmHD5vGMwQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط «صابر ابر» برند خودش رو با شعار زیست پنهان راه اندازی کرده.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/123390" target="_blank">📅 00:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مهر: نیروهای مسلح ایران در نزدیکی تنگه هرمز به چهار شناور خاطی شلیک اخطار انجام دادند، این شناورها قصد عبور بدون هماهنگی از تنگه هرمز را داشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/123389" target="_blank">📅 23:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭕️
⭕️
این روزها بعضی از سلبریتی‌ها، چه از روی فشار نهادهای امنیتی و چه از روی منفعت‌طلبی و ترس، شروع کرده‌اند به تخریب انقلاب شیر و خورشید.
🔴
بعضی‌ها هم تازه رنگ عوض کرده‌اند و می‌خواهند با حاشیه‌سازی، مسیر اصلی را کمرنگ کنند.
🔴
بهترین پاسخ، درگیر شدن با حاشیه‌هایشان…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/123388" target="_blank">📅 23:54 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
