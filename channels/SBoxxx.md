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
<img src="https://cdn4.telesco.pe/file/itY2Rjh8UKWkF6CMdzyOMPYZvQbBJIbKCPwV7ErADP8Rdy5Wo5jO0rFux80mNy9ooLK81oVsruMsJ_P0pOiQTvL2vgX80IbgnVAaZc4IwL36XF57-Usx15nIm0DXqkZyj41LdUEERTFUp_ysv2LuP_aMV22CGr5ZGWyM4EX5D5RNIc79FkDJg_Hbup4MTjeKgELxpaqQ_fRckruYeYQuvTo5cPNicPVPpgjRxJi1ok_KY0R2e9tR1pCyhbQOMqemuxZt0iu7pH1NwST_xTZQCgjOc6IQJJX98aQ85m7TVpcxMSQAp0O4EGaIr8MstALamrWk4WspOdjjj4OCORxsLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 23:46:47</div>
<hr>

<div class="tg-post" id="msg-21462">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش از صدای جنگنده های ارتش در آسمان تهران</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/SBoxxx/21462" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21461">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش از صدای جنگنده های ارتش در آسمان تهران</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/SBoxxx/21461" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21460">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/21460" target="_blank">📅 19:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21459">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏ مهدی کوچک‌زاده نماینده تهران در جلسه امروز مجلس:   به خدا اگر از جهنم نمی ترسیدم خودم را جلوی بانک مرکزی آتش میزدم ‎ ‎</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/21459" target="_blank">📅 19:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21458">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏
مهدی کوچک‌زاده نماینده تهران در جلسه امروز مجلس:
به خدا اگر از جهنم نمی ترسیدم خودم را جلوی بانک مرکزی آتش میزدم
‎
‎</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/21458" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5d6c545.mp4?token=tyrvkrM1-O_ScR6-TQMHfpeSipLvNFOcZ17RA30IovzDIJF0WQBC_2vTsRov1E9pl6ESqsFv8GhHJPHigotO1JDELTeO26caYZ8FV5dYVYhCdi2Z1D2tzxrZO5HvWQBvejZEJCO2scAi8Clt7GVzRTT6LyXL7v0hPy-YTJpYCpchuaNsF4xFTFurTU6l0O6ZXih8zf9IC8cn8un8iNUmRl8efOqjKv9VRnXIY1MZirZjc9o8KZB53vNP5zHEs4IM2zIJz0cxeN9WQUrKSOASF41ehz8lbaDhSqkU_ZjHZw1Lmj7B_BZa_H4SlD4b0HYul-ZG9bKtncDZU-Wwwdv1qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5d6c545.mp4?token=tyrvkrM1-O_ScR6-TQMHfpeSipLvNFOcZ17RA30IovzDIJF0WQBC_2vTsRov1E9pl6ESqsFv8GhHJPHigotO1JDELTeO26caYZ8FV5dYVYhCdi2Z1D2tzxrZO5HvWQBvejZEJCO2scAi8Clt7GVzRTT6LyXL7v0hPy-YTJpYCpchuaNsF4xFTFurTU6l0O6ZXih8zf9IC8cn8un8iNUmRl8efOqjKv9VRnXIY1MZirZjc9o8KZB53vNP5zHEs4IM2zIJz0cxeN9WQUrKSOASF41ehz8lbaDhSqkU_ZjHZw1Lmj7B_BZa_H4SlD4b0HYul-ZG9bKtncDZU-Wwwdv1qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار بالن هواشناسی خودمان توسط نگهبانان غیور!
آقایان صیدی و رضا عصمتی!
احمق‌ها کجای این شبیه پهپاد آمریکایی است؟!
هر چه میزنید ناموسا ۱۰۰ گرمش را برای ما بیاورید</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21457" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گویا حاج عباس پرینت خیلی مهمی در نیویورک داشته.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21456" target="_blank">📅 16:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مدودف:  هرگز روابط خود را با جمهوری اسلامی ایران فدا نخواهیم کرد، فارغ از اینکه چه کسی از ما بخواهد این کار را انجام دهیم.  ما شرکای راهبردی هستیم و برای همیشه نیز این‌گونه باقی خواهیم ماند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21455" target="_blank">📅 14:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مدودف:
هرگز روابط خود را با جمهوری اسلامی ایران فدا نخواهیم کرد، فارغ از اینکه چه کسی از ما بخواهد این کار را انجام دهیم.
ما شرکای راهبردی هستیم و برای همیشه نیز این‌گونه باقی خواهیم ماند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21454" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگوی ارتش ایران
گفت جنگ اخیر باعث شده تهران به این نتیجه برسد که باید
برد موشک‌های خود را افزایش دهد
و کار روی
سرعت و دقت موشک‌ها
نیز از هم‌اکنون آغاز شده است.
او گفت:
«در این جنگ به این نتیجه رسیدیم که
حتماً باید برد موشک‌هایمان را افزایش دهیم
و اکنون در همین مسیر حرکت کرده‌ایم.
نسل‌های آینده موشک‌های ما توانمندی‌های بیشتری خواهند داشت.
»
این مقام نظامی افزود که
دشمن اکنون در فاصله دورتری از سواحل ایران
و تا حدود
هزار کیلومتری
قرار دارد؛ بنابراین ایران به سامانه‌های
دوربردتر، از جمله موشک‌های کروز دوربرد
نیاز خواهد داشت.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21453" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21452">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21452" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21451">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mABwgRY-pS-eDVPo_sJb_Ie2eY9wFz1m08BzQZgl7G49Otz0mD6I0Ln2obCmMC3p6DN3Lx72stIhUpA4cuyhd2i9nsnfy6gFgsKojOODNR8uDOPV4S-FqzcDSrvHo4uuqw4kxqbxvnEabqfjUd5_8jGPvytgllbB2HX0HXzeZsNty28aPpprxpro5AIElEANNGLd6VJin-y41DTXhlAULyMsVpAP_zTyjUDGWOpjd8qTI1vQM0gxi94lj92IiDeE8TVZqJ4aKMH2iwX1iF8fvCKh4MKOwte1JiIGmX1E_gSrfa-zk1XiOFf3BMHk0yhVOcyVnCQi99BDeHzz8gES4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بار هم که شده فریب نخورید!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21451" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شما ولی قبول نکنید</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21450" target="_blank">📅 11:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21449">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قالیباف:   آمریکایی ها برخلاف حرفایشان در رسانه‌ها، از طریق میانجی ها پیشنهادهایی مطرح کرده اند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21449" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21448">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قالیباف:
آمریکایی ها برخلاف حرفایشان در رسانه‌ها، از طریق میانجی ها پیشنهادهایی مطرح کرده اند</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21448" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21447">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بفرمایید ؛  پست جدید ترامپ تو تروث:   «صبحِ شکوه: آیا ترامپ تو جنگ با ایران میره سراغ مدل کامل “شرمن”؟»</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21447" target="_blank">📅 09:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21446">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چون نمی خواهم به وحشت افکنی متهم بشوم، فقط به شما توصیه می کنم این قسمت را درنظر داشته باشید و خود بیاندیشید که در «شرایط کنونی» که کشور تحت محاصره است و چپ و راست اتهامات تروریسم و .... به ما می بندند و همسایگان عرب نیز از حملات موشکی و پهپادی و حوثی ها و…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21446" target="_blank">📅 09:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21445">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد  من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.  اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21445" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21444">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/partw-QdO3G62uq08KLkj25xA6KLB93l6CxGXRvLlOzcj0adwkGOuDImOBey-QjYoDYvZKv0Br93Cc7objhiOXdkTx9ZSFQPrq0Hif8K-aeiIcnBRj4vptIN7hdOd7GmGxj3P1Au9wI32j90DwWdxSmhroeWBknHq64YNkLUggFsParhd7qKVYWVx0YHgdmejb0mtuvjLzRJCYFgbtOZ_1110uZ1Psb7foOezRxRf_376FI1mHZcA04iY5cFeWr7MLwGuEqeTTKvQDPFIdGm_w4fL_y98gEyRno6srhESL0k7gifxLua5_NDzjvviwrJEYScv5t1z1u4C3Xla_uJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">report_onthe_nuclear_employment_strategy_of_the_united_states.pdf</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21444" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">report_onthe_nuclear_employment_strategy_of_the_united_states.pdf</div>
  <div class="tg-doc-extra">172.4 KB</div>
