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
<img src="https://cdn4.telesco.pe/file/nDNjPIM_DSd-c2uXfSExS60To_frAVbQuVV2HSLR40zzAk3urnJ_EAs4DOzoT13WKpisFyySxKR7fftxlwIARt9ROiV4lMQdi0m-OoI4TU5qlHKv2Nr3sa31yo8FycJqBu72hIbLIJQd2FwDYtVp7T36zJ7yEMXjYipyTqVgur1js1Fex7MeCrxoUhtct1njsqfj-CdOzUgv-fo0OxYUnAECy_uLT5VHyln_05Z0j2386DsShkeZEkKCOAkRxNNrpmDGq0qT9VwWmhXoSzpSalYc5LNVy2QuHgsDEp2NBUHoIWZR7uDTh7gM4lKbCGx2Dfu2E1QFifliRiV3-p_LBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 993K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 13:27:21</div>
<hr>

<div class="tg-post" id="msg-142802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آکسیوس: روزانه ۱۰میلیون بشکه نفت از تنگه هرمز خارج میشود و ایران هم شلیک دقیقی نمیتواند بکند و عملا تنگه باز است
🔴
پ.ن: اینم از تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27 · <a href="https://t.me/alonews/142802" target="_blank">📅 13:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5tf3eWQWYbyHOo-C1r9FWnZwTjDapHIWGBsoXZ8tux4f3iZVc6PVPg-f_F_-R3cTpAbj4vw8YD9Hj_tT2qz_UxapVagDr4FDZk4xhx7jpYBSfWeDB0idtHaQCuhRpr0gm_kqeWTUjg2egnTnAsVtrd8zm3pzGb9YZIJ0uikr4iYBna04QbbS6AUqy-DNrhgH_xPIHCa77yBMKhzmO65D6XehkyGgXziD5dH1TAuZoaNid3zzVjsnvAUDmjbyGmUcKijScfovjh1fXCi5kXIV_z0u6hssn_BcNJ8UHnPTjvMwXcETOnsWDRbIpQpHIQmyWgpjk59tWEomMpPYB55Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حادثه در نزدیکی سواحل یمن رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/142801" target="_blank">📅 13:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csxkq7MzX2jPnWZZZX67v8OiazMwHRsQnjDXFJmlukRkIXqn5nzcRYdmY20amtSqPd3uu4Qku3nc7BG67MtGqIucfuczQRggQtlvuD_o0u3-ezSlAV_xYwfTlkGbflQMwn2ktx9WbioxfWQGxdxnunXvP8eCtWJUaAOl32z5rS93Rk8M_yJv1k8UH6YqO7uOBvEWDcd7_8qb5hbxprNmhPagyltZIGhcASdXy6wisQjq29fRmk0l1RnTjPV7yoESr2QcWrfjevFlfWQ9P_k_6Lcdc8qudpaqKD5AZ7T1G-AA6_3D7X5YzdJ2eUwhbGSkzlET3lir1g4gYfDUsp-L1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۳.۸۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/142800" target="_blank">📅 13:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSS1omGigjYkGtP_Xsd9awUQPyVYsaftbjtnUfzzR51JOXDJZkkT0k17a_768wI50XMXwyvFx_A4UCKwBPGF8CVFC39OXRz-2Gpk8J-eWqn1khwtgs4BzOG9stT6LM34d3DZx8Jg_xFhbJfHcpvVilmKIOkkRZGScoc7jS2TigzpSbuhf6_DGc1zth2gEHAgC8OaUau2FSChYz-Z-z3I6QWGNkOrIXWc950r_fozY2o-JtAW_Dz2bS2oxyZU_SGTZh82xSbZevAaZkoerIvkAXnTDAh6DpD5yDj3WZa5U9eHj9dFcyTo6oUYjz5BdjaM0UTLDxGIxHZjK3Tq6YqQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروتمندترین مرد آسیا به حبس ابد محکوم شد
‏
🔴
بنیان‌گذار گروه «اورگرند» چین که زمانی ثروتمندترین مرد آسیا بود، روز پنجشنبه از سوی دادگاهی در چین به حبس ابد محکوم شد؛ پنج سال پس از آنکه فروپاشی این شرکت، اقتصاد و بازارهای مالی چین را تحت تاثیر قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/142799" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سازمان بهینه‌سازی: مسئله بنزین بحرانی شده و نیازمند یک راه‌حل فوری است
🔴
دست‌کم به حدود ۱۵ میلیون لیتر واردات روزانه بنزین نیاز داریم، اما تأمین مالی و دسترسی ارزی در مسیرهای جنوبی، محدودیت‌ ایجاد کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/142798" target="_blank">📅 13:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142797">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdTmS3F7DlIQCb5wNDiq2QvX1aHGS4Vp11Uh3yE3JyGMtJauxyb1eRNWvKMQdajlQZXNPdxUDOpanMVsdm5cg-2zBc0gVRKC5ZFA8MBUen-WJXPHBfmMQqKh7wdZjVDzvLri7zQy55BKAvUVGbgD55L9E96j7R7ApgZB4JATzrsRonv0dhX-9N8WXjEr4wtyclDq1XnlcUIY8dIr0p9X-kQsJHY3vuPlrBh5fZMQ1X7yeeT6n17MlIdstkT9BzVETQxKC6f9R-MGDa4HmV_ZjsQ0QH1a3o7ZL1JtWLGZvg8DC_WJ8MRuHhPz-AIkPYRgGf5AhrhpsUqyoepY1hm4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش لورا روزن، خبرنگار ارشد المانیتور به وعده اعمال تحریم های شدیدتر علیه ایران توسط ترامپ
🔴
ما کاری انجام می‌دهیم تا مجبور نشویم دوباره به تشدید نظامی روی بیاوریم (عمدتاً به این خاطر که موشک‌های رهگیرمان تمام شده، و شاید هم تشدید نظامی جواب نمی دهد)
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/142797" target="_blank">📅 13:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سازمان سنجش: میزان تاثیر معدل در کنکور امسال، ۶۰ درصد است
🔴
۴۳ درصد به پایه دوازدهم و ۱۷ درصد به یازدهم اختصاص دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/142796" target="_blank">📅 12:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142795">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قیمت هر بشکه نفت خام برنت از ۹۳ دلار گذشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/142795" target="_blank">📅 12:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
منابع خارجی مدعی شده اند که ترامپ به مذاکره‌کنندگان گفته که چشم‌انداز توافق با ایران ضعیف است و ممکن است در صورت شکست فشار اقتصادی، حملات گسترده‌ای علیه ایران دستور دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/142794" target="_blank">📅 12:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKHlRWcaljk6_nxsH6c5iwnzihmRgWeN1Pf2XLPh8kElUVBH139aZ1v9cx2c-TyjGVkzc4AEIh-NNAssoARyQE9crsaz7u7cBk1MerZhhODwaJHYcXvpf3XCFaIR3ar8ASqxz5FeEBdrN-NmbFQ96UJKV4FxGdAlJ52aEQrWxBuQmPGLlSs5nwsk0RkPZ3k5qNlxp85pXS1SRCaPUWaNtOuyatT8698dHw29kEwpFAo1KtVTKsNNgt8igDmza7cwT54HUqtVQrj0jx8c0tnIrja3zUc-1LtBrEgEj5y-zirVjpBAo4Bcw2Lm5_OqEJ76RlWCIcY_9L4S2Tuhj4YKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین پس از ۸۰ روز به ۷۱,۵۰۰ دلار رسید
🔴
بیت‌کوین برای نخستین‌بار در ۸۰ روز گذشته از مرز ۷۱,۵۰۰ دلار عبور کرد. قیمت این رمزارز طی ۲۴ ساعت اخیر ۱۱.۵ درصد رشد داشته است.
🔴
ارزش بازار بیت‌کوین نیز با جهش اخیر ۱۴۷ میلیارد دلار افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142793" target="_blank">📅 12:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کره شمالی 10 موشک بالستیک را به سمت دریای ژاپن شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142792" target="_blank">📅 12:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فواد ایزدی تحلیلگر صدا سیما : اگر ۲۰درصد نفت دنیا را حذف کنیم؛ اقتصاد آمریکا فرومی‌پاشد!
🔴
با این کار نفت ۲۰۰ دلار خواهد شد؛ باید تصمیم بگیریم که تاسیسات نفتی منطقه را طوری موشک باران کنیم که دو سه سال برای بازسازی زمان بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142791" target="_blank">📅 12:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=XZp5bbO26L78F1A7aHN8n3FTZT5NeoFTSAgxf7z6yWStA7AoNpQwenqj4tn3xOF1sZJuSqMjjjeOgBtZAOZzZEKWnC5eY-U-DLXxJaLssEks3AqiKYfpC8aZYL3PKqkiQAVuQG-mXKHWJACW7czcxlDAMHpD4Wspa8K8iuc-xTGxJYyEKBaSgwj4ZgIDGDx90WwhuEbOq4qzbj--q4gsC5n0bXa9uzEzbIzhdSn4S5339eHUptr536qgv95F_Vx-4O8biXRQFRmSDDWA_2E4AOcjcikd4Hy8PFvjQvY0boewJP_UEhTWBQdxbzkUYyG2y1z7Yd2Yx81w3qoeFBcngg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=XZp5bbO26L78F1A7aHN8n3FTZT5NeoFTSAgxf7z6yWStA7AoNpQwenqj4tn3xOF1sZJuSqMjjjeOgBtZAOZzZEKWnC5eY-U-DLXxJaLssEks3AqiKYfpC8aZYL3PKqkiQAVuQG-mXKHWJACW7czcxlDAMHpD4Wspa8K8iuc-xTGxJYyEKBaSgwj4ZgIDGDx90WwhuEbOq4qzbj--q4gsC5n0bXa9uzEzbIzhdSn4S5339eHUptr536qgv95F_Vx-4O8biXRQFRmSDDWA_2E4AOcjcikd4Hy8PFvjQvY0boewJP_UEhTWBQdxbzkUYyG2y1z7Yd2Yx81w3qoeFBcngg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: آقای شهید یک پله از امام علی پایین‌تر بود و معجزه هم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142790" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⁉️
بیت کوین تا کجا بالا میره
⁉️
🔴
بخرم یا نخرم؟
این پسره پیش بینی‌هاش ترکونده
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142789" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raci1KbBF4Bal2xqisjUwDaSSsTJwjIzCP7uNVW21ACVch6_65jEeuPr7B6qOqmYSR6zqP8Y7Mcg_7ekQMpPT5TJDxrhnV5bvEzBvgFdtlEv-GgodtcFMLNqQR2UtyueOYf-DPpsVq4RdVY4CdtYm9IH9sDP1qc_E_aAHXBsBExLVPH8LjOua_9RTjXFXCiBmDFVegFUp66JAemXC-DgJ4Ng59r6E_zZaVdMDQY-EM5oXn39dwevExxCG5iKdwuJK4Z_3fTI7oxL9OxFzOAZzGAgXWnvPjMNmeoFE7OjWsw_MnvqUcKJDv3lDMkf42cm_-QYBlyLyZ-JABCWGPiYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر متفاوت ایسنا از  آزمون سراسری در دانشگاه امام صادق
🔴
این دانشگاه محل تولید تندروهای ۶سیلندر و بیسواد و عربده کش هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142788" target="_blank">📅 12:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37020c0eb4.mp4?token=G2jIsEWClqgCrmjjqXR6CI-AaCcCrkwoKQEannlmv2wEgGSytxkf3XJqOdwikJzCkJwMyfWqDKu5orHQeBY6ahi1NgOnJuSjvFjamxKv7xNjejLr12BNQYGUFD2tJkMB98ZARV-rE28QtBjmkez7eD7v1g3HD0Kuy76nZwuBrncTQPF-y7BABZq8cudFIW6kc4le5uuMweElPMLT-Yvo4gREAcQxX0LT3MW41nBYjPaAKCERfmH3fr9IGfQPggalDjPl8H0gg5FSwIdNwFcFzIxcVugcnAdNvkJpcYs4JX1OzufOUvtD1qevESVQHJC3XodMOajLdD7tkyahhva61w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37020c0eb4.mp4?token=G2jIsEWClqgCrmjjqXR6CI-AaCcCrkwoKQEannlmv2wEgGSytxkf3XJqOdwikJzCkJwMyfWqDKu5orHQeBY6ahi1NgOnJuSjvFjamxKv7xNjejLr12BNQYGUFD2tJkMB98ZARV-rE28QtBjmkez7eD7v1g3HD0Kuy76nZwuBrncTQPF-y7BABZq8cudFIW6kc4le5uuMweElPMLT-Yvo4gREAcQxX0LT3MW41nBYjPaAKCERfmH3fr9IGfQPggalDjPl8H0gg5FSwIdNwFcFzIxcVugcnAdNvkJpcYs4JX1OzufOUvtD1qevESVQHJC3XodMOajLdD7tkyahhva61w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحید خضاب مجری صدا سیما: تفاله های پهلوی دست روی شما گذاشتن اقای خاتمی !
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142787" target="_blank">📅 12:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی در مجلس : بهترین واکنش به تشدید جنگ اقتصادی ترامپ، خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/alonews/142786" target="_blank">📅 11:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f0c39a2d.mp4?token=bSWRItbQNEeOAKuLzsHIukUX8BscOPWHT37_P9C7V_eupQ6AEGyAgMZ4t_hdZ9ZWFFcOoFpy2k-g7asTAdBZpmoIro6QVHN6fyYXgS7hn-HSEKT3DKP1-DBoNUh9uG0scojOfLXKNOGBMrtp_fV7GHCo_ojn3I1PFguYmU69h0J075kQ4zP_gFVCzE-5TIYCJBJ9ZFTcObng1trc-wmS2lsVftVjw5aOy9dKseJRBV-CfhzDGg4AcutSJ3mcO1RUCVPk28VktF0A2PrJ2bJkjj9S4kizKSJQ97Scq97BjRC9-Lw0wV4XlOhwI0_5DgcpPl-Q1Q2JYmxJu8mLgkddpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f0c39a2d.mp4?token=bSWRItbQNEeOAKuLzsHIukUX8BscOPWHT37_P9C7V_eupQ6AEGyAgMZ4t_hdZ9ZWFFcOoFpy2k-g7asTAdBZpmoIro6QVHN6fyYXgS7hn-HSEKT3DKP1-DBoNUh9uG0scojOfLXKNOGBMrtp_fV7GHCo_ojn3I1PFguYmU69h0J075kQ4zP_gFVCzE-5TIYCJBJ9ZFTcObng1trc-wmS2lsVftVjw5aOy9dKseJRBV-CfhzDGg4AcutSJ3mcO1RUCVPk28VktF0A2PrJ2bJkjj9S4kizKSJQ97Scq97BjRC9-Lw0wV4XlOhwI0_5DgcpPl-Q1Q2JYmxJu8mLgkddpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات مسلسل اسرائیل به سمت شهر تلوسه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142785" target="_blank">📅 11:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSGsk7StFB8_td5LwnsspJxubgLw_grlG25weQUxdaqB__Ce_WIu-cylDX0JngTwa-RZNqXltHNPbUxy2ed3xVyz0x_kYjXXkJr39ag1xz5riFtFH79BNZOSEM4BTbJ12y7WOR9g0Sl5QCb6Ke2k0JR5DEgyX6FQkipyhWhQ_kxy587ZjmH2CJOplKvrcWGBkF8K9cWIHW4nXk_t1XZemhIlgWV-_NKcYfWu19IiISP1k7CrwEhXrQSD1evc51zb01IKuqS1d4cFG7O8Sfz5ZM1YZ3ACHj5HtE9Wu9MpBJl0eqGZDJnTh6zUIwwAtF3GfpVJZj-NInmUtsX20yeJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین بروزرسانی قیمت طلاوسکه
هرگرم طلا ۱۸عیار، ۲۰میلیون تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142784" target="_blank">📅 11:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه:  ترامپ دستور داده است مذاکرات با ایران برای چند هفته متوقف شود و احتمال تمدید این توقف نیز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142783" target="_blank">📅 11:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJiYuibqItqgf95f09AB0rNshUUqN4E_s2W36fZOZyBYfwmCri-FBPBQXUQdoroQOUBeYstFQxsxti1Wk9HdwJmi-Kc12mUza9EaNoXPW8FBb8EIXYOqnNV7AfqL7nclPJxeKIkpJZ3DUoub7pHt_uN9QvrHyGJRUtGLkgbaCz7rClOxlKKt9yXBSoSZg6i5b0SztPEiL_xNET-H3YcV4M0Mc16MPc4KFnKYHhwBcrLDDodLwtY_3lcG98ZCgkv3x-xohFqkVdLhs-sSC27w9-5Du904M0ILYNWX6ZLaFs78M7ieZgtpwvBB1pDuM1wVH_PiBVlC-ICeQFYtRpi2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر نفت چین از اوایل ماه می ۵۴ میلیون بشکه کاهش پیدا کرده و به ۱.۲ میلیارد بشکه رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142782" target="_blank">📅 11:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_LTXuD36seQlxwVDTBNg8VuIMvd3qvwJzXVqdn1_G2AIEWLNkhK5cgNe2QuKk-8WeZD6DY60Me5ivQaZzaJKmBDEfNPK14ApWs0SYQxq_aeXbBZIdVyQA010rCa9pGXP0-j03riTmgLyut1rN4wEpcdvHpqqDVvBZgCSr7lOeA6ZOOle0eY9G6h998ysWe5lj7TdW1wTYjGprMTWSxOF-ZW7BucjoTomjxNPCv4iKtC1NrhAIMzB804oe_Mw-jYuXl3MaDgdzjVshLscC07L-oXSXcv7TAstfS5gN8u6sv5yupXUq3IV2HrnVjrvkefhC67Xwo_nvhwwYsdkYR4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد اقتصادی عربستان در فصل دوم سال جاری منفی ۴.۸ درصد بوده که ضعیف‌ترین رشد از دوره کروناست
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142781" target="_blank">📅 11:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAWYtjYCadoIU4fYRONtKr7sIXM26uGK8C7Xej3ummALMvwiRiZUBR8-dd4e6ffJx54TYcpLJZkwNkAWLNlHZgxq3L6QPtAyGqqfu0nWv0M1ECJo9kYo-EFTa1q4veofQpPSUH7lMJBXE90xaM0AMGqRPl6sVJRlBiwmuy2L2tnQOn8LczpuQ2HuktsXTc-G1UBUX2tGv3ihNPrjPz0TpdABY1ixin3xwwlVeyn5OXBfHDiZ5R9lDRURojZgnFawnFuDDenm7QcvWar5e6rMm1EEs2gfl4bDENFthVzOKrUetKdweyJMOdIjgjIye-OrkFR_q1e1pK64vpEFgfvGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی، معاون وزیرخارجه: آمریکا اسم شکست بعدیش رو «جنگ اقتصادی» گذاشته‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142780" target="_blank">📅 11:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8LOTGsW3L4oCMeCcCaBZVZhc0PzwYPfGxag_Ie4hhO7HJgE9jH28TWQM-VRrmMv517Pbc6EQAIhRDHlTyOIaIID7gOXu-mJ6pCaGoSrsANAJTPUC6k4BNSVpi_xPHtoMnrJ8By0iKfYt5cZ_P1XQjt5p5ZokMh0A_U7-JEvExm0zSG1P01rv75a094-jrn4HNlTcyacp8JMCjx9Brmak7jSuSrr7dW2-ADFiqGtOwlSQxdUwdNWNsjejl7akiwccCRwXLoCIaJ_QVIDhkAUG1_Jjmcs42qq4JM2a-isP-ilqgRwSvJqfKJrkA1S08eUi8i2mdUOsIz8oQBb350VqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت به حدود ۹۳ دلار برای هر بشکه نزدیک شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142779" target="_blank">📅 11:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl0OTV1FzOpchQ6sVI7VhVrrN0uBGHNhDet2f8C-r_zRjnjZax8m6m2ziEc_BGLaVhx3SAwgv6wRJF_eC6E6B8l35vpwSw1oIdgjiHdFQj-KY4yCPLn4vUdOwJhQ-rBiUao7OobPVUasJA8NV38ZxwR8u6ZvAjD7wW8z6lQKJx1q6_UNfrX2m-6cJF5h3QMjIiHJcYkpV2-RPsfXXF9E1qx8u_eYEUlx-XSMmznj4TWxq88VmuHccVoEi-oMFO8imE2duOZsRZeq46E4sb7FECWQDCNIqNsA1Lz4i5W7dz_UlnA4odH_rtQqo2ezeMQCAr1Q15u8IqWJxIop7aUQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماری جوانا به محبوب‌ترین عادت روزانه آمریکایی‌ها تبدیل شده است
🔴
مصرف مشروبات الکلی نیز کاهش چشمگیری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142778" target="_blank">📅 11:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سخنگوی سپاه: با وقوع جنگ جدید، تسلیحات مخرب‌تری به کار می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142777" target="_blank">📅 11:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVXZMjv7fzYF7DuxCzUDKugHxI8YovZ0UnwuLaQ9DdItxe3x3-hxhOqwu3kHhQsn0Abdhe_uy3tsgSjdoCYdIn5fIeUQvn51PKdjmLS6T-njOmwhEoNachCedmiA-HAkHQuVKOpgjbd3Y093bzd_GAeyBt7gxusC0nie0DPonzhZkPpRYK2fbXz3OJ4tjMvOlW9wbhU_u_R3tRCoqAfmARR_GFL7xtPtFxBmGRbySdmPZzVosmddB7pW74CFOG-D-u_IUofnp9JeX2yoDqW0Zyr0IFGPDrL_H4-vWoTppHrm2ey-6qhw234Z7Gmx6WTIjQGphbwcvD0bH301qACj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کره جنوبی تخمین می‌زند که کره شمالی بین ۸۰ تا ۱۲۰ سر جنگی هسته‌ای دارد، که بسیار بالاتر از عدد ۵۷ اعلام‌شده توسط ترامپ است.
🔴
سئول می‌گوید این تخمین از پژوهش‌های خصوصی به دست آمده و به‌طور رسمی توسط ارتش آن کشور تأیید نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142776" target="_blank">📅 11:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUyzDCDBEtq9sigg_ojQqTrPy7bMhOv20z2SM2ZztZfu31zD_ViisqVCusx1KwZIbSKZ1AisJmuy0Sz9YUMDguVk0eIGeXZWIDAs51BGcNpyOfxcnapwCittTF7SogE87xtC_ehbfl8jbO0L6LbiUW9DMzhsB-BUjvOaoZs0nZK9gNQjy8UyPXJkZBpe0cuhnCJLYUvh8MQdye47-IO7ArJ6uC1kyv76tkBxN5ywEsCzw6vOX48YnR-Bsp_SGy6tg6RbhUppq_p65Smg9eUOIlCtI46W5j9kV0iHFdkreKGiQlxk0JtwpyNcC7HuiF6fYIk4G2rKh-x0-447JMmASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه یک تانکر گاز متعلق به امارات را از عبور از تنگه هرمز منع کرد و مجبور به بازگشت به مبدأ خود نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142775" target="_blank">📅 11:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزیر علوم: آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142774" target="_blank">📅 11:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142772">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb38b789a.mp4?token=LCUOtBx8Ed8rHBa9n0RTndReLZQDbB4EuaVtgHBiC5akJVjhFEookdzyKEAgSvLoDWhB2BLmHfkEK7T_yxutROL-3A78qGU6a-dq_NjjXEAtK2OtVtdsxoOQ9pnFztuVDh1sSulrI55MHUXnW7RuV7aLj9ueq8DDmjfgysRFjvtRblf957KFNaeWG-GHYBB0tQXrlmKrUjrfqxCaZCl55rzRhRT1axxt0tDbGD1GnOy8HyfTJGvtHrb6USRDZI_XFSeSEw4cwKwXPKG2nzFEqLsgyiIn-DfkYRHlz4vf7nbH45CjVTi9K57Jlmnkx9SPfLi1WeKX5_HqZi44zcZHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb38b789a.mp4?token=LCUOtBx8Ed8rHBa9n0RTndReLZQDbB4EuaVtgHBiC5akJVjhFEookdzyKEAgSvLoDWhB2BLmHfkEK7T_yxutROL-3A78qGU6a-dq_NjjXEAtK2OtVtdsxoOQ9pnFztuVDh1sSulrI55MHUXnW7RuV7aLj9ueq8DDmjfgysRFjvtRblf957KFNaeWG-GHYBB0tQXrlmKrUjrfqxCaZCl55rzRhRT1axxt0tDbGD1GnOy8HyfTJGvtHrb6USRDZI_XFSeSEw4cwKwXPKG2nzFEqLsgyiIn-DfkYRHlz4vf7nbH45CjVTi9K57Jlmnkx9SPfLi1WeKX5_HqZi44zcZHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانش زمین عظیمی در معدن طلای زامبوی در مرز کامرون و جمهوری آفریقای مرکزی منجر به کشته شدن ۱۰۷ نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/142772" target="_blank">📅 10:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4BHHgFfWnCM-ncDTA4wWR6nUx57uKF7v0YoMbreTPlZT7H5i3A3jwPkchWxoRNvLQvAIjG0GYIf0SXVw9qg1sLiDG3F57j_4NLKbkXG-mTryoAHIfhsTTtm5rwYxd2qruBX_7ouDugeHI8tKfyZt-8IRVADuloWa_lUb0uHyJMYNzTwW_I3tFvgM2aKCa1mLo6ueKWiVvhumepQoH1Ny6UnmvZUq0JXhvITfMRUZ5S5SRlFELcGgVLsyCPMRiGkxXBQwieh_fgI9vSFJYno5lmHzZ0Zi6_-2MqMZItcgb7I9H6_RK8goa_EzX9yemtKl9rMmLJfjve8sIL7lKgzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره گزارش داده تهدید ترامپ به اجرای یک «عملیات اقتصادی خردکننده» علیه ایران، ممکن است روابط آمریکا با برخی شرکای مهم تهران، به‌ویژه چین، عراق و ترکیه را با تنش تازه‌ای روبه‌رو کند.
🔴
نادر حبیبی، استاد دانشگاه برندایس، گفته چین مهم‌ترین هدف احتمالی تحریم‌های ثانویه خواهد بود و پس از آن عراق و ترکیه قرار می‌گیرند.
🔴
به گفته او، اجرای کامل این فشارها آسان نیست؛ چین با تبعیت از تحریم‌های آمریکا مخالفت کرده و محدودکردن تجارت زمینی ایران با عراق و ترکیه نیز با موانع جدی روبه‌روست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142771" target="_blank">📅 10:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
عارف، معاون پزشکیان: گران شدن بنزین تا محدوده ۸۰هزار تومن قطعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142770" target="_blank">📅 10:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhmS-32MQu-jhNTtudUcpqK-mM9xJUOMdsyb8z-3mnsmafqrKjh1d9rlyHn30PDsF_DsyRVdiuvKnTJYvCX8E1pFIlZCQH-zrkch9txc9sPFh5YSpgKWcqitVtqJVzaewW_8yiaYSnDj64oG9EnB5qpnHi6NwYUNRAtA3KSauyxhgGUHpOdfg5nzIm-_HWn80dohkZemf4_Jq_2hZxmEEZLWCYhNuSPtl5WY8ieVdfKd49VpF7Wt4e1A1dUvsIa2A2LpLSao9vix5o5MoAW_a0yUxreSnPAhmh4Jt3PIa9GOEgOdsugB_4fdCKpwiqKZm-83wvvvyaposnhrpcrH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBdgC2rcy_6ePgk_EXEx0rPhmOpIHYY8dawktZzIU9PFya3fW33Cupvur3I1nTfCXKefg47JCFLuvUktpkU8gJiAXPdjMUV8cshuzTIXcAfeAW7OAiLy18FvIX0b1aeeT71qkIfDw2YpLCgzSdDGV6lNXtorLC4gl5kIFj0KIwz4lfwkrYFVJJfzGNmcaNZ3AM66B8hIhOLIHkiPxW3BHrjPp-JhMB91ILWJOa6clEBDDeGDTgXM0bM_4ps3GaZ1y2ZAbVG1gywfpnh64ovotKqsHipjtz_4ZBjzK-az5KuRmp3rD2cZLY0fP5bF_I1odCufFqiY8OfSXbYLNlbQxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک تانکر نفتی هندی تلاش کرد از تنگه هرمز عبور کند، اما به دستور سپاه ، مجبور به بازگشت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142768" target="_blank">📅 10:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
قالیباف در دومین روز سفر هیأت پارلمانی ایران به عراق با قاسم حسن العبودی، مشاور امنیت ملی عراق، دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142767" target="_blank">📅 10:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn67MNh-IiU3OlGz0w-4ehcDsBw0ZZZ66JNKE462aK3NIsL9zUNABAF5xLdvLbWtl0Rc7Q3aawv3ycN6XNGhKx9Qh-QiAjU1vc8mUReWqCnp3BD_ciUAep7NMYabgRnF8Gn2aQfWlNokPhnejhko9DGQ78NSExoeP1TpGpa3oXKwlQDHXrcmlIZMnX1bwf_0AwjMC1WNO9kdQyoKYofTPbZkwPqeBrXoZW--yi57Yt9dxWHIVovT1VCXY_meAIb_IepDoknS2FVjg4i1y4Df5GqihmAtKiax8S__yMeB35nj_ZeJVx9v48jwdZ1ussLpYLoBfNSNikJTfYJHzS1BXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل به نقل از یک مقام امنیتی: اسرائیل از آمریکا چراغ سبز برای اجرای عملیات‌های ترور در غزه را دریافت کرده است. همچنین تأکید شد که ارتش از «خط زرد» عقب‌نشینی نخواهد کرد و تا زمانی که حماس خلع سلاح نشود، روند بازسازی نوار غزه آغاز نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142766" target="_blank">📅 10:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDlVTCnhHH2kPh4UduWYv_m9jmNIawj4EyOt6s8d0zftbwmRPEhMBGyNPhIbmBrspzTCv86LEM-vHwZSfwEpLFiCCbf10Z60V-TJz8S3w5Mosfq-tQaskmFN7OZXC_npeCaWvUgoQtSbbEdOpm-XeER9EJhr1U0SWiuvXlgJXLuUYwGvp9MURubHxUPA9XkdTrG4z9SAN1qrgG9mpyqSTtz1LutdnPjxeZ3ffWBUMJhTh5YKkdbFdcMy4yFrqAps6xdzwVnJB0PJmR8-2bef-37YZQEPBAkhF05h0D5wucZoMWqXwqEI1ul2QAkeP6X0gciVDrwJLBFPGSAVc7n9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین یک جزیره دست ساز برای بزرگترین پایگاه نظامی خود ایجاد کرده است
🔴
چین ساخت یک جزیره عظیم دست ساز در آنتلوپ ریف را تکمیل کرده است که به عنوان پایه ای برای بزرگترین پایگاه نظامی پکن در دریای چین جنوبی عمل می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142765" target="_blank">📅 09:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry4J1hz-iNGGL_b0sthVQeGCvRNUPVIq84tQWf6mQRAlC4VP3sOFi9k0cWnX9y8n5BrErtx5LHwP-tq1ZajHKdR0dSdhksF__n5oZyQ4DI3CjSg8CICzv3ROtIrHfGdvWpUK7VbcUC9sKramJZQSyZQ_XWAnbvqEo-xWg7V2vKb4WoGIICaUtgq9J7eR8joyyENQ5QeWMeKxW0LaLW6Gjkq9uvklQA0DJEC35jks7ktJiGVr3kmuSGhyWy54lvroVPQ9lxDzB1HQeOwg_4GFmWYXHS0oBvowYhNsx2aPWNK8iMxzeFYEA9-DfMdVz-F8Ny7ys48IgEn2_347PmhR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل به حومه حولا در جنوب لبنان هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142764" target="_blank">📅 09:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP32lYjcHiOJvXEKJwx-HILbyWFVODXidhSXO81POt2Q9o3CRqVKMh_ztcs54tTvGsaa-S2otfeC__sFnN_QOJ5-GJT-HavI24Cion0HxYz4Gqa2nRhm18lF353NYfhGAcnxUIGL05Tv0aYYWy_UYHL0ccW4o1iVgKUJaEnUzf46qu2MAFBX50OsGjRdumBfbOcQZHeDKbfPY-OqxAkXmCAovwelWzzmEHeAgBdBMX7IGUfkVM5wqvRMsUPhzmDrxfzJXWbDBwv14MS0muOs6n5W0FiRA0EcTEHIzMGaviVF01BxpatiMiTqKKJNTwDVnkerg10bgS29g1g-X1KAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=uUVeuubkL7HUgUfrFEU3pGruKWT8HSxRaKSkUwnYRbBc3NHuv-AZ8szNC9PofUSWMprfBMjCkXb48w1JIld_ucZJCUyKrPK4FcnLBBnHbuBMB2x09cVX-3Xnb03OLQFkMln4eoPVxHXkh6P1syQwZQQ4UnGCa--tGiddpTEkXH4y1s71B7-D-NV5g-8k7fMdcNVSXJYBMU3CfjVYO3FUu2IEvjUTX1ssA-WpLM06q9O5hUcNLbZ3W1-b8Q6qk9Zu3yatwZOIPwzEOIkSufXj4-L-to9KUk-bsYcrnEO1ubS1TlbXeTBt7GS2CDmNnkFhuOcYawXYd64Mh9C6PSZCPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=uUVeuubkL7HUgUfrFEU3pGruKWT8HSxRaKSkUwnYRbBc3NHuv-AZ8szNC9PofUSWMprfBMjCkXb48w1JIld_ucZJCUyKrPK4FcnLBBnHbuBMB2x09cVX-3Xnb03OLQFkMln4eoPVxHXkh6P1syQwZQQ4UnGCa--tGiddpTEkXH4y1s71B7-D-NV5g-8k7fMdcNVSXJYBMU3CfjVYO3FUu2IEvjUTX1ssA-WpLM06q9O5hUcNLbZ3W1-b8Q6qk9Zu3yatwZOIPwzEOIkSufXj4-L-to9KUk-bsYcrnEO1ubS1TlbXeTBt7GS2CDmNnkFhuOcYawXYd64Mh9C6PSZCPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله موشکی شبانه روسیه به کیف منجر به کشته شدن ۶ نفر و زخمی شدن ۳۳ نفر دیگر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142760" target="_blank">📅 09:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq4EB9S9lpeFdyIr4QvpdAT9EhcY2sctl-2RRIA-gRThhkyShB3XQ_rGlCitxiktqhVOwrfbTyfwL8HwSSGMbEIjvn0avi_4bcuseL5MXaSX1nAmTDqKVLJ6ws5hGmlUTvHmIO7PSFyiM8-mSIKfV9QgBmS7uu8hnYJ0llFZwrNcfE0ESv7C1iE7nMtbpV1iqrmp81D16Zy1F5unOXxvkTywP6tJu2azBl1oFU42yIdpptzkL7berVPSCCMoTUBSxQi3KJtuK0PfcGCyW8nkNvhoj-q5WYg3SApGkypf90ZbtlSKX3sUPo4h8hmGgBzExV4fMkJ7ErKFyOoLsC_iZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: تهدید به «شروع عملیات اقتصادی» علیه ایران، در واقع برای انحراف افکار عمومی آمریکا از بحران‌های مالی داخلی است: یعنی بدهی‌های بی‌سابقه و افزایش سرسام‌آور بهره‌های بانکی در آمریکا.
🔴
اصرار بر ادامه سیاست‌های شکست‌خورده، تنها شکست‌های بیشتری به بار خواهد آورد و دشمنی ایرانیان را در پی خواهد داشت. تروریسم اقتصادی آمریکا، اقتصاد جهانی و حاکمیت ملی کشورها در سراسر جهان را تهدید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142759" target="_blank">📅 09:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPajVaDjPnIlMPQ72GvVfxMwc4pvorzTIaTCVUdqPPnI4fQG2oGZ8sTL99A9Vns92jfPXLn8op9qkkue4nUklYUJqw3_dzqlIXOYw9PDXDOqDAQLIG_d9ZzKewZKWC3rvhiz-jvWc1lpEb-YRQZGjZKkhXONP2OT3hI0l44svOYnyIjE7f84RxasY4L3ZfJ4OA3tLbkyDJ0s13p9tJjkXKdxvtiuy6ETfIoDqMknuZibfkyoKUUknofUtEupJWpgutrXS6zRaI8B6f7dFu9h8qyHSBOhruKx0xazWxjs2DX-zFmwxkudi4tyllXzosFMwQlvjlnVKt_MQA9O1cGnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتز، وزیر دفاع اسرائیل: اردوغان ترکیه را به ماجراجویی‌های غیرضروری در سوریه می‌کشاند.
🔴
اردوغان نباید عزم اسرائیل برای دفاع از خود را بیازماید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142758" target="_blank">📅 09:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پروازهای «العراقیه» به ایران از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142757" target="_blank">📅 09:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رئیس سازمان سنجش آموزش کشور:
پیرترین داوطلب این آزمون ۸۵ ساله و از استان کرمانشاه است و جوان‌ترین داوطلبان، یک دختر و یک پسر متولد سال ۱۳۹۳ و ۱۲ ساله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142756" target="_blank">📅 09:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
به آسیب‌دیدگان جنگ سهمیه‌ کنکور اختصاص می‌یابد!!
🔴
وزیر علوم: برای افرادی که در جریان جنگ منازلشان تخریب شده یا آواره شده‌اند، تمهیداتی برای اختصاص سهمیه در آزمون سراسری پیش‌بینی شده است که پس از تصویب، امکان اعمال آن برای مشمولان فراهم خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142755" target="_blank">📅 09:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
پنتاگون: تعداد نظامیان آمریکایی زخمی شده از آغاز جنگ با ایران، به ۷۵۷ نفر رسید و ۵۰ تن به رقم قبلی اضافه شد
🔴
۱۸ نظامی آمریکایی هم از زمان شروع درگیری‌ها، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142754" target="_blank">📅 09:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142753">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqbgPEfCzTqago-pojQ5OiA9OPAUsmpmSP7SjetK-DlMj-lHQ08IwHlTqqSLq_m1-NQY6oMLJcBGErdQyfMyl4sZZFE7ODbe0kwP8MFkE43kBf9I_zIECMBRmn43bGk7ufJBZhk3vOzXEwhXsnplXEMfVdvnoitjS-1cnIk7km9jAV9cDGR9MANuqZCgjOEvRIlFas1WXHmU3J2fmMACLPN8xc5Z9lWVRf9LLPqr9QgOcOeT_DtK98MGDbiN05eggujhIBLuzl9-CGyXc-lEKONGVLWCi9IvG8pfB7uwb2ed6XEsVf0RqVu5fBvjo-YiAmK20fw44NMqw808FIyZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابولا در کنگو از کنترل خارج شده است
🔴
سازمان جهانی بهداشت: بر اساس آخرین گزارشی که دفتر منطقه ای WHO برای آفریقا منتشر کرد، تا ۱۶ آگوست (۲۵ مرداد)، جمهوری دموکراتیک کنگو ۵۰۲۱ مورد تایید شده در ۵۵ منطقه بهداشتی در شش استان را گزارش کرده است که میزان مرگ و میر آنها ۴۷.۴ درصد است.
🔴
تدروس آدهانوم گبریسوس، مدیر کل سازمان جهانی بهداشت، گفت: «شیوع این بیماری خارج از کنترل است» و نسبت به خطر بالای شیوع بیشتر در داخل کشور و در سطح جهان هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142753" target="_blank">📅 08:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142752">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قیمت نفت روز چهارشنبه افزایش یافت و در بالاترین سطح خود طی حدود چهار هفته گذشته بسته شد؛ این افزایش در شرایطی رخ داد که نگرانی سرمایه‌گذاران درباره احتمال تشدید تنش‌ها در خاورمیانه بیشتر شده است.
🔴
قراردادهای آتی نفت برنت ۶۰ سنت، معادل ۰.۷ درصد، افزایش یافت و در قیمت ۹۱.۶۲ دلار در هر بشکه تسویه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142752" target="_blank">📅 08:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142751">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
آزمون سراسری سال ۱۴۰۵ از صبح امروز پنجشنبه ۲۹ مردادماه با رقابت داوطلبان گروه آزمایشی علوم تجربی آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142751" target="_blank">📅 08:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142750">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj7_PHlUXjgA6-Lya7oZNCSbCq3qDheis6EjzPtJfPxsWKUeHKd7CklUbG3iMyT7HLLythPFcx4JYcPOO02wMtmUK9kjmO9slRa8ldhXBQoFKWIKGjV8X2NqJJY-5dh4eVeyLG5ciBIOF1MoB0bTp-IsLfIdRQFozLhjVwHEvObOFTddy00_DHXFHgJW-a7cz5o4eTSjipxlhUm4LAjIjygGwoHG0Apzr0mTTCoCfdowsar_ZVpYbtELP-71XDfQqt06VgfLAdSBMvJHKgTBCYyUkWGQ-t8WGqqRvo5TK3ruySksxJ2T059ScTa0p3X3xLegcWpzx15vpIHNHzIn7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
واکنش تانکر ترکرز به ادعای انتقال روزانه ۱۰ میلیون بشکه نفت از راه مخفی تنگه هرمز: شاید منظور مقامات آمریکایی انتقال ده میلیون بشکه در هر کاروان باشد، نه ده میلیون بشکه در روز. برآورد و اجماع فعالان صنعت بسیار پایین‌تر از این رقم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/142750" target="_blank">📅 08:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142749">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4669764466.mp4?token=BOwxcJMz9OqAiWJT85vAIdFFqxRcV3d6VFAaszyXQUdmTHmI4ijm-zQ1ydHC0t6JHgy1AA4F1Lc25e3TvyNdmMDONxeE7N3yER1GGIjxsZVFoHBartEvS6OXB8Lm7kTBYcWtdHPhbGRttp_1Raea369vn9FYHldFNUG5WLBiXrV1HBt9yhiAbmSKKP6NsTgLrap1d1zuct0NlEjKhFXdQFhKwj5VWOrr9hPFhBjdas-Cx-l1q-XTGhvQ_A22nG4wN3kJlmEcVKLpYhsx-bF5SGTMtBnzNRI_uTNRrTX6iG-4asMkrzRpDgcVEIWYnoUh9oG3A0w4rSMNPh8sTPHHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4669764466.mp4?token=BOwxcJMz9OqAiWJT85vAIdFFqxRcV3d6VFAaszyXQUdmTHmI4ijm-zQ1ydHC0t6JHgy1AA4F1Lc25e3TvyNdmMDONxeE7N3yER1GGIjxsZVFoHBartEvS6OXB8Lm7kTBYcWtdHPhbGRttp_1Raea369vn9FYHldFNUG5WLBiXrV1HBt9yhiAbmSKKP6NsTgLrap1d1zuct0NlEjKhFXdQFhKwj5VWOrr9hPFhBjdas-Cx-l1q-XTGhvQ_A22nG4wN3kJlmEcVKLpYhsx-bF5SGTMtBnzNRI_uTNRrTX6iG-4asMkrzRpDgcVEIWYnoUh9oG3A0w4rSMNPh8sTPHHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: جوابتون به صحبتای ترامپ درباره تنگه هرمز چیه؟
🔴
حداد عادل:باید بگیم تنگه، تنگه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/142749" target="_blank">📅 08:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142748">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رویترز: زمین‌لرزه‌ای به بزرگی ۵.۸ ریشتر بار دیگر منطقه فلورس در شرق اندونزی را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142748" target="_blank">📅 08:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=dS-_QA4ZR7bQeDw71cPS7ATyDPiRyyl0cMD0zrVz9-1xH0a2QENf35KQEg834RrbqqXcmX12OheBal2rRcP6bE_PfdrDhhsA9AjfZ90h0c_Bo45dB2a0O0-WePzK_IruPnyxLcisyPjYbofF50SCfUplLLLVkQBFI_DJJtt5DhVPsSCEdSLc5iI_lh2mZx2JMxJsPpTRAouKN7QhHEGZLxtpiPsm1Gma5Lr1KcUkQnX0uihnB5WHy0TlUWzGtCUMaeuGfVYGPpGefiqRZYN4fPrIgt_h8jv1ZaPA-_Q6EfoFL8mAFDr07cPm9_Zt3h3OtMfH2awe1-_BmCzS6aPRLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=dS-_QA4ZR7bQeDw71cPS7ATyDPiRyyl0cMD0zrVz9-1xH0a2QENf35KQEg834RrbqqXcmX12OheBal2rRcP6bE_PfdrDhhsA9AjfZ90h0c_Bo45dB2a0O0-WePzK_IruPnyxLcisyPjYbofF50SCfUplLLLVkQBFI_DJJtt5DhVPsSCEdSLc5iI_lh2mZx2JMxJsPpTRAouKN7QhHEGZLxtpiPsm1Gma5Lr1KcUkQnX0uihnB5WHy0TlUWzGtCUMaeuGfVYGPpGefiqRZYN4fPrIgt_h8jv1ZaPA-_Q6EfoFL8mAFDr07cPm9_Zt3h3OtMfH2awe1-_BmCzS6aPRLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک چینی بعد از پرتاب دوباره روی زمین نشست
🔴
چین با موفقیت مرحلۀ اول موشک قابل‌استفاده مجدد «ژوچو-۳» را پس از پرتاب روی زمین فرود آورد؛ دستاوردی که می‌تواند رقابت این کشور با فناوری موشک‌های قابل‌بازیابی و کاهش هزینه‌های پرتاب‌های فضایی را وارد مرحله تازه‌ای کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/142747" target="_blank">📅 08:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3ybU1-dTAtVYFpm0LD5dehYO7r5-04s8NHLdNo5PXYd3B6KxvZ21t5Fd1C9_aHTU4G1_wQfGjPQBneGdj0KHudYjhU15y6EhNbdiZHBMrbtx5U_T4sV5v0J6GvT3UDdyDw20QuLtbIyQ6Z9TfFcFBuhMFgI0UT_H3V99e487vsP8_oKCySwZKPUeMQ1GwrjUHUEeQH5AwqL6KY_5Q8UuoZLgJv1upuRNTeKZRZ9D13FKJ-L9AvM-LZC-c57r-8zH2azBfgZcZBePrsS29bhxHet5kVAYwfdAkW7iESwB8ZYNY4aoAGSxbJsa5XEo1AmCsrRhwe3yD0K7w5e2fcoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ترامپ:
‏هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند. بنابراین، امروز اعلام می‌کنم که کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد! این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
‏
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
‏امروز همچنین اعلام می‌کنم که هر کشوری که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با پیامدهای اقتصادی عظیمی روبه‌رو خواهد شد.
‏قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید همین حالا متوقف شوند. خودتان می‌دانید چه کسانی هستید.
‏این یک روز دیِ اقتصادی (ECONOMIC D-DAY) خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
‏این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
‏ایران هرگز سلاح هسته‌ای نخواهد داشت.
‏از توجه شما به این موضوع سپاسگزارم.
‏رئیس‌جمهور دونالد جی. ترامپ
‏realDonaldTrump
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/142746" target="_blank">📅 06:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
برای فردا انفجار شدید قیمت بیتکوین و اتریوم
اصلا نمیخوام جو بدم یا ته دل کسی رو خالی کنم
ولی این چنلوحتما داشته باشید بدونید واقعا چ‌خبره :
◀️
@agha_trade
قیمت طلا رو هم صعودی پیشینی کردن
😳
☝️</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/142745" target="_blank">📅 01:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142744">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32c922962.mp4?token=XLOU2-VCnGxkjvC0Sm-YdBGg9Ew7h5qj203MOZclo_rwIONZ2Nq2gdjV_pHebYUq0WomWcuS0F56qVaY3LzHcW6krFyQebaBLMaseNaUauumw53tLY04Gs2JaoYlnkwDx0C2pwPbf7g-4tF8mavhH5iltc19YXAR0fIAkw9CR4NjLdu6S3a1k93KqmRo0bTR7OmK9CekJsxrZM3ONx_mvmwSV6FCjKtMpnPdYPsw--uwv4IcH78JqHBraKCRFP-h2wBaYl13BLcVbAdE8P5lK6fVS-7uWyORuB9iRLKpfMw_dBKl4THr3pRh61MMzaI0iPNOfDlXhmkkp5Of-gbV-CLYsJJ0c1-rY6CfPt89Ou8vOxrte1cdyHPs66tUqWqBXNdhtAewGYl_PM8fesYz8B9LwYkZQ1_dkm2k4fnfJc6ppiO3GcHhBB-frFW8d4l4Q_-MyAC8WM74E5o-NWK15mnN6D_ov2sumQw06wwh_qY92gYy3UzLRwLqWnCL13_7GWJMLGvR7FiuGqFGOSNZQbGIm7QipZHuYyuTjB0J_HTwpBwxyMYs_SZRF7GslDOTd1dDIOz1kl1WOIZkkkJ5yQjpbaZLqt9JY8zZOhvm1fYsHwTUj9gIUNlVCLys6nzf9m2-MWqyD-bvnqtpNbfP-dBwpbSHJj964wIWEovs8qo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32c922962.mp4?token=XLOU2-VCnGxkjvC0Sm-YdBGg9Ew7h5qj203MOZclo_rwIONZ2Nq2gdjV_pHebYUq0WomWcuS0F56qVaY3LzHcW6krFyQebaBLMaseNaUauumw53tLY04Gs2JaoYlnkwDx0C2pwPbf7g-4tF8mavhH5iltc19YXAR0fIAkw9CR4NjLdu6S3a1k93KqmRo0bTR7OmK9CekJsxrZM3ONx_mvmwSV6FCjKtMpnPdYPsw--uwv4IcH78JqHBraKCRFP-h2wBaYl13BLcVbAdE8P5lK6fVS-7uWyORuB9iRLKpfMw_dBKl4THr3pRh61MMzaI0iPNOfDlXhmkkp5Of-gbV-CLYsJJ0c1-rY6CfPt89Ou8vOxrte1cdyHPs66tUqWqBXNdhtAewGYl_PM8fesYz8B9LwYkZQ1_dkm2k4fnfJc6ppiO3GcHhBB-frFW8d4l4Q_-MyAC8WM74E5o-NWK15mnN6D_ov2sumQw06wwh_qY92gYy3UzLRwLqWnCL13_7GWJMLGvR7FiuGqFGOSNZQbGIm7QipZHuYyuTjB0J_HTwpBwxyMYs_SZRF7GslDOTd1dDIOz1kl1WOIZkkkJ5yQjpbaZLqt9JY8zZOhvm1fYsHwTUj9gIUNlVCLys6nzf9m2-MWqyD-bvnqtpNbfP-dBwpbSHJj964wIWEovs8qo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاکی، درباره ایران:
ایرانی‌ها دو بار به‌شدت تنبیه شده‌اند. باید فکر می‌کردند که پس از این، ممکن است شروع به یادگیری کنند که رئیس‌جمهور ترامپ جدی است وقتی به اقدام نظامی فکر می‌کند و آن را تنها گزینه می‌داند.
او به آن‌ها ابراز داشته است که اگر حاضر به رها کردن جاه‌طلبی‌های خود در زمینه سلاح‌های هسته‌ای و غنی‌سازی اورانیوم نباشند و اگر حاضر به باز کردن تنگه هرمز نباشند، آنگاه درگیری نظامی بزرگ روی میز است.
آیا او این کار را خواهد کرد؟ من نمی‌توانم به این پاسخ دهم زیرا او تنها فردی است که انتخاب شده و تنها فردی است که مجاز به اتخاذ تصمیم و سپس اجرای آن است.
اما من به شهود او اعتماد دارم. او در این مسئله شهود خوبی داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/142744" target="_blank">📅 01:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=a6CG6apLDsUR9_sbLFtWxvPX7siXW4h1uhNTcc7bhTuBQmmaDX2Z4cskqrBec7Bj7nU0Zb84gnXlczlepOUClYIPwgsAGxc2YybEgRV6PvzjVDmJKFoXRJt8RPkZUFIA2EBH067awdWVQ-fCzHLkJgWeDdIANvqWsdJhx8EWfE6DRTpAUM_-YbSjPcpA8ctCLH-GpYX6wpjuf2MSbYlaDCF70RehdccHfFA-GWNmDBpSjdclDGf9w2LFq9m5WW1yVLpHeB1CqJk2HlDoJa70qUmXdScHnu-NIDxjrlwK_OE4ByHjd0F03sOpmB75mWvaH4xKkDSLg_WFVCR-jrJc2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=a6CG6apLDsUR9_sbLFtWxvPX7siXW4h1uhNTcc7bhTuBQmmaDX2Z4cskqrBec7Bj7nU0Zb84gnXlczlepOUClYIPwgsAGxc2YybEgRV6PvzjVDmJKFoXRJt8RPkZUFIA2EBH067awdWVQ-fCzHLkJgWeDdIANvqWsdJhx8EWfE6DRTpAUM_-YbSjPcpA8ctCLH-GpYX6wpjuf2MSbYlaDCF70RehdccHfFA-GWNmDBpSjdclDGf9w2LFq9m5WW1yVLpHeB1CqJk2HlDoJa70qUmXdScHnu-NIDxjrlwK_OE4ByHjd0F03sOpmB75mWvaH4xKkDSLg_WFVCR-jrJc2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهبازی:
نوید محمدزاده یه پست گذاشت زامبی ها ریختن سرش
فحش و ناسزا و تهدید و انفالو که چی ؟ حق نداری با این زامبی ها اختلاف نظر داشته باشی
این وضعیت زامبی هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/142743" target="_blank">📅 01:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhp3o3fztfHZEYn6pzyMp177ECRqcvEkAZ4Q6ncrxpvba_yNbqlu0iPSAu8dOHLEMU2beNa7ws2VMzO71-Z-gL8BAZV8Lbq8D-8uwEVwDhgptziyPj2sh9wKZVGpYvKbtm63GPt9hDbnP7LgIdLWOOuWBmNPmaPXK1ual5No-pP121uH3A37kqmIDlA7yE8KbzpxTKpaSPUV-N_e29UZS1VqTZhxgE0LgHpNy3OVkCPbqQ_UJ1xt0N0a6nmCIiCFH0xA_FcZAAymJtjSQLr3HTHE2Uy8z6Sbwz7AdQPVbLYbCVEwx3FnLSwztex1VLogJIMB63PiUhdngBjIavgWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: آمریکا مسیر جنوبی تنگه هرمز رو هموار کرده و کشتی‌ها در حال تردد هستن!
🔴
پ.ن: تنگه بسته نیست فقط ناامنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/142742" target="_blank">📅 00:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اعرافی رئیس مرکز حوزه های علمیه:
۶ ماه که هیچ؛ حتی اگر ۶ سال هم طول بکشد ملت ایران پای عهد انتقام رهبر شهید خواهد ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/142741" target="_blank">📅 00:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c0c04f93.mp4?token=cuivfyjfvd5-q1u1w4nc5AcYsK_7hnO-nNYy8odKZoWgtQQ0CySzUXKFGl6GdJPRTZ6vnOvDEvGsj1Xf0ygmVNbHVJ4g2ThYavb0gSd7UYKrAoeLa8uyIMu_Rts1bDRSamNQuhXOedyKhTpCilpg_Hgj5HNxYfSPjFhG9LkRL3h_Bb9mlKJio9YdDnN9Pv94nrep7uqj1zZI4BAeWcqoux7UsTfDFVIoTeOxZXIvjUsnXpSe9wTBtcbyJX2i1S3CnDDtsGPeyMsBb9MbM9bf_CQRtRTjLgXiB8f9EaoZTePSIZeKrP9FsLnXW9PHbBjBrAzBqdSYnRv8o3iW8QDJTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c0c04f93.mp4?token=cuivfyjfvd5-q1u1w4nc5AcYsK_7hnO-nNYy8odKZoWgtQQ0CySzUXKFGl6GdJPRTZ6vnOvDEvGsj1Xf0ygmVNbHVJ4g2ThYavb0gSd7UYKrAoeLa8uyIMu_Rts1bDRSamNQuhXOedyKhTpCilpg_Hgj5HNxYfSPjFhG9LkRL3h_Bb9mlKJio9YdDnN9Pv94nrep7uqj1zZI4BAeWcqoux7UsTfDFVIoTeOxZXIvjUsnXpSe9wTBtcbyJX2i1S3CnDDtsGPeyMsBb9MbM9bf_CQRtRTjLgXiB8f9EaoZTePSIZeKrP9FsLnXW9PHbBjBrAzBqdSYnRv8o3iW8QDJTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امام جمعه حاجی‌آباد بندرعباس به دلیل افشاگری علیه مسئولین شهر، به دادگاه کشیده شد و مجبور به عذرخواهی گردید؛ اکنون عذرخواهی کرده است.
🔴
نوعی جالب از عذرخواهی:
«من از بانک‌های رباخوار و از قاضی ظالم و مسئولین بی‌کفایت عذرخواهی می‌کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/142740" target="_blank">📅 00:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142738">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL-Y4fHB9hBgjNHoo-3-twmYkAi1nF9Csec_jLZasse-iF9qbYqLCrNEkyzUICKaIQhADFNEM5EBky81Fdnh8R41q97OOmn2g8HLWifkmJ0aVN10GooeId3iKnsr5J4cGnoOg1RIh9spU3cn63nlBWYx55iWc7pNl624DDhjZ3ubmB1wiDyE0FJReCbNQs3GfWyKW9kLS75NOnrQ3gkeNkNJjQoqcxaWKDj_9zUGVXi2BKJDqKDu9oBvPdD8RZSZZDacx1b-EpmfM2hakXA5GzUpvTZSpbkf9zelWPg3ENLM_yAQMvCT04Gd9qqWXbxcBV-Zd7x8uWwEoP8WWFSE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
کوچک زاده نماینده مجلس:
عراقچی اولین وزیریه که بعد از باز شدن مجلس مورد بازخواست قرار میگیره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/142738" target="_blank">📅 00:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142737">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4023a2d84e.mp4?token=E5cu5W2utt72VmCfOM-iatavfk1gt6Io5rtIWr68sS309t44wRo01g68ZMF9aDyzBFe4GubbQe5qER2rIcamoudymMhivuzPpWqnIQ9csmxPnmxxpTqBv3jjx-B5t4cos_9tfsao0wnLyubu40g49yv-5YtFevK9IvrTBANXkUhPe3FEQ5rs6pc6Xz7Y1V53Y5_C6gKyecliugcaRF5hMavj-uComBFashqQdCS0vhdjnk0bBA2kBFq2q_c3CxX2mI4uU4C62w0XZAdLniTvNQVEE95OWhTHBCv16BZyHlRxo9iTznASmIydSc3NpJ6Sk0hBJPTYVE3oCZNYpzlA5oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4023a2d84e.mp4?token=E5cu5W2utt72VmCfOM-iatavfk1gt6Io5rtIWr68sS309t44wRo01g68ZMF9aDyzBFe4GubbQe5qER2rIcamoudymMhivuzPpWqnIQ9csmxPnmxxpTqBv3jjx-B5t4cos_9tfsao0wnLyubu40g49yv-5YtFevK9IvrTBANXkUhPe3FEQ5rs6pc6Xz7Y1V53Y5_C6gKyecliugcaRF5hMavj-uComBFashqQdCS0vhdjnk0bBA2kBFq2q_c3CxX2mI4uU4C62w0XZAdLniTvNQVEE95OWhTHBCv16BZyHlRxo9iTznASmIydSc3NpJ6Sk0hBJPTYVE3oCZNYpzlA5oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنسرت نانسی در شهر صیدا(جنوب لبنان) برای شیعیان این کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/142737" target="_blank">📅 00:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142736">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کنسرت شکیرا تو امارات به خاطر تنش ها و احتمال وقوع جنگ و شلیک موشک، تا اطلاع ثانوی عقب افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/142736" target="_blank">📅 00:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142735">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگر دونبال یک کانال شرط بندی خوب هستی که همه فرماش برد باشه بهترین کانال تلگرام براتون میزارم
👇
👇
👇
👇
👇
👇
1.94 dor 1 win
✅
1.85 dor 1 win
✅
1.84 dor 1 win
✅
fulllllllll winnnnnnnn
❤️‍🔥
https://t.me/+vqAEK47dmPViYmQ0
❤️‍🔥
❤️‍🔥
https://t.me/+vqAEK47dmPViYmQ0
❤️‍🔥
…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/142735" target="_blank">📅 00:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142734">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd8f66573.mp4?token=KN-5soBlIxcKfilZjGmAsBJlT9jw0PgVifVZHUVnF1ytqpnXHRxB7FiCIUsuE4AEBNS3x1asTqMobBmA0lH1MYByuS9nfZeR7VW-PERHSinPN67uaMwlLRNIpyR0EoQvfxmOMFjRIiQQZuygDAFgrp-8PtO-gXBkv1lusIVNXzVrxMMT19vofrIQLlAO9iCmQKWrJQVpT6ehQaS9RtJZX7coykubFrBlU1OBEFE7JcvZOcqxuj4GMov3HHsI6pbcFHqwSS4YNR75ZFPGjwPKpe6VcQt1Zb8bWwEqVihxJfH4ggdNVmB8m0LpSdEWvjUndbdgBZiW4h4D2U3yleYg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd8f66573.mp4?token=KN-5soBlIxcKfilZjGmAsBJlT9jw0PgVifVZHUVnF1ytqpnXHRxB7FiCIUsuE4AEBNS3x1asTqMobBmA0lH1MYByuS9nfZeR7VW-PERHSinPN67uaMwlLRNIpyR0EoQvfxmOMFjRIiQQZuygDAFgrp-8PtO-gXBkv1lusIVNXzVrxMMT19vofrIQLlAO9iCmQKWrJQVpT6ehQaS9RtJZX7coykubFrBlU1OBEFE7JcvZOcqxuj4GMov3HHsI6pbcFHqwSS4YNR75ZFPGjwPKpe6VcQt1Zb8bWwEqVihxJfH4ggdNVmB8m0LpSdEWvjUndbdgBZiW4h4D2U3yleYg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی رئیس بانک مرکزی: کشورهای همسایه حاضر نیستند با ما عکس و فیلم بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/142734" target="_blank">📅 23:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142733">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
همتی، رئیس‌کل بانک‌مرکزی: ذخایر اسکناس بانک مرکزی ۱.۴ میلیارد دلار افزایش پیدا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/142733" target="_blank">📅 23:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142731">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNwQr9_noODcQ62LmK5OLOXoDeRip7WM-2LkcOYfr64YsXeiEd9uXFLSKpX_H1XeUNAI6iYDZQdNXfGXHrpz4iQJ5JNyBpVQoZyRT2FLf8RG2_Q3u4PTMjOTGdxnKCcDtlzlIqpzBB2o_c_zUuG-fELqYnCPI685yYjeqdC9AwblTgHwO7wP3CTTTjtvhmVGSWiqksYRv3ZhJMwYfybzF69_GgVURo4AlDOt90KnBFT46L1bvJ-KwsGFYbyBIdlxsE9p-Yq9WFuaGlCpo9nVxPs3mT2h8SFp7EtmS7BOvUgJfA7mmDrlQIddg5ur2KSZZXtOojBeLf4Tgbuz6SkgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmcgjgLTsXyOxm1BMx2OuEKkjeJoaRrAxwLiowvFfjijnG5UFElCvjtBXJetURoTv_khUOP6Dy0wxS3EoA1QdEV5LwTCg1llMduCaUfuUehfuoNVUg9EJJPajzeuRbf7ErrI9Ak0lx9Mg1bRIeDJzPkGqs_6cRTgzyOBh2kTk8KCKbHoPi67v5oQ4oxLgwATyTa1__xGiqyVqGVlEcNUlsknqJzayv-7u4uZ1v2RvlNI0Pb7fqY58wX5cSOejARuGEzCg3qAxWIJw3pNPG3sH0f5h1svckPblYCJyZlgCq1L1J37AEg7vyTvqhYm_ONqTB_UyJ1FVF1Cfzi3T-jo0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یه فروند هواپیمای شناسایی آمریکایی مدل P-8A از جیبوتی به پایگاه الظفره امارات منتقل شده. هم‌زمان هواپیماهای تانکر سوخت‌رسان آمریکا هم از قطر و تل‌آویو تو نزدیکی تنگه هرمز فعال شدن تا به جنگنده‌ها سوخت‌رسانی کنن.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/142731" target="_blank">📅 23:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142730">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSd1iU26adCeMvsCG0CodTaARxsuMufilYdx2IEPilP-L41GeZFTGR_k7LDkLtoT8FLbR93CluCgsALlx5ZuRumY_BGSysH1dxjeqqWh55do7RPE3YIXreD2U4FfCHWkFGvMQFr-GnUTepKgkx8ZIIefuruMUFh7Kry92rnqXG41iaV72pSxXX_6J8t6O1sUrQrumYRXM0XX2or-eO9XC7VIq2gRwcaM8qEo8NNvaN5UNl0PYLs1t-H_hJRh1fSo6JjA797-M4HVL22BdykvhzlGAVyAJwHjR5f6Kxk4zFgASa0Z8L7M-oH04HLWkoRormJVJ4zx6VbSttW-7YUsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت الله عابدینی:
مردم هرچه سریعتر ده هزار گوسفند برای سلامتی رهبر نذر کنند.‌ عجله کنن چون فوریه!
🔴
پ.ن:گویا آقا رو سیوینگ پاوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/142730" target="_blank">📅 23:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142729">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
قیمت مسکن منفجر خواهد شد
⁉️
این تحلیل رو گوش بدید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/142729" target="_blank">📅 23:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142728">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دفترچه سوالات آزمون سراسری رشته تجربی هم اکنون از فرمانداری به حوزه های آزمون ارسال شد و در مخزن طبقه بندی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/142728" target="_blank">📅 23:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142727">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
همتی: امیدواریم با احیای یادداشت تفاهم، مذاکرات بر مبنای منافع ملی کشور ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/142727" target="_blank">📅 23:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142726">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
همتی، رئیس‌کل بانک‌مرکزی: کالابرگ باید ۲۳ درصد افزایش یابد و به ۱ میلیون و ۲۳۰ هزار تومان برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/142726" target="_blank">📅 23:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142725">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ درباره تنگه هرمز:یا اوضاع بسیار عالی خواهد بود و قیمت نفت به شدت کاهش می‌یابد، یا ما به همان کاری که تاکنون انجام داده‌ایم، ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/142725" target="_blank">📅 23:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142724">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771a45bdd5.mp4?token=oE202flPRJBQNPB353xIUuEyMy7rLUfQarDC0j8HbI8sXxwp1tTycAi17XFfJNuHfvAJ8jxCDoll4ly08S41UwEjBil0I_-aetk6OHePHOt9Bxf-BN6WFXBCyvbmAHO2k17qEWF3mPG5NkN4n4eDRdoP44dwEj_cqMI4-WvKDl_k-QgxKfnV1tNz5R2G7tb4E2JGC2mKwGKPRb1-7VzF94oEHVqpCf2RGdOBGMp3Y8yQlqg_VF_fpHVnklqRPzzG_VEN6ZZ78-chGGMM-fg8sH4pJNLy75Ba6KNe-FOXPe9XoaJdNJGG3rq335c3g8gzG2huKtRUHglawMK3l-ihM3RcTuuPKsDwO0IVwLeO-X5oi57TCZTdpXs6EYTK-95rkjJAxV2vV0mkC5rPxUf6zZZ3lNDL2RCN3OKJmcy9tZPMk7sGLOR1Zw_e9KSVWNpVU56AIdZaqt4kfrAQnoGohZElB3cIC4a7FgBOZIz5AMqNnBqC7GhDuItQhBlLjn0MfrL1RQjj9rbtQMee71NeFFtSs3wZNcRzIBol-rBSDgvLKWf84WIULXKuFBJobREhvAMAWDccTiH-_1O7S3Yroqe1-TTLf8USs2KxPei-JqnRLF-1FnU7M8cbLNNFSU3pFoTz62sbU6j-oSgi3SQc_9aVaWL8Ssw6-tw9hV6l338" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771a45bdd5.mp4?token=oE202flPRJBQNPB353xIUuEyMy7rLUfQarDC0j8HbI8sXxwp1tTycAi17XFfJNuHfvAJ8jxCDoll4ly08S41UwEjBil0I_-aetk6OHePHOt9Bxf-BN6WFXBCyvbmAHO2k17qEWF3mPG5NkN4n4eDRdoP44dwEj_cqMI4-WvKDl_k-QgxKfnV1tNz5R2G7tb4E2JGC2mKwGKPRb1-7VzF94oEHVqpCf2RGdOBGMp3Y8yQlqg_VF_fpHVnklqRPzzG_VEN6ZZ78-chGGMM-fg8sH4pJNLy75Ba6KNe-FOXPe9XoaJdNJGG3rq335c3g8gzG2huKtRUHglawMK3l-ihM3RcTuuPKsDwO0IVwLeO-X5oi57TCZTdpXs6EYTK-95rkjJAxV2vV0mkC5rPxUf6zZZ3lNDL2RCN3OKJmcy9tZPMk7sGLOR1Zw_e9KSVWNpVU56AIdZaqt4kfrAQnoGohZElB3cIC4a7FgBOZIz5AMqNnBqC7GhDuItQhBlLjn0MfrL1RQjj9rbtQMee71NeFFtSs3wZNcRzIBol-rBSDgvLKWf84WIULXKuFBJobREhvAMAWDccTiH-_1O7S3Yroqe1-TTLf8USs2KxPei-JqnRLF-1FnU7M8cbLNNFSU3pFoTz62sbU6j-oSgi3SQc_9aVaWL8Ssw6-tw9hV6l338" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چه تحریم‌های دیگری می‌توان علیه ایران اعمال کرد؟
🔴
ترامپ: خب، ما مواردی وجود دارد که می‌توانیم تحریم‌هایی را بر آنها اعمال کنیم. ما تحریم‌های بسیار شدیدی داریم و خواهیم دید که حالا چه اتفاقی می‌افتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/142724" target="_blank">📅 23:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142723">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfc9f28ad.mp4?token=PYSqilC8wM0I8kEQ7uWe-2w2XUgzmlraEO9y5uJJaTs0XtN5l8_hpTCaZ-23eU3CNEF5OckYwFRPCPGGk1BkwgsWGbRw6OG7Kp5UKQFQonDQA9kTfzLQhPRu93ZQ89zP_nIfddpg8Z7sUwSkP1BYfnlnuiXJDfL7gUqJPKFMwbm2QbRrM9oTZLt05tf4dTwbn6rOuoCS6PEJYXlHicoIsCca56hXlOqslChVTVFSpxyD22OQr6BqErskZeCkp2C6E9jojvAO0kerc40TceTy54SvduZrW_f3XCw5ztw4T30C5stHBwvP84DhHhYAC8RRs3oDPuB7saBGpIpR54TkNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfc9f28ad.mp4?token=PYSqilC8wM0I8kEQ7uWe-2w2XUgzmlraEO9y5uJJaTs0XtN5l8_hpTCaZ-23eU3CNEF5OckYwFRPCPGGk1BkwgsWGbRw6OG7Kp5UKQFQonDQA9kTfzLQhPRu93ZQ89zP_nIfddpg8Z7sUwSkP1BYfnlnuiXJDfL7gUqJPKFMwbm2QbRrM9oTZLt05tf4dTwbn6rOuoCS6PEJYXlHicoIsCca56hXlOqslChVTVFSpxyD22OQr6BqErskZeCkp2C6E9jojvAO0kerc40TceTy54SvduZrW_f3XCw5ztw4T30C5stHBwvP84DhHhYAC8RRs3oDPuB7saBGpIpR54TkNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد سوئیس: اگر کسب و کار ما را از سوئیس بردارید، آنها مشکل دارند.
🔴
چرا آنها نیم امتیاز می پردازند و ما بسیار بیشتر از آن می پردازیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/142723" target="_blank">📅 23:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142722">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c441e5115e.mp4?token=gW8nL7yVWicZhuyr0tDnHTM-IltSVfDpc94jn4Qe8cj4X95ByP2DTutlBggdAQGC2p-YNuIcBgBYE_FCP8cCS9W0FLVBf_eTGtJFxUb4WumiWoR_GKnaAESewonAwfJSLsGTmd_FF-Bl7dQ5Ge6ONZsYtiWIOw3xe7EpOcMHmninbiyR_dOsKP51Arb8gYcAxW5Zqr3okAolpj0i45PSWeffgV4qWdFH9BRlKZK_TJG5KXLKGOLZk3V86iW4jYt5bgKdNfhI02u1p0V69U9YB5bOncM4SsYLrJaFfdhkejFx-uKYKfQy_W15KZ4cmWOyX_uUaQJL2TGyTlRLuAgf8WpVY3K6FUlopxmr9rdgYoGJkMUj6VwJ_DiR-T-KeCxWx2i4w7maBvkyDA3sC6PvlI99zBxBNIIdGOGY0Q8MO9PULAYGgNrzmVlZnEYQ2J5dWnN23W7H_Q7YW6vCYOirjuDwTOrSj_LWKY7ehA0pTbRTacHCShb1YP6x5QpeLFEhhP0nmWgDkJg2HIB6B3k02RBevofWgzHWFaHz7cbBwj-AvU1oJDIfEwT5LHTMfdjhEDOCKch0t-J7CsPuSqu_OQk39WyY5zLYV3d4AaULrVb6F1-c4O7C_3naXRwRIgXmU-edFO5S7EBltOwKnaXn7sD_dIHc3tz4-epGHKgAlUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c441e5115e.mp4?token=gW8nL7yVWicZhuyr0tDnHTM-IltSVfDpc94jn4Qe8cj4X95ByP2DTutlBggdAQGC2p-YNuIcBgBYE_FCP8cCS9W0FLVBf_eTGtJFxUb4WumiWoR_GKnaAESewonAwfJSLsGTmd_FF-Bl7dQ5Ge6ONZsYtiWIOw3xe7EpOcMHmninbiyR_dOsKP51Arb8gYcAxW5Zqr3okAolpj0i45PSWeffgV4qWdFH9BRlKZK_TJG5KXLKGOLZk3V86iW4jYt5bgKdNfhI02u1p0V69U9YB5bOncM4SsYLrJaFfdhkejFx-uKYKfQy_W15KZ4cmWOyX_uUaQJL2TGyTlRLuAgf8WpVY3K6FUlopxmr9rdgYoGJkMUj6VwJ_DiR-T-KeCxWx2i4w7maBvkyDA3sC6PvlI99zBxBNIIdGOGY0Q8MO9PULAYGgNrzmVlZnEYQ2J5dWnN23W7H_Q7YW6vCYOirjuDwTOrSj_LWKY7ehA0pTbRTacHCShb1YP6x5QpeLFEhhP0nmWgDkJg2HIB6B3k02RBevofWgzHWFaHz7cbBwj-AvU1oJDIfEwT5LHTMfdjhEDOCKch0t-J7CsPuSqu_OQk39WyY5zLYV3d4AaULrVb6F1-c4O7C_3naXRwRIgXmU-edFO5S7EBltOwKnaXn7sD_dIHc3tz4-epGHKgAlUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: وقتی با کیم جونگ اون دوست هستم، از این واقعیت خوشم نمی آمد که ما در حال انجام این تمرینات نظامی عظیم علیه کره شمالی هستیم.
🔴
ما در حال انجام یک رزمایش بزرگ جنگی بودیم. من فکر می‌کردم که برای کسی که، رک و پوست کنده، حداقل در دوره من، رفتار بسیار خوبی داشته است، بسیار توهین‌آمیز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/142722" target="_blank">📅 23:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142721">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc770e4cec.mp4?token=Op54nTkmY92Qs7z9rORfQ3NOrqunG6GjXnHh9IY0rGZXidP1vNwX65gLn8UzKwihkjUkrUB2-rNR147qBa7pXlnCZt7nrwb7xJtXaMp9nreZTQ_KCw75edCw28Ms26HS9XQeRKxptzPw179MjnO178dyKR1mFtydvhFA0bEe2_Q4mf76x_0BPJXpzxgNH2JELD0YD7Tbo_xMzFDm5XgM_hq3LFj1J9gtPLrq3P5WF7D3VEdzE7knoRYrg0BqzowBbdG7zzYgGZXWCJmVrlL4w45lTqnG1UfeIRQVzjK-2t8Wd6Vby5U1xWgpZCn6ZVLYEXWFF1-QcFgoe9pOSVYymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc770e4cec.mp4?token=Op54nTkmY92Qs7z9rORfQ3NOrqunG6GjXnHh9IY0rGZXidP1vNwX65gLn8UzKwihkjUkrUB2-rNR147qBa7pXlnCZt7nrwb7xJtXaMp9nreZTQ_KCw75edCw28Ms26HS9XQeRKxptzPw179MjnO178dyKR1mFtydvhFA0bEe2_Q4mf76x_0BPJXpzxgNH2JELD0YD7Tbo_xMzFDm5XgM_hq3LFj1J9gtPLrq3P5WF7D3VEdzE7knoRYrg0BqzowBbdG7zzYgGZXWCJmVrlL4w45lTqnG1UfeIRQVzjK-2t8Wd6Vby5U1xWgpZCn6ZVLYEXWFF1-QcFgoe9pOSVYymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر من شهردار یک شهر یا فرماندار ایالت بودم، و این شانس را داشتم که یک کارخانه بزرگ هوش مصنوعی یا یک مرکز داده در آنجا بگیرم، قطعا آن را می خواستم.
🔴
مشاغل بسیار زیاد هستند و مالیات ها بسیار زیاد است.
🔴
اگر آن را نگیرید، عقب خواهید ماند، زیرا جاهای زیادی وجود دارند که آن را می خواهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/142721" target="_blank">📅 23:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142720">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f54a41a38.mp4?token=SgC0RjZ-JfeVCPXfEHkU2XGjSnoNPPWFTRCKI_kOz5yp4YXFF3HNcj6fHmhKycdp72hccs6RutJgvJ552W4jVPOWpAXOTCMp33aJL2qqdo0Dcp_ItNyWzrsKoT37ikB0hvX6MKopnxE9sWG4f96VN8h8LdTeN4yniM0rn3BTxlr4VOtYyrbhIR5QGv9Mmjv0g_OXWx5VLdb-7KjC4NkqSFLDC8YoY1tJoPgnzXS3suNKuRL7DhzIu0COLis5w_VitNwv6Ni0Pg3W4ifJn4GLM6oQgUkWNnjD_M9JtaVOv_ye9wvGusQ0Ex8I3qgf2wx_vXBmgDeg_U_lVFIDEqVK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f54a41a38.mp4?token=SgC0RjZ-JfeVCPXfEHkU2XGjSnoNPPWFTRCKI_kOz5yp4YXFF3HNcj6fHmhKycdp72hccs6RutJgvJ552W4jVPOWpAXOTCMp33aJL2qqdo0Dcp_ItNyWzrsKoT37ikB0hvX6MKopnxE9sWG4f96VN8h8LdTeN4yniM0rn3BTxlr4VOtYyrbhIR5QGv9Mmjv0g_OXWx5VLdb-7KjC4NkqSFLDC8YoY1tJoPgnzXS3suNKuRL7DhzIu0COLis5w_VitNwv6Ni0Pg3W4ifJn4GLM6oQgUkWNnjD_M9JtaVOv_ye9wvGusQ0Ex8I3qgf2wx_vXBmgDeg_U_lVFIDEqVK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هفته آینده با افراد هوش مصنوعی جلسه ای خواهیم داشت - افراد برتر وارد می شوند.
🔴
ما با هوش مصنوعی بسیار پیشرو هستیم. ما می خواهیم آن را به همین شکل حفظ کنیم. ما می خواهیم مقرراتی داشته باشیم که در آن آنها بتوانند به رهبری ادامه دهند، نه مقرراتی که صنعت بسیار مهمی را خفه کند.
🔴
من فکر می کنم هوش مصنوعی شاید بزرگتر از اینترنت باشد، بزرگتر از هر چیزی که کسی دیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/142720" target="_blank">📅 23:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142719">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: من از مانور های نظامی گسترده‌ای که علیه کره شمالی انجام می شود، خوشم نمیاد. این مانور ها که انجام میشد با خودم فکر میکردم، این واقعا برای آن ها که به خوبی رفتار کرده اند، کار توهین آمیزی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/142719" target="_blank">📅 23:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142718">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: بسیاری از خطوط لوله در حال ساخت هستند، تنگه هرمز دیگر آن اهمیت گذشته را نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/142718" target="_blank">📅 23:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142717">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8505479f85.mp4?token=VPZZWE74ZoLKNZChIZmI5Ww0wVLaa8blqFpfWRr7uWU18_EbClQV3mLAa6yo4roGFIbWaUdgVsYco8cWs8_jNY9V7paFPMBg-bCR4BQ4R-BXr3bJQ5iGN2WPFteTnyMk4e5aax-crFBnk9gO9Pl44cF7jvCgbcIqUCcC9PZ8WQQH6eRE5P108dvKRhlB2SB9Em_2a84PYiWdqpAetCj8McTWwYkSmJzt6BfxNhPtXbFF3Li4-fLByHrPATnQFS8PWynI4grB3fviNp9T2jAgXHK0-DhXe9ERk9Bfe86_Yr0LkFmEpIQFF76N8YBWYYyC7usoNt8TN9RjT-1RoP9GDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8505479f85.mp4?token=VPZZWE74ZoLKNZChIZmI5Ww0wVLaa8blqFpfWRr7uWU18_EbClQV3mLAa6yo4roGFIbWaUdgVsYco8cWs8_jNY9V7paFPMBg-bCR4BQ4R-BXr3bJQ5iGN2WPFteTnyMk4e5aax-crFBnk9gO9Pl44cF7jvCgbcIqUCcC9PZ8WQQH6eRE5P108dvKRhlB2SB9Em_2a84PYiWdqpAetCj8McTWwYkSmJzt6BfxNhPtXbFF3Li4-fLByHrPATnQFS8PWynI4grB3fviNp9T2jAgXHK0-DhXe9ERk9Bfe86_Yr0LkFmEpIQFF76N8YBWYYyC7usoNt8TN9RjT-1RoP9GDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: دو سال پیش کشور ما مرده بود و اکنون کشور ما گرم ترین کشور در سراسر جهان است.
🔴
هیچ کس نزدیک نیست، هیچ کشور دیگری نزدیک نیست، و هر کشوری آن را می پذیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/142717" target="_blank">📅 23:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142716">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4f790df8.mp4?token=Dgx90pnRVY4eTCddGSRPWS15pSqYWrI8SnkV0nrvRTcRZoDQZCB0eX0yCHvBnMPlZ1se7S9QVXNue8S-maLVjZJsPk-FzdA2gfK1DZ8TYxqxOTGkXEKyAgKLoNn_PV_FBoQH8wfwH98sGc-QmRgJ2A1E9zSRjEdgBgwtWCgynPOKW2k1J8j8YsRujjnHxIynXI1tR2XTy79L_nXQgMCyyXSFK1UiEGtR8o3f7I948bcn-IaZsFOmYfCzxa-j6QLAHDcXldtXfrpBAu1NbMqb33yjUcDNKMJzjl8YWXYLgDnPuPvfAse46bEJ8nqcO-LZ3RA3Ts9ccpBxidbLM5KQ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4f790df8.mp4?token=Dgx90pnRVY4eTCddGSRPWS15pSqYWrI8SnkV0nrvRTcRZoDQZCB0eX0yCHvBnMPlZ1se7S9QVXNue8S-maLVjZJsPk-FzdA2gfK1DZ8TYxqxOTGkXEKyAgKLoNn_PV_FBoQH8wfwH98sGc-QmRgJ2A1E9zSRjEdgBgwtWCgynPOKW2k1J8j8YsRujjnHxIynXI1tR2XTy79L_nXQgMCyyXSFK1UiEGtR8o3f7I948bcn-IaZsFOmYfCzxa-j6QLAHDcXldtXfrpBAu1NbMqb33yjUcDNKMJzjl8YWXYLgDnPuPvfAse46bEJ8nqcO-LZ3RA3Ts9ccpBxidbLM5KQ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به شوخی می گوید: من قانون GENIUS را امضا کردم. اسمش را به نام خودم گذاشتم
🔴
من نمی خواستم از نام خود استفاده کنم، بنابراین فقط آن را قانون GENIUS نامیدم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/142716" target="_blank">📅 23:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مجری تلوزیون: مردم میگن حاضریم زیر فشار اقتصادی له بشیم اما جلو آمریکا سر خم نکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/142715" target="_blank">📅 23:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142714">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z53lZPP78iyWHGGuO0prlV3QxRAUasJRJa88K35yBeu00XprOcJBOn7KZIZ3q6UK-rnK0DiIrjI0f0CK_3xB_OuYfUm_EyLgRsQO3r01RQuh54n4OKEo_APdFKBLCm6Z256hd9HbULCSTN0noMHq5wiJoxLOeNfyhqEYOvMmvIaN4Af822ny3RCFEEI5InqjuFj94SQNtoWKM6wG3ds36ExbEC9sZHwp7xeJNxkIWkZxoXbFVheJ5KkQ2rngZFqzhvp45fZVHkyBsw1cVwlw-16bu_ij_e6TwPXg0Rda7QmMsUBBLc_Hd1lfiQMEuCr6St23t5xo0DDxkV66iUQWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دونبال یک کانال شرط بندی خوب هستی که همه فرماش برد باشه بهترین کانال تلگرام براتون میزارم
👇
👇
👇
👇
👇
👇
1.94 dor 1 win
✅
1.85 dor 1 win
✅
1.84 dor 1 win
✅
fulllllllll winnnnnnnn
❤️‍🔥
https://t.me/+vqAEK47dmPViYmQ0
❤️‍🔥
❤️‍🔥
https://t.me/+vqAEK47dmPViYmQ0
❤️‍🔥
🥷
ورود به چنل شرطبندی مورتال کمبت
🥷</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/142714" target="_blank">📅 23:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام‌های آمریکایی: نیروهای ما برای ورود و خروج از تنگه هرمز به منظور انتقال روزانه میلیون‌ها بشکه نفت، کریدوری ایجاد کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/142713" target="_blank">📅 23:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142712">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ به آکسیوس: در حال حاضر، ایالات متحده با ایران مذاکره نمی‌کند. آن‌ها در حال تلف کردن وقت هستند. مذاکره با آن‌ها تلف وقت است.
🔴
ایرانی‌ها هنوز مقداری قدرت دارند، اما به طور کلی، آن‌ها دیگر آن قدرت قبلی را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/142712" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142711">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام‌های آمریکایی: نیروهای ما برای ورود و خروج از تنگه هرمز به منظور انتقال روزانه میلیون‌ها بشکه نفت، کریدوری ایجاد کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/142711" target="_blank">📅 22:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142710">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVZc5CWDq3XzkN9zzGxpPQTkOqfVPXZlezazZNahH0SkDXuag0-U_BCqK6jXKCfX_5jZC3VqypDTlFdj8eYYl5UMAYBWRh9CTlS1TY6biGSy6Yoq9LBbihXMYQvS60ri3OR0jhTqyosMSpyGow3qnmWdCB6XMYaAurS1pcposGdIFZLTseA7u5UrBsemHnwi1fBX4PzglmVaP5A3D89zTgGj8A1KZHAahYF9-zZeHDm8g_iPgUoTzQPm0tqcU4NZMYgT7c9Yhve22EU7ZT935bbV1PzzsPvelqtxEGVH1RBN_LT1_6jjrm_hUjdn-ykpGSwUCMaUkXjZKtruw3V15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی با وزیر امور خارجه موریتانی، در مورد حمایت از فلسطین و مقابله با اسرائیل و توسعه روابط دوجانبه گفت و گو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/142710" target="_blank">📅 22:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142709">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
همتی: هم‌اکنون صادرت نفت ایران قطع شده و نفتی صادر نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/142709" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
یحیی سریع: نیروهای مسلح ۹ عملیات موشکی و پهپادی علیه تأسیسات نفتی عربستان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/142708" target="_blank">📅 22:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142707">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74ede774bd.mp4?token=fEvBtojaPnc3UkEaQT6-xtHxkmLIHHJ4iVIrzdhEIc8Im4U-B7ekTvJ6mccWWEsqJ8UZnGT3UsKFyMACpyZncC-a2EVpKwUiX56lk5fnmUhXZ8L5XkpoTUkv1cSj2cDfH6NY_5uFe3XHiuJK8Jxq6tJFkrIKC5Q4nojVg13tjzhanoEke7gF64a1sIRpOCcEThRYqQuKwJSMFxpQhpXAl7TEKpz4fCof-mfSNNVD8HyzhjzGpb7mtgjAm4PVHBPtQmofgSLxK64eLKnyb6kz-0bWr6NGCps0iuqY15fAO8V4_3Ro-5ifh4sWsW2MWXQqqDW7A2Vhog-3qcqZ0WaASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74ede774bd.mp4?token=fEvBtojaPnc3UkEaQT6-xtHxkmLIHHJ4iVIrzdhEIc8Im4U-B7ekTvJ6mccWWEsqJ8UZnGT3UsKFyMACpyZncC-a2EVpKwUiX56lk5fnmUhXZ8L5XkpoTUkv1cSj2cDfH6NY_5uFe3XHiuJK8Jxq6tJFkrIKC5Q4nojVg13tjzhanoEke7gF64a1sIRpOCcEThRYqQuKwJSMFxpQhpXAl7TEKpz4fCof-mfSNNVD8HyzhjzGpb7mtgjAm4PVHBPtQmofgSLxK64eLKnyb6kz-0bWr6NGCps0iuqY15fAO8V4_3Ro-5ifh4sWsW2MWXQqqDW7A2Vhog-3qcqZ0WaASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: تا الان پول‌های تعهد شده در تفاهم‌نامه پاکستان آزاد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/142707" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142706">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بلومبرگ درباره سفیر سابق آمریکا در لهستان:ایران انگیزه‌ی چندانی در کوتاه‌مدت برای بازگشایی تنگه هرمز ندارد. ایران می‌داند که زمان به نفع او است و به همین دلیل، نیازی به ارائه امتیازات فوری ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142706" target="_blank">📅 22:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142705">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت نفت عراق: از ابتداى ماه آگوست تاكنون روزانه بين يك ميليون الى دو ميليون بشكه نفت از تنگه هرمز صادرات داشته ايم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/142705" target="_blank">📅 22:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfd0cd9fe.mp4?token=W8vYKFPnmqGppAEtk97q6lOwRcXSIZt2GY2scwPn2thgfOMthvbRfpwDxQ9P52hNnR8pDcc2evNUFa4DpWvYVxSNUnc8K5XYJEPgKqXmWVPYAbAoFOdbrDfDa5_8Tah9jAhoyH-K1SLJSQ7lCSP-YWsMFzt5CZW-IVmsiuag-fgQb86blmFyiWactQxU4mY85Ixb9Wl_yYcmw6jxTotRqqFpJ98jX3nozIiZJWvAUXFauMxjScVqZblMnuj5VrBb_ziOiijE01T4FH5xJ_NWxP7j0c4KXV1Kho8ZEvA9E8YNvF0frl-yy7xwIsOfazJsM-KDmwZLE4z-D6UfR59fBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfd0cd9fe.mp4?token=W8vYKFPnmqGppAEtk97q6lOwRcXSIZt2GY2scwPn2thgfOMthvbRfpwDxQ9P52hNnR8pDcc2evNUFa4DpWvYVxSNUnc8K5XYJEPgKqXmWVPYAbAoFOdbrDfDa5_8Tah9jAhoyH-K1SLJSQ7lCSP-YWsMFzt5CZW-IVmsiuag-fgQb86blmFyiWactQxU4mY85Ixb9Wl_yYcmw6jxTotRqqFpJ98jX3nozIiZJWvAUXFauMxjScVqZblMnuj5VrBb_ziOiijE01T4FH5xJ_NWxP7j0c4KXV1Kho8ZEvA9E8YNvF0frl-yy7xwIsOfazJsM-KDmwZLE4z-D6UfR59fBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: مشکل پول های ما در بانک های عراقی حل شده است و به تدریج بهتر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142704" target="_blank">📅 22:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142703">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy4trCp7nxptTLROi3LnV6f2WPWffxxypnbaaemA2cAi5kgQkNItAYmfFwc2N27-QDnCH5CyEcAChbda_m0lfOMd7vn_KPoOq9fFxoKkA18w5gSs5rCWYlQ7nCt8j69s3QVuuP6VL5vTbQ4AHUm6FFnLN1vgkpeYfGAIBpv05QRghwkKRoHctxlbkjkDklN0z3gsSHvStB_0YB2NYx1E7HPy0CCHNbvkELX972UQyPY-kcgKgVlv088ENRNJZElrBg3531azIpP0JQprTHQoCfq7Sdy5GHe6_7VL_5cLXVaLmwfr2blLUduf09ack5NFWjlP1ioK0L5-fj10aaGniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما رسما دیگه عکس آیت الله خمینی رو حذف کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/142703" target="_blank">📅 22:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e789ecd273.mp4?token=Qy2OzaoRUUe11rFQtGLYaBZDjjQ45pUG2aRIgx1To6xNSOYr-jsjNx5OswpS25dMhg5FSsV8JtFMGFqRr3V544BrDIywJwQAiWa820Eah50TVIZszawBrlhbH2Rvls2eGefUw8Jc2qsrKniP8GiflOutjrnGVdR6C2-Eeqn3BtEn1IbMmjBVZlzO0a0hea_38cD4MuG_qfFX5qmj0SfY8qMeYqut99oJ1W-DR7652y-V98-zWP6jaj7CmkwVF1-Yx35cBtF7Rxz0cDbKwUUSf1-ORsoy-1xIkYJxkfF4eCo3Q4muDQncd7HK5udbfrrRrBe6BSEdPBGJmw9JH85ZHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e789ecd273.mp4?token=Qy2OzaoRUUe11rFQtGLYaBZDjjQ45pUG2aRIgx1To6xNSOYr-jsjNx5OswpS25dMhg5FSsV8JtFMGFqRr3V544BrDIywJwQAiWa820Eah50TVIZszawBrlhbH2Rvls2eGefUw8Jc2qsrKniP8GiflOutjrnGVdR6C2-Eeqn3BtEn1IbMmjBVZlzO0a0hea_38cD4MuG_qfFX5qmj0SfY8qMeYqut99oJ1W-DR7652y-V98-zWP6jaj7CmkwVF1-Yx35cBtF7Rxz0cDbKwUUSf1-ORsoy-1xIkYJxkfF4eCo3Q4muDQncd7HK5udbfrrRrBe6BSEdPBGJmw9JH85ZHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی اسلامشهر تهران؛ یه مادر و پسر گدا رو گرفتن که فقط تو نیم ساعت ۲ میلیون تومن پول از مردم جمع کرده بودن.
طبق گفته این زن روزی ۱۵ میلیون تومن از مردم گدایی میکردن.
ماهی ۴۵۰ میلیون تومن درآمد داشتن. بهتره بریم‌ گدا شیم.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/142702" target="_blank">📅 22:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/142701" target="_blank">📅 22:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
زلزله ۴.۲ ریشتری حوالی گیلانغرب را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/142700" target="_blank">📅 22:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751a5db559.mp4?token=RT3Ru8q2i4dXwoV67WGYtqbWGzO6MpeKMe4WYZFfH3W8JmBqNWmgj5-MwTZmkwkRTHRax-BdEs0jH_D55L0uImwtPMlxzV_9RW5DhjwF6wsiCt9DMyF_9z7KWnGCpL3uneHYNITMCFy4QxcgVsVd65zjH4qI7IaJb_jLx4XnkmAQjObqcavVXuK6PEsNIcZN7L1xU-G7ach_iblsothUKbPQzSWy8DYFC38Qh2gzDVJA_OFH2maqtltgk0DUuUObGD8Ww_OxGq9AqghYLVYC15_BcMURxwtnmf8gJxPTj-qiExMGfYVjGG3dD7Sr0TQwO7zcJ-82nUJaMenOqyqrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751a5db559.mp4?token=RT3Ru8q2i4dXwoV67WGYtqbWGzO6MpeKMe4WYZFfH3W8JmBqNWmgj5-MwTZmkwkRTHRax-BdEs0jH_D55L0uImwtPMlxzV_9RW5DhjwF6wsiCt9DMyF_9z7KWnGCpL3uneHYNITMCFy4QxcgVsVd65zjH4qI7IaJb_jLx4XnkmAQjObqcavVXuK6PEsNIcZN7L1xU-G7ach_iblsothUKbPQzSWy8DYFC38Qh2gzDVJA_OFH2maqtltgk0DUuUObGD8Ww_OxGq9AqghYLVYC15_BcMURxwtnmf8gJxPTj-qiExMGfYVjGG3dD7Sr0TQwO7zcJ-82nUJaMenOqyqrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده ا
ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/142699" target="_blank">📅 22:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وال استریت ژورنال: دولت ترامپ نگران است عمان به ایران برای رسیدن به توافقی که بیشتر به نفع تهران باشد کمک کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/142698" target="_blank">📅 22:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWJw3Ab83NH0-ACNu_6viE9SX9KI7uCBsmcvXFyjaOJwy8Qf9F9dCJaIvCxap_VkC_bEzglpV_ealdhSzioeIlLbEuvj9gc8SGQr1jhzedQuez6NFQ1QDXvycIMmIq-4a6WB_12Oq9YmVtEJujdOu22bto1h-OO1oTPcFwfcphf0V1f6grFPskFDbiaMqeHr7_xr_2QUj9Vd4_8aR4bXvYYdQBBrOGxQhdmfMY-29gt8xozdoexhhCjSchxzn4CYmANHZm4aWSBYL0_N2MvVmeo7D8W5gxnedrXKyiR99BVlZ-1w3p1FCGhkk9ILO4D32bcUSMP-M9dTMO8kOcgEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت معناداری که قاليباف منتشر کرد
🔴
پ.ن: تنگه قالیباف
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/142697" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66593eb30b.mp4?token=ID0UR9UDFch_0_kvRDNCSKdUP8kGsPFTOns5B77y-LcHjtWSXyxbUgyTCBvCd4yiPNVlUTaFYe8cQxlN7jIRP03hUa1TLb1vUbxYYMydqqeUT7kUDfQ9SB2CxlCYSxBptV2XTYgtBFFluzdFBggcQe7X1K6Cz582XDVgtyw2-SkVdAXW2ujiAYb0Pq80ikVRucQyxZJDwIE__TRgbrjut4EyXFSkVHjHCbx4TIDAGT2Kg7P2PFmpAJJaODo7GNCpWe1Ky0Lw9e9vSM_QdnM9Wg4Ga6i-uAZb_w2wwcHv3H1ESrsGBpXyBc0_FE_A-Gn-MHqoVip4gLsSqP7jScFdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66593eb30b.mp4?token=ID0UR9UDFch_0_kvRDNCSKdUP8kGsPFTOns5B77y-LcHjtWSXyxbUgyTCBvCd4yiPNVlUTaFYe8cQxlN7jIRP03hUa1TLb1vUbxYYMydqqeUT7kUDfQ9SB2CxlCYSxBptV2XTYgtBFFluzdFBggcQe7X1K6Cz582XDVgtyw2-SkVdAXW2ujiAYb0Pq80ikVRucQyxZJDwIE__TRgbrjut4EyXFSkVHjHCbx4TIDAGT2Kg7P2PFmpAJJaODo7GNCpWe1Ky0Lw9e9vSM_QdnM9Wg4Ga6i-uAZb_w2wwcHv3H1ESrsGBpXyBc0_FE_A-Gn-MHqoVip4gLsSqP7jScFdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین، پالایشگاه نفتی "اوفا" متعلق به روسیه را مورد حمله قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/142696" target="_blank">📅 22:00 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
