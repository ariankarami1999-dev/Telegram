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
<img src="https://cdn4.telesco.pe/file/EqFI2UokJEolmIbK9pNbdtcJ1NZQQurgw03JUc5bzQVSn_7Zw_QFba2wIJaBfJ4Dv0k93QsTHbAUtxGlBPqQVt_3WYlG7Xi7sUmGrNWCYv6NTq6nIJk6N3eCwif8MSSwIUQTHeUQMsmzP7OQtVLvzlCVg0REnEWNabnNRfu6mwB3l9HNUZnogGONSsTN8RrhNI11N0J-I3HRGz7ouemnTT_TLadha9vbVlJHoXtU000ed42pKxxQWhs9hibs1eOyvTN7i_kri4jx4xX28LHZDSerfA9IUY8TJKQG6xVJlUFnos2CmCmGHNIuOiOMbkTnnAWuI6eo5mvl9-jDZf5aqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-132546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پرس‌تی‌وی به نقل از یک مقام ایرانی:
ایران در صورتی که با حملات جدید مواجه شود،
تنگه هرمز را خواهد بست
.
🔴
ایران در پاسخ به هرگونه حمله، اهداف دشمن را با نسبت دست‌کم دو به یک مورد حمله قرار خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/alonews/132546" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6e761e2c.mp4?token=NVO0JBjck8GKBbTEwBohEnKjp5UW4kmt-l1P9EaKnaIC1JhnVdn0ZtfbUEEUUOepDizclksLg1cxAZ8FXYYlG3FbboZqzEtS3ZX7in7g83JYa4Qg63DU1gqUTt44zmChtVWFs1MRta9gK4lkVhy_zpjMgmxAvWG4Ab0gDgfEmoNea3RDAzmZ6-N-l1Fc2Ctr1WTLtH7g3TQgmd318OpW2uTaMlDHR02I6Trn5HHNnZlqJRincZlWHh5P_2PcCCG7ryeVqLOngmuY46grZpPNXxeXKXL3q7xyJR0jp3ADK_P-4sYa9A50hOdhoxAGhCDrgskoY0vVT4FCvBpJIdYURw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6e761e2c.mp4?token=NVO0JBjck8GKBbTEwBohEnKjp5UW4kmt-l1P9EaKnaIC1JhnVdn0ZtfbUEEUUOepDizclksLg1cxAZ8FXYYlG3FbboZqzEtS3ZX7in7g83JYa4Qg63DU1gqUTt44zmChtVWFs1MRta9gK4lkVhy_zpjMgmxAvWG4Ab0gDgfEmoNea3RDAzmZ6-N-l1Fc2Ctr1WTLtH7g3TQgmd318OpW2uTaMlDHR02I6Trn5HHNnZlqJRincZlWHh5P_2PcCCG7ryeVqLOngmuY46grZpPNXxeXKXL3q7xyJR0jp3ADK_P-4sYa9A50hOdhoxAGhCDrgskoY0vVT4FCvBpJIdYURw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره اسرائیل:
اگر نخست‌وزیر دیگری داشتید، اکنون اسرائیلی وجود نداشت. توسط ایران به تکه‌های کوچک تبدیل شده بود.
اگر من به عنوان رئیس‌جمهور نداشتید، اسرائیل امروز وجود نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/132545" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9b8be6df.mp4?token=Z8jZGLSqtzPUgryQLb_2vO_VX98FU2RWLzT12MfYufxotv5QaVI6VnKK3-GdiOKpGHP0W_z_meTsTleppGrtXCoHYcYfza21lS99XcAauIMQdX8myLZ-E5l975DW1BE9DAqZzXuWiFjLXG6HFTLle_V_biyts1X29vug4PpQbCTjvXeW8jXNbWC1sLHNM1JkBXDwxP4U3FeqD527Hob29MJaFeGNGQhDTc6LaL91J8EI_mSuqYgU8FEpUtO3TFdbp8Kg8jETLVeIl5UfpKQDeuYvSzukC-BROlYiMIXE1RyLJBk-tHWTG_NpB464FsH2KMyGFpET1HAxrlOV1Za9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9b8be6df.mp4?token=Z8jZGLSqtzPUgryQLb_2vO_VX98FU2RWLzT12MfYufxotv5QaVI6VnKK3-GdiOKpGHP0W_z_meTsTleppGrtXCoHYcYfza21lS99XcAauIMQdX8myLZ-E5l975DW1BE9DAqZzXuWiFjLXG6HFTLle_V_biyts1X29vug4PpQbCTjvXeW8jXNbWC1sLHNM1JkBXDwxP4U3FeqD527Hob29MJaFeGNGQhDTc6LaL91J8EI_mSuqYgU8FEpUtO3TFdbp8Kg8jETLVeIl5UfpKQDeuYvSzukC-BROlYiMIXE1RyLJBk-tHWTG_NpB464FsH2KMyGFpET1HAxrlOV1Za9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره لبنان:
به نظر من اسرائیل در حال عقب‌نشینی نیروهای خود از جنوب لبنان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/132544" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e990ae2ff8.mp4?token=HM3WZoxoJXNjaWdO_qCYVzavFG8N_mHRCwZxkpfw_RQ7-10AudnvF-U5LbScYZR9I4QondLug-mkostlyp5yYnTgS55XmU9BwV1HeLkVwox72mmhpB1P7QGmO8mI_FdrotA7CqG96n8mXLXhWnXJmHIpx31MoXzuqUdtt4xku5f1CVojLzEvY1gG3pZSmThNWEWACMfOrogZeiXgP4Ivwnvn6PQOuAr4jT6A-N48kt_ebDwHP1O9pVNd7sZdZiGL2jAoQ4EHRxHFAyQxx7iRFRnpxG5vR3lx-DIHLCB5Y35gFKvT28z5jCr33i6Jev7QGTe6MOWqd8ma5i7uClKs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e990ae2ff8.mp4?token=HM3WZoxoJXNjaWdO_qCYVzavFG8N_mHRCwZxkpfw_RQ7-10AudnvF-U5LbScYZR9I4QondLug-mkostlyp5yYnTgS55XmU9BwV1HeLkVwox72mmhpB1P7QGmO8mI_FdrotA7CqG96n8mXLXhWnXJmHIpx31MoXzuqUdtt4xku5f1CVojLzEvY1gG3pZSmThNWEWACMfOrogZeiXgP4Ivwnvn6PQOuAr4jT6A-N48kt_ebDwHP1O9pVNd7sZdZiGL2jAoQ4EHRxHFAyQxx7iRFRnpxG5vR3lx-DIHLCB5Y35gFKvT28z5jCr33i6Jev7QGTe6MOWqd8ma5i7uClKs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هر وقت به ایران حمله کنیم، قیمت نفت کمی بالا می‌رود.
🔴
اشکالی ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/132543" target="_blank">📅 18:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ee945f4b.mp4?token=NkC0ohBMQ2YHQ4CD08KCNDysHMNPJ6qfFDesH9dH0aCUmn2EjEgyu285tYI_IAUAQu9PGXcJLF7yzdU7ccx-zQaB-mPN9DVOZsZib6aQb9L8uknltuD8qr84T4HJgbqFo-1T3LDHUPshTmBfbdjYwwQr5VUrkpRVu1lD9WEPQ9B4NLUO_Cn10EzLCIN0z-nvdEwTyS4K82AoveEVrppXjfx-EKezC9ABnhZrAu9vMaTW3ozG4tj2LWHGvfoI3IwbSGI4dIDRqevLqbxIjsyANWHPWN3Ozda5C-8ntrHkB4UkyMRo5w7qaGjQSwd-74zE0pWB5G4a016rI4kMLvIlbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ee945f4b.mp4?token=NkC0ohBMQ2YHQ4CD08KCNDysHMNPJ6qfFDesH9dH0aCUmn2EjEgyu285tYI_IAUAQu9PGXcJLF7yzdU7ccx-zQaB-mPN9DVOZsZib6aQb9L8uknltuD8qr84T4HJgbqFo-1T3LDHUPshTmBfbdjYwwQr5VUrkpRVu1lD9WEPQ9B4NLUO_Cn10EzLCIN0z-nvdEwTyS4K82AoveEVrppXjfx-EKezC9ABnhZrAu9vMaTW3ozG4tj2LWHGvfoI3IwbSGI4dIDRqevLqbxIjsyANWHPWN3Ozda5C-8ntrHkB4UkyMRo5w7qaGjQSwd-74zE0pWB5G4a016rI4kMLvIlbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ در مورد غبار هسته‌ای‌ جمهوری اسلامی ایران:
این‌قدر در اعماق زمین قرار دارد که هیچ‌کس جز ما نمی‌تواند به آن دسترسی داشته باشد زیرا ما تجهیزات آن را داریم.
این‌قدر در زیر کوه قرار دارد و اکنون مشخص شده است که به ماشین‌آلات عظیمی نیاز دارد که ما داریم و هیچ کشور دیگری ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132542" target="_blank">📅 18:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=qyTkufY8RfKaIWlgrqXYABVVhWe0rTgrY7IAMcaTHrhGe99qPrSAoxuixS-3RjZ9M1V718nqlIUcteglvrVGD3S6RbBDqxwuq_5vRUmEJz0ORm2_CPQ46QXDw_zmbyS1pJz6NuCPXSG8JJRhHx5jZAWKPuxbTugo1Y9it-9TNOIxEzpD_QMqMffgXytk7mKovaqp-yLuE3140wB549jfyhwtdh9KX48nIwlhUiudTLuV-6df0vxs0BStUI5pz1pg4ehiJDWBb7bqXm5Km6a4Aw0XXxmJhvkTHw6ewVtwMpAcqYL1W_i5AGrj8xRCmQ7_qpoK_1e4vT9DTCg_h0bHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=qyTkufY8RfKaIWlgrqXYABVVhWe0rTgrY7IAMcaTHrhGe99qPrSAoxuixS-3RjZ9M1V718nqlIUcteglvrVGD3S6RbBDqxwuq_5vRUmEJz0ORm2_CPQ46QXDw_zmbyS1pJz6NuCPXSG8JJRhHx5jZAWKPuxbTugo1Y9it-9TNOIxEzpD_QMqMffgXytk7mKovaqp-yLuE3140wB549jfyhwtdh9KX48nIwlhUiudTLuV-6df0vxs0BStUI5pz1pg4ehiJDWBb7bqXm5Km6a4Aw0XXxmJhvkTHw6ewVtwMpAcqYL1W_i5AGrj8xRCmQ7_qpoK_1e4vT9DTCg_h0bHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میرباقری تو صداوسیما:
دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
🔴
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان شهید شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/132541" target="_blank">📅 17:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h27dMrdSbK4gHipNXTTHTIXhRQhnMxwuKsnggzB5A1n1cXVAC4-1W776zlWlJoIopb3cHYnjtEO0ew0_fuUqEDVmFTt_NgXN36zGgs_H4QzKsp7CbHTBp6cWqy4saDXLl0gQ2w7oChcK7ZVsSPqzZfp3g5BBzwJ84r3lMSeKtubQ5kFXAwkeIbTV0WkyDAOmEHoLbnRa_JCF-aGXssD9EHqVudhG_rGydkeyC142lNBH527hnnZPAtqQzCs7YYLoFV8LcifYLmO5EJjMHoKmco6W6idC46B7Tjbd3-ljiJDWbFs2L8pMFnraFqMy1NmtXQQHisqZFZljcD5Cd28-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خلاصه از اظهارات اخیر
پرزیدنت دونالد جی ترامپ:
ما دیشب به جزیره خارک حمله کردیم.
ممکن است جزیره خارک را تصرف کنیم
من قصد دارم به ایرانی‌ها یک هشدار ساده بدهم که امشب به آنها ضربه سختی خواهیم زد.
در یک روز، می‌توانیم تک تک پل‌های ایران را خراب کنیم.
اگر مجبور شویم، نیروگاه‌های برق آنها را که برق خود را از آنجا تولید می‌کنند، از بین خواهیم برد.
آنها کارخانه‌های آب شیرین‌کن دارند. اگر مجبور شویم، آنها را از بین خواهیم برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/132540" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3pk_gbvSO3vQh9YfVDuN8sQAktScmYU0MPsuNr_tWjqiyig6FbUoyCTI1UOF8I_P5gHiVoLCfX5pzGZR--gkLCdibE_64gFA7PZVgzmWk9kNuPL32lcRGnwAibGMKEygv9QHPy-nlkmqvahhzt_qh3bkzeWN0R97uzDhdBxskcuM0QfaRuyzGxFKZdJzFFDVq10-39t9AJS2MqNS5Zr8hH-ybp-yemEm642ymV6VTXw-EpN2PSphCYnJmFD4dOhfX6_HobI_swqeHK_lCcBK_q3eyjAIC26rma4GdtiM6IMc9tU9tYCy-iNUexCA8jqZwYrpSFArJ5HrtCeLx5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یک نفر پیدا نمی‌شود پاسخ فحاشی های ترامپ را بدهد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/132539" target="_blank">📅 17:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام آمریکایی:
تمام موشک‌ها و پهپادهای شلیک‌شده از سمت جمهوری اسلامی رهگیری شدن یا به هدفی اصابت نکردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/132538" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/cde45b3538.mp4?token=OsV4nnmqheosbxxuBKxulBS_WS4f-ybEFeSIhuve9ceJr8B4ImucP4FvrgDrrgaT3IhBm8sjHk2SO9dDaXaxUmH9P1jxSuehQaW3pPh5prR0pTLgY8ZBM0U6Ur43D0jNKbiRjGHdxaMJaN7H3y5cB-Ep3tg9avy10I-_uJwB_stBbcRSJWOQVSzWZlWx9Qp0GxOp3iuO6j1z1E79-da2IW0qUTuK7PLRVkHzsP4tIZi6SajcKTeYVOv591HmteF7MNYeQWbq34DaFIl35EsugPmOl65zYkMQF3FSQB3Vg2SVbDsDuedicdnmVSw6NOVYvD-7Y3IlF1fFWgBfyVRF9g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/cde45b3538.mp4?token=OsV4nnmqheosbxxuBKxulBS_WS4f-ybEFeSIhuve9ceJr8B4ImucP4FvrgDrrgaT3IhBm8sjHk2SO9dDaXaxUmH9P1jxSuehQaW3pPh5prR0pTLgY8ZBM0U6Ur43D0jNKbiRjGHdxaMJaN7H3y5cB-Ep3tg9avy10I-_uJwB_stBbcRSJWOQVSzWZlWx9Qp0GxOp3iuO6j1z1E79-da2IW0qUTuK7PLRVkHzsP4tIZi6SajcKTeYVOv591HmteF7MNYeQWbq34DaFIl35EsugPmOl65zYkMQF3FSQB3Vg2SVbDsDuedicdnmVSw6NOVYvD-7Y3IlF1fFWgBfyVRF9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
«شب گذشته ۲۸ قایق را منهدم کردیم، آن‌ها فقط قایق‌های کوچولو دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/132537" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/980e8489e8.mp4?token=mc-TSi5Fj9P3fe2gdhqp3zH8iXy01hI17sv6HN009cPoYrfAzNkAO-crv-oFxGbucTwk7JfAkUbuVvpMzj-E-gtCPd-bsqdrXC1TlrDRKtZ7yN0xPZWrRckuy_StsMV184uYJ3aH33ckSzOtScln6ZCYDeTHZzPiVqTWSMLLlsqvVUjWNhedcxunY7AoTp84IZVVaYqaxVcSAKYhwrWbcUO-azialD9HjaLf0rA2JiXmKfKcUwYWVXBmXw91AjqHC8ogk1D95qCoMs33cmt3mJI-bmHTzI-qO6lDWsHm_ljGOoEQTsqhe-NdBEMMSZHKQfdhbY141NpsQMQVkw7q7g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/980e8489e8.mp4?token=mc-TSi5Fj9P3fe2gdhqp3zH8iXy01hI17sv6HN009cPoYrfAzNkAO-crv-oFxGbucTwk7JfAkUbuVvpMzj-E-gtCPd-bsqdrXC1TlrDRKtZ7yN0xPZWrRckuy_StsMV184uYJ3aH33ckSzOtScln6ZCYDeTHZzPiVqTWSMLLlsqvVUjWNhedcxunY7AoTp84IZVVaYqaxVcSAKYhwrWbcUO-azialD9HjaLf0rA2JiXmKfKcUwYWVXBmXw91AjqHC8ogk1D95qCoMs33cmt3mJI-bmHTzI-qO6lDWsHm_ljGOoEQTsqhe-NdBEMMSZHKQfdhbY141NpsQMQVkw7q7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ هگستث:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
🔴
پرزیدنت ترامپ
:
«ممکن است محاصره را اعمال کنیم، ممکن است آن را بازگردانیم؛ این محاصره فقط برای ایران خواهد بود، هر کس دیگری می‌تواند هر چه بخواهد داشته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132536" target="_blank">📅 17:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11b06ef2b9.mp4?token=dXx8jvckdI-aWthJuuRVK2Uc-3FWIi_JkYs3ZhmSQ7jeW4XEcyudGhQuma_Ciy4REc8Q9D2Hu3g4I8IBpuPM891pHit4HW6dxEzGAp510CSLLmS_UfU7Symo-zaD9jBuO8l8IqNo10HhaC1q7Sn5PUlTzVHUXbJExggEhOHxOXqz0S3XJPNH5hYNNbVhyEG4LamdX_aNChHgQXPz_va9w1MBW4Og7ghH_cCV-889v1oUBymOFPUvNhqgzx_7hpNnmBP20OvXNlj6jQXfPZ_Ph3hdYwkgZYGbc_jIrOU7-jpZdw39BtoDJibcrly_0Qj4woNefAPR0N1KCRj2JwQAQ34HcXKDgS0QKmZZluie9WES_2FkzGWDYXKBfejBEaPxc2sgdfbB-NzUHPZmquuf-HPTpXRHyo5c2TMx_eXgEFdV0ZXgazp-f6yo20E8YtSyrWUQXjoQH2K6UxXIZqZK7V_nXoeXwC35_HES7CUnaj0PI-WkINau-Qd2N556I_U7hXEacOGQfTNYcdv3o5kwvRyqF10Yr_3a2pgExmPGaXndVweUicy33qf-p5WAhXUw7hE0dYi0__1Cs3B-jZEDes8HEUHeEgMO7tU47tB4uQKhuw3y6ZTg87PRvI6ZgG-QAjkllQveo1xo18EKNbmZXqDGe-u2G_Y_Ze7kUmu5NaM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11b06ef2b9.mp4?token=dXx8jvckdI-aWthJuuRVK2Uc-3FWIi_JkYs3ZhmSQ7jeW4XEcyudGhQuma_Ciy4REc8Q9D2Hu3g4I8IBpuPM891pHit4HW6dxEzGAp510CSLLmS_UfU7Symo-zaD9jBuO8l8IqNo10HhaC1q7Sn5PUlTzVHUXbJExggEhOHxOXqz0S3XJPNH5hYNNbVhyEG4LamdX_aNChHgQXPz_va9w1MBW4Og7ghH_cCV-889v1oUBymOFPUvNhqgzx_7hpNnmBP20OvXNlj6jQXfPZ_Ph3hdYwkgZYGbc_jIrOU7-jpZdw39BtoDJibcrly_0Qj4woNefAPR0N1KCRj2JwQAQ34HcXKDgS0QKmZZluie9WES_2FkzGWDYXKBfejBEaPxc2sgdfbB-NzUHPZmquuf-HPTpXRHyo5c2TMx_eXgEFdV0ZXgazp-f6yo20E8YtSyrWUQXjoQH2K6UxXIZqZK7V_nXoeXwC35_HES7CUnaj0PI-WkINau-Qd2N556I_U7hXEacOGQfTNYcdv3o5kwvRyqF10Yr_3a2pgExmPGaXndVweUicy33qf-p5WAhXUw7hE0dYi0__1Cs3B-jZEDes8HEUHeEgMO7tU47tB4uQKhuw3y6ZTg87PRvI6ZgG-QAjkllQveo1xo18EKNbmZXqDGe-u2G_Y_Ze7kUmu5NaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زیرنویس فارسی/
پرزیدنت ترامپ:
آنها ۴۷ سال است «رفتار بسیار بدی» دارد؛ پاسخ سخت آمریکا ادامه خواهد داشت
دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ۱۷ تیرماه، گفت نیروهای آمریکایی شامگاه گذشته در پاسخ به حمله جمهوری اسلامی به کشتی‌های آمریکا در تنگه هرمز، «ضربه‌ای بسیار سخت» به ایران وارد کرده‌اند.
ترامپ گفت جمهوری اسلامی «چند پهپاد، یک راکت و یک موشک» به سمت کشتی‌های آمریکایی در تنگه هرمز شلیک کرده و افزود این کشتی‌ها «کاملاً حق داشتند» در آن منطقه حضور داشته باشند.
رئیس‌جمهوری آمریکا همچنین با تهدید به ادامه حملات گفت، «احتمالاً امشب هم دوباره ضربه سختی به آن‌ها خواهیم زد. این یک هشدار کوچک است؛ ما امشب ضربه سختی به آن‌ها می‌زنیم.»
همچنین ترامپ در بخش دیگری از سخنانش، جمهوری اسلامی را به «رفتار بسیار بد» طی ۴۷ سال گذشته متهم کرد و بار دیگر از سیاست‌های تهران انتقاد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/132535" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
دبیرکل ناتو: تنگه هرمز را باید باز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132534" target="_blank">📅 17:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/ترامپ اعلام کرد که در تشیع پیکر آیت الله خامنه ای ممکن است تروری صورت بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/132533" target="_blank">📅 17:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: در یک روز، می‌توانیم تک تک پل‌های ایران را خراب کنیم.
🔴
اگر مجبور شویم، نیروگاه‌های برق آنها را که برق خود را از آنجا تولید می‌کنند، از بین خواهیم برد.
🔴
آنها کارخانه‌های آب شیرین‌کن دارند. اگر مجبور شویم، آنها را از بین خواهیم برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132532" target="_blank">📅 17:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f407ca85.mp4?token=cMJUVfpvCamdk4rjhliAQ2uLrnIUoeCzTD3S19hCpoBB23NAvq8EB37LJbt1enkiUyqVU-HJszQ1DKG8chOplT8abYmhSdSc-UgPiaTKt1IrDdAIvb6-ZVrXTVQYHQSjYLyFdmVQOU5p1Ov-KK18oCtwuixQDgmNQK6l1ystuSEmgE_LlMtCA4AIXojgGuKHlrl0yW-dWo50zDKyeWClg_spelR6y3jlzU0G2CaXuK7PmAsi3ykro5W3VA1q-kZuf6EmbVJiRfWhqEZLe794cdICczVl0Bxbi5tidw3OH4CjYwmo6y4FgLCJRHEFtoS6r07JIJmbExCBNR7Pm58EtaijKf0o9nO45ZfVeQW4Hvo6hHsoy_HdLTcVPAS0doHG1wyanxSjgSkL-oYQb92oBAg53Qyqt01mP8qbRgwIbBWt5vsQlqtVltMWnn9eHlHqyrQQFkeddyGEEL5ZLuLPKudR-qUHbUxDBqkQqQv70-SPsCdDuBazOVMttkpQMJhSbW4LoqDFDKORcT8kjM6WVY3lo7e_lifGHvQvDSytI7nQnKhQhg1kSy6Gf_CtfjujUlWWewypbsT8mgz0kpO_Pg57vsp2-5qiB2yLAiJBwhhpxXhbmo-mVR3hiq1U2DATk4pWPRKHRm-NoFw6YhoohLjSt5XlTnfGC8Dux9l2TLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f407ca85.mp4?token=cMJUVfpvCamdk4rjhliAQ2uLrnIUoeCzTD3S19hCpoBB23NAvq8EB37LJbt1enkiUyqVU-HJszQ1DKG8chOplT8abYmhSdSc-UgPiaTKt1IrDdAIvb6-ZVrXTVQYHQSjYLyFdmVQOU5p1Ov-KK18oCtwuixQDgmNQK6l1ystuSEmgE_LlMtCA4AIXojgGuKHlrl0yW-dWo50zDKyeWClg_spelR6y3jlzU0G2CaXuK7PmAsi3ykro5W3VA1q-kZuf6EmbVJiRfWhqEZLe794cdICczVl0Bxbi5tidw3OH4CjYwmo6y4FgLCJRHEFtoS6r07JIJmbExCBNR7Pm58EtaijKf0o9nO45ZfVeQW4Hvo6hHsoy_HdLTcVPAS0doHG1wyanxSjgSkL-oYQb92oBAg53Qyqt01mP8qbRgwIbBWt5vsQlqtVltMWnn9eHlHqyrQQFkeddyGEEL5ZLuLPKudR-qUHbUxDBqkQqQv70-SPsCdDuBazOVMttkpQMJhSbW4LoqDFDKORcT8kjM6WVY3lo7e_lifGHvQvDSytI7nQnKhQhg1kSy6Gf_CtfjujUlWWewypbsT8mgz0kpO_Pg57vsp2-5qiB2yLAiJBwhhpxXhbmo-mVR3hiq1U2DATk4pWPRKHRm-NoFw6YhoohLjSt5XlTnfGC8Dux9l2TLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
آن‌ها به ما گفتند: لطفاً در مراسم تشییع جنازه ما را نکشید. من گفتم که این کار را نمی‌کنم و ما هیچ کاری انجام ندادیم.
🔴
سپس آن‌ها به سه کشتی حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132531" target="_blank">📅 17:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: من قصد دارم به ایرانی‌ها یک هشدار ساده بدهم که امشب به آنها ضربه سختی خواهیم زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132530" target="_blank">📅 17:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: ما دیشب به جزیره خارک حمله کردیم.
🔴
ممکن است جزیره خارک را تصرف کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132529" target="_blank">📅 17:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / وزیر دفاع آمریکا: اگر رئیس جمهور ترامپ دستور دهد، امشب به ایران حمله خواهیم کرد و ممکن است محاصره دریایی را دوباره برقرار کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132528" target="_blank">📅 17:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: اینها دیوانه هستند و باید ۴۷ سال پیش از بین می‌رفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132527" target="_blank">📅 17:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرنگار : امشب هم قایق‌های ایرانی بیشتری رو هدف قرار می‌دید؟
🔴
ترامپ : معمولا بهت نمی‌گفتم ولی می‌دونی چیه؟ هیچ کاری از دستشون برنمیاد پس جواب احتمالا آره‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132526" target="_blank">📅 16:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ : توافق ممکنه دوام بیاره، و ممکنه دوام نیاره، ولی میاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132525" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
خبرنگار: آیا به اوکراین خواهید رفت؟
🔴
ترامپ: من می‌روم. ترجیح می‌دهم جنگ تمام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132524" target="_blank">📅 16:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ درباره حملات اوکراین به پالایشگاه‌های روسیه: این یک اقدام تحریک‌آمیز است که می‌تواند به پایان دادن به این وضعیت کمک کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132523" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132522">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d492dd26e.mp4?token=EV5l665c6EBf332GcvS50ycze4PkXB5zkm1DluSK89TyXOM1MRg9SjYx3cJd1KAviKW18pwSjfqA5lBWn7NeY7z3CiobRLS4slbN3R-lJP32j0wNQKZWTVXYU1HoS-IVUPlg8bMUb8ZRhvr9KEfzK8uyQ0RHQQWPPB3PQiEIBQyXxQY_JGxBt3Ojc0rlN5gqemscYAIzdsqrkVOf0AgsyXCLJLgm60Zu_wsjfONZrcAq2W5SpA9-g8i1BByCEuO_7SaoATFHQ9EUDTMG7N2Xiogj9ZAz12ADisDrhiHvIrDqoW7zMddpI9b2BhqIX_dcZLKuXU8R7u4WdhxgJnICww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d492dd26e.mp4?token=EV5l665c6EBf332GcvS50ycze4PkXB5zkm1DluSK89TyXOM1MRg9SjYx3cJd1KAviKW18pwSjfqA5lBWn7NeY7z3CiobRLS4slbN3R-lJP32j0wNQKZWTVXYU1HoS-IVUPlg8bMUb8ZRhvr9KEfzK8uyQ0RHQQWPPB3PQiEIBQyXxQY_JGxBt3Ojc0rlN5gqemscYAIzdsqrkVOf0AgsyXCLJLgm60Zu_wsjfONZrcAq2W5SpA9-g8i1BByCEuO_7SaoATFHQ9EUDTMG7N2Xiogj9ZAz12ADisDrhiHvIrDqoW7zMddpI9b2BhqIX_dcZLKuXU8R7u4WdhxgJnICww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره جنگ روسیه و اوکراین:
ما جنگ‌های زیادی را حل و فصل کرده‌ایم. و این یکی، جنگی بود که فکر می‌کردم شاید از همه آسان‌تر باشد.
🔴
اما پوتین شخصیتی پیچیده است، و این فرد هم شخصیتی دشوار دارد.
🔴
این کار، کار آسانی نیست، اصلاً کار آسانی نیست. این نیازمند تعهد زیادی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132522" target="_blank">📅 16:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132521">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ به زلنسکی: ما به شما مجوز ساخت پاتریوت‌ها را می‌دهیم.
🔴
به این ترتیب او نمی‌تواند شکایت کند که ما به اندازه کافی به او امکانات نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/132521" target="_blank">📅 16:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132520">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fb7d4eaa.mp4?token=H145zeerAfw5dxSTVMYh8UgcPqUlO32aYXXjnDIcW-AXTrTzvcCtx5ybcw1kstvX2KkrcCQzwf_EQKbnHTzUeXFbtepH9ZxvDOEhTsR3TsnxqWSOVeSnUz0EgyZ_oJ6q6VlV5VAqggAIF0Y2e0fstsxz6ywR6izPjrhVPma3JNeOJVIMgraeHIvv4lXXVJcweXu52RIGmDYfh36Dq940Q7rn1YdcCRbjwtnHicMiGWNjC_aB7Q5_voCqrASK10Nq8lu-aRllM96jLRu8q0-X4CeR7QbHv6lY4YoH6ENKksBQhcjmVUn97VAlPCcOpo4DM7Oc61TfjuBBXZmbYJuGPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fb7d4eaa.mp4?token=H145zeerAfw5dxSTVMYh8UgcPqUlO32aYXXjnDIcW-AXTrTzvcCtx5ybcw1kstvX2KkrcCQzwf_EQKbnHTzUeXFbtepH9ZxvDOEhTsR3TsnxqWSOVeSnUz0EgyZ_oJ6q6VlV5VAqggAIF0Y2e0fstsxz6ywR6izPjrhVPma3JNeOJVIMgraeHIvv4lXXVJcweXu52RIGmDYfh36Dq940Q7rn1YdcCRbjwtnHicMiGWNjC_aB7Q5_voCqrASK10Nq8lu-aRllM96jLRu8q0-X4CeR7QbHv6lY4YoH6ENKksBQhcjmVUn97VAlPCcOpo4DM7Oc61TfjuBBXZmbYJuGPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران: ممکن است ما این کار را بدون توافق انجام دهیم. این آسان‌تر است.
🔴
این افراد دروغ می‌گویند و تقلب می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/132520" target="_blank">📅 16:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132519">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: رئیس‌جمهور اردوغان مدت طولانی است که دوست من بوده است. مردی خوب، مردی قوی.
🔴
او کارهای فوق‌العاده‌ای انجام داده است. همه جاده‌ها بی‌نقص هستند. همه چیز عالی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132519" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: ویتکاف و کوشنر به کار روی پرونده ایران ادامه خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132518" target="_blank">📅 16:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132517">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5cb41015d.mp4?token=Tee77USMWt7cr_8GqFhXC3Ju0qJTfWCjpzGhpxcOKMLl0kFq9ueOIGMJ9Y2mPYkTmXilfB9qMj4cEBY7QggdICF9zzGORtTW4-kjbuIG-mWwwUrm0tejwV1xNKUM3f46YqWMGEKIFiPGzuXoJzS62YOF-3h5OM4ANIxeOnsEFu6follloY3zXWHGP8XJC4K05xN0nt45vz4Ny8j8Hr0okz0Xhmpuvn2SdTdsmqxW2pkf0QysaqLL3ODdiylXtcnRgMVfVkuJElDDuWw3RkazM6FUSofI7o_cuML7CHvfvGCrZQ0pJLCvLd6aWSdAf1cNWbcd9SONrCgnzNTOUYiIfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5cb41015d.mp4?token=Tee77USMWt7cr_8GqFhXC3Ju0qJTfWCjpzGhpxcOKMLl0kFq9ueOIGMJ9Y2mPYkTmXilfB9qMj4cEBY7QggdICF9zzGORtTW4-kjbuIG-mWwwUrm0tejwV1xNKUM3f46YqWMGEKIFiPGzuXoJzS62YOF-3h5OM4ANIxeOnsEFu6follloY3zXWHGP8XJC4K05xN0nt45vz4Ny8j8Hr0okz0Xhmpuvn2SdTdsmqxW2pkf0QysaqLL3ODdiylXtcnRgMVfVkuJElDDuWw3RkazM6FUSofI7o_cuML7CHvfvGCrZQ0pJLCvLd6aWSdAf1cNWbcd9SONrCgnzNTOUYiIfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به اشتباه جمهوری اسلامی "ایران" را جمهوری اسلامی "ژاپن" خواند
/ترامپ: جمهوری اسلامی ژاپن 111 موشک به ما شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132517" target="_blank">📅 16:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132516">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40023a358f.mp4?token=OAHcyMrsFXQ3fYCGB14K19JU270uVttblruoSAA4UCalD6u-qM-t3p4gHLi2GcV9QIWvDJxDdjPBmaxWSUwoLsWV_GC4q8RdERWSwLUbmy6VeFL6-Ykwt1JYN19vFb53mIODo85ICmUQqbBq61wx-SSVTvNDt96oG_S36wbR6g6OV54PPOJnUrHWUGpqGo_Esd7gmiF2solgwCpnVWdAwoq3YAkeFB8r2zk6I8Q9LB2BqpMdVkTpFC4ZdR2K6tWrDUeFsHnYtEn1dyuUl5v-8-h0ood9ixH74h1nlBV_egdmKm62j_mpxJdOexh9wXs4GpPOTHV2bLDalnIftGbkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40023a358f.mp4?token=OAHcyMrsFXQ3fYCGB14K19JU270uVttblruoSAA4UCalD6u-qM-t3p4gHLi2GcV9QIWvDJxDdjPBmaxWSUwoLsWV_GC4q8RdERWSwLUbmy6VeFL6-Ykwt1JYN19vFb53mIODo85ICmUQqbBq61wx-SSVTvNDt96oG_S36wbR6g6OV54PPOJnUrHWUGpqGo_Esd7gmiF2solgwCpnVWdAwoq3YAkeFB8r2zk6I8Q9LB2BqpMdVkTpFC4ZdR2K6tWrDUeFsHnYtEn1dyuUl5v-8-h0ood9ixH74h1nlBV_egdmKm62j_mpxJdOexh9wXs4GpPOTHV2bLDalnIftGbkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جنگ با ایران: این یک جنگ نیست. این، خلع سلاح هسته‌ای ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/132516" target="_blank">📅 16:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132515">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها بسیار بد رفتار می‌کنند، همان‌گونه که در ۴۷ سال گذشته به همین شکل عمل کرده‌اند.
🔴
‏ ایرانی‌ها رفتار بسیار بدی دارند و ما پس از آنکه آن‌ها کشتی‌ها را در تنگه هرمز هدف قرار دادند، اقدام به بمباران آن‌ها کردیم.
🔴
‏ من از اقدامات ایرانی‌ها رضایت ندارم ولی موضوع مورد نظرم تغییر رژیم نیست، اما واشینگتن نمی‌خواهد ایران به سلاح هسته‌ای دست یابد چون اگر داشته باشد از آن استفاده می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132515" target="_blank">📅 16:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132514">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ: ممکنه امشب دوباره به ایران حمله کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132514" target="_blank">📅 16:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fcj2MKyG7VHOsv5NSsqb33wTlURjPiDFJzLM10AfuOBv3lZDNsEkQlj9WuVruV0rW52G4LZvIq27olPp_IsuT9zA28xQvYDl3WNC-lPuUwJjn4dp1nvNk8IsRDIMK6rAGIa9K9-I2TZLOsaQu3WC5J7OYF70xQZees0db7hC7ydGsbZFZTuN6WdR-gjlHywhazrIw4Hs--nrHW11pFNZNDf0yWFg-I8J4G80frDgrn2u7DvKD9LKhI2IwIE7kyS6HD5-gb82epuih2-7sPNvHQYlCXUSFilPPJlNBvcGbGy59oy8wdw-szl2lzfT4TOrY9SIIJUKvHdXCGyIkcgpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واحد آسیب‌دیده نیروگاه ری پس از حادثه حریق، دوباره وارد مدار تولید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132513" target="_blank">📅 16:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
شیوع ابولا در کنگو ادامه دارد/ شمار قربانیان از ۵۰۰ نفر گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132512" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/همه فرودگاه های هرمزگان به دلیل تنش ها تعطیل و پروازها کنسل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132511" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy52_PIN5h40Ofn4pZDDL3NfuIPz3LL3JtuQGklZalPokk7CaKTng7XAN485HrKC5LKlxFIBVoFmWeXW8V089GVIA5MQGfFZH8IW7mPAMYr6bwuy8LMaiWsdZ2B1p9lpMpVMfStBpwJYSSxv1X4OaX0QfVC-teNMq7qS-ydCbuZESNTSGC_gOGDYQ1__il51_fY2pOQHrm6X9QupG8rgImm12Entg_OOC872rjmR3cQARR_4M0XzDmaQCKhDGkTguIux1_aNEWVFzYsaVNlgF6cuYexrN9iNxH3KIhAWTqg7RSbrecALOyl1Yp8Xc7zdwgJVdMakKs7rPNmAKD2V9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایمز اسرائیل: "ارتش اسرائیل اعلام کرد که انتظار چندین روز درگیری با حکومت ایران و احتمال ازسرگیری کامل جنگ را دارد؛ ارتش اسرائیل همچنین از «هماهنگی کامل» با فرماندهی مرکزی آمریکا، سنتکام، خبر داد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132510" target="_blank">📅 15:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnrXP-eurUG0oumvuAC7-dY0rX9PYbN0xkfE8lDySCWPgLJwkQXGntyhRFxl-JA37vpsr5wFLXjR3-5VUAYGIOm72x00I33gD35MZRFNZjjuab3XEvfyYa0cjs_f9l0ZYzZ79pe1ZUo1BTlQs80mflC2s64qezQyn6wS8KpDGh2VzW1uB8jhH1p9srIIgkVVhnbcaLKlfGu7IvWHO-mMDnU8-6nxWMmfTng2KrK2oW9lcf0NsATVnoW3LYMk6Dx6vwrOHuyyRSLGhN2RQt_Q9RMLLtof75lAFA-UFAaQkv-K6s0BE0-VBLFiB91H-gHJYZQU8gCI9geIXtkvsAqivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت برق، آب و انرژی‌های تجدیدپذیر کویت اعلام کرد که تعدادی از خطوط انتقال برق هوایی در اثر ترکش‌های ناشی از عملیات پدافند هوایی، در جریان حملات اخیر ایران، آسیب دیده‌اند
🔴
این وزارتخانه اعلام کرد که این خسارات باعث قطعی برق یا آب نشده است و تیم‌های امدادی کار بررسی زیرساخت‌های آسیب‌دیده و انجام تعمیرات را با هماهنگی مقامات امنیتی آغاز کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132509" target="_blank">📅 15:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع آگاه: ترامپ در جریان نشست ناتو، پایان دادن به توافق موقت با ایران را تکرار نکرد.
🔴
او همچنین انتقادات خود نسبت به اسپانیا را تکرار نکرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132508" target="_blank">📅 15:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مقام آمریکایی به NPR گفت: «به دستور رئیس جمهور ترامپ، آتش‌بس با ایران پایان یافته است. رئیس جمهور صبر خود را از دست داده است. از این لحظه به بعد، واکنش نیروهای آمریکایی در خاورمیانه نسبت به ایران به طور قابل توجهی تشدید خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132507" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RONb0U4gq5f2EEllfcNomk9spNv59GPtn1P5jh5Nr7JGVO1u0obsGIQEM6sS-cKLYa0wGog79KVuowLmeHG_2UMvV2GLhFqDo70pXmrbuU_wHpX7In0cDKxNqRokidtx4kC9X3V-riwnqlaptm5VKXrdolWx1ViWqAlM-U_bNy-h4Nn1qN3JfosbLsl68r7ZCN65BjYb7ZYfmQPlYWq5IDc3EbCaD5ungT-y9Yy5_iP2gSHwIgpl5eXeFrMlyqWHzLDi5GOH8Ilqg8IxLiGM-KimNVfDwwwBdjfHDH5a2BeIO04kf5M8N8Iwm8DzkCV-oFfVn4mp2n19foTRc0ukwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عزت‌الله ضرغامی: سفیر ‎ترکیه را احضار کنید و به او هشدار دهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132506" target="_blank">📅 15:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
فایننشال تایمز: عربستان انتقال‌های بانکی از حساب‌های خود به دریافت‌کنندگان در امارات را به تأخیر می‌اندازد یا مسدود می‌کند
🔴
این مسئله تجارت را مختل و برخی شرکت‌ها را مجبور کرده که وجوه خود را از طریق بحرین منتقل یا از روش‌های پرداختی گران‌تر استفاده کنند
🔴
ریاض اعمال محدودیت‌های خاص علیه یک کشور مشخص را رد کرده و گفته بانک‌ها اقدامات استاندارد مبتنی بر ارزیابی ریسک را اجرا می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132505" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ام تی وی : لبنان موضع خود را تغییر داد و با رفع نگرانی‌هایش، موافقت کرد تا در مذاکرات رم شرکت کند. در همین حال، طرف آمریکایی از شرکت خود و حمایت از این مذاکرات با اسرائیل اطمینان داد.
🔴
این بدان معناست که این مذاکرات صرفاً دو جانبه بین لبنان و اسرائیل نخواهد بود، بلکه یک مذاکره سه جانبه با حمایت آمریکا خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132504" target="_blank">📅 15:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQCm_prhauNjSkBrb7ZkWQRTbtcq7C0-q2FlYqk3u490SCv8fSKsl5vyB8KXE3y2Be2GrwJlfluFjxglX7PC69bcR1P5PVTUWPJgRUQpigen45o0TQaXdXXTWapPcHgXTpgSAb1zA61KvlMV3R2LbLj2bFUckDyZVx_mjImpHfbipoUPkXFsan666zG25yiUKil4KX68Naa6_7yNfjEpg6oUrGqZ6RILwA5Ky7fAhIVWqZGiAWUVJs8Ott-cFz_qXN6y21GcilzgiVIh0hAkHCjaxYGaPCDaKChAzyaoLFIJBig9eFH8mCQEG93N8lRfMAkbM7BWEEaXnm7a5_ve1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترافیک دریایی کریدور عمان در تنگه هرمز به صفر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132503" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7EP1FE8Z_KK05RWY5JKqGvBYfH4XX75iJVeGaGQ0RLXlda3MO6FPZBKYjrTKGHpDgBgBgMHrJoZ1OXMDg_55xkEWspeZvFPUCDaw6rnDe64kcOpp8BxwJc4nzSt5JviGXMScsnoO-Surg__ibra3NZUKUthe5896NOqyILJsgP87SF-ioqe_0efL7wq67dgBJZCAAiQ23v4pd-qb48VCCcyY4tjmwRbmEK1tbYGPex2q-PxC0-fuZTcKT7f5kPz8Uyk7k1z3z_T_t_DzLPCMFnKvgD5uPjgLnunNotMSkNC54tYQL77h4Ig_JiqAldj952Ioh5oSfxRd2VjNAscxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل عملیات تخریب در شهر ارنون در جنوب لبنان را انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132502" target="_blank">📅 15:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رئیس جمهور لبنان، ژوزف عون: من مسیر مذاکره را انتخاب کردم، زیرا نمی‌توانم بی‌تفاوت بمانم و تماشا کنم که کشورم به خاطر منافع یک کشور دیگر، به سوی نابودی پیش می‌رود.
🔴
فرآیند مذاکره از حمایت اکثر لبنانی‌ها، از جمله اعضای جامعه شیعه، برخوردار است؛ جامعه‌ای که در جنگ‌ها، سنگین‌ترین هزینه‌ها را پرداخت کرده است.
🔴
من مجبور بودم گامی بردارم که بتواند ویرانی و تخریبی را که توسط اسرائیل انجام می‌شود، متوقف کند و در نهایت، به پایان دادن به اشغال را به ارمغان بیاورد.
🔴
من انتظار دارم که سفر من به واشنگتن و ملاقاتم با رئیس جمهور ایالات متحده، نتایج مثبتی برای لبنان به همراه داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132501" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-9kWWsSuDs3wfkMM4QnUEMKnvOSyWJospNYuDRxLYXKSDllIOY-_cyCgo06z9Lr4fk-4X_jdJyGM44beqkC4XFJ7EM00LciNlmza4h5AxTQrtMYncDLFHZNAJOo0dfB3sFPRV4k3854vuySyk0TRizDhFKAPk5ikjAe4wh4TdpReUJR1e24-IEr_2ScDq3aBebMUS1pRnbAcedosodHUWa9zv4ildbkYcCPK_O0JG8V49NzA5WcCwrVFoUKUgnDQRr4282MMTtgCLMXMOiEzfKogYyYq09M2f8TVnQmfH39poiVXEaNqvv5IVtlJ4dvP2W4SIQYfihA2HfGmYatSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اصلاحیه برنامه امتحانات نهایی پایه یازدهم تیر و مردادماه 1405
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/132500" target="_blank">📅 15:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4268fce83.mp4?token=DlwLAPtODX0pE6JLNqi3zqIUbELaDd32osnOE9GbNpErrS9Nnp8cZEmFPnZBHOWMa4fzPOXVAWEn_j1rz4ehQ7V9p6Lir-KydQaS2uyHxaqQOaqbgy4uzOPwCe3X98VbEmv0c2-jwmGtaSjiETHbhNffP4J4cUCkFY35AGJzkbXFXJqvKt5Xrmeu8Mfamspu1Siq7cUDNZIp5xosSxIobDHh7RTRgqUJ6b8WzwH70rUgrureuOQneP92kRhkQYuo6LVkI3f8hftrjXqkg4UXMly-kRxFXRK32GnZug00vuqHFAkjQ9a_yUm1OEfv26v_IwGyWe0w5YdXTe6UzRFQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4268fce83.mp4?token=DlwLAPtODX0pE6JLNqi3zqIUbELaDd32osnOE9GbNpErrS9Nnp8cZEmFPnZBHOWMa4fzPOXVAWEn_j1rz4ehQ7V9p6Lir-KydQaS2uyHxaqQOaqbgy4uzOPwCe3X98VbEmv0c2-jwmGtaSjiETHbhNffP4J4cUCkFY35AGJzkbXFXJqvKt5Xrmeu8Mfamspu1Siq7cUDNZIp5xosSxIobDHh7RTRgqUJ6b8WzwH70rUgrureuOQneP92kRhkQYuo6LVkI3f8hftrjXqkg4UXMly-kRxFXRK32GnZug00vuqHFAkjQ9a_yUm1OEfv26v_IwGyWe0w5YdXTe6UzRFQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: حملهٔ دیشب آمریکا به ایران کاملاً ضروری بود
🔴
فکر می‌کنم بسیار حیاتی است که آمریکا با قاطعیت و قدرت واکنش نشان دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132499" target="_blank">📅 14:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avD1XXyHyr-I1fCO3ALRlrfWGYflI0kEidwQFXkyUgv3_LBCibd6I2a2n5keBaUEOiBRALFdFL1iY8Q35d-h4PeVxY-Rx-9_KoR-ifSjLz51JqFj5qFlKVFKN6ezLCIQ7TFR7S9cdnoVStZvWwaBjrn6UeAnf80AN5IL-VIDKdXf1RnmNmchnO9G38IzukbiZD4uguHepcWsz252Y6YIo_tanKJ6fgfTV5IjpOVKo9Qmwrs5wUbrdlvnuEsNoChGvOu_4wBfYPuZkuONHHpm6cqenpv8x58l0O_NR2Q3ejW11AXZY8cm4T_tIWFR5XDLAystYmP7JLVfxggMKdwySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55185ece21.mp4?token=oGwBtzsO6MN-7gFZKuqhyhWxHkOPQJ6ddta3wbS-cTUSyjNUuJKXS3KPU7z-5RlL1gOjKXfVOl3TgsnrLTmv5bSOCSLqzsPZFg77ssvdy64WyxmiA2N18ZvNhd11ugaJdT72H1-9AS3MBlVni39NmSDzw7At28mw67nUH_ET2lC7VMDKIPnibrlz2EKFDLGmbap5XGnwTEBV7kLsls7Z9NyY6GS5P44Z2r_ylXAB2KGosSP4fqWZWd7z0DAQ95rBrXbfq9I9EzsDsSIreyrix8LiCk0JBTPAf7o2J3iFBoFCXDNzFb8xfYH5ZtPWDrRKcw-sPzS_eNis3zUYaBoWCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55185ece21.mp4?token=oGwBtzsO6MN-7gFZKuqhyhWxHkOPQJ6ddta3wbS-cTUSyjNUuJKXS3KPU7z-5RlL1gOjKXfVOl3TgsnrLTmv5bSOCSLqzsPZFg77ssvdy64WyxmiA2N18ZvNhd11ugaJdT72H1-9AS3MBlVni39NmSDzw7At28mw67nUH_ET2lC7VMDKIPnibrlz2EKFDLGmbap5XGnwTEBV7kLsls7Z9NyY6GS5P44Z2r_ylXAB2KGosSP4fqWZWd7z0DAQ95rBrXbfq9I9EzsDsSIreyrix8LiCk0JBTPAf7o2J3iFBoFCXDNzFb8xfYH5ZtPWDrRKcw-sPzS_eNis3zUYaBoWCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایالات متحده، هواپیماهای تانکر خود را از فرودگاه بن گوریون در اسرائیل به پایگاه‌های دیگر در خاورمیانه منتقل می‌کند.
🔴
تقریباً 15 فروند از هواپیماهای تانکر سوخت‌رسانی نیروی هوایی ایالات متحده از فرودگاه بن گوریون در مرکز اسرائیل خارج شده و به پایگاه‌های منطقه‌ای دیگر، از جمله پایگاه هوایی الاودهید در قطر، منتقل شده‌اند.
🔴
تا تاریخ 24 ژوئن، حدود 47 فروند از این هواپیماها همچنان در این فرودگاه مستقر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132497" target="_blank">📅 14:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE2z5vM-BvxntVBTcYQXQm24X-ugjxRvMdyMv7OxKV9rw9Q3FnpepgiAFCYiyyiXkHnjPnyO4dx9r3t0C8tVr_qQ8LCcZjNrMP_Ld1ETJJM2eunMjyjbL1QPplzDcErh4Xfqc_wPAFcszMfdhLthwycqD28Z6Ocvtad9TdtjAQt1I0PidBKCN14IizI5lxvpKCbJ-9sOOiCj6FMS3LLwizxcOdXXWQR2FdyfO_iFlL3CW4QrJC3zojCpk3M_teqaGGDeuL9Evxaciu6X5f7tkrvy9NKCAYrR-RQqODJamEva34OurBz47uWnd_TrKH-paX8jUDu5ytpXdzxCiH8R0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای از یکی از سایت‌های پدافند هوایی ارتش در جنوب کشور نشان می‌دهد یک لانچر صیاد-2/3، یک رادار کنترل آتش نجم-804 بی و خودروی ژنراتور همگی در جنگ اخیر مورد هدف قرار گرفته و سرکوب شده‌اند. علاوه‌بر سامانه‌ها، شلترهایی که طی یک سال اخیر ساخته شده بودند نیز در اثر اصابت بمب‌های SDB-1 آسیب دیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132496" target="_blank">📅 14:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
موبایل در امتحانات دانشگاه آزاد، آزاد شد
🔴
بر اساس اعلام دانشگاه آزاد، همراه داشتن تلفن همراه در جلسه آزمون پایان ترم تحصیلات تکمیلی با رعایت ضوابط و تحت نظارت مراقبان مجاز است. همچنین در امتحانات نظری دوره دکتری (غیرپزشکی)، استفاده از ابزارهای هوش مصنوعی نیز بلامانع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132495" target="_blank">📅 14:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGey7cunPzJXZzBxSSuQ6UJcONCD4Xe7ANldTDTC8pJ5DTA__fh66p1atJfXGFpyg-0qaxQn5RdNK0mtvjEt0QrkyWnjAKuf_nBfahha4SIS7N9Z8g0qwhgs-RohixuyTrA7J-sW5Z8zCEyBeDgw6lWAVulRSfeBCDg4LxcRHTsufj_2sDk-wVwbch7ygcHYIH6SMr3V-tPvBL2NarW0duBuv0unJ1le1wQasjv94J8ug-LZ1RW1UFghlwwhVw4Jr2_lPpL582UQZENzuD-_I2VKUOPzhuKcU40TWhuM5isQeChL-xS7QFdeHPyTUMJk2Xy8xLGqBg-DDGxOEZH_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اوکراین گزارش داد که یک هواپیمای جنگنده روسی را سرنگون کرده است
🔴
آنها محل سرنگونی این هواپیما را فاش نکردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132494" target="_blank">📅 14:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فارس: ایران باید پایان رسمی تفاهم را اعلام کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132493" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
مردم محلی شمال شرق تهران میگویند پدافند در پارچین و خجیر فعال گردیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132492" target="_blank">📅 14:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یک کشتی در تنگه هرمز مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132491" target="_blank">📅 14:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
چین به آمریکا و ایران درباره «شعله‌ور شدن دوباره جنگ» هشدار داد و از هر دو طرف خواست اختلافات را از طریق گفت‌وگو و دیپلماسی حل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132490" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
جو کنت، مدیر سابق مرکز مبارزه با تروریسم دولت ترامپ: حالا که تفاهم‌نامه با ایران عملاً مرده، دوباره به تلاش جهت یافتن یک راه‌حل نظامی برای تنگه هرمز بازگشته‌ایم
🔴
مشکل این است که ما این تفاهم‌نامه را امضا کردیم، چون هیچ راه نظامی‌ای وجود نداشت
🔴
بهترین گزینه این است که به سادگی کنار بکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132489" target="_blank">📅 14:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل اعلام کرد فرمانده یک گروه ویژه «حماس» را در پی یک حمله هوایی به جنوب غزه هدف گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132488" target="_blank">📅 14:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اسموتریچ، وزیر اقتصاد اسرائیل، درباره ترکیه: ما برای هر سناریویی آماده‌سازی می‌کنیم
🔴
ما درک می‌کنیم که یک تهدید وجود دارد و اجازه نخواهیم داد که چنین رژیمی، وجود اسرائیل را تهدید کند، همانطور که اجازه ندادیم و نخواهیم داد که رژیم ایران این کار را انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132487" target="_blank">📅 14:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWRCgy_tV26lbay1LBz3dfH02LAHEZwoAbayVWRYCxhOXU51oK6YvNdU0cohd43UHB0o6RTSzmWrv7LnjCaLFxh2YiVd0S9ifwUN1aSpZLDbuU3ZX-INYYAjImKergkM7MNdoUluWryXQ6IyjzkDsQxkvUaHHyfiGOFxhR9GKVCFomifO-RMqpoZA-IxIsaqRCh2sSZyiOqv2bRiYrQbTC1kkRpHxwFnwt0XaCu-IwplD5GKyxUxuLcZ3CkDp-FFEfzonEugQFXiwJafKdWoWjFtceGWUhVM2JENqbi94-etIMUuR6K9exKaYxuQRbGocnK1s_aMZm4fmo5RvkKYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان نیروی هوایی آمریکا هنگام پرواز بر فراز تنگه هرمز در حال خاموش کردن فرستنده‌های شناسایی (ترانسپوندر) خود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132486" target="_blank">📅 14:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اتحادیه اروپا: حملات ایران علیه بحرین و کویت غیرقابل قبول است و حملات به کشتی‌ها در تنگه هرمز را ناقض مفاد تفاهم‌نامه می‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/132485" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / رویترز: نفتکش آمریکایی شورون در دریای سیاه هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132484" target="_blank">📅 14:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سازمان دریایی بین‌المللی: ۶۰۰۰ دریانورد همچنان در تنگه هرمز به سر می‌برند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132483" target="_blank">📅 14:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / یک مقام ارشد اماراتی به روزنامه هاآرتز: جمهوری اسلامی ایران امشب بهای بسیار سنگینی خواهد پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132482" target="_blank">📅 14:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت خارجه عمان: تشدید تنش‌ها در منطقه، تهدیدی برای امنیت و ایمنی دریانوردی است
🔴
طرف‌های درگیری، راه‌حل‌های دیپلماتیک را در اولویت قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132481" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: ما دیشب با رئیس جمهور اردوغان شام خوردیم. من به آن نمره ۱۰، شاید ۱۲ می‌دهم.
🔴
ما جلسات بسیار خوبی داشتیم، به خصوص با ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132480" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
قیمت گاز در بورس‌ های اروپایی پس از اظهارات ترامپ مبنی بر پایان توافق‌نامه با ایران، افزایش چشمگیری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132479" target="_blank">📅 13:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad_UlZAe13JfsUEQnFxCMc1n_R9LvuU3BbbkKrAGTSukZWmYuRR5lr0oHkCnJ1OBsYTKh6pfitOmucEjQoak3oZAapD4FfsofTS19xtVzggbTj9lMlsaFDpa7yNUABewy992bfD-LMQMB9luKaET5QpT1AKqt7lMxMImx_cAmzBR4Nx1Wkboi9D9MxQ_S4JYdpZyWCd4rh9Dq2V2vI5hiJfj1AfHwgWAKmR28ueuQ1WTwuK00tRBMNewJufC6fut_T0KYCXaYhijrPe5VDZr6uzoGKzBPJP41a1EM2pzruSUjI6DoDbKEh-j4_RrDzrGmInZeoFAuScUg4nQclEk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccshJRVWksTzkIFJAcakUg8IgkvT_vQVo0NXM2xH72V0Aatm7bsRn00hcB_d6_RUV3jSX4ssaeEJ2g_UE5q4_xnbRhUsCQ15fY4pBC_y9udax4lQjkQ4AH1eZbirI93LZY9HElEM5KyQ4m-67BNP_DgMuPGLcTIVGDjjLHujEEJJrU5WILUpFve4yYiPE2rKLB8-1ErWOhuqoYyk7Ebr7XDJXtI7P1dKMbXvyogHVlhMOMmZvqRupY2-5e1wX-7W1HL7p2cHLiUcJtqlN1ZMzqLcmthKHjsbVhBhbhrGxqRqFF5Raqmf6p44HCl-5L0sMr4w--9M7K_4ThP202pWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpsfKOK-5Qw28I76OjYfGe7clBQY7BqtrfloD1NJ-gYCK4di8D3nBLcaPGgXt9GKZh10MJwEEJ2VQE3iyuUWeuUKrJRe_T4A2iTjITDJMglZGDa0wZmOIjFTMo0rzluxMgdVQbg1oNmOUk-u2nd3ktEsB711hGH8faDvagb4DzMBxOO1O_bv4YibeecTjg4TtZYUb0CcLw60nTwyHGdL1X0tKgLEfDV0Ow7RVtukB6VcpY-M7rmRuCn1HDPU7fdzdnCsLYK8fQrKk7mLD0g6XxRbhZxLmph7qc6wjL6Zvr6f-MC7DWhk93M_ounD5ZqdgSRyy5UuTdkM59vwpZNF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XnE1i_HoX01cDVf-WlnxfAX-KnFmBkLbD6HnysqSbjd9TqVQGEyFLapie9XoGD_2c3mcHNkZVNQnMm_SqU82BRjGCx_uR0q0DGlUizwbOf0a6Meq_hRGKMDjIKAxx3WCGiOhvYvfe1R0EpAyExsNrwp9GTJgcA3BpL6WbRW0kmhL1g0H-gzBnUqJH8_ROD8tshRbvSYtNZ2uS-JuV2uzX9s8o2M0bdFlSQOSQUUSuPUU-ZGhP-EQmHgreRcXpYwnW8s2bZNmXikP1fQnaYJt_SIR0poH6T8vSNQt6_7fm5in9v6ZA_WN-8ARegoMZsA8tU16Qv4GkOsQrgtUvB2wRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تسنیم با انتشار این تصاویر نوشت دیشب یه پهپاد MQ9 زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/132475" target="_blank">📅 13:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کرملین: در برابر استقرار سلاح‌های هسته‌ای در کشورهای بالتیک، اقدامات متقابل اتخاذ خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132474" target="_blank">📅 13:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3ZK3HH1sTJWLzTDFkI6SII5GXRwKvRLIMEZG5KiZ8kaKY1lVnZRboA-HJMigqnsOknDPRYaWpT8fUhdkHDaa9Rj4IWMkzyuEs5XBjwniQ3b8i3ZkZ-L9NB-ky2j0JxDBzJxPI1cwxx_KSg0cITrTnv0Lo0UErIh2SM6-Acsj3-8AR30QIva_DF6Xd0JYPiCkRia4D4MWra8CiD4n6XeSoBPwFYEhEXEgn_6XwFPWlDYi6waiO69EPGHWjCE2TL3OlE6VVcAsPxn0KMRQevJMaI0LHDJPOk7WBoO_dhuIttBgXI2rBymqfYZ5v6Sswpwg0aeI2-fwzxTmhrMG8tgDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاهده دود در آسمان بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/132473" target="_blank">📅 13:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM6QLPVqWV9vny7R8oK03qXsT9z6swPdSn6K1lg6tLBvodF889EIUTZgK9IwjiKwt8Ng0TuDj8niuX3UuVArMRM3EcMAm8dQR9ZxwdEWlVe0qGt7sZHFY08DmbK4Du_cNZzUWAnFXWrtcGDLvblMmvZfYePu1Wjf__3gBZvzBZMrlneE53IlZIII86AjQwHmkUXpuSR0_EXPjTolojL8ZaDV1o8-yBfKgv5Guwhy3BUOdVGI-iu9NPRr1bGNz1tpAD6AV7dTuuZwIT55L7OftWHptv78JLpTTwLxqLUcKQ1NzGqdCMiq_vQ3oHVIT8QEukE6GrR7JLJn-5hkK8UH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات شدید تندروها به قالیباف و پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132472" target="_blank">📅 13:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132471">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb8b1d87d.mp4?token=iiIAUSjbNWVjojpauUcazsrSERKod2kN2Mu6QuCsN2ffMBXUC63iZykGld3Gg4dNDkRznrPuAKw9aFGZEhZ5xmJMJxn7gHO2wCkb05gdiW0J142k0pWA3codedbpUf_-6ZtiXYR5i02OaM2xKHAY8EGqzymLW76c6GJ6aUivS2Idkb4UKu77wKgz3VipKumHCTUjjRaO5YEzIYl5J0oB1MUNvvUAmgXMqsQf8kQWDKXY0BomTKe2Dcf6DUsJ2FrO-3gszH_QXl3Y2-yILnJppnW10_z4PsKe4BVHIh0L0ObbsL5jAiQfSYANlrLYbu_BSn2Vj-32qBzo866i3BVSoxye4U4lgBgWfgZu5EoRn3sQsg1l0BCwFcHVAKqLz3s78FV-x7Rc8ccShpVXb-WEu-dyxDs2u3Ay2fqd_gyojNNd9E4kOLoYRH7IT6JKQagCqmJZDZRnR027wFPQfA26KLEK_PNo5suq3hzFmAJT3GTRoNgWpM4t2qk0PfB4fC0BsG0Jj0oRTvJq8u24f5nPA4VCZzCbr51kpZFtpbnT6hie4FXeLHTwAq0g2nehW7c-6J1hEmUabWBZtpMOFfazAk_8WSs421tjzdNwyXQPxWxpq17rhKvcqBZInsWDOjGENHz49sVCuW7G0d91GG5aoN2Zb-I3PpKDAdQLhYlaY64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb8b1d87d.mp4?token=iiIAUSjbNWVjojpauUcazsrSERKod2kN2Mu6QuCsN2ffMBXUC63iZykGld3Gg4dNDkRznrPuAKw9aFGZEhZ5xmJMJxn7gHO2wCkb05gdiW0J142k0pWA3codedbpUf_-6ZtiXYR5i02OaM2xKHAY8EGqzymLW76c6GJ6aUivS2Idkb4UKu77wKgz3VipKumHCTUjjRaO5YEzIYl5J0oB1MUNvvUAmgXMqsQf8kQWDKXY0BomTKe2Dcf6DUsJ2FrO-3gszH_QXl3Y2-yILnJppnW10_z4PsKe4BVHIh0L0ObbsL5jAiQfSYANlrLYbu_BSn2Vj-32qBzo866i3BVSoxye4U4lgBgWfgZu5EoRn3sQsg1l0BCwFcHVAKqLz3s78FV-x7Rc8ccShpVXb-WEu-dyxDs2u3Ay2fqd_gyojNNd9E4kOLoYRH7IT6JKQagCqmJZDZRnR027wFPQfA26KLEK_PNo5suq3hzFmAJT3GTRoNgWpM4t2qk0PfB4fC0BsG0Jj0oRTvJq8u24f5nPA4VCZzCbr51kpZFtpbnT6hie4FXeLHTwAq0g2nehW7c-6J1hEmUabWBZtpMOFfazAk_8WSs421tjzdNwyXQPxWxpq17rhKvcqBZInsWDOjGENHz49sVCuW7G0d91GG5aoN2Zb-I3PpKDAdQLhYlaY64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، رئیس‌جمهور ترکیه، رجب طیب اردوغان، را با کیم جونگ اون، رهبر کره شمالی، مقایسه کرد و گفت که نمی‌توان به ترکیه اعتماد کرد و نباید به آن هواپیماهای جنگنده F-35 تحویل داده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132471" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132470">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کلاس های تابستانی دانشگاه ازاد مجازی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132470" target="_blank">📅 13:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132469">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نخست‌ وزیر بلژیک: ایران موضوع ناتو نیست اما درباره آن نیز گفت‌وگو می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132469" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132468">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اروپا: شرکت‌‌های هواپیمایی باید به دلیل تنش‌ها از حریم هوایی ایران، عراق و لبنان اجتناب کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/132468" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132467">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: اگر ایرانی ها سلاح هسته ای داشتند استفاده می کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/132467" target="_blank">📅 13:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132466">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d24ddfc6.mp4?token=SsfiTLk-j6GixS_9ZnRkuLQOqh9-0CboOqd5ejQhe8BcERON05grOIn7vbWIEGm8-nnQtd7aVN3KuuL1a5x8cG8Sx22LXJW3ygq0bM-1VnOJrnOSOv-R3IiesJyHcuwigCcTznaMM8g739UdYaEJmgYOOHi1zFJyd008KbUMWa1C90DIgxuH2NZUiY1EobMGvcVAgoDVTnW08Ekm3gBxwg3CJ4eJrxwJEDKd3Emc9Y4fPS4o9awjkQVkv_ZyLssocRD97GjbWVQWDMOFNaeprMbX3S8f_Rz00rcmTRV91vuXsH2C9zu7-WTMyz0pxOqPyqBUVBzEMC1lRLmele7LzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d24ddfc6.mp4?token=SsfiTLk-j6GixS_9ZnRkuLQOqh9-0CboOqd5ejQhe8BcERON05grOIn7vbWIEGm8-nnQtd7aVN3KuuL1a5x8cG8Sx22LXJW3ygq0bM-1VnOJrnOSOv-R3IiesJyHcuwigCcTznaMM8g739UdYaEJmgYOOHi1zFJyd008KbUMWa1C90DIgxuH2NZUiY1EobMGvcVAgoDVTnW08Ekm3gBxwg3CJ4eJrxwJEDKd3Emc9Y4fPS4o9awjkQVkv_ZyLssocRD97GjbWVQWDMOFNaeprMbX3S8f_Rz00rcmTRV91vuXsH2C9zu7-WTMyz0pxOqPyqBUVBzEMC1lRLmele7LzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخبه دانشگاه شریف: تنگه هرمز عملا از دست ایران خارج شده و ایران دیگه کارتی نداره، اگه شروط ترامپ رو نپذیره کارش تمومه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/132466" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132465">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
والا نیوز عبری : ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132465" target="_blank">📅 13:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132464">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اتحادیه اروپا: درگیری‌های آمریکا و ایران مذاکرات پایان جنگ را پیچیده‌تر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132464" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132463">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اردوغان : با وجود کارشکنی‌ها از ترامپ بابت مدیریت قاطع بحران ایران و پیش بردن آن به سمت حل‌وفصل تشکر می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132463" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132462">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزارت برق کویت: خطوط انتقال برق به دلیل ترکش‌های ناشی از پاسخ به حملات به این کشور از سرویس خارج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/132462" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132461">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
اردوغان : تو غزه و لبنان، همه ما مسئولیت داریم
🔴
همچنین باید با تروریسم، در هر شکل و هر جایی که باشه، قاطعانه مقابله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132461" target="_blank">📅 13:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132460">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نتیجه نشست ترامپ با اعضا ناتو / ترکیه هم وارد شد !
🔴
اردوغان: ما برای یک عملیات احتمالی پاکسازی مین در تنگه هرمز آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132460" target="_blank">📅 13:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132459">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
اردوغان در جریان نشست ناتو: «ما تلاشهای دیپلماتیک خود را دربارهٔ ایران و بازگشت کشتیرانی در تنگه هرمز ادامه می‌دهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132459" target="_blank">📅 13:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132458">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJrdeu5zqyMeDZcGg-6J9ETXqaLwq5hG5d-eXDFkJUv4yCAbuv01V3268W7WXQhJ0MIaBjrH4jmOqOYRYQBTAzzig4otJV0qfG53vBJAOpnWFzVfc43kSllIR9H8F2Th27LtKwxKJqcU_A61UsQLBxWbOcRw9ldA1fazU9XNy12wUeRw1c6nVKmxDlmfjBkbt05GLW-2PXckPu0RyS54OAwQIu70LNhmE2Qi_F4_llIV5EG2GUs-5Rs8zcko5OcwZBjL4fleQGBa4LjaS_mlOgKa017oKGtXg6LHRJlVzFr-dc-8FRgIzY3sQjSwG_L16-EM2O5Yq8uLkQkz1xAfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت تتر در پی تنش های ۲۴ ساعت اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/132458" target="_blank">📅 12:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132457">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef22ccab1.mp4?token=gPIEJv5-dF7DjcEj7IwZjypEi2GhwcEoV3JGqO9SCGNjNjizFNicjg4wIyYoCQ8zYL2iJPwT7xVLIv7jU9dfPxDnMDNq0HkhLgjZHT90fpuoCastf0526Ke46Bgid7Nwv2DH8zOfhPN99j9lqLCSSFprwgOv-zw_YmTD0KUmk1CfctcwVElV4nFzhwVaJbPVwtineOZG-h2KXwg6pZSSYZaBvRYWJ-NfMpCODtMfR19mziWEz5IaZOhDc3mn0jrhcPJL0WbVHesS1-ZjbeIa_iShDaMjrJyjFxJHX3WWYLT404xcT1quUqOhWy_jUqsPnFL1I9Zo6zG0u7v6EfXAJQXnoVre7_226BRgShGH-TeQ8JJ6ucGZTxuZMQeOWH1chUxtNmZdoucDQ3ayCOK0OtWzdFw848AT0iv636Y8w4861sJVm5uhfYTz0lst4_22Mdm9aoZoCXfi3mzy9LTtYff2TyBYvQ1cpkxNqz2GlnRacYZXnV80QY2WgIFV3LRQyVH6uvnjSoJK9jrPzK7s1Vc5uXIZ7ZFhAqtkCb4dZhYewJzDnPhUXQzc2Rb4wt6sbJ3JPzbmB6H5oBXk_A392l6RKyHiV-bMUeXbTsxqmpHb2z5jZqSPcvFfOeeSfK2rb_TDd7kVfpE8zJ7O6PmyqZS3ZBg1GZo_FYS7ZX7_ams" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef22ccab1.mp4?token=gPIEJv5-dF7DjcEj7IwZjypEi2GhwcEoV3JGqO9SCGNjNjizFNicjg4wIyYoCQ8zYL2iJPwT7xVLIv7jU9dfPxDnMDNq0HkhLgjZHT90fpuoCastf0526Ke46Bgid7Nwv2DH8zOfhPN99j9lqLCSSFprwgOv-zw_YmTD0KUmk1CfctcwVElV4nFzhwVaJbPVwtineOZG-h2KXwg6pZSSYZaBvRYWJ-NfMpCODtMfR19mziWEz5IaZOhDc3mn0jrhcPJL0WbVHesS1-ZjbeIa_iShDaMjrJyjFxJHX3WWYLT404xcT1quUqOhWy_jUqsPnFL1I9Zo6zG0u7v6EfXAJQXnoVre7_226BRgShGH-TeQ8JJ6ucGZTxuZMQeOWH1chUxtNmZdoucDQ3ayCOK0OtWzdFw848AT0iv636Y8w4861sJVm5uhfYTz0lst4_22Mdm9aoZoCXfi3mzy9LTtYff2TyBYvQ1cpkxNqz2GlnRacYZXnV80QY2WgIFV3LRQyVH6uvnjSoJK9jrPzK7s1Vc5uXIZ7ZFhAqtkCb4dZhYewJzDnPhUXQzc2Rb4wt6sbJ3JPzbmB6H5oBXk_A392l6RKyHiV-bMUeXbTsxqmpHb2z5jZqSPcvFfOeeSfK2rb_TDd7kVfpE8zJ7O6PmyqZS3ZBg1GZo_FYS7ZX7_ams" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سران ناتو در یک عکس خانوادگی در جریان اجلاس در آنکارا، ترکیه، حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132457" target="_blank">📅 12:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132456">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpVMbJ1pv85kF4VegM3esHK9QtoHdXlYhE0BbECJe31WP6skMKZbvC0rdZmvZDl2fx79jS77DgND-G7HHXDKsmARUpX6-rNjcmLsM1Aa5I61-zq6CODVckfjGH3RF_lV0P2VbICdvY1cKf0ZAw6YhOzxDWyJlJsjA-f0rsbf2TaCAGkCb09_BE95x5WSWaVb5fdSJxIBIBwUpVKl7ng5KYvlb-cIrbCMvXfR95306gJ-Eneng4reFyF3ugZerKHNU1PgMuGE3FfS4sXLXvvpjMN0kFLbSMzF62COXBgk8dL8fQCH5Iy0X-C_61LgKiqlxnd2yDtusQNwkz90msiAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:باید حملات رو شروع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/132456" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132455">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb87e8e96.mp4?token=eDTjic0et9Gl1KTgaVHHg_1qq7VDUNHLwa9gHwLFgVDUpv-IyLt9FiVWV0PG_z8caXKsnzxKP9BLTVFRxfsLK0jTk5Omzu6e-QhHX4OmSs9AI-XV6wO32dbR1GwKePXG58DaygM5Ea-or6uQ8dl4D6T0ZxHCk5yYSXfBKSx_moxAzDciZm4oQ_KoblgMC3c09zciKcF_ZLu4747slBXSfR-ENZEUZY6BPPSZV1BBMwrzhH7byKGGupB-nTOk1uegIS4EUo9welnuEPqgkwzoeOjtUFZnAfHA22LEiVQQl8jKv2XH1to8l8VlwgPWxR2Cc77VlXi-cK1d1eMcLwYO6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb87e8e96.mp4?token=eDTjic0et9Gl1KTgaVHHg_1qq7VDUNHLwa9gHwLFgVDUpv-IyLt9FiVWV0PG_z8caXKsnzxKP9BLTVFRxfsLK0jTk5Omzu6e-QhHX4OmSs9AI-XV6wO32dbR1GwKePXG58DaygM5Ea-or6uQ8dl4D6T0ZxHCk5yYSXfBKSx_moxAzDciZm4oQ_KoblgMC3c09zciKcF_ZLu4747slBXSfR-ENZEUZY6BPPSZV1BBMwrzhH7byKGGupB-nTOk1uegIS4EUo9welnuEPqgkwzoeOjtUFZnAfHA22LEiVQQl8jKv2XH1to8l8VlwgPWxR2Cc77VlXi-cK1d1eMcLwYO6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به نظر من، اردوغان هم از ایران خوشش نمی‌آید.
🔴
اردوغان شخصاً فردی عاقل است، در حالی که ایرانی‌ها (به طور کلی) رفتارهای عجیب و غریبی دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132455" target="_blank">📅 12:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132454">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عمان: حملات ایران علیه نفتکش ها در تنگه هرمز را محکوم می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132454" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132453">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
العربیه: قیمت نفت حدوداً ۶ درصد افزایش یافت و به بالاترین سطح در دو هفته اخیر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132453" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132452">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: "من از بیبی (نتانیاهو) خوشم می آید، او دیروز حرف های بدی درباره ترکیه گفت. اردوغان عالی است - او به دلیل من به جنگ نپیوست."
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132452" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کویت اعلام کرد که نیروهای مسلح این کشور، دو موشک بالستیک و ۱۳ پهپاد را در فضای هوایی کویت، بامداد امروز، مورد اصابت قرار داده و ساقط کرده‌اند.
🔴
وزارت دفاع کویت همچنین افزود که این عملیات هیچ‌گونه خسارت مادی یا جراحت انسانی به همراه نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132451" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس امروز نوشت که رئیس جمهوری آمریکا، رهبران ناتو را که برای حضور در اجلاس ۲ روزه آنکار در ترکیه حضور دارند با انجام مجموعه‌ای از حملات علیه ایران و لغو مجوزی فروش نفت این کشور غافلگیر کرد.
🔴
در ادامه گزارشگزاری آمریکایی آمده است: این حملات متقابل پس از حمله به سه کشتی تجاری در تنگه هرمز رخ داد و شکنندگی توافق موقت برای پایان دادن به ماه‌ها جنگ بین دو تهران و واشنگتن را برجسته کرد.
🔴
ترامپ این حملات را اندکی پس از ترک ضیافت شام به میزبانی رجب طیب اردوغان رئیس جمهور ترکیه، انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132450" target="_blank">📅 12:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Icb_gFlYVavzVGk-jDV6AN-TiYtOAXmu6PBO_lOoSh-AMSCtamKexCzbu9NNsM51Em3JovFns4kpF48q0I5-Iv60x9vOQKxBu3d6vOhcbadG56rk97PaA7_MhFprO1bOZ2jlIQb0f1VGcdmKDr-rjOBuIAk9cKpyNaVLFrc78Bb1FUFMHJXHVhPlJm0PrcMgNLOlM4qQqr-zJj4h96ZCIqrJjEBRRPY3K9dB6YUJEzu_cHgmglgVS8COi9yu0Qyu0cKDXfjLjyWHdu0T9vDtH2lFFCcULi8pjLzoa6R_AC9Sct0k6aA1IjanzrtFI8L31leoCYOmHjZ2xSvEh54vag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، احمد الشعار، به آنکارا سفر کرده است تا در جلساتی که در حاشیه اجلاس ناتو برگزار می‌شود، شرکت کند.
🔴
قرار است او امروز با ترامپ دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132449" target="_blank">📅 12:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRWdjTK1vnq5zsWWBYXfW0E5K-zZo7f2g3tZt0Ulh1jLWPl4uhmUi0Gqh7RmVoeiBBeaWTmQBnK6tYOQ7Ih34x9r68gUPt4zEqxdxOb6D9cJ4_pFmaSMVbvgNd1k0hP45k4CkjhJwjUHvy98obAajR4Ag0GSTWSNdiPzpjRwhG00RxblxLwvkOImG_B7H1VlPE1W4WEzMuBTAq87Ma13_7aUFJxtfRR3FgBFKP7W32CsWLB9JfUAbCzAtPoLDWMWLiKQdG5ws6F3v3AECfeID7c-4_2U2GnWkMKJNRtYfGZZPC4vda2GhCCfAf4qjdd-pCFaAJJbZdal9b_VlZ4GKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : رفتار دولت آمریکا به عنوان میزبان جام جهانی، نشان‌دهنده سیاست خارجی همیشگی آن است: زیر پا گذاشتن قوانین، زورگویی با رقبای خود، ایجاد موانع و تقلب.
🔴
این همان روش "اول آمریکا" (MAGA) آن‌هاست. ایران از چنین بازی‌هایی امتناع می‌کند. ما به طور قاطع از حقوق خود دفاع خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132448" target="_blank">📅 12:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست.
🔴
ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. دیشب خیلی سخت به آن‌ها ضربه زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132447" target="_blank">📅 12:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دبیرکل ناتو: ۵ هزار هواپیما برای حمایت از عملیات نظامی علیه ایران از اروپا پرواز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132446" target="_blank">📅 12:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / جروزالم پست: وزیر جنگ آمریکا، به دنبال حملات علیه ایران، سفر خود به اسرائیل را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132445" target="_blank">📅 12:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً.»
🔴
او ادامه داد: «من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.
🔴
چون اوضاع همین‌طور پیش می‌رود، اما ما آدم‌های فوق‌العاده‌ای داریم.
🔴
اما این‌ها آدم‌های شرور و مریضی هستند، و ما باید سرطان‌شان را ریشه‌کن کنیم. سرطان را باید زود از بدن بیرون کشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132444" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ : فکر می‌کنم مقام‌های ایران بی‌کفایت هستن
🔴
اگه کاربلد بودن، ۴۷ سال پیش توافق کرده بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132443" target="_blank">📅 12:18 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