</div>
<a href="https://t.me/SBoxxx/21443" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این فیلم از این ماده چپول مزدور را ببینید تا بعدا بگویم چه توطئه ای در کار است</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21443" target="_blank">📅 09:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">توطئه در کار است؛
توطئه بزرگ در کار است؛
توطئه ها در کار است!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21442" target="_blank">📅 08:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21441">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد  من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.  اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21441" target="_blank">📅 08:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21440">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد
من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.
اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21440" target="_blank">📅 08:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21439">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">— وزیر دفاع بریتانیا:
«حکومت ایران نیت‌های خصمانه دارد و تهدیدی برای کشور ما و متحدان ما محسوب می‌شود.
تحقیقات در مورد پایگاه هوایی RAF Fairford ادامه دارد و چندین سرنخ در حال پیگیری است و این موضوع بسیار جدی است.
ما پس از رسیدن به نتیجه‌گیری قطعی در مورد RAF Fairford، به یک پاسخ مناسب فکر خواهیم کرد».</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21439" target="_blank">📅 00:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21438">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👨‍💻
کارشناس صداوسیما:
چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است
چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21438" target="_blank">📅 23:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">1-USA 2-PRC 3-N/A 4-IRI</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21437" target="_blank">📅 19:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21436">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">1-USA
2-PRC
3-N/A
4-IRI</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21436" target="_blank">📅 19:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21435">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهوری آذربایجان  : «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21435" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21434">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهوری آذربایجان
: «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21434" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ادعای بِسنت درباره ایران:
برای اولین بار در تاریخ، از زمانی که شروع به استخراج نفت کردند، این هفته هیچ نفت روی آب نخواهند داشت. آنها هیچ درآمدی نخواهند داشت.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21433" target="_blank">📅 18:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حملات سنگین حوثی ها به تاسیسات نفتی آرامکو در عربستان</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21432" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">— پلیس بریتانیا دو شهروند ایرانی به نام‌های رحمان صالحی، ۳۵ ساله، و سلام احمدیان، ۳۶ ساله را دستگیر کرده است که متهم به توطئه برای هدف قرار دادن جامعه یهودی در منطقه منچستر پیش از یوم کیپور هستند.
این دو نفر به «آماده‌سازی برای ارتکاب عمل تروریستی یا کمک به دیگری در ارتکاب عمل تروریستی» در منچستر، در تاریخ ۲۰ سپتامبر یا قبل از آن، متهم شده‌اند.</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21431" target="_blank">📅 08:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMgWUjpwJt3lA-sn69y-tndnszIEoB9gvYtLPBwCaFFpekuwmLzDQeJxxQwDf1ZaYFloV_Sw8P65JohUjZNKiN2K1yBx-vyQjUIX6CGHZitd24SU3mzhH_V3Oqq3zfRCGAYJhNOVpQNUhYEMK8NvRc2XJ6S1a1-xoZ6bvXHaZHJWVS2nLEnA_s3rPBWQ143cjhzjJFWttS2kocEPiVs6yBpEu7GI56cezV7Nl2rmi3dT8niZbvWaze-mKubRwqDKXurovkAO6Rv1ge1VGIKBs6VT1cv6HCivYr9ENjI9eLzXHgHK4L82UTEAXcom58WOY8en4L3JL1ysB1P5zWXJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SBoxxx/21430" target="_blank">📅 02:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ادعای جدید ترامپ:  یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود  به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.  ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SBoxxx/21429" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ادعای جدید ترامپ:
یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود
به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.
ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد و این "کارخانه‌های مواد مخدر و هسته‌ای" به‌شدت هدف قرار گرفتند.
بر اساس گزارش رسانه‌های آمریکا این نخستین بار است که ترامپ به طور مستقیم از "کارخانه‌های مواد مخدر" در ایران به‌عنوان یکی از اهداف حملات هوایی آمریکا نام می‌برد.</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SBoxxx/21428" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">«چرا جنگ می شود و چگونه؟!»</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نشست لایو لغو شد.  در یک پادکست مفصل، خواهم کوشید اوضاع را از دید خودم بررسی کنم.</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SBoxxx/21427" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حمله با سلاح سرد به یک روحانی در رشت؛ ضارب متواری است</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SBoxxx/21424" target="_blank">📅 16:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SBoxxx/21423" target="_blank">📅 15:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21422" target="_blank">📅 15:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=kYispceXx27fzIMUQs-jt7bre78uDCia7eTRvFmy6dsF0gRNeNjOhcYbnGOLdXPQV8os45PZxbDxeoSt5MHaWoxkj-3ZRt7fwOkfRtBni0LoW_rpv0NQPmqTWuoJr9o24NCLpSKQCUmMQ7SSrAwvCmbpFnPmQCWqSzs6wkY0h2bZPFi_1nNz0scKmpGs8bpvXFs-mAhDqkN9UVWJGor1sA4knMP04gBt9MK-UbPjs_fdahrAboRyFCBum3iz9XoH9eHdxHZ8vvZAqN8cqxsCgRpb_cLCFILCHdIzVmS-xPcM7D8YW2R2Gv5KDHk_KMtjohCi9KzITacUCrCzbpDYBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=kYispceXx27fzIMUQs-jt7bre78uDCia7eTRvFmy6dsF0gRNeNjOhcYbnGOLdXPQV8os45PZxbDxeoSt5MHaWoxkj-3ZRt7fwOkfRtBni0LoW_rpv0NQPmqTWuoJr9o24NCLpSKQCUmMQ7SSrAwvCmbpFnPmQCWqSzs6wkY0h2bZPFi_1nNz0scKmpGs8bpvXFs-mAhDqkN9UVWJGor1sA4knMP04gBt9MK-UbPjs_fdahrAboRyFCBum3iz9XoH9eHdxHZ8vvZAqN8cqxsCgRpb_cLCFILCHdIzVmS-xPcM7D8YW2R2Gv5KDHk_KMtjohCi9KzITacUCrCzbpDYBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21421" target="_blank">📅 15:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21420" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">واشنگتن پست:
وزارت جنگ آمریکا برای اعزام 20 هزار نیروی نظامی دیگر ارتش آمریکا به خاورمیانه آماده می‌شود.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/21419" target="_blank">📅 13:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صداوسیما:
درگیری مسلحانه سپاه با تروریست‌ها در راسک
برخی منابع از درگیری مسلحانه میان نیروهای امنیتی و عناصر گروهک تروریستی در یکی از روستاهای شهرستان راسک در جنوب سیستان‌ و بلوچستان خبر دادند.
نیروهای امنیتی در حال پاکسازی منطقه و بررسی اوضاع هستند.
تاکنون جزئیات بیشتری درباره وضعیت عناصر تروریستی منتشر نشده است.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/21418" target="_blank">📅 12:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpY4MlsnNEjD8HJFBklJvVZILDqrQnO5xnHM_8Zvc-Xa3jjimg4-sAYDCKTWUVXLFNOO1rhXW-Ip0z9KmKy5y4Yd-6q7T1h2TnsK9fgm9p-5L9_aSQdO-pl5j55GWQDTGaKoDiglvTsEPZv8L64pxmOdeojlKBxDWzasdsx9fQhvqHZARF0XLAj3EviBi7zrvwAMAxcKCfP59aXyMTworp6tcdnetH6NjJZLu39czdnby0X6aIlYaCpRbOXGdmywYNndGapX0fC8IyjWE_9agOtqGP6XBx6Q0pATKXc0KiHtATKjWAPGJuzX6qeiQQiF5lR1ijp8Onup4dtnhWLwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/21417" target="_blank">📅 11:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNBZpoFBldPjTh6ZmRTVPNE-1O0oc44AKh7YysHcGjSEj4dmgxyh1XMytapYrs-Xv1d43SZGqZ0P_NR9xj7NX38yYlOhmKP4rsr_ZBOksmcbTcH_risU9HYR50KftUvm5IHPC42pkWwaLg_yWD0XvyAqvqWgMFuaMGJ6x_aBa6LucchbXjZQN1YG7UOcs6Wq_hPO5crgV1g5kAy-_vAEI7cHGVM30VK6polRJm3IPkbSTE33NFEk1eqmXR7rKn7C0tbZI1nee7wCtOQ4VJ_lN6StFEcqeOyii0jKJeLB2p5IbtKobmI8Zd13bHT5t325z0Bfj-Bs_3UKdrS14xBG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC هم تغییر خاصی نسبت به پریروز و دیروز نداشته است چون عملاً قیمت همانجایی است که دیروز بوده</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21416" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taKYyFir39bZ3T9uUcU3s-8PZpzAEB6czGZvJWRkt1SwE601sPqpUCz99zw7YH4pdr0QxnPzHjCG-3IHeVPH0Ge-jIVmY2qCzWRW3xUx7iJnpk-CyF4Q9eSaX3qcek0kBV9LIf4K0tnQCU4aZ0gaIZ7p0Z8NRsDPlPH_sJlb9QAHlVKlACtjtwRhiBVZVLWjc7faUahtTNlyPKwutBGBVsivtYnPs681MQRC6WQqLNaTxb48yfU4-ZoG4J9UU6KQdOS73OAHLKX6jf-OSqyaLV1QA4wCmVK7tYAgKLH-MYIpiwglSkNXIKhONYHNtau_lTtqv90RZX3hf2qKvfWmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسط به بالا قرار دارد.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/21415" target="_blank">📅 11:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اگر دوباره به پایین برگشت، تنها روی محدوده دوم ۴۱۴۸ ورود مجاز است.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21414" target="_blank">📅 09:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SBoxxx/21413" target="_blank">📅 00:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21412" target="_blank">📅 00:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51530cf576.mp4?token=CTTtuih17bcEL_VmEEJLz5EHTKjj9T6IBhL26998E_-NWKcboXHqO9hCIO2kxmIE-zl-gegOD2Jta6iUw9L1Tg3FbSzvFfCB_RRd7LgblSQqgMkumoT7rE01oAl_pzME7dzPp__F4ZZntp4aRyInUnlpa7-TYhSHz_2T4p3gZUYOz_RjNNrWAEyhihBK88OR3eNyFyd_cq8b3RZLq8MyQWVfgb97TYY07zvS4aa1i7vj34Sk0AdnWj1R1NHu20EAhJ3ew8qzKuX09JsmNqBme7mQqljGDFNStPjMnEz2chBCLc4WrHU-3rcS6rGqf6oA82sFbQuKtLs9f743DhBVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51530cf576.mp4?token=CTTtuih17bcEL_VmEEJLz5EHTKjj9T6IBhL26998E_-NWKcboXHqO9hCIO2kxmIE-zl-gegOD2Jta6iUw9L1Tg3FbSzvFfCB_RRd7LgblSQqgMkumoT7rE01oAl_pzME7dzPp__F4ZZntp4aRyInUnlpa7-TYhSHz_2T4p3gZUYOz_RjNNrWAEyhihBK88OR3eNyFyd_cq8b3RZLq8MyQWVfgb97TYY07zvS4aa1i7vj34Sk0AdnWj1R1NHu20EAhJ3ew8qzKuX09JsmNqBme7mQqljGDFNStPjMnEz2chBCLc4WrHU-3rcS6rGqf6oA82sFbQuKtLs9f743DhBVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SBoxxx/21411" target="_blank">📅 00:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارشگر:
«آیا ایران در حادثه پایگاه هوایی فرفورد دخالت داشت؟»
ترامپ:
«به نظر می‌رسد که بله.»</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21410" target="_blank">📅 00:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ادعای وزیر خزانه‌داری آمریکا:
جمهوری اسلامی در یکماه گذشته حتی یک قطره نفت هم نفروخته است!</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21409" target="_blank">📅 23:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هدف قرار گرفتن شرکت آرامکو در شهر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21408" target="_blank">📅 23:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مقام ایرانی:
ادعاهای بلومبرگ در مورد پیشنهاد هسته‌ای ارائه شده توسط ایران به طرف آمریکایی در جریان گفتگوها با میانجی‌گران نادرست است</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21407" target="_blank">📅 23:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سوپرنفتکش ۲.۵ میلیون بشکه‌ای در تنگه هرمز هدف قرار گرفت</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/21406" target="_blank">📅 23:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
معاون وزیر ارتباطات
:
اگر استفاده از استارلینک گسترده شود ، در مواقع بحران مجبوریم تمام برق را قطع کنیم تا مودم های استارلینک هم از کار بیفتد؛ چراکه حکمرانی اینترنت را نخواهیم داشت</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21405" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مقامات ایالات متحده به الجزیره:  ناو هواپیمابر یو‌اس‌اس تئودور روزولت به همراه گروه ضربتی خود، پایگاه سن دیگو را ترک کرده و به سمت خاورمیانه در حرکت است.  تا پایان نوامبر، ۳ ناو هواپیمابر و ۲ گروه ویژه حملات آبی-خاکی در اطراف ایران مستقر خواهند شد.</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/21404" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:  به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SBoxxx/21403" target="_blank">📅 18:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ:
به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SBoxxx/21402" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SBoxxx/21401" target="_blank">📅 17:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تا نزدیکی محدوده دوم ورود آمد.  پوزیشن اول را اینجا با حدود ۲۰۰ پیپ سود تسویه کنید</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SBoxxx/21400" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#FairValueCurve  نمایه FVC تغییر خاصی نسبت به دیروز نداشته.  محدوده های مناسب خرید:  4165 4148  تارگت ها:  4187 4213</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21399" target="_blank">📅 15:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIFhLl34aXzoOMDhLR2XC-jtR3GMKOSDhvmxl8MvU0No2sEc9qDJUfdXIxH77sW_pqkazMYnY2CUkjWQbzsRF1FrKaR-TBXYeJ84JxTHAxMSfJBSYWmT_bpCZVktin3qhHadxzQqBCtjHcwBZt6div_Oy6mbptTeWSIiaKAPsB6csdmcjw3S_FzGC7zgMEnzwKExy6nA0Hbrpm0J6HZiffyS_Wnu6Atwmt8F1xMJ4O_q_qESEAcrLGrS2HvAEQaEmPCYFDA1xxPhgYv6T1tpC4uRmxzlrAZ72IeMg5O62Eb4f8cFGtLXoqyIM74VyGOaBDK9X8jE9IVQZyWvvIErkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیآمدهای نظامی امپراتوری ایلان ماسک</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21398" target="_blank">📅 14:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رویترز:
مقامات دولت سوریه و نمایندگان حزب‌الله در سپتامبر به‌صورت مخفیانه در ترکیه دیدار کردند که نخستین گفت‌وگوی حضوری شناخته‌شده میان این دو طرف پس از سقوط بشار اسد محسوب می‌شود.
این مذاکرات که با تسهیل‌گری نهادهای امنیتی و اطلاعاتی ترکیه انجام شد، بر کاهش تنش‌ها میان دمشق و حزب‌الله متمرکز بود.
سوریه به حزب‌الله اطمینان داد که برای تسلیح‌زدایی از این گروه، مداخله نظامی در لبنان نخواهد داشت، در حالی‌که از حزب‌الله خواست قاچاق سلاح از مرزها را متوقف کند و سلول‌های باقی‌مانده خود را در سوریه منحل سازد.
حزب‌الله تعهد کرد که در امور سوریه دخالت نکند، اما پاسخی مستقیم به این درخواست‌ها ارائه نداد. هیچ توافق نهایی‌ای حاصل نشد.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21397" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IMG_9826.PNG</div>
  <div class="tg-doc-extra">4.7 MB</div>
</div>
<a href="https://t.me/SBoxxx/21396" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali_SharifAzadeh – Podcast</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21396" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21395">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Podcast</div>
  <div class="tg-doc-extra">Ali_SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21395" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_445
🗓
October 1, 2026
✔️
تحلیل گزارش دیروز شاخص خرجکرد شخصی مصرف کننده
✔️
ارزیابی وضعیت تنشهای مربوط به ایران
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21395" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21394">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">درگیری مسلحانه نیروهای انتظامی با شبه نظامیان مسلح ناشناس که از صبح امروز در زاهدان شروع شده طبق اخبار تاکنون ادامه دارد</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21394" target="_blank">📅 10:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21393">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21393" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21392">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUHHfbqjQASuUbErepjBmZTvdHLv5K4omk_XdXF61wjlaXqRixEeSeND3DTLPO7QgHkMlVl4ue4AUTAlEp3wfHmQ7bo8bq2YeQekng8mTIV2kUYXLs76oGJgvtXBAMExaCKq6pethieb-lERaUDPK-XuO4jJclOqAUhWw4N_RWLxUdb7S2GGxeJ0mS_JNadh2T1v-9ZSPthwhayWWWlMxVsoeG0QYjVEPX9_3zMDBrapVUpgg29tGCTePiBJdOxIbKaMb5NkP-tvhN4emlZH0ODa_76u__3bH4byXa6Ege5AWieExmjjYZDxvMl6rd2aUNkjAXawzFVamxqUAOrMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC تغییر خاصی نسبت به دیروز نداشته.
محدوده های مناسب خرید:
4165
4148
تارگت ها:
4187
4213</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21392" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHiSYqCCWVDDZxhRojdoi6lnXkCCtnNJcUxqlv7E6rYmzfN0WP2iQhK9y48EiqsAszJTfMCgKTbidsCqMZKVkup6CdLNYruNVCrC6UyY9M3Hu9xBiI46pfjjY0S0J-VNuuaj5tJIUUGopMmCCi4lDKhxDYiwqkN7c4jaMhZ5whqfV4_ApyNDrRexE3Xrqzsk9LhBYyap40hhjwsmxLRkVVkZCYvh0rwK61L4xoUrL9v7LOGfV7Ebw-x5HRqoaixeZnzThMXGiyYAa1F-3LGrxY4cWX_kNe8bg219wiQgFbRux0tvfeR9fng3LMwKZ2IExJlhiGYBTqP63_sQZUtTzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در اصلاحی ها توصیه می شود.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21391" target="_blank">📅 10:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس:     روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21390" target="_blank">📅 10:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اکسیوس:
روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21389" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21388">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ادعای عجیب هگست وزیر دفاع آمریکا:
امروز دستور دادم ساختار عقیدتی سیاسی در ارتش آمریکا تشکیل شود!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21388" target="_blank">📅 09:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21387">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELPiSDzvLuBtdGWdgmdeAQDh9yIpUoNM9HG2HQE2HH5ajuDe0J191K39_q4us1ib9LuVvuaPNJnTwRLDOcA2SV9FJOB9hzk4WtnTGYwa7qguy5mmMUa9Mm0muUOrm2iJRshTbeXnT-xlNQuALhBLX8PWX_DyoPBArIMynrfx0mwen3vo9VbrwRIjkGER5HytSnDZS7WTsbZx_zcANvChH0zIXkdzusz7EDMaTABLC06SKcEiJUsPHfqegGkkn4XRzwIBKkVSvZ2jRRfgE1fkUSa7S4s23XcLEW0DMTFIETL4q8A54dzNgdchxcyOHRe6P0SyGJimuhoxCTdOYL02TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تحلیلی بر گزارش PCE دیروز
گزارش PCE در ظاهر Dovish بود؛ Core PCE به ۳٪ رسید و احتمال افزایش نرخ بهره کاهش یافت، اما تورم خدماتی همچنان چسبنده است.
مصرف قوی و پایداری Supercore نشان می‌دهد فدرال رزرو هنوز نمی‌تواند با اطمینان از موضع انقباضی فاصله بگیرد؛ بنابراین پیام PCE برای طلا کوتاه‌مدت Dovish است.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21387" target="_blank">📅 09:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21386">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ درباره ایران:
به‌زودی شاهد اتفاقاتی خواهید بود.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21386" target="_blank">📅 21:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umkBmorBrBNwz1xX4RxQGMTdbcAuGbdIMAO8CBbuLwJvWF5KR3IzdTv0RgDBQL0rLTSHcsZxLw9Q6Nfhmv_f8KvX3hET8jCu_aeSAOatYtl8D8RzesuFsL-m9np3Eh9c19Lv-DVf9gD-8bgeSxsFMuAqTbCSgSFwCCAxNkTqd4WUiIxro7rzAIKRr9QHofCVUmJ8ia9EAGnxlrnmqyI-EDzcIR9wrOhf7yjFv8n5wcNyBNioC9BQB-Uf-GmdlsT9QFFAxxVoo0nCx0ga_9IkXqxDjg0Qlq47rUzwTRgSSpPQva0vI3Vv1u6H_-npbpUxACLSZ7T9f_b0R2t7_O7f5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به توپوگرافی یمن دقت کنید!
آن مناطق کوهستانی در غرب این کشور، عمدتا دست حوثی ها است و از علل شکست سعودی ها و متحدینشان در ۱۰ سال کذشته بوده است</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21385" target="_blank">📅 21:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21384" target="_blank">📅 20:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21383">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
دبیرکل ناتو: اروپا باید به ایران حمله می‌کرد
دبیرکل ناتو بار دیگر از حمله نظامی علیه ایران حمایت کرد و گفت که به جای آمریکا، اروپا باید چنین حملاتی را انجام می‌داد.
روته در گفت‌وگو با یورونیوز مدعی شد: «صریح بگویم، اروپا ظرفیت آن را نداشت که توانایی هسته‌ای ایران را از بین ببرد. ما نمی‌توانستیم، ظرفیت آن را نداشتیم. در ۱۰  سال می‌توانیم و باید این کار را انجام دهیم.»
دبیرکل ناتو ادعا کرد: «این کار را نباید آمریکایی‌ها انجام دهند. ما باید آن را انجام دهیم. همچنین باید ما باشیم که به وضعیت حوثی‌ها (انصارالله) در دریای سرخ رسیدگی کنیم، نه آمریکایی‌ها.»
‎</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21383" target="_blank">📅 20:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWCtP_18_b0OIuXZrKg9q9cN646fny1DfUALXT4myINuSwTYDXQj0xGMgFAu1DPOjtKc64o0ik_gwYhK7dIcrEC6VWYmwdkNRCOS6GN1s7zeuyuKbe_nt-guRQqCvvFF7viSSNWqtSUZkxLSv4LYGUJNS9EIXbqgO6PUuWJexNg_zfnknS6yzBy3dCT5qkENI86TPwj9xbTzVH5DBCs3RZ7QGkkFB373G4YUC0jwxExVsX2Jf0TklLY6zWEAB2JhG8mpDpCmiofPjfLLok2bcka8DcqjuqwwxyZ-nk2RSoMIBamZKP-sxDeilWnJtXX4gULO1rZ-c1k0g7f1uyDjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21382" target="_blank">📅 19:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21381">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21381" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21380">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:  فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.  بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21380" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21379">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21379" target="_blank">📅 19:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21378">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حالا آنهایی که دلار را ریال کرده و در بورس بردند برای برگشت به دلار باید تا آخر پاییز صبر کنند!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21378" target="_blank">📅 19:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21377">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نامه بانک مرکزی به تمام صرافی های دیجیتال :   هر کاربر فقط روزانه اجازه خرید ۲۰۰۰ تتر را دارد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21377" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21376">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21376" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21375">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی خطاب به امارات:
میزبانی از قصاب غزه پیامد‌های مثبتی ندارد/ از جنگ اخیر درس بگیرید و از آغاز جنگ دست بردارید</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21375" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21374">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">— لحظاتی پیش پرتاب یک موشک بالستیک ضدکشتی از فارس، ایران انجام شد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21374" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21373">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21373" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21372">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به همراهان ما روی ۴۱۸۷ سیگنال سل داده شد و اکنون نزدیک حد سود نهایی در ۴۱۴۸ هستیم</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21372" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شکست جعلی که در سقف کانال روی داده، اتفاقاً فروشندگان قدرتمندتری را تحریک به ورود کرده است.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21371" target="_blank">📅 18:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn6Gnwn3scAzn2EiHNUw48JyayRzaOoRQX4yJQdRK6bT-7U4hM3m8qAmPwpqBv-ElloUtXtb2MBE1_IHxGHBobDgXPJMAHGK30PK75r8_Me-wFHJEhxw6bIjFLQSus3VkJUudtWCQyXjACf6MKMwop5fVYRslrhItnU2PmqmphxwmFqpM3z5jOfPKUknFQG2FoVaRJhZxMz5nBR-kvQ1E1wBVApzv-ow5LUR4ygN0cQe70cGXucjyhriwtN2UjJJtdzMe_7DtNtay6Xdhm6Fpr2afosa2oOEjfiz_uroI4ekxzJL38A4QOEhVD7ZDGdSOt_rlqwxQ0Rf8H1eUR0RNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21370" target="_blank">📅 18:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21369">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoKqbcdUAajqaAOuciI9H8414Nf05Xqs4kJ3-iRaWrGltVqPDqBF204vXpzYEraeCMSrVIuG-QxGX-uUlnp1lmNka4iPihe0LXRo8uv9MTG5aDTI9qthk5-6QM1iPcMAvNZLuMaFwl5AdcGaEvhkIFfan3fUosp89A28Cv8HgMlDxZVbeJcakNPyP3f4NimaFUIRB_zT053bKRoy87nSyUkg5eAE1_47yG_aDjJw3W3-u7ouxxUHf1RV41lW4FJ9lot-J83lXZ0R-Z9Ke5uRBnnW08-U55VfaJ4CHuNf2rdWdQpqwIaK6HreLxA-1v8e3Er7jDmS6vbJjE_iELsG2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول سناریوهای قیمتی</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21369" target="_blank">📅 18:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sunrun_RUN_Democratic_Congress_Scenario_2026_Revised.pdf</div>
  <div class="tg-doc-extra">84.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/21367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21367" target="_blank">📅 18:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/21366" target="_blank">📅 18:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=aN2lm4Mf8Oiur3DEJRmKqiyldNsdlT_WKhRFCWUuIH3vMkENCPFlKAGsEiG54rSmWOLvZWrQsOsT5gnt8vGhajYjOP3FsQ6bgGc9CZSIzadtoYoH8IvEp1kz7FQwgkaxI3qODZRoSyWs11JzqftNbTWNEuSrpVcu4hNClMITlggGE1DlHlafCfpOsXdaeygQBHE6GlzG-vG8dcm-NR_DOxHgfSThzzbQPjpK9wNMD9RyNNOWMO7gS_6tM0i5qBA-kF06iWxzvVY2bfTels58N-_n_VnnflDQIuY0j7vwnm5byShzWmLWFnEeJguh8GzMl48RPKYHFyzvMxFx7JwzhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=aN2lm4Mf8Oiur3DEJRmKqiyldNsdlT_WKhRFCWUuIH3vMkENCPFlKAGsEiG54rSmWOLvZWrQsOsT5gnt8vGhajYjOP3FsQ6bgGc9CZSIzadtoYoH8IvEp1kz7FQwgkaxI3qODZRoSyWs11JzqftNbTWNEuSrpVcu4hNClMITlggGE1DlHlafCfpOsXdaeygQBHE6GlzG-vG8dcm-NR_DOxHgfSThzzbQPjpK9wNMD9RyNNOWMO7gS_6tM0i5qBA-kF06iWxzvVY2bfTels58N-_n_VnnflDQIuY0j7vwnm5byShzWmLWFnEeJguh8GzMl48RPKYHFyzvMxFx7JwzhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی    این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21365" target="_blank">📅 18:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این چه پاییزی است که هنوز پایانش نرسیده!  نکبت ها تخمهای خودمان هم جوجه شد از بس که در بحران زیستیم!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21364" target="_blank">📅 17:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:   جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21363" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:
جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21362" target="_blank">📅 17:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21361" target="_blank">📅 17:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuI_CSTgQgcMAOjOPBcUKrY4ZEbDvox3u4HiUMbwZ5FFdf9A4Q-MZmx6k-jnpVQg4VEcaH9je0dT3KbM_JaxFhe0OtfjFd-OSYesBDB9CwdTCHVN20ayYOtvzdyPKMSD8B-_UzAOaMx105a0S70RNKGI4H-psEjKCCf_rlAtnSxhCko7IoLeK9LvL1RXmPvHJxU8rr5HiDd5dS-vPbbrgqLjqqOaLwsiuh8AlQMvCDTvkhZ2BwPoNAIBP53hmBOm5vOTmb-MQ-2Qb0oQrUV_ilVsBJaICOeiYoi15IKU9Us8BbSRcxHmzfYzXiOvzzUfrH3t22Snti3xUz1FjApj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21360" target="_blank">📅 14:51 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
