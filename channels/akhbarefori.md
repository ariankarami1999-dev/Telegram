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
<img src="https://cdn4.telesco.pe/file/kmqVdmv_W0POiirb7oTCLSt75G3UT-bHbk_Ek4AO566FNcRNq3KbQu7-HFZVIiFupW8mwzsROQJ0aQNxrsesJxYOaLfuH4GExlDV8Qk0SPtcFbDR37sT7p1sBT6GD5MWgFymVroJBtRA-ZFj3sTmWtERcAkWJ1YHmqd_qUQk1dDldrkXrj_VpJtVnpbf06ZmFKtO3OsB_qt4z-z2dxSGLGECp-3S0YgYnIVJlOGRbWM0BRbDCUJsG-N3lCLkcHkZZ0GMltNZRhiTINpLDIu0RThW4XVVfRzFLe_6kYHiAYzeJApr_8wyDzAHrkmrf2l1OaUYFypft3xSmW7umG9m-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 00:10:36</div>
<hr>

<div class="tg-post" id="msg-673924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سخنگوی هیأت رئیسه مجلس: دولت پذیرفته است که فعلاً هیچ‌گونه اصلاح قیمتی در حوزه بنزین انجام نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/673924" target="_blank">📅 00:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=jBGQKRoJoG_6qin37v2642rDK25Z8zmM_fu_j_GTc8JjgE3F3gBikOOiCy7vcVsbYeS5YeKnErXo7ARr2K-v0Wi1gDs8A0mSDw7yVUwdPUKzSV5E3ainyhhyyZncxjGCBxrPw3RuzEIqY_vIaUlwTrYpF5tcSYLHkE5eTu5T1KdIWb3rbFENqKKIQWGW4L-tH9hpP9TAtOsUwUFY2VyoyRg04H4BUUI28LVaGw8ovFqazFXQ5ZhlPdzFL_ZvtkkAx5EOYWIQD80jSCa021bT1A77REbOrk0s1JzFGwws6ONAoUKJCkVpu2Xz8xKMSjPn_2LGC5equ1I3SqoRlwHqkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=jBGQKRoJoG_6qin37v2642rDK25Z8zmM_fu_j_GTc8JjgE3F3gBikOOiCy7vcVsbYeS5YeKnErXo7ARr2K-v0Wi1gDs8A0mSDw7yVUwdPUKzSV5E3ainyhhyyZncxjGCBxrPw3RuzEIqY_vIaUlwTrYpF5tcSYLHkE5eTu5T1KdIWb3rbFENqKKIQWGW4L-tH9hpP9TAtOsUwUFY2VyoyRg04H4BUUI28LVaGw8ovFqazFXQ5ZhlPdzFL_ZvtkkAx5EOYWIQD80jSCa021bT1A77REbOrk0s1JzFGwws6ONAoUKJCkVpu2Xz8xKMSjPn_2LGC5equ1I3SqoRlwHqkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی خطاب به وزیر جنگ ترامپ: شما چندی پیش ادعا کردید که ایران کنترلی بر تنگهٔ هرمز ندارد. اگر این حرف درست بود، ایران چطور توانست هفتهٔ گذشته دوباره رفت‌وآمد کشتیرانی در تنگه را به حداقل ممکن برساند؟
🔹
ادعای مضحک وزیر جنگ ترامپ: ما مدت‌هاست که کنترل عبور و مرور از تنگه را در دست داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/673923" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=TPJrUgv8e6MNQgnUsZQW6gN_MRQp0vcF7WIkWRtEn_9Fn1Pesq7vphXpDz8UUkaddadzkHLVhL7ake4kTOFIv5lPuIcXc69FyX_z-2fNTxyhsjU5_pdVNLfRpDgDQpsv6HdIs7WqweVoHG0NUmzxdfi07lTNHOkSeragSQTNiwBiJ5n7ibQEE736wqk_xeYxlXK6kUecwUjbUFb9LNJKYuT7VbcbeVs3_xE4am7gSyI4I_IHIbCGbYeaklrXf08osrbyUa76eDnYBbnvGFdiJfx69S-XoikjDdxldJ0SbopCJozQhh5oeIhambv2ZVZDHWGdOVrZRRZoj6Kx3wHJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=TPJrUgv8e6MNQgnUsZQW6gN_MRQp0vcF7WIkWRtEn_9Fn1Pesq7vphXpDz8UUkaddadzkHLVhL7ake4kTOFIv5lPuIcXc69FyX_z-2fNTxyhsjU5_pdVNLfRpDgDQpsv6HdIs7WqweVoHG0NUmzxdfi07lTNHOkSeragSQTNiwBiJ5n7ibQEE736wqk_xeYxlXK6kUecwUjbUFb9LNJKYuT7VbcbeVs3_xE4am7gSyI4I_IHIbCGbYeaklrXf08osrbyUa76eDnYBbnvGFdiJfx69S-XoikjDdxldJ0SbopCJozQhh5oeIhambv2ZVZDHWGdOVrZRRZoj6Kx3wHJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: آیا توانایی نابود کردن آنچه را که زیر «کوه کلنگ» ایران قرار دارد داریم؟
🔹
وزیر جنگ ترامپ: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/673921" target="_blank">📅 00:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyzemymJEu5J9j1g_fq3obVsQKiOQdd48wk_R5b3mxFoq5qF8u6bfFDnd-OcY7UDWonnFMVbkT3gtRXqAzuixuohvxs5Y3vkQ9pGbcYzwDWCALo6brC-LKgiJ6aOWqWQ9jS_z8NDHw7as2U8bIlvff1xMDCVjnCqj65FXVJMqXDypL7m47bNJa7Ijt8cnom00b1A25R2EO-cte7BB1Dmoxh45NiHwDuRijYiK5SJ0KBmhqjH7UE5jNqxK-EukWhWEz22rODVHtvGZ9L81OmFJV4LAcL9NHKj9VC_dKlAMIPpSG7nTg8Nb3fAtgwYtdByCR6z6tqfXZe3AVzJG85ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/673920" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673919">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJr10TIUEogfrtitFSxUJfrUEazEIGe8GNAotXmBfkvJEQByN8f5-0SK08sMWdt8Rg3mBLu4buwdPkaaDigj4RrDUUBKJR-eW7mtO2zNoU35wLnxUZ-LvptwZmQCVCW8FDKKnyCNUQ_FbpOi01KIbcnHZJ0eniTNSVcAEPwf_HQdDDvjhhsV5EVV7qn7YbjLGQIJjx_jAPzh0LC0KbVLiJCv8ikXQnBxny1caz4GyLGDVs1sEhs4iwdPg-zittu3X9kwxsp2ZN3gJplVdtT5IDcawExBZ9-Q-RNrIjBsIMPgW8mcdiEmeNHtipMQSD5CbQvwUeZNMkFYR5QLcKpEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه ترامپ برای حمله زمینی به جنوب/ ایران با این سلاح ها آمریکا را شکست می دهد
🔹
نزدیکی ایران به محل استقرار نیروهای آمریکایی سبب می شود که توپخانه ایران فعال شود و ثمربخشی چندبرابری آن را تضمین می کند. توپخانه به دلیل نوع پرتاب توپ و نحوه عملکردش قابلیت رهگیری توسط پدافندهای دشمن را ندارد و به دلیل نزدیکی به محل استقرار دشمن (در جنوب) ضربات سنگینی می تواند به آمریکایی ها وارد کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3232047</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/673919" target="_blank">📅 23:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای پیت هگست: انهدام تمامی قایق‌های تندروی ایران، تمامی تیربارهای نصب‌شده بر روی این قایق‌ها یا تمامی موشک‌های کروز آنها امکان‌پذیر نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/673918" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای وزیر دفاع آمریکا: ما در حال حاضر محاصره‌ای مؤثر علیه تمام کشتی‌ها و بنادر ایران اعمال می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/673917" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfd4c9329.mp4?token=gsbrYDoJvCQrMAnyy4gELd9Ci0pc9IP0IN3LHnVVnMBg5njziVz3FE95nz0zyc8JAdiTQAe96YHyyXJ9UOSxrXnCrxKcgxebCPVuaC_Dcmggjr_TB4R9xvGb3qh9TVyfw9pyT3cBmZvf9iK88CoR3Xft_nm11AWbXj-tIjjWc5vSM0p-F6sMt2sDA34paTC5PKBxQynwUF7bbNfsLVq2T38DdW8iYr2pwzhdKDjGRl0cMQVMI5S27uP914yeTy1aca0I-VsEK5EwupCRuC0nWOQYKT5sljFZc_wKRhfoQPlqe4rPsbxNsp9lEObTPM5TUtRixEkvE7WBn6a2859XEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfd4c9329.mp4?token=gsbrYDoJvCQrMAnyy4gELd9Ci0pc9IP0IN3LHnVVnMBg5njziVz3FE95nz0zyc8JAdiTQAe96YHyyXJ9UOSxrXnCrxKcgxebCPVuaC_Dcmggjr_TB4R9xvGb3qh9TVyfw9pyT3cBmZvf9iK88CoR3Xft_nm11AWbXj-tIjjWc5vSM0p-F6sMt2sDA34paTC5PKBxQynwUF7bbNfsLVq2T38DdW8iYr2pwzhdKDjGRl0cMQVMI5S27uP914yeTy1aca0I-VsEK5EwupCRuC0nWOQYKT5sljFZc_wKRhfoQPlqe4rPsbxNsp9lEObTPM5TUtRixEkvE7WBn6a2859XEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطرۀ ایمان تاجیک، سخنگوی عملیات وعده صادق از دیدار با رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/673916" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سخنگوی ارتش: اجازه نزدیک‌شدن دشمن به مرزهای کشور را نمی‌دهیم / از زمان جنگ ۱۲ روزه برای احتمال حمله زمینی دشمن همواره آمادگی داشته‌ایم
🔹
اگر جنگ به روی زمین کشیده شود، نبرد چشم در چشم خواهد شد و به دلیل ناآشنایی دشمن با جغرافیای منطقه آسیب‌پذیری آن‌ها به شدت افزایش خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/673915" target="_blank">📅 23:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673914">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: جنگ با ایران تا کنون ۳۷.۵ میلیارد دلار هزینه داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/673914" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673913">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=R5-trgeH_F0p5pFlCozucFODMwbkuTA9qIpnkDT7qdyf9QFGKT8aw754ykr_mpzvOuphlP7H1DNnJc7IEhMnP-oxe8Fln5cDL3bD1mS7khywsxYp9hbr0lNzXfIcjGUfEI9t9hgE9vvuR-6Y4IggkUaglXJAyvmX7NjnxNGRiQLOMHZztDxXuYZCtcBttfjYcUC7wfZI6eCKBXCB8h9c8ets3kgTa5pmJM4YkF70edb3SY_HBHUnUt0Ib89HuM1C3i99Ki4g-N_cwkpNLW1jmo5euyGYiStv0THTnQkv7LIBqmKa5ikqoVPmHv_uPck-HIb6Mer2_J4EGKUMnuPVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=R5-trgeH_F0p5pFlCozucFODMwbkuTA9qIpnkDT7qdyf9QFGKT8aw754ykr_mpzvOuphlP7H1DNnJc7IEhMnP-oxe8Fln5cDL3bD1mS7khywsxYp9hbr0lNzXfIcjGUfEI9t9hgE9vvuR-6Y4IggkUaglXJAyvmX7NjnxNGRiQLOMHZztDxXuYZCtcBttfjYcUC7wfZI6eCKBXCB8h9c8ets3kgTa5pmJM4YkF70edb3SY_HBHUnUt0Ib89HuM1C3i99Ki4g-N_cwkpNLW1jmo5euyGYiStv0THTnQkv7LIBqmKa5ikqoVPmHv_uPck-HIb6Mer2_J4EGKUMnuPVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌پردۀ فراخوانی که به‌ اسم انقلابی‌ها منتشر شد چه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/673913" target="_blank">📅 23:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb25034032.mp4?token=hkM75rGSxeZEcs_IBE3yGNdi2AHChgJiAUxQxBpaJ1n-AvVRBDXdGBFyIV08exIv1zVCzBINsDegGkTFaZXNuSepcAL9Qyk4XZ-o4UfZv3j-2OiupeioUDJoiQYMx7V-yW3W7lJEQutQQf5aej4ep0BIbpWo0am_FO7NNsJxpjfb2iRrKdzXNTH5GryuLF60dmQx0Oc2IoAcn-B5dZs2yLWLALMMMNM3ax4RYoeSnksk7m8n1nNeECGXiS0LrF_1zZ04W6l3TeiQYttfwxYLnVVyc4LjZ0u2qFWMIWkzTK0JAM2EQ5mJIyxyn9CR5haL8hM0NYoDeZEM8guL-FX35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb25034032.mp4?token=hkM75rGSxeZEcs_IBE3yGNdi2AHChgJiAUxQxBpaJ1n-AvVRBDXdGBFyIV08exIv1zVCzBINsDegGkTFaZXNuSepcAL9Qyk4XZ-o4UfZv3j-2OiupeioUDJoiQYMx7V-yW3W7lJEQutQQf5aej4ep0BIbpWo0am_FO7NNsJxpjfb2iRrKdzXNTH5GryuLF60dmQx0Oc2IoAcn-B5dZs2yLWLALMMMNM3ax4RYoeSnksk7m8n1nNeECGXiS0LrF_1zZ04W6l3TeiQYttfwxYLnVVyc4LjZ0u2qFWMIWkzTK0JAM2EQ5mJIyxyn9CR5haL8hM0NYoDeZEM8guL-FX35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضدجنگ در جلسهٔ سنا، سخنان پیت هگزت را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/673912" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlijnJ8EW09oJsobnvM7g_Z4hpLPPi4E7K5egDIZzHu104XYb0wsuoSrwf34yWFt1Bsw1gqHOJWuleakiWm8xZ3m83MpKKXvcTX06L0qhadvuh5byUMifJXW4wUUmvpxSWYKaE9uFtB9V6Pk1Cj6zkP5zBlKueU5L1v5FxM7wt4Y3a6XfuhFeAjXO0Fg5AgKB69luhpVaBbttTObaQRmwomRqDR03iIwD-Nn07DRboDNOs8AfXDw9Xfxfuck8Huaa6AxaHIVVHI9oGOqFxbLCHZ6dSiCSExAAYQFktY8_2yN2QLX6QgStLzSoRGNxMXhr37baE01a1gQ4DRXPLlVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار: ۱۸ آمریکایی در جنگ علیه ایران کشته شد
🔹
جنگ افغانستان: ۲۰ سال، ۲۰۰۰ کشته
🔹
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
🔹
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔹
جنگ کره: ۳ سال و یک ماه، ۳۶۵۷۴ کشته.
🔹
جنگ ونزوئلا: ۱ روز، ۰ کشته.
🔹
درگیری نظامی ایران: ۴ ماه، ۱۸ کشته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/673911" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3ahwWr2Q0pjXDsnYu-6P2qghDfRB5b16fuHeGET3mn1Zp0QDxKEVFe7e6tyZobWZ-9JliFyaHGFvpkallfOuH9EV840PYc1ax_hC2jOOG1o6WnvWh5qWg5R9Tefxcux20nZUg3exzl518Wj-EbgYp58xCHNEUklTFMzbm1cknBR4S52MPqIeQ37X4YNvrGUOB0k48rfOGzoFREQKZvkAZ6khaTEEvdMTTt67smITLHI2tViee1Vfp6Cco3fqteL5F2SHHMwXWYzsy6TuhhAQYmm47pS05MOXgJUmk_F2sGkX4zq4bo8hWHTe5hPA2UpUVa4xS2Bb_JHjB9LCm3qlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام معنادار امارات در روزهای اخیر: اقامت برخی ایرانیان در امارات دوباره فعال شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/673910" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
خوک نجس: پرواز‌های مستقیم شرکت‌های هواپیمایی آمریکا به لبنان از سر گرفته می‌شود.
🔹
وزیر جنگ آمریکا: اقرار میکنم که ایرانی‌ها هنوز هم توانایی‌هایی دارند.
🔹
الجزیره: آمریکا در حملات پی در پی به ایران دستاوردی نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/673909" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNEgdx5Xn2-CnvuyPPigT-z6RekhF0fWTZS3hzLBh-ZhM6JDmJcA-XhaWqtu_CCqVPu_DyNnbb6mm2rJwzyoquXPrD73yZ-1b9cL1DaF10BxbX1EGf6pC9NyJqjuYKF-ax2miO84SFUQyO-O_x0U64GYMljdRlvHDOqgcpxfkcwcQhMcYadVZ8MfsgTJ2ivNeaLJ5g0n2DcFLXXxorQ6eud6rsmTIX8zzHTm0XShU7XocO1UuB4nPFdPzU33JA08NfSdQOheax9BWAT_IIvNNhn9Um_rKiLJjsieSv96Q9LNyi0o9wJY3borcLM4kd5n_Fh67O-_NoASC3JU7OB7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ اپلیکیشن هوشمند؛ برای یک گوشی حرفه‌ای تر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/673908" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0add65574.mp4?token=H2-5cxk2APYmBKBbyss3zIm-gFNbsDHgke0cYd0ar1mKY0am_WOHf5TuUSLUtMUSJ-BYhewGOkg4REjWWLmnMs48KOoJGeoVGqP7NIdernr-hqrTp75BhCkLmBRR5YojtI8_tdsdvk-7Q-iqKv9UB0FbqI3S3SWrYY3bkwkSxVFMOBgwKrmKCFshrm6NH3rAG__TRliSdwWfdbobd9DwVYzPg8E8YqkK7nypALlQyXHBDLr_fUt7zf8z1pFy_MM5Ck8NklSA16ixuN9xhXyCACZ3eNVPAWIQpiQ3FHp1oq0xBTtL6sNGoUjgPAlI6g45stxQPz-aYClTSZwslkQPcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0add65574.mp4?token=H2-5cxk2APYmBKBbyss3zIm-gFNbsDHgke0cYd0ar1mKY0am_WOHf5TuUSLUtMUSJ-BYhewGOkg4REjWWLmnMs48KOoJGeoVGqP7NIdernr-hqrTp75BhCkLmBRR5YojtI8_tdsdvk-7Q-iqKv9UB0FbqI3S3SWrYY3bkwkSxVFMOBgwKrmKCFshrm6NH3rAG__TRliSdwWfdbobd9DwVYzPg8E8YqkK7nypALlQyXHBDLr_fUt7zf8z1pFy_MM5Ck8NklSA16ixuN9xhXyCACZ3eNVPAWIQpiQ3FHp1oq0xBTtL6sNGoUjgPAlI6g45stxQPz-aYClTSZwslkQPcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس مسائل استراتژیک: نقد‌هایمان را «مشفقانه» بگوییم؛ باید از شخصیت «عراقچی» و «قالیباف» حفاظت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/673907" target="_blank">📅 23:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تغییر ساعت ۱۵۰۰ مگاوات در برق صرفه‌جویی می‌کند
سیدجواد حسینی‌کیا، نایب رئیس اول کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از ظرفیت‌های عملیاتی برای کمک به ناترازی انرژی در شرایط فعلی، بازگشت به تغییر ساعت است. برآوردهای کارشناسی نشان می‌دهد که این اقدام حدود ۱۵۰۰ مگاوات در مدیریت بار شبکه تاثیر مثبت خواهد داشت.
🔹
طرح پیشنهادی در این زمینه تدوین شده است و امیدواریم در نوبت رسیدگی قرار گرفته و به مرحله اجرا برسد.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/673906" target="_blank">📅 23:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVIPu3P6VQyX0zq7QY88n1yCaxslyCTkt1xp3W9oigZ_ouYkg16bOXqrn6vzaLN8ERp1z4Iekzy-xsVB1xKbVuNHNObzqrFnkK_HdRK7NZwAmKcgv5sd-m6YgxAtB3QN_ceCxbizYO3x4eEjQszaNCIbRdXHBmObX4JZuWUQ_PyJrr_MZMSW5e9yX0xMDZhrIevrXrp8FR1Fn3f7dSPSwS-upTAxZhBe6HQ3EndXHzcYkf-XAX1E26qgl6E07bBpaGw4MfDC56IGD-AExzXgRV-IXG3H0GWI67KOnGbsKF5D3EGgU40bKpjeJeZqgMM5TKQgKy0uJL2gkqwe2TSzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر جدید بریتانیا استفاده ایالات متحده از خاک بریتانیا برای انجام حملات بمب افکن به ایران را تایید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/673905" target="_blank">📅 22:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673904">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۰/ هلاکت تعدادی سرباز در هدف قرار گرفتن مجتمع محل استقرار نیروهای ارتش تروریست و کودک‌کش آمریکا در منطقه‌ی الرُکبان اردن   روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت بصیر و همیشه در صحنه ایران اسلامی،  با دعای خیر شما عملیات تنبیهی رزمندگان…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/673904" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673902">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpFZFzII_KPcGRmPesVkAlxWdqKwHlThYovMN6RVvcvIa7-VGmOcBHPMI4rxmh-NOZUEUIzIc9hGEupSsitLBJ7vJ6J4ZKXNa75-R2Cmhwvt-17njcDlFJ9x-V_ja8O0aPtPmdXTCHdedewvW75mBADuhosExrVvIbfy_HrcjTZBOegp3NZ4rIrnb5Y287UwJqiy9IsU3uizKqUv2iYLtJ76P0DzNIvM75XKZZMw-3Sr_ESjvLyYMsdXrzsW5KpCmo0RfmGjweQodiB8OkK_Zjyv5qlk5uJj3RcaTPt03kRwI9pTZBBgsVESoZF4kvG6ahCXhOQQ1ehMlL6ynljjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عدالت از منظر امام علی (ع) چیست؟
🔹
از نگاه امام علی(ع)، عدالت تنها اجرای قانون نیست؛ هنر و توانایی فهم درست موضوع، دانایی عمیق بر قوانین، داوری شفاف و بردباری است. کسی که حقیقت را درست نشناسد یا در برابر فشارها آرامش خود را از دست بدهد، هرگز نمی‌تواند…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/673902" target="_blank">📅 22:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673901">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تحلیل جنجالی مصطفی خوش‌چشم از تصویر مقاله ظریف در نشریه فارن افرز: تصویر می‌گوید موشک را بده تا بتوانی نان بخوری
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/673901" target="_blank">📅 22:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673900">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71aa646a5e.mp4?token=Vnr38bAOu-LJ0GEg8-E4nO394OULhQjleJT9ctOSHtcIYbowtV0YkPpmjpJBScBo2VqMrlkvCZuibv89yIuT31NKGVvt9zStPpktnB_OnCBpit_I5-z0_WU-nzHjTWU2yNJCqHDI3xgzpH4cX_9Mdd6TQv6qdMiUfPZbN3sLYWrJsxWrYKMnBC3TvvFND9xTAvV4O-iK0daEDsnZBLGYNmZktrMho0AraUk5ByaxyLoXkligplIZZywPSbuFDOdueBy4zZ8d2VqYrIq2FfMuGMc_rBSM69ruobJj1OdNa7E0kJrEDqadtMHxb9iU5ltkyVdgJYeK-BiYnVPc0ubrDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71aa646a5e.mp4?token=Vnr38bAOu-LJ0GEg8-E4nO394OULhQjleJT9ctOSHtcIYbowtV0YkPpmjpJBScBo2VqMrlkvCZuibv89yIuT31NKGVvt9zStPpktnB_OnCBpit_I5-z0_WU-nzHjTWU2yNJCqHDI3xgzpH4cX_9Mdd6TQv6qdMiUfPZbN3sLYWrJsxWrYKMnBC3TvvFND9xTAvV4O-iK0daEDsnZBLGYNmZktrMho0AraUk5ByaxyLoXkligplIZZywPSbuFDOdueBy4zZ8d2VqYrIq2FfMuGMc_rBSM69ruobJj1OdNa7E0kJrEDqadtMHxb9iU5ltkyVdgJYeK-BiYnVPc0ubrDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که یک ایستگاه پشتیبانی زمینی و یک مرکز تعمیر و نگهداری مربوط به یک بالن شناسایی آمریکایی در فرودگاه اربیل در شمال عراق، مورد اصابت قرار گرفته است
🔹
به نظر می‌رسد پهپاد با دقت هدف خود را مورد اصابت قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/673900" target="_blank">📅 22:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673899">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d504030f.mp4?token=JhPQA3xIIA33zWnZPXlZqB0-QX_fBGR-WSiGtOobUjQq36ZTTNEK9yq7N2ZSXl3zddgAG3WspyWQF452HcPd0jA3HJWf3E2fqWtHCjJeagpAmUYSPSGEgk95xicRiJyB7vcFLgR9Tpa1H4AN0w3bcWin-hsvo5Q_vT9qAWXQH_XfKhIi52yGUlZtixX7o2VyeBfPa-5kf49SUIgFtR7Y0fKmJmB8aHym7E5qBRJhgcl7r0ySa8siI19u2_zhVsqLMl4pBsvFLuQY1AdXf_lAMmWVn_hxzEjkxNZu_087BQVT4RDsGesPpNE7pB2xTa-8DbgdaTVsBTdOQEuK8DvW04diFmJWwddu4W62ywcy7rjzQ5XELYnUykU6dLzpxf_AWmStOcdbzp2plhsUmWOcIK-j-14DjBXv_OPn-_fjGY5LtAI4ZAl-ZMet3ol4yBHmVqLSPtxYCBAEdvvz0qstMmXYDRzsStPHvoA2eQZ5mP5UkseFKMhE_eKTGL_4FAM8SrfJ8HbN1Uh7hxohQRDcOHWhIFfzhAalZq0zvGfKUgvJpezZkjMFaUenYPZS_ZwqLoBcPVZ3dlv4BkBAXrT8QkYO0ztVEehfpbuqbq2MkDuO0gqGn5iES3pSWpVw76f1oeLurTonzjZ8AC9zVzrdT1hDEooBhJMWZQmYyC7vH84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d504030f.mp4?token=JhPQA3xIIA33zWnZPXlZqB0-QX_fBGR-WSiGtOobUjQq36ZTTNEK9yq7N2ZSXl3zddgAG3WspyWQF452HcPd0jA3HJWf3E2fqWtHCjJeagpAmUYSPSGEgk95xicRiJyB7vcFLgR9Tpa1H4AN0w3bcWin-hsvo5Q_vT9qAWXQH_XfKhIi52yGUlZtixX7o2VyeBfPa-5kf49SUIgFtR7Y0fKmJmB8aHym7E5qBRJhgcl7r0ySa8siI19u2_zhVsqLMl4pBsvFLuQY1AdXf_lAMmWVn_hxzEjkxNZu_087BQVT4RDsGesPpNE7pB2xTa-8DbgdaTVsBTdOQEuK8DvW04diFmJWwddu4W62ywcy7rjzQ5XELYnUykU6dLzpxf_AWmStOcdbzp2plhsUmWOcIK-j-14DjBXv_OPn-_fjGY5LtAI4ZAl-ZMet3ol4yBHmVqLSPtxYCBAEdvvz0qstMmXYDRzsStPHvoA2eQZ5mP5UkseFKMhE_eKTGL_4FAM8SrfJ8HbN1Uh7hxohQRDcOHWhIFfzhAalZq0zvGfKUgvJpezZkjMFaUenYPZS_ZwqLoBcPVZ3dlv4BkBAXrT8QkYO0ztVEehfpbuqbq2MkDuO0gqGn5iES3pSWpVw76f1oeLurTonzjZ8AC9zVzrdT1hDEooBhJMWZQmYyC7vH84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشورهای عربی دست از پا خطا نکنند!
🔹
کشورهای حاشیه خلیج‌فارس معضل بسیار بزرگی دارند که اگر همراهی آنها با آمریکا ادامه داشته باشد، شاید ایران ناچار به یک تصمیم مهلک برای آنها شود.
🔹
ماجرا چیست؟ در این ویدیو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/673899" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673898">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
آتش‌سوزی در ارتفاعات دراک شیراز
رئیس سازمان آتش‌نشانی و خدمات ایمنی شهرداری شیراز:
🔹
آتش‌سوزی در ارتفاعات دراک رخ داده است.
🔹
در حال حاضر ۹ ایستگاه و تیم‌های عملیاتی آتش‌نشانی به محل حادثه اعزام شده‌اند.
🔹
اخبار تکمیلی درباره ابعاد حادثه و روند عملیات متعاقباً اعلام خواهد شد.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/673898" target="_blank">📅 22:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673896">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326e59136a.mp4?token=OCl9F8eqcnpCryjCTzMxxGOtWUsbIvPTdtVc6E4vUcWvyTzpzHAMLdOmbZOrrjh9WtnhJ_KPYCohf87fWI7nbEYcV0h8OeavTcruSKkx1FSvEJxQ8zORf-9uymRY3-kFGw1M-1ZLrilK-_JYigulRh-eaaZvueYGGAcaizzONoDfLug6QjXb5bQF_bCQLf7lxwJ6__zyhRYjrSlcSiSP3aiE-OCVgyOuFaWKUaDc7TzL1sbYpj8qWILeilH4D0sdzka6vjdU7L-PWOpLNNArryCQ9f1_cGEPIMe-MDkT0UtjDCMr88zSb8J2AwPdJlAC61EtKdrNVW6j_meHaGRISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326e59136a.mp4?token=OCl9F8eqcnpCryjCTzMxxGOtWUsbIvPTdtVc6E4vUcWvyTzpzHAMLdOmbZOrrjh9WtnhJ_KPYCohf87fWI7nbEYcV0h8OeavTcruSKkx1FSvEJxQ8zORf-9uymRY3-kFGw1M-1ZLrilK-_JYigulRh-eaaZvueYGGAcaizzONoDfLug6QjXb5bQF_bCQLf7lxwJ6__zyhRYjrSlcSiSP3aiE-OCVgyOuFaWKUaDc7TzL1sbYpj8qWILeilH4D0sdzka6vjdU7L-PWOpLNNArryCQ9f1_cGEPIMe-MDkT0UtjDCMr88zSb8J2AwPdJlAC61EtKdrNVW6j_meHaGRISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسربچه دوست‌داشتنی فینال
جام جهانی فوتبال
🔹
شیطونی‌های برادر یامال در جشن شادی اسپانیا پس از برتری مقابل آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/673896" target="_blank">📅 22:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673895">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
کویت سفیر ایران را احضار کرد
🔹
وزارت امور خارجه کویت ادعا کرد نفتکش «کیفان» عصر دوشنبه هنگام عبور از تنگه هرمز هدف قرار گرفته و در پی این حادثه چند نفر از خدمه آن زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/673895" target="_blank">📅 22:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673894">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
رسانه عبری: الجولانی برای عملیات علیه حزب‌الله آماده می‌شود
شبکه صهیونیستی «کان»:
🔹
با وجود اینکه مقامات دولت انتقالی دمشق به صورت علنی از مخالفت خود با ورود به مساله لبنان سخن می‌گویند، اما در عمل دمشق در حال آماده شدن برای انجام عملیات علیه حزب‌الله است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/673894" target="_blank">📅 22:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673892">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR-KiskaLIVsA3zL5RUbKxAtrj3DiJtiQOn6VNNG1s3sJQTG2aWIDLz1-uR2XSw7_4AB4bpwyVEL6Qt_VPQdEL7PL1FEmeUHNp-YBcqj6_ILkvn87od7ZOVojo51psuOTW47TkxwucAcG9VHdkj8y19OUN7g4sOofjqCiYrtMJNS1DltdAnkJvqERBl96uUO48ZVJAWbv3hlvGO3srtCaZ8myCgxusA07GtcvkqN5dyU0gn0KLXFbI5zD2B1gslPgFP3tHCbdYtmRo4BkUbnbuOQPuzyipaOPLvVQNjBMbG0m-Z33Tf6_rCeJxUmOddCmTgH22OXp5AXVfYYXc1xmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزبانی از دشمنان ایران و همدستی با آنها، نشانه ناسپاسی و فقدان آینده‌نگری است
سخنگوی وزارت خارجه با انتشار عکسی تاریخی از سال ۱۹۹۱ یادآور شد:
🔹
ایران در سال ۱۹۹۱ با وجود حمایت کویت از صدام در جنگ تحمیلی، به درخواست این کشور، تیمی ۴۷ نفره از متخصصان خود را برای خاموش کردن ۲۸ حلقه چاه نفت در میدان برقان اعزام کرد؛ عملیاتی که به‌عنوان یکی از بزرگ‌ترین مهار آتش‌های نفتی در تاریخ ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/673892" target="_blank">📅 22:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673891">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
بازسازی زیر سایه تهدید؛ فرزانه صادق در کنار کارکنانی که خدمت را تعطیل نکردند
🔹
فرزانه صادق، وزیر راه و شهرسازی، در جریان بازدید میدانی از محل آسیب‌دیده راه‌آهن بندرعباس، در کنار کارکنانی حاضر شد که در شرایطی دشوار، هم‌زمان با تهدید حملات مجدد، حضور پهپادهای دشمن و گرمای بیش از ۵۰ درجه، مشغول بازسازی خط ریلی بودند.
🔹
این تلاش بی‌وقفه، زمینه ازسرگیری خدمات جابه‌جایی مسافران از ۲۷ تیرماه را فراهم کرد. خدمت، حتی در روزهای سخت، ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/673891" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673890">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBDJH2dMtIFUwPXrGrU8NXB84O1S2PvVAJPtQH-dAK8vW-7QsJuxHsPUW4wiG4AIC9SJslM4cKQNPnl0rUtQAJHWddjvSyCiKjcQtvuNjUPUoJV_8J_Gs0J7EW4fLxvnOi1Bhb4rVTaL87r9Z8cVpKAqYnhCE_mezwp5ihcZFThsOcev0Xl6ksMiQEZ6P0db5e_BDzRv97abZKfBEYJlTAR4WYwCih4ror0AZoRZMXCnTwD91K95L4k3WjFUK0Y8ZAxcQDN8OQKr_C_Fl8wZ6I-h_l7yx0Dv5U7_B1_mND1aB5Vh61f8tNdntTRjod5ACjrbWZQ4k8VC_6VQhSaCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام چند هواگرد متخاصم در ارتفاعات شیراز با سامانه نوین پدافند هوایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/673890" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673889">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
نتانیاهوی خبیث، دقایقی پیش، از عون و سلام، چاکران درگاه ترامپ در بیروت، اینطور تشکر کرد: از دولت لبنان بابت شجاعتی که نشان داد، تشکر می‌کنم #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/673889" target="_blank">📅 22:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673888">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNJsSsAgiVQpU_SCGWJGmtmBA5UxQ0Du3yN--4j0o4hl1ehFGRswl3th7yq4CEB2ZDmG1Wt243EaegfUEwOGXaoCdv2RvFcFshkLdOEtD0WPM1PJKHNllFnauLmfbb9uMlq-nIbqW4opFGRm-Z1pS0dlrklTcQobnqXMlrbwZYUVX286uvbChQ2mDq_ZoMZW6W5Xdrdq7P49JetdmWdscbzSxCDrS0cct6A1-lZx3R00K40WI4QmxoS4P2-k_TP0EVfWGGJY438Q1wzLW4qw6V0eqdAV6csnA7TBIuB-vayEZP4RyDgCryJRlf_br04UrixK2hkzv-aJ_da0x57Lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب؛ غول درآمدزای ویدئو
🔹
درآمد جهانی یوتیوب از ۱۵.۱ میلیارد دلار در سال ۲۰۱۹ به ۴۰.۳ میلیارد دلار در سال ۲۰۲۵ رسیده و در کمتر از هفت سال حدود ۲.۷ برابر شده است.
🔹
بیشترین جهش درآمد یوتیوب در این دوره، بین ۲۰۲۳ تا ۲۰۲۴ رخ داده و درآمد این پلتفرم از ۳۱.۵ به ۳۶.۱ میلیارد دلار افزایش یافته است.
🔹
بخش عمده درآمد یوتیوب از تبلیغات تأمین می‌شود و با رشد تولید محتوا، افزایش کاربران و توسعه سرویس‌هایی مانند YouTube Premium، درآمد این پلتفرم طی سال‌های اخیر روندی صعودی داشته است.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/673888" target="_blank">📅 21:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673887">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع: منطقه‌ای که در بحرین هدف قرار گرفته، محل حضور نظامیان آمریکایی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/673887" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673886">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb76U0BxJsuA1NWxZw8xZnm5m3xuNpzyqBmH3jWg_gkXO8GXCvnsdopp-7WYJKQE7JLmpCODfSqPJbxJVhcGwbVaJ8W4hX652wY2Un-ky8fgMuBReSYCCHF62qvqzcU-Cn8us9HzF7eiYJFiB828FjHwtrtepaNZyNdHTNDx9lXOa9aAkMKyINYS84zTg47N63vh4Sjx73jzqYucDYxTgly30Q9u7lHLqIT0GLvBGZQoIDnTn2bQCeJcSiRKUEY3-l3vsu4FS4CLsYrxGBfTHBhHo_3rQqlSxnv_PfRi70vTTj7hORCMt00FLEJK3G7nVqwxwu67OCa_Chw2xvpubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱.۵ میلیارد دلار سوخت‌رسان آمریکایی در تیررس ایران
🔹
حملات هوایی ایران به پایگاه‌های آمریکا در منطقه باعث کوچ زیرساخت نظامی این کشور به اسرائیل شد.
🔹
تصاویر ماهواره‌ای نشان می‌دهد، حداقل ۲۴ هواپیمای سوخت‌رسان آمریکایی در فرودگاه رامون ایلات اسرائیل پارک شده‌است.
🔹
ایران در طول جنگ ۱۲ روزه و ۴۰ روزه بارها منطقه ایلات را هدف حمله قرار داده است.
🔹
هر سوخت‌رسان آمریکایی ۶۵ میلیون دلار ارش دارد و تنها یک باند فرودگاه رامون ۱.۵ میلیارد دلار تجهیزات در خود جای داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673886" target="_blank">📅 21:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673885">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbe7bed94.mp4?token=AyvINQ_upuJBPiDxc3kEIc_gR6y11pQfPWeyDLfaHcT4x1dy_tB6VncDZRGzC4nEkl0LM5-qVYvZEL5J_AazbMsq2d-EkKZIZz1WZb9U74KOAI26IklZGwul9pRZTPatV76p0Vyl_9hjhWk7LqwDLkb11gcqoQBsswmdzVqHXe8yZCOes5OIkYQ_04qAdkT4q6xqmTA6GjTe7Cp5nT1gIYus7pNrWgP8wr8jlCqvCKDI37igTV7xImEn-B2ujo6CCOw9I-8RjwpyrURI18MUyAzBF4JDmsvFa83KUZpKI_UUfY48FEjPlb3ZPmZLE3xz_lBeaUVPQp8v6POG9pVbeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbe7bed94.mp4?token=AyvINQ_upuJBPiDxc3kEIc_gR6y11pQfPWeyDLfaHcT4x1dy_tB6VncDZRGzC4nEkl0LM5-qVYvZEL5J_AazbMsq2d-EkKZIZz1WZb9U74KOAI26IklZGwul9pRZTPatV76p0Vyl_9hjhWk7LqwDLkb11gcqoQBsswmdzVqHXe8yZCOes5OIkYQ_04qAdkT4q6xqmTA6GjTe7Cp5nT1gIYus7pNrWgP8wr8jlCqvCKDI37igTV7xImEn-B2ujo6CCOw9I-8RjwpyrURI18MUyAzBF4JDmsvFa83KUZpKI_UUfY48FEjPlb3ZPmZLE3xz_lBeaUVPQp8v6POG9pVbeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: حوض نقاشی
🔹
ژانر: درام اجتماعی، خانوادگی
🔹
خلاصه: «حوض نقاشی» به کارگردانی مازیار میری، داستان رضا و مریم، زوجی با کم‌توانی ذهنی است که با تمام وجود برای ساختن آینده‌ای بهتر برای فرزندشان تلاش می‌کنند. فیلمی سرشار از عشق، امید و انسانیت که با…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/673885" target="_blank">📅 21:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673884">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
لحظۀ اصابت موشک به مقر ترویست‌ها در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/673884" target="_blank">📅 21:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673883">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنگوی ارتش: اجازۀ نزدیک‌شدن دشمن به مرزهای کشور را نمی‌دهیم
🔹
اگر جنگ به زمین کشیده شود، به دلیل ناآگاهی دشمن از زمین، احتمال تلفات او افزایش می‌یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/673883" target="_blank">📅 21:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673882">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d9d5e5da.mp4?token=DPxRW2UGFb6SskMsKjgQApo2A4tu5SoC-_4ykys1jkNkG6DRY6HqeIjtooMzZjjGVLxvYxJp6CdEoYYqQ8JhZmiCxpTg6-4ISjviabW8IXbHWA2rqPH8DEi7s5GKWCvy2H3tPV-CocyetUVk1xrFchpS1hKs5-THgdcakBaRxAsWDMQJ2NmZUkewPtyfgiHDz2QuB2VpuQdEjArIgMp-3S72PdfwTH1_T-UqUeMuZ8sZ3pFs0Xv-K9QYgkAmBN1Xdm6J-NE8qjVegn5TbHhKEQdtN8ZZC3QMgpwr7MQT8LeXRrmHBGc7WUgaPa-Kksp_4l7wlTqrg8fgs9va8ndgAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d9d5e5da.mp4?token=DPxRW2UGFb6SskMsKjgQApo2A4tu5SoC-_4ykys1jkNkG6DRY6HqeIjtooMzZjjGVLxvYxJp6CdEoYYqQ8JhZmiCxpTg6-4ISjviabW8IXbHWA2rqPH8DEi7s5GKWCvy2H3tPV-CocyetUVk1xrFchpS1hKs5-THgdcakBaRxAsWDMQJ2NmZUkewPtyfgiHDz2QuB2VpuQdEjArIgMp-3S72PdfwTH1_T-UqUeMuZ8sZ3pFs0Xv-K9QYgkAmBN1Xdm6J-NE8qjVegn5TbHhKEQdtN8ZZC3QMgpwr7MQT8LeXRrmHBGc7WUgaPa-Kksp_4l7wlTqrg8fgs9va8ndgAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از اصابت مستقیم موشک به مواضع آمریکایی‌ها در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/673882" target="_blank">📅 21:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673881">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhwFJWAX4GmHVhI0clH2rE-qPxkJGNlLL_qqhskzbyerqKr46fI_i1scQLfOhjesI6hDgVXjitI-f95-7UKaJVqyJ2Ce3BzgZCIPoAc00NNCdwP1xUvYXfTiMRxbOj7ULmH25JD_vwJlqspVuR6rTXlg_FOpWyvF7M5X_YA_AJ5NAI8T4Z3vkaTE2KVkv25vmvJqVbnmR0GtkWwlIAYVTRDlMrONeXMXSFJomrW-Ak4qoHteDPywiNOaOnlvH3esCwuckK2ajwECVY9vKPuGROZJAFOM7B6aJJYKey2mSPTAZuewr8Oz33Fjr3JG_XXBmIn1J2QZil2phI1I3GMexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر آرزوی
زیارت اربعین
را داری، این فرصت را از دست نده.
🔸
به همت هیئت قرار،
۱۰۰۱
نفر به قید قرعه عازم سفر کربلا خواهند شد.
🔸
اگر می‌خواهی به نیابت از رهبر انقلاب در پیاده‌روی اربعین حضور داشته باشی، همین حالا عدد
۲ را به ۳۰۰۰۱۱۵۲
پیامک کن و در قرعه‌کشی شرکت کن.
شاید امسال، نام تو در میان زائران اباعبدالله(ع) باشد...
🏴
🤍
@Heyate_gharar</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/673881" target="_blank">📅 21:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673880">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fujFvC1hZPl8L5Ah8P-5oIWv9Afy62OHVfk6nY60yIfGdzshRLxIa6FYTZBO939pWX4P3PKiZAf9TQFCatH7KYlddODUmlpq5ChM99UWg6aGbP0qafdftEMfpjljbgYTmdad7vTiekoq30f9Agou4dMcg0FFbJTHubIvd_QmutgJxbxW-1FJf0W_FmDM9xpwukcC78VChivJBD-5v6EZ2045wtg1koe-YjKezVnhKS2107LPUBfKcTDFEulwL6a6XYjx9m45FSe1YyH604YbaPcFvfOZku2Gy8io5S7dc1Aa120xsUdzpgy34kRGr0VYrX6I3VS9xT_4S2OGLSIfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
براساس همین یک توییت می‌توان یکبار اختصاراً تاریخ تحولات سیاسی معاصر را توضیح داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/673880" target="_blank">📅 21:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673878">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCWVg2ajApHQW72ejor3bVl1PJcAN-CUZhhXp-6A6-7rwPjoF-xuwZqCUcpPGcpEm-0U8QDEoA8fZ3dFt6E-EXydGVgEJBQpxz1EyX_aRBb2F1VK0EiXeRDsmjreCnvlzrl36rbOQhmi19hmSB3wyU1zky-ZPiC6Rku6M14STPdewWZhCdcWowTVuQRxJRvyfLRMfbOY2nGUlg9XH9AJijXX7sQ53h-Uqvk5rwVSV8Arx_TikmFb9TCbtaRuiJsFQ1But6H0ZXD4oZ42W3vB8EYVgXIyLe4lmw4wIcsQXpD4zRD_vU6yd2W0G_XyzBKZWLaMFptuXcDAEmFdul2Plw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد رآکتورهای هسته‌ای فعال در کشورهای مختلف جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/673878" target="_blank">📅 21:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673877">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6af6d1f6.mp4?token=HDZX7pS_uAzT3bbjE_9ep9TNa5FBPFiFNsmp6F8SbhNnS4IbearV9BgdTv7XrRXhKHUfcAR9bHFbmfx6xY41q6NMp2BoouM3e0UOetYboWF9W31-WJgon8IeJmmWaRapA5S1zYxrjQ4nOKhrdd_qzSsioOS5s7SyOQhiguywf0UNXByVOFpz16fQEp7nSPHYrdLrLPJqi56A9CZUZwHGUU1bavuh3nrEX4C0qAg-koLKY3AjpriKTzgwWVmWX8dak3fF8JW8ufY7d8lJjfcydQnXFOxgGI5Oma_Prx4ynOOCAut5tXnTyZwr2R3W6AQZRjBgmwPURxfSxqNwclNs-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6af6d1f6.mp4?token=HDZX7pS_uAzT3bbjE_9ep9TNa5FBPFiFNsmp6F8SbhNnS4IbearV9BgdTv7XrRXhKHUfcAR9bHFbmfx6xY41q6NMp2BoouM3e0UOetYboWF9W31-WJgon8IeJmmWaRapA5S1zYxrjQ4nOKhrdd_qzSsioOS5s7SyOQhiguywf0UNXByVOFpz16fQEp7nSPHYrdLrLPJqi56A9CZUZwHGUU1bavuh3nrEX4C0qAg-koLKY3AjpriKTzgwWVmWX8dak3fF8JW8ufY7d8lJjfcydQnXFOxgGI5Oma_Prx4ynOOCAut5tXnTyZwr2R3W6AQZRjBgmwPURxfSxqNwclNs-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی منتشر شده در رسانه‌های اجتماعی پلیس نیویورک را نشان می‌دهد که بعد از قهرمانی اسپانیا به هواداران کمک می‌کند تور دروازه فینال را تکه‌تکه کرده و با خود به خانه ببرند
🔹
اسپانیا در این بازی با شکست آرژانتین، برای دومین بار قهرمان جام جهانی فوتبال شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/673877" target="_blank">📅 21:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی کنسولگری آمریکا در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673875" target="_blank">📅 21:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
♦️
منابع عربی: لحظاتی پس‌از به‌صدا درآمدن آژیرها، یک موشک‌ به نقطه‌ای در پایتخت بحرین اصابت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/673874" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf309493d9.mp4?token=O1SYASCXFu0RHyq4PgGOLsnHCK5LWtxRwx940FYP5XIE79ZtHA9rpr2hwWXiNiT30VtSCY3rZ_Ln3BN0kwt5KSz4NypZ-gRta5fZZ3RpQEdthz5CFZEnHs2QG6EwZ_l6uH-WpUaoBTHEPgWkTmUw0R9N6RPHko4UwNO7glcIEvNMQo6FLNuZUzsUQuBClyxmXdAAFw6KNVlKInbj4ohrQ9pTrDFfcuqwZISm-gh8ZxF-oHRa69zGpfe5gDV3V8JpQA3aN84tfkNSVPyRZ38fyDzQd5aJHF-f95zD0PxRzLF9l8syfOlkManyRWR2rh8isGtxXiOrlcVpw-yVufLeME18yvqn6HGMsCK13kUn6ZsZpkK_e9tYYbWd6pw-pDNwFJzpV_0Vct_QqbqDE5WOnUrQGvUnkroacmGS9irsiNQ-16OBdBk-JBUvhSB3hfHBs8C1_GVA9BvMKhff6pD6CzbqTdLj8J7utU5WfqRTFA4UKQnlmO8r8_kxQ4wwcT3fdFcCDgMk8PzFxmLYBP-QldAsUlNZUx5DhCRq74CsOu4sRDqXdeXLkNZFM1IuGuVYZ5mt41gUWDyVtaHrBb_4T5pKwM959pBjV8yfrZVfaTRC3PytK18-Gla7cMwYthMdUX6WzkZQcGbE-X6dw67sUh0NRHNw0Ga9ZfgjTVTrrA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf309493d9.mp4?token=O1SYASCXFu0RHyq4PgGOLsnHCK5LWtxRwx940FYP5XIE79ZtHA9rpr2hwWXiNiT30VtSCY3rZ_Ln3BN0kwt5KSz4NypZ-gRta5fZZ3RpQEdthz5CFZEnHs2QG6EwZ_l6uH-WpUaoBTHEPgWkTmUw0R9N6RPHko4UwNO7glcIEvNMQo6FLNuZUzsUQuBClyxmXdAAFw6KNVlKInbj4ohrQ9pTrDFfcuqwZISm-gh8ZxF-oHRa69zGpfe5gDV3V8JpQA3aN84tfkNSVPyRZ38fyDzQd5aJHF-f95zD0PxRzLF9l8syfOlkManyRWR2rh8isGtxXiOrlcVpw-yVufLeME18yvqn6HGMsCK13kUn6ZsZpkK_e9tYYbWd6pw-pDNwFJzpV_0Vct_QqbqDE5WOnUrQGvUnkroacmGS9irsiNQ-16OBdBk-JBUvhSB3hfHBs8C1_GVA9BvMKhff6pD6CzbqTdLj8J7utU5WfqRTFA4UKQnlmO8r8_kxQ4wwcT3fdFcCDgMk8PzFxmLYBP-QldAsUlNZUx5DhCRq74CsOu4sRDqXdeXLkNZFM1IuGuVYZ5mt41gUWDyVtaHrBb_4T5pKwM959pBjV8yfrZVfaTRC3PytK18-Gla7cMwYthMdUX6WzkZQcGbE-X6dw67sUh0NRHNw0Ga9ZfgjTVTrrA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت دوازدهم مستند احیاء و حقیقت | «جوانه می‌زنیم»
🔹
گاهی، پس از عبور آتش، نخستین نشانه زندگی نه در هیاهوی ماشین‌آلات، که در جوانه‌ای کوچک نمایان می‌شود.
🔹
در دل دیوارهای سوخته، میان قاب‌های شکسته و سکوت پس از حادثه، هنوز نشانه‌هایی از حیات نفس می‌کشند؛ گویی…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/673873" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673872">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auOMfW2zlsXK7L2iObBlnrM8xVOLZeGAGvalFnkkF6CLX2MR8O7NfjvsonT-frswkif7MuDY_v1WNJ9l6KPYHksCsRwnjX_Y2prd0-TsEzndX7vWkCZeopqRboRDo8LzfQvPvEjSVk9aKkaXYxoaDrjVBRteAlOVmCqIRKqlycSNmDSnUkgkVPFfOa73kI4-XVtq6U3BO8upbHkE3Xpd1xGWYLsUWZQFEEzgoKpxV2nBlzG-PIQZGTxCgZ9vCVYpjhiQEclxOiiPbuG3kkCUHtgf4snaOPykqKrWEwkT8Qt7vpFiMHiFfo-FH-USTipfYtSnVev8y9X5s-LVT3ayYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت سیاوش اردلان، خبرنگار BBC: ابتدا همه فکر می‌کردند حملات اخیر امریکا مقدمه حمله زمینی است ولی نتیجه ضربات ایران نشان می‌دهد امریکا باز هم بدون برنامه وارد عمل شده؛ یک مقام نظامی آمریکا می‌گوید ما قابلیت دفاعیمان در برابر موشک‌های ایران مستهلک شده اما کاخ سفید به حرف ما گوش نداد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/673872" target="_blank">📅 21:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673871">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f568acff.mp4?token=UpZVSOvckPdeeASt7b3ns2tcTy9MR5ILq70X1g3-vafZSSY01xXkgt5s8hOF_JgDXoF8EM6QU8eKcaZNjUuuK2K62WARW2ZFeyqtCEKh0V59soqxy1zTH75KRLARcbV7oKKQNra6XYNJ4PCXfEUuiXYyNAxn9WKu_o-CX3ZhhwIIGfV2fkJW25NrOBdHQQ9KBXo_phQl-Spm0aIchaMbWhMTWhCcK2WfLjB6Nz2iOhJR7p9Wql9WpevDEZqB1EeMAzzgXqePm1hHTardnxXpsczke1OyrNt2cZLznGwkMAaEgrQqp-6m4Dfux9yaWqsJDxU-8z7bMvvNmPMyR_d3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f568acff.mp4?token=UpZVSOvckPdeeASt7b3ns2tcTy9MR5ILq70X1g3-vafZSSY01xXkgt5s8hOF_JgDXoF8EM6QU8eKcaZNjUuuK2K62WARW2ZFeyqtCEKh0V59soqxy1zTH75KRLARcbV7oKKQNra6XYNJ4PCXfEUuiXYyNAxn9WKu_o-CX3ZhhwIIGfV2fkJW25NrOBdHQQ9KBXo_phQl-Spm0aIchaMbWhMTWhCcK2WfLjB6Nz2iOhJR7p9Wql9WpevDEZqB1EeMAzzgXqePm1hHTardnxXpsczke1OyrNt2cZLznGwkMAaEgrQqp-6m4Dfux9yaWqsJDxU-8z7bMvvNmPMyR_d3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم از عشقش می‌تونه بگذره ولی از وطنش نه #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/673871" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673870">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cc59af399.mp4?token=cjoPWOqMLAMe43ETsSWz6w4KmddNQC9ut2nRHJw5_PaVN-i-4j7l8VV5vmdTrBW-8BvHRyBx6eGg8y1OYqIcJ2yEBkQEoySX8Z8yxfKWHc-_dED38vSnBWSrqxmj-0raBwH8OHIM0MVd0zdoc0Hlw5mM4vWPDWbyxmEPDvV0Uw0SoBtb4gcVznjtpdf8OUR1G8I_htaprZyNMxEsvfWGlYdCIHuX3ZF5yjeVqBZv_mtZNLo5VJAi69JgYsiEePZ-GgUQcZ1SRK3jp8uTllWgjmVzoPh8mVjnaK13Sh-yLvkQsGn_cSBgNwWMoVkg6I5L95DPV_ANU-jNXFF1MzUGFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cc59af399.mp4?token=cjoPWOqMLAMe43ETsSWz6w4KmddNQC9ut2nRHJw5_PaVN-i-4j7l8VV5vmdTrBW-8BvHRyBx6eGg8y1OYqIcJ2yEBkQEoySX8Z8yxfKWHc-_dED38vSnBWSrqxmj-0raBwH8OHIM0MVd0zdoc0Hlw5mM4vWPDWbyxmEPDvV0Uw0SoBtb4gcVznjtpdf8OUR1G8I_htaprZyNMxEsvfWGlYdCIHuX3ZF5yjeVqBZv_mtZNLo5VJAi69JgYsiEePZ-GgUQcZ1SRK3jp8uTllWgjmVzoPh8mVjnaK13Sh-yLvkQsGn_cSBgNwWMoVkg6I5L95DPV_ANU-jNXFF1MzUGFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای پیاپی بحرین را لرزاند
🔹
منابع خبری از وقوع چندین انفجار در بحرین خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/673870" target="_blank">📅 21:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673869">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پاسخ به یک نگرانی بزرگ؛ وضعیت ذخایر کالاهای اساسی اعلام شد
محمد جواد عسکری، رئیس کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
در حال حاضر، حمل‌ونقل و ترخیص کالاهای اساسی بدون هیچ‌گونه اختلالی ادامه دارد و در روند تأمین اقلام مورد نیاز مردم مشکلی وجود ندارد.
🔹
حتی اگر حملات به زیرساخت‌ها تشدید شود، ذخایر کالاهای اساسی به میزان کافی پیش‌بینی و تأمین شده و از این بابت نیز جای نگرانی برای مردم وجود ندارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/673869" target="_blank">📅 21:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673868">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در شمال اربیل
🔹
رسانه‌های عراقی از حملات به مقرهای گروه‌های تروریستی ضد ایرانی در اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/673868" target="_blank">📅 21:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673867">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
انفجارهای پیاپی بحرین را لرزاند
🔹
منابع خبری از وقوع چندین انفجار در بحرین خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/673867" target="_blank">📅 21:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673866">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رئیس مجلس نمایندگان آمریکا: جنگ با ایران باید خاتمه یابد
جانسون، رئیس مجلس نمایندگان آمریکا:
🔹
جنگ با ایران باید پایان یابد.
🔹
فکر نمی‌کنم در حال حاضر رأی‌گیری برای مجوز استفاده از نیروی نظامی مناسب باشد. فکر می‌کنم باید این موضوع را به یک راه‌حل برسانیم.
🔹
نباید فقط تعهد آمریکا باشد. دیدگاه من این است که همه باید نقش ایفا کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/673866" target="_blank">📅 21:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673865">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در شمال اربیل
🔹
رسانه‌های عراقی از حملات به مقرهای گروه‌های تروریستی ضد ایرانی در اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/673865" target="_blank">📅 20:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673864">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مردی که پس از مرگ موقت، عذاب گران‌فروشان را دید
🔹
00:08:30 پرسش و پاسخ در مورد امامان دینی
🔹
00:16:40 گناه گرون‌فروشی و فریبکاری در حق مشتری مغازه
🔹
00:25:10 نظاره‌گر حادثه‌ شش‌ماهگی‌ام در حرم امام رضا (ع) شدم
🔹
00:36:10 درک عمیق از عذاب رباخواران و زنان بدکار
🔹
00:40:05 تغییر احوالات من و پیدایش نور با صدا زدن نام خداوند
🔹
00:54:50 رؤیت اتفاقات روزمره توسط روح انسان در کما، از نظر علم پزشکی
🔹
01:01:00 تغییرات رفتاری و اعتقادی بعد از تجربه
🔹
01:03:50 آثار مال حرام در زندگی دنیوی
🔹
قسمت هشتم (تاوان)، فصل پنجم
🔹
#تجربه‌گر
: سید حسین موسوی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/673864" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673863">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سرلشکر رضایی: بیانات حکیمانه رهبر معظم انقلاب غبار تردید را زدود و توطئه دشمنان را نقش بر آب ساخت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/673863" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673862">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF37BqzujQoNdRmLlWMsa_H_04ESAP38VIxgo8E-sInsg5AfhAl_o5LkPdCvnvaXvl_wyr03sXzm6aJe-tqzpm7gb8nhOh46i2312sBrvbWUbTtFGHRkRXwAsOmRrkhjD7egp7_9vG3v_UWLmd53HilKNO4ry6dG_TzmkxptBiXLl2KxUAGvwhNSd5Rih6bP3PZkgv6wFZckfX1noKVM9wqnXoBcwMx7ZwxJJ5tjkQpN9k4Zcbaw3_Ro2jzww6e6z_CG2QWCI0LP-M8zsw7Tgv7nbKZo05bgHIIjG0OuC3CLEizJd1Nnfr9unMy22zRiJ6ykAcuDUPnDWLN2-78KIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثبت یک رکورد تازه در صنعت پتروشیمی؛ امیرکبیر یک روزه سود سهامداران را پرداخت کرد
🔹
حسام خوشبین‌فر مدیرعامل شرکت پتروشیمی امیرکبیر: واریز سود سهامداران حقیقی، صندوق‌ها و سبدهای سرمایه‌گذاری تنها یک روز پس از برگزاری مجمع عمومی عادی سالانه این شرکت انجام شد.
🔹
در این مرحله، مبلغ ۹۳۲ میلیارد و ۱۰۴ میلیون و ۹۶۶ هزار ریال بابت سود سهامداران حقیقی، ۱۴۰ میلیارد و ۲۷۴ میلیون و ۳۰ هزار ریال بابت سبدهای سرمایه‌گذاری و ۳۷۷ میلیارد و ۵۱۳ میلیون و ۵۸ هزار ریال بابت صندوق‌های سرمایه‌گذاری به حساب شرکت سپرده‌گذاری مرکزی اوراق بهادار و تسویه وجوه واریز شد.
🔹
عضو هیئت‌مدیره شرکت پتروشیمی امیرکبیر مجموع سود پرداخت‌شده در این مرحله را یک هزار و ۴۴۹ میلیارد و ۸۹۲ میلیون و ۵۴ هزار ریال اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/673862" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673861">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef8bbJRHsobXFIiniQ_ra6BZZ0K4D3TFw9NyNx-xHuhbTvBjx80_x2Z_cl-8fLX90zk9OEW6dxpIE1S8ck8BYAEjREUtj-b2gNee-KyqmUpJa_-aSfpc_fsJ1A_-MF30WJ-PXb80JFFkEoOulK3V6Em1TtAcxTvkVQ-G5GzC9KrASJK-rfg2yIfgFA3hBym1mi1dE6O5Vm5yG5RZCwCifajX0-bV6TsO5SIJpUvCFJbxAF0F2Ytdm2JdXBobxq4rGw2-xWmaBbnRMbjeoYOXV4JtKZg-8cJU3VPRlI0pCXuxGuw35JTwlpLsAByzFDREO32fVcdhVHhhAUI_JLaIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان شانس برنده شدن در لاتاری‌های ایران‌خودرو در سالی که گذشت
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/673861" target="_blank">📅 20:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673860">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5r8wCtACkMqtTm0L7bqkFfEfwRcX_YVXs1WDioSwiPXMUVcABH3w_fK9AiG-VdKSMKKQAUGOLc87tgF1RqsGY1XBb7Q_nG3dODAGi0ar0VK4g2hdgpf6I2WW33zXR7YzoyAgbckpGD6SH6eIFelzBHb7WblXy0IUqa2pZ6xFhVxVm_qq2u52qOvlYj13iqPzKr8LZlPWGqswmIDxEkpIRTMND2U3P1ok8G2eBQUeZNX4dJhryVMCNcjS5V8eL1Hr1kr9yK0Xg3DHwFxyu-BhrCldYk4tY7dDRtRfKyVFc4OPkiF_0baecqkp5RtwjqQxLgcm5oQrLb-b4DrmH3u6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد انتحاری متجاوز توسط پدافند هوایی ارتش
روابط عمومی ارتش:
🔹
ساعت ۱۸:۳۰ امروز یک فروند پهپاد انتحاری دشمن متجاوز با رهگیری و شلیک موفق سامانه‌های نیروی پدافند هوایی ارتش، در آسمان استان آذربایجان شرقی مورد اصابت قرار گرفت و منهدم شد.
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/673860" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673859">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEXYIX38_PmePH68Efr6hIvWDFZMnneHtQBA_KZrX2GFzoHXmfewDtNJOWwktZLPhYas5wXca6HAzIOL0pNtt5NBhXllH96kzedJqoMsi1lfSsSFRfnmrneNR3aR9hZyYP2Z7CfyIYxw_LeTgvzIDxgUokGP0_DBqcSquw__5wc40EXFmRkvEs6nuRkxUsr3RMunspdItXZ0AledgiiNVL7v1sX3bP--Juw6btmdv21cUDq00zpTfo-KjErFW1xe45wA9LHf4sIqFHZ-sLSpWUx0FgM-chcURrLD-eevyEdowwpQwMk5OQ2WszlDxat-a5EnjumTC4TgFL06CKCjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درجه آسیاب قهوه؛ کلید طلایی برای طعمی بی‌نقص و حرفه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673859" target="_blank">📅 20:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673858">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtExNZl5V0l3Nn7axDtCVF-X_vJvs13AZJ_7JqoycmWBKrbiZBeLdX-TMc6PVQfNrJN54riKL8dcSXel7L3P-HGj_PyjvvE7-ChMuLDvhA1AB9FsY0Y6__wb_vOcq9XePFbmU7TIflBj7sKo8TB4_pIQKaHc44Tl9aFWKMdQFo0eBOB0NezKB22pXql_Ayv4qMDnSps0F2zQvGGjZ-ad4hYOL1YmkMjQqkqqxPCDG4kgsOUtoTivQbUIbSSNP2GxVCG8Jjx22oaAPvqU9dm__Js8B-IBUFnhRsLqYkWP2LkPanyu9tPyeh-mI3pZCFq3kkaEEt7toPL9a-5Ly9b7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار ارزیابی رگولاتوری ارتباطات از مراسم تشییع رهبر شهید؛ تمرکز ایرانسل بر مسئولیت ارتباطی جواب داد
🔹
رگولاتوری ارتباطات با انتشار گزارشی، عملکرد شبکه ارتباطی کشور در مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی را تشریح کرد. بر اساس این گزارش، ایرانسل موفق شده است در محدوده مصلی و مسیرهای تشییع تهران، رکوردهای قابل توجهی را در زمینه سرعت دسترسی کاربران به اینترنت نسل چهارم و پنجم ثبت کند.
👈
جزئیات بیشتر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/673858" target="_blank">📅 20:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673857">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/542bb9fba7.mp4?token=q0DYjPq_E0NPq-L9mNIjkRnCPtWkiufs_GDShohhakuUHk4Dl6_PUEjYzz0impk5KW6htO26CELTmwIBOMWuj73OcxihQJjP5tpbjB-VRhXIcJ4utMuTZ0orMTyDg7iSh20F-rjRYu84loj-4Lk-FnqtqEbS-k3Ew90lScRaC2-tfw8jnON7xmD8erFKceKVwAPFR8YfZHG9Ts3-L1dHFE6RKFsC_E4apbN8PfGjtGla3CmVfpWA9I4pqE_M95KSUZ_DkyZz3Q0OMjioJ9KKjVH44Qhsn8pkkjUeAdxmJAk3-ck6YRJQ21KqocekSjQCKuVPs-Smu_dRQnLfRw8fTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/542bb9fba7.mp4?token=q0DYjPq_E0NPq-L9mNIjkRnCPtWkiufs_GDShohhakuUHk4Dl6_PUEjYzz0impk5KW6htO26CELTmwIBOMWuj73OcxihQJjP5tpbjB-VRhXIcJ4utMuTZ0orMTyDg7iSh20F-rjRYu84loj-4Lk-FnqtqEbS-k3Ew90lScRaC2-tfw8jnON7xmD8erFKceKVwAPFR8YfZHG9Ts3-L1dHFE6RKFsC_E4apbN8PfGjtGla3CmVfpWA9I4pqE_M95KSUZ_DkyZz3Q0OMjioJ9KKjVH44Qhsn8pkkjUeAdxmJAk3-ck6YRJQ21KqocekSjQCKuVPs-Smu_dRQnLfRw8fTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توده‌های دود در شهر جده عربستان سعودی بلند می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/673857" target="_blank">📅 20:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673856">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfFwYIv_ifx1KrcfFg82swve19qEjZciMger5EcWchCJ-5ZX_hvA6DhCqr445yI1CcXRguj8y6JbSDP1xzdVu2KezgW7LHOZh1ld2tkDjlbdO6W4FF3758XlfmlFnTr7HIbhYQ1IrxvCkBc-17vSzg58Lr_M4rIci9Jrzew_OcnWJHvfD3JWKCWucxmrE3sd7OPIy85mYYcnVLoSMqyXExgXWsEmmnRhm7qeS7fYnjPh2zqXJ3GCZYDlzUJVAfWhA6ieA4dFT-tPRyw5K0a8ZBLyELTvefJXLtc36bVv9dvc4lWTTEKKBslD8sxjCMOdVmxiPedJErugzVbuJkfaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه با هم برای ایران
🔹
در روزهایی که کشور با حمله تجاوزکارانه آمریکا و فشار بر برخی زیرساخت‌های حیاتی روبه‌روست، مهم‌ترین سرمایه ایران، همدلی و مسئولیت‌پذیری مردم است. امروز بیش از هر زمان دیگری باید مراقب باشیم اختلاف سلیقه‌ها و نگاه‌های سیاسی، ما را از یکدیگر دور نکند، چرا که هیچ آسیبی به اندازه تفرقه، توان یک ملت را کاهش نمی‌دهد. در کنار حفظ انسجام ملی، باید هر فرد به نوبه خود پای کار ایران بیاید حتی با کارهای کمترینی چون مصرف مسئولانه آب، برق، گاز، سوخت و مواد غذایی و کمک به هم‌نوع.هر چراغی که بی‌دلیل خاموش می‌شود، هر قطره آبی که هدر نمی‌رود و هر قرص نانی که حفظ می‌شود، سهمی در پایداری کشور دارد. ایران، خانه مشترک همه ماست؛ خانه‌ای که عبور از روزهای سخت آن، نه با اختلاف و اسراف، بلکه با همدلی، احترام متقابل و احساس مسئولیت جمعی ممکن خواهد بود.
🔹
هشتصدوپانزدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673856" target="_blank">📅 20:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673855">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLa7peH1IPLngysNp2BMDaCW2xuckMYozwauhQY0vAg7T-RB3JUsOZVO5H8LRA2uWp9ZvCFMqCrWSRxvb2ZoNgetf1vpqY6amFO_B-PTXM9b_9Hcy5IZjZp0Y5FHts08DxgLcDCB-DGZ_MAycMRpHXK7jRRcCWxvbtmfL3nN-G7IO5_Y6HpxAkgQ5lISA29xVIr7a5UTia8fsLcDwRqWWCPrM3Lf1KCAQZC9BFwKucfksVOJYRKR-ojgj-n_Om3h63qd3H04eW77sTz0ZcCecg8mAhve8bfOM_mcqnLv70CGbpfgVSIWHzQpuRcYvhj3kD14RqwhK15lbTZ9F9nhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/673855" target="_blank">📅 20:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3HIA-H4k5YONRmv4rZKdm8yjWWjv--R8UA8uoflyybA5EmWPnwjmLnuVFv2jV543KMJUWkLKdBGkVnYfcAWIApmDaUvEAzAG1aZR3g1DMPB0-F-QhZjw2w3iglXo0sZH0eLCH07YV6UhYW9DjjtHYCWNatwMDmSJlGxik0nR2YTqUll4k07ttqEuDkDuejJaLY9855XgfV-cMxkA_l2oBrrNX0ABgZ25EWFpicVDXreUko6rTX3WwysrpDKvpYt7Td6M-USQpw400uYEdgKCCe29Esw2O8FCOSTzatiKwPH9QnomGZ7-5_46qyHnQdaYN0HA8yOyb-grHNQEnx_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7tDAhAQDTXIE_FLUAa_XrbcXqn8WvvsKs8HwQ6JN7bbJ6aShLyaxX7hRifLv8DWrDF2DaJ-bF24xRj2Kn6oBPj04PKTyH6ib9DMKF-lQVzQiXBVyRMHC0Aj6PwBbDoT4-YOcWZ24ZlLwZR4O6lt5wmxPrsTO0LDoW_qAvEsC5OyJWMWhMUhIOEgoao_pF3DZQTX2Z9ISDEuGaPRy8ibPGAfdzFgUTalblyF9FnG7rdGRaiXhI7rJ_ncxfg8NgrPIhL69fbQDBDqS3e2U-Bg4-lY1A29D9Cfrm8AJtuOnNwBNy_Mv0w5zk5sXXAWuXym-9bYnReDp8LD7JUf0uHNAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جوونی و با این اوضاع اقتصادی نمی‌دونی چه‌طور باید کسب‌و‌کارت رو راه ببری؟ این کتاب رو بخون!
🔹
اگر فکر می‌کنید برای  موفق شدن به پول، استعداد خارق‌العاده یا شانس نیاز دارید، این کتاب نظرتان را عوض می‌کند. تینا سیلیگ، استاد دانشگاه استنفورد، نشان می‌دهد چگونه با تغییر زاویه دید، هر محدودیتی می‌تواند به یک فرصت بزرگ تبدیل شود. کتابی الهام‌بخش، کاربردی و پر از ایده‌هایی که می‌تواند مسیر زندگی و کسب‌وکارتان را متحول کند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673853" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
عراقچی به همتای فرانسوی: رفتارهای غیردیپلماتیک دیپلمات‌های شما در تهران غیرقابل قبول است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/673851" target="_blank">📅 20:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu_Ljs6Vp-nIsJFQPm0QXY96mj8jE1kNynx6RyAYdj-6Pap_-cQyYNKlJCtt_PXiqJfqv6cWJOi9x6_XwQECp5l5xL4rwnEEV33yEraU-tebkluntwi8-COa0nGdbYCVXbhp9ftzEEUvnTD2DA27JcAdA51BTQlIwqg6oaWpLOKzHFFilbaO7sddldMAjA3G6vq6KBNID1aHdvUBZIRERRZCMOxG20RFU5J1HgVzbPG79f9lAYwBOEgtY0eGQ2HCNiN6sA_Y6X2x3u139NxXCPAuw77_x_1PFfT_s-3kSv0RdY0wA4d1590GY_4fWdrCqhFV1dE0gqVRjNDBpAcxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاهی فقط چند روز... فرق بین فرصت و حسرته
💎
طلای اقتصادی  اجرت از ۳٪
🏦
خرید طلا از ۵ میلیون تومان
🔄
تعویض طلای سالم با عیار ۷۵۰
👰
سرویس عروس از ۵ تا ۶۰ گرم
کانال رسمی ما :
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673850" target="_blank">📅 20:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ایران به بلغارستان هشدار داد
🔹
سخنگوی وزارت خارجه در واکنش به گزارش‌ها دربارۀ بررسی درخواست آمریکا برای استقرار هواپیماهای نظامی این کشور در پایگاه هوایی «بزمر» بلغارستان: هرگونه همکاری در حملات علیه ایران، از منظر حقوق بین‌الملل به‌منزلۀ همدستی در تجاوز و جنایت جنگی خواهد بود.
🔹
در اختیار قرار دادن قلمرو یک کشور برای انجام اقدام نظامی علیه کشور ثالث، طبق قطعنامۀ ۳۳۱۴ مجمع عمومی سازمان ملل، از مصادیق عمل تجاوز محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/673849" target="_blank">📅 19:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49763aaec.mp4?token=D3Lq0a0FVQWC5FG5cSIraznirem0Pzrc9HcB3X2_sosj6ux_HZP6rgHCIi5bY1JU8qfgi3Ih6269XZzkdKVdXXJOd35CcyaQdsPDsMQuQniV4eYLbEkyDpxRdCdInL0YIvLcNgKnT-Dxmxo750-hTUBHX1vZ0rTz6vR-todOzGlAWDv9dOqvloTZTVRD53Hl2xqmtF0WiTG4RLGA40QzSSOh8V8_dTd1j65VBNNctPef6YyNY_xRGxu_VBSKfZotQJi9l_K4aUGrwsTiSEEiNVVOX3MylEPJplO7tj6C503n3lNvskANEGQckMpwCzYLRs5bQ2uvzEa1h-3G1awaaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49763aaec.mp4?token=D3Lq0a0FVQWC5FG5cSIraznirem0Pzrc9HcB3X2_sosj6ux_HZP6rgHCIi5bY1JU8qfgi3Ih6269XZzkdKVdXXJOd35CcyaQdsPDsMQuQniV4eYLbEkyDpxRdCdInL0YIvLcNgKnT-Dxmxo750-hTUBHX1vZ0rTz6vR-todOzGlAWDv9dOqvloTZTVRD53Hl2xqmtF0WiTG4RLGA40QzSSOh8V8_dTd1j65VBNNctPef6YyNY_xRGxu_VBSKfZotQJi9l_K4aUGrwsTiSEEiNVVOX3MylEPJplO7tj6C503n3lNvskANEGQckMpwCzYLRs5bQ2uvzEa1h-3G1awaaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: خیلی حرف‌ها در دلم است که نمی‌خواهم بزنم و نخواهم زد چرا که احساس می‌کنم وحدت از بین می‌رود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/673848" target="_blank">📅 19:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
گزارش‌های تائید نشده از عملیات  هلی‌برن نیروهای آمریکایی در صحرای البادیه عراق
🔹
برخی گزارش‌های میدانی از انجام یک عملیات هلی‌برن (پیاده‌سازی نیرو) توسط ارتش تروریستی آمریکا در منطقه صحرای البادیه واقع در غرب عراق خبر می‌دهند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/673847" target="_blank">📅 19:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده ماهشهر: هر تیری که آمریکا بزند، ۱۰ برابر پاسخ می‌دهیم
امیر حیات‌مقدم، نماینده امیدیه، بندرماهشهر و هندیجان در مجلس در
#گفتگو
با خبرفوری:
🔹
ترامپ آدم دیوانه‌ای است که اصلا تعادل روحی و فکری ندارد و به جای آن‌که در بیمارستان نگهداری شود، در کاخ سفید است. ما با دولتی مواجه هستیم که هیچ اصول و منطقی نمی‌داند، اصول بین‌المللی را زیر پا می‌گذارد، نه دین دارد و نه آزاده است.
🔹
هر تیری که آن‌ها بزنند، ۱۰ برابر پاسخ می‌دهیم. جمهوری اسلامی اکنون در موقعیتی است که به‌طور کامل می‌تواند پاسخ دهد.
@TV_Fori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/673846" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJN_lgOKcby05UuIc8xOS2U8j_DDhNDA5BKHPlNoeBzcwtUjbfJtDQx1nEM2dgn2wEowbcogI08ACQyX7xpE6ZHdR_YFqGvei2ldMQEMsH6sqPigz6L67X0T3iiSzAg1ZSALoBRA6eATJe0p3h_T1Cxj1_FHxzSguSmeoBVC7Ik40CS7QbKcbod2tGJ_UplW7OKTbDBPzlPwHFUOtAZVY_-PsK9JYPdnShXIVd2dk6teSTHDpMc1TYhfdZ-pcjncr4Te_x0BZ8__NJhCqA8maxWmyUHxev1Ta5s2H94RyjgdVTjJ02aIqwHYy_KTKML6n8j5eTrdtiQJ1hydW1amRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقتصاد دیجیتال؛ پلی میان دارایی‌های خرد و فرصت‌های بزرگ
🔹
اقتصاد دیجیتال امروز دیگر صرفاً به توسعه فناوری و ارائه خدمات آنلاین محدود نمی‌شود؛ بلکه به یکی از مسیرهای جدید برای مشارکت مردم در اقتصاد، خلق ارزش و افزایش بهره‌وری تبدیل شده است.
🔹
سعید علی‌عسگری، مدیرعامل «میلی»، در دومین روز همایش «چشم‌انداز اقتصاد ایران ۱۴۰۵» با اشاره به روند تکامل اقتصاد دیجیتال گفت: پس از ایجاد زیرساخت‌های ارتباطی، موج جدید این اقتصاد بر توسعه سرویس‌های دیجیتال، دسترسی آسان‌تر به کالا، خدمات و  اعتبار  شکل گرفته و در ادامه، دارایی‌های دیجیتال می‌توانند به بخش مهمی از این اکوسیستم تبدیل شوند.
🔹
او تأکید کرد که بخش خصوصی در این مسیر می‌تواند نقش مهمی ایفا کند؛ به‌ویژه در شرایطی که اقتصاد با بحران‌ها و محدودیت‌های مختلف مواجه است. به گفته علی‌عسگری، تجربه روزهای دشوار نشان داد پلتفرم‌های دیجیتال می‌توانند با حفظ تداوم فعالیت، بخشی از نیازهای مردم را پاسخ دهند و به افزایش تاب‌آوری اقتصادی کمک کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/673845" target="_blank">📅 19:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f93d277e.mp4?token=fcm4OgR1jGr_Eif2kVl6ncwemC8HibRqG8jTGb-r-uVqxELPFUDHYF9SEAHYijAESRb3RRV8CnB_j6xiXPNudupVNjqpa4KAjmVFg0tIbe5CZZj_MbPZqP0OyjRnbJvXFIp0AulMwtQjPWWZfxHL0hzzOatO0LLRtmwtKjPkk0rizvxDPeGT0mHqZ-25x0Wj5RsirbaSQ9lYY6A5B30ty44mokIFzGIFw-kn6CWd5-HN6oiK72yMzgLhDtl_eC1YZXeWFDhX7GQEwfnhiKVQVPOIax1sOKHmiCbWVobBvas0IOw3RT7BFkYlWIcMAzmZjnKIeu_4jFOVx4UGjk4n2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f93d277e.mp4?token=fcm4OgR1jGr_Eif2kVl6ncwemC8HibRqG8jTGb-r-uVqxELPFUDHYF9SEAHYijAESRb3RRV8CnB_j6xiXPNudupVNjqpa4KAjmVFg0tIbe5CZZj_MbPZqP0OyjRnbJvXFIp0AulMwtQjPWWZfxHL0hzzOatO0LLRtmwtKjPkk0rizvxDPeGT0mHqZ-25x0Wj5RsirbaSQ9lYY6A5B30ty44mokIFzGIFw-kn6CWd5-HN6oiK72yMzgLhDtl_eC1YZXeWFDhX7GQEwfnhiKVQVPOIax1sOKHmiCbWVobBvas0IOw3RT7BFkYlWIcMAzmZjnKIeu_4jFOVx4UGjk4n2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای که دیروز گرفته شده، خسارات گسترده‌ای را به پایانه صادرات نفت خام اسکله شمالی شرکت ملی نفت کویت در میناالاحمدی نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/673843" target="_blank">📅 19:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673842">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ac18bcd6.mp4?token=G2enAgCdsQtLsTVZM-xKCOuISitMlK5oCSv3BzhC2LqpYlBEUMYSFKqhI2cGU0EM359tMca0RfawHsfO3zYUyHpogxf0PnWWhVsrNxIxUlOBARKV-KVyWtoTLLturvB6AG1f9hHKNn5_o5rZOVfNbqe6YsYOaFFTceIfWVYvTgWgJGvwL-d__GiCx8ebAa35PJN9BVgJnqD1ZGGb54lQZtL99K-wPyK0DtqddfmaCuEM29nlvl72gAbMNsGJXhMyJ4UJ8-fZpLDa4p_BK_yqIwBh6AGKYIPd8miPxh7mXcC_TXtbxbzCnub3tHWPqhhOH8g6d475asylb3oqmKyrtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ac18bcd6.mp4?token=G2enAgCdsQtLsTVZM-xKCOuISitMlK5oCSv3BzhC2LqpYlBEUMYSFKqhI2cGU0EM359tMca0RfawHsfO3zYUyHpogxf0PnWWhVsrNxIxUlOBARKV-KVyWtoTLLturvB6AG1f9hHKNn5_o5rZOVfNbqe6YsYOaFFTceIfWVYvTgWgJGvwL-d__GiCx8ebAa35PJN9BVgJnqD1ZGGb54lQZtL99K-wPyK0DtqddfmaCuEM29nlvl72gAbMNsGJXhMyJ4UJ8-fZpLDa4p_BK_yqIwBh6AGKYIPd8miPxh7mXcC_TXtbxbzCnub3tHWPqhhOH8g6d475asylb3oqmKyrtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر رفاه: کالابرگ برای برخی دهک‌ها افزایش می‌یابد
🔹
مهلت اعتبار کالابرگ خرداد تا ۱۴ مرداد تمدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/673842" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913265ae74.mp4?token=mwQ78Np4NLxT6Ii0MnoHn-Y-6x0zm-p2vIwk3fkYsuV9TLNMKXqQJdxWy7blvDvoay0IUvJRTSUfvFnyrRivxfN9MCdoY32lWoKdnuGFS8RTWrsrU5Og0Its3x6gvfEocHx9wUfzRdloOnqQ2hFMqjtrcfhpjDouUfFANx1nMywl8L3PvpkhJNJULjuku9rCF6exJcg8o4RgKYDE8X-Alj46qCVvX781tdMgYy8GXWMQOyKiwW325WbKya5lpjXgQIKRaikxiVAFHDscQfpwP1f2Qds5-kxLXVvwU9ZsvjMy5M8MgPnSVFSQLWLjns9adCC6OETj4kVkB6QOzjJ17pgEufs1XY_SWfO_kS2lUCKmySTQkDfaXePaiAU_TfagvNNj11ciBbCf5LpOFdOWRIx7VXWjQ9EqCIjIdGwE0nLwBLbotFf0YGAfroOtW8JTogUrA6wDDKB4pAG_c7fgIQtZczWRtZ0elOhTLnopj6kAfzn6EF_4IoxP7dsdil_njFoMhk0inSG3usqZKtsPcza8qSw-VMqH14KR0zAl2Gh05D3lMIHcIhRdc5O-iGFd5NsS5hmZwoDlbUG6uM_NI1tC_MxxcT_KzqOqxlWUcalkcqjJzQ1EWwC9gIFsoNodtGS4jPJnCJ4Dbag1skH4G0F5dO5ZPNUkI7eWOY4oZVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913265ae74.mp4?token=mwQ78Np4NLxT6Ii0MnoHn-Y-6x0zm-p2vIwk3fkYsuV9TLNMKXqQJdxWy7blvDvoay0IUvJRTSUfvFnyrRivxfN9MCdoY32lWoKdnuGFS8RTWrsrU5Og0Its3x6gvfEocHx9wUfzRdloOnqQ2hFMqjtrcfhpjDouUfFANx1nMywl8L3PvpkhJNJULjuku9rCF6exJcg8o4RgKYDE8X-Alj46qCVvX781tdMgYy8GXWMQOyKiwW325WbKya5lpjXgQIKRaikxiVAFHDscQfpwP1f2Qds5-kxLXVvwU9ZsvjMy5M8MgPnSVFSQLWLjns9adCC6OETj4kVkB6QOzjJ17pgEufs1XY_SWfO_kS2lUCKmySTQkDfaXePaiAU_TfagvNNj11ciBbCf5LpOFdOWRIx7VXWjQ9EqCIjIdGwE0nLwBLbotFf0YGAfroOtW8JTogUrA6wDDKB4pAG_c7fgIQtZczWRtZ0elOhTLnopj6kAfzn6EF_4IoxP7dsdil_njFoMhk0inSG3usqZKtsPcza8qSw-VMqH14KR0zAl2Gh05D3lMIHcIhRdc5O-iGFd5NsS5hmZwoDlbUG6uM_NI1tC_MxxcT_KzqOqxlWUcalkcqjJzQ1EWwC9gIFsoNodtGS4jPJnCJ4Dbag1skH4G0F5dO5ZPNUkI7eWOY4oZVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای دو نقطه اصابت جدید را در پایگاه هوایی ملک فیصل در اردن نشان می‌دهد
🔹
یکی از این اصابت‌ها به محوطه استقرار هواپیماها برخورد کرده و همچنان ستون دود در محل مشاهده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/673841" target="_blank">📅 19:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ecd7985c.mp4?token=og-eLKKQ8bNzFVCCN5oJPXuTS2CFPngVBwFRbZ6T4ACxKh2sacvOKfAHSFo2RsBgGGBQVQfIJ8FWx4MHq8nRSQcqy1MQDa9ATIgdLbYokI_DB8k7ezGKlcJnYnJmIhiKeanXC9vvKKVV0AT8Admp1-pj9_Ve-4bKieU-2RUbgrYMK7NDkyFq5TDUUn5ExSJLpt-mnRP5PEofALzGm0CPEuBIjkm_jDIYQoQBehdzlOsggz5jVb9TVCWJ-6MF5mCNmPygaGZl1K9Tpp446yQpH9u6EA4BcZqihuKVb3jFMt5gxvUw-3hg_S045qnDKY-OqvxjdMK9BHDLNLW07O8ZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ecd7985c.mp4?token=og-eLKKQ8bNzFVCCN5oJPXuTS2CFPngVBwFRbZ6T4ACxKh2sacvOKfAHSFo2RsBgGGBQVQfIJ8FWx4MHq8nRSQcqy1MQDa9ATIgdLbYokI_DB8k7ezGKlcJnYnJmIhiKeanXC9vvKKVV0AT8Admp1-pj9_Ve-4bKieU-2RUbgrYMK7NDkyFq5TDUUn5ExSJLpt-mnRP5PEofALzGm0CPEuBIjkm_jDIYQoQBehdzlOsggz5jVb9TVCWJ-6MF5mCNmPygaGZl1K9Tpp446yQpH9u6EA4BcZqihuKVb3jFMt5gxvUw-3hg_S045qnDKY-OqvxjdMK9BHDLNLW07O8ZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک هار: اگر فردا آنجا (ایران) را ترک کنیم، موفقیت بزرگی به دست آورده‌ایم اما ما فردا آنجا را ترک نمی‌کنیم
🔹
خوک‌ هار: ایرانی‌ها در حمله به نظامیان ما اردن موفق بودند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/673840" target="_blank">📅 19:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وزیر جنگ دولت تروریست آمریکا: به ایران فرصت داده شده است تا مذاکره کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/673839" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673838">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293924ca0e.mp4?token=v9N2L0D1YMZfYfO36G0YUjXpG29MUE3TM3wVkOE-Q53s2xDTtaGF-cKmupd9gR98-CXIzcsj_cwv0J9CrZbBs6xicRD3oAw0jO2i4er0Ii5hmd7QU5dB3RYCcAj9F1syak-uqwvUk2fv0tJ_6lO7QUwrWgnwsiVmfVLvSaqx57DZsazmmn0lgKaVdM770Is4B9dK7YJ-vXdEmnfefMeck-De7c2MroURNy6UNEW93zkwg9F-COfstJ3bAeua0kHf83apO4vQdqW0kveUIJ1OvY5NfEI8X1O4vuyjjl3ywgGgBy2sqxQ2EbvMLmT7iHqhTWUgLj6dNTAXSJQjxzjLcHYVWOu9KVcnV1DfwoRkpqi8Mhh8snAAtTMrobpZbAmO2TDvGinqppaiBtj0S3D091SUkxO5azzBwN12Ie4yIo1PpoJ0bOgE6dgjQX894BAsPlBS3Mk9_mcBi1WMXL37N5A61BWGs7frmfaEHGcTnZQjXJj_PuIdkxbznTED02jUtnAAsYJ8DE8Ds8Wr6QyfjPEz84iUKQPoRbCmryTcNu6srT87zCGFUuKDEemnNt7HCO4q_Z-xCliAawZLN98CgT0JKSY4Mdxt0uXFnaqvqg6PwGJbg55iyzfBnSA_kQvVECPEUmMywhJwvYuBEllx0sHFYHpNkgn901EDferpFUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293924ca0e.mp4?token=v9N2L0D1YMZfYfO36G0YUjXpG29MUE3TM3wVkOE-Q53s2xDTtaGF-cKmupd9gR98-CXIzcsj_cwv0J9CrZbBs6xicRD3oAw0jO2i4er0Ii5hmd7QU5dB3RYCcAj9F1syak-uqwvUk2fv0tJ_6lO7QUwrWgnwsiVmfVLvSaqx57DZsazmmn0lgKaVdM770Is4B9dK7YJ-vXdEmnfefMeck-De7c2MroURNy6UNEW93zkwg9F-COfstJ3bAeua0kHf83apO4vQdqW0kveUIJ1OvY5NfEI8X1O4vuyjjl3ywgGgBy2sqxQ2EbvMLmT7iHqhTWUgLj6dNTAXSJQjxzjLcHYVWOu9KVcnV1DfwoRkpqi8Mhh8snAAtTMrobpZbAmO2TDvGinqppaiBtj0S3D091SUkxO5azzBwN12Ie4yIo1PpoJ0bOgE6dgjQX894BAsPlBS3Mk9_mcBi1WMXL37N5A61BWGs7frmfaEHGcTnZQjXJj_PuIdkxbznTED02jUtnAAsYJ8DE8Ds8Wr6QyfjPEz84iUKQPoRbCmryTcNu6srT87zCGFUuKDEemnNt7HCO4q_Z-xCliAawZLN98CgT0JKSY4Mdxt0uXFnaqvqg6PwGJbg55iyzfBnSA_kQvVECPEUmMywhJwvYuBEllx0sHFYHpNkgn901EDferpFUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر ماهواره‎ای از خسارات واردشده به پایگاه هوایی موفق السلطی در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/673838" target="_blank">📅 19:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673837">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
زیاده‌گویی خوک نجس درباره حمله به سایت «کوه کلنگ»
🔹
در صورت تلاش ایران برای احیای فعالیت‌های هسته‌ای در سایت «کوه کلنگ»، این مرکز را هدف قرار خواهد داد؛ هر سایتی که برای توسعه سلاح هسته‌ای استفاده شود، با قدرت زیاد هدف گرفته خواهد شد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/673837" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673836">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/172556ab59.mp4?token=KgGBo7upYbmXBRbMhChbgZwUoUyOz_9EDnoy3Y1AYYVI7-UhgdZnVw-xCeVFvp-G70kzbq5yVpIwLKt6SOfeMuQSuPiMG-JjyEDPgb2ymABuHfFev7qBGxaOCI1__r2Mjruj4vtcOF0jtg8eLPbmg9TQ2MOyexD8KEFyVzEorRwHR5IdbXink1O_ZxrcJHEdZtd9_0RhaumBbafO43IEuT4DObHW1bt6NjFh5ktWat_UxCfIN3WW6I9kYCMUQDjXijJHmW1Dkq5e4qzSFClus7RPKGqM6qG9qm_0L_q-QG3hsd2o5y8WRlJ4R_2xMxZBU7IzYK4SmxW9svlZoCYoZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/172556ab59.mp4?token=KgGBo7upYbmXBRbMhChbgZwUoUyOz_9EDnoy3Y1AYYVI7-UhgdZnVw-xCeVFvp-G70kzbq5yVpIwLKt6SOfeMuQSuPiMG-JjyEDPgb2ymABuHfFev7qBGxaOCI1__r2Mjruj4vtcOF0jtg8eLPbmg9TQ2MOyexD8KEFyVzEorRwHR5IdbXink1O_ZxrcJHEdZtd9_0RhaumBbafO43IEuT4DObHW1bt6NjFh5ktWat_UxCfIN3WW6I9kYCMUQDjXijJHmW1Dkq5e4qzSFClus7RPKGqM6qG9qm_0L_q-QG3hsd2o5y8WRlJ4R_2xMxZBU7IzYK4SmxW9svlZoCYoZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادق خرازی: نهادهای اطلاعاتی باید پاسخگو باشند
🔹
برداشت مرحوم شهید لاریجانی این بود که بعد از جنگ ۱۲ روزه آمریکایی‌ها به سمت جنگ نمی‌روند.
🔹
بعد از آشوب‌های اجتماعی دی ماه ایشان هم به جمع‌بندی من رسیده بود که آمریکایی‌ها هدف‌شان این است که بخواهند تهدیدات‌شان رو عملی کنند./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/673836" target="_blank">📅 19:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgWTPkxWnt1oQvZUQdp5SQmDUFNU_WOKRLcIVfgiYqCL82VhbgOzlP6S6W8mt3PDkBB52ttPZGkQaCQvb_-i1r7eJq9KjAkywwadm0qw5kpRS89LTequpo4aLy8WjtJ6ITRHaJcmO8-UzANemF2M44JlXBeiGOE-kd17d7RM4_BsTSJZAAVpE0-KOz9XT7f4lc3ZAY32Y0xMqba94cM3s_LRuG4qW0pZvTyFIAPmv-KJVMX1i2V2f9kG97loQCYp3VvnWBbUiOksFuCMHc8h-heQbT-cpt45N3UiGe15veWBU2-HfscGKT5VB4P_spNrnKS1QV8FQJZ6BO399RnvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز آسمان تهران؛ شبی که جنگنده‌های ایران به مصاف «اشیاء ناشناس» رفتند!
🔹
در ۲۸ شهریور ۱۳۵۵، گزارش‌های متعددی از مشاهده نورهای عجیب در آسمان تهران مخابره شد.
🔹
دو فروند جنگنده اف-۴ برای رهگیری اعزام شدند، اما خلبانان با اختلال‌های عجیب در تجهیزات راداری…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/673834" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
واکنش سگ زرد به احتمال توقف درگیری‌ها با ایران
🔹
دونالد ترامپ در پاسخ به پرسشی درباره عدم وجود نشانه‌ای برای پایان جنگ، مدعی شد که مذاکرات پشت‌پرده در جریان است و ایران تمایل دارد برای خاتمه‌دادن به تنش‌ها دیدار کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/673833" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673831">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیشنهاد امتیازات ویژه برای دانش‌آموزان مناطق جنگی
مهدی کاظمی، معاون وزیر آموزش‌وپرورش دولت سیزدهم در
#گفتگو
با خبرفوری:
🔹
همه‌ ساله اتفاقاتی مانند سیل یا زلزله در برخی مناطق داشتیم که برای دانش‌آموزان آن مناطق، شرایط یا امتیازات ویژه‌ای در نظر می‌گرفتند.
🔹
از آن‌جا که شرایط جنگ به‌صورت سراسری و یکسان نیست، برای حفظ عدالت‌ آموزشی می‌توان چنین تدابیری را انجام داد تا این دانش‌آموزان متضرر نشوند.
@TV_Fori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/673831" target="_blank">📅 18:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673830">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رسانه هندی: موشک‌های ایران وارد نسل جدیدی شده‌اند
رسانه Firstpost:
🔹
موشک‌های ایران در حال ارتقا بوده و با بهره‌گیری از فناوری موسوم به MaRV در حال تبدیل شدن به سلاح‌هایی پیش‌بینی‌ناپذیرتر، دقیق‌تر و مهلک‌تر هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/673830" target="_blank">📅 18:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673829">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
هشدار ایران به بلغارستان درباره میزبانی از هواپیماهای نظامی آمریکا
سخنگوی وزارت خارجه:
🔹
هرگونه همکاری بلغارستان در میزبانی از هواپیماهای نظامی آمریکا جهت حمله به ایران، مشارکت در جنایات جنگی محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/673829" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673828">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71544cd353.mp4?token=dU65xmVGLRZLy60KFd8ap5TppCf5L-k81TvR-U6iO2HfXbZf_39hY9FtFWqsvOAPbuMw-rW5ShRp35yGTUBefVvAoLpPZ8KikuyZSYgBAYWEw016YVSqigRMOa4AZ9QcdQi0Q1MZKbptjHEhV4T5_WFuUUGthmPsQBiNwUq7CiCecOkJ7_qPUnFN4EJIncrI5435oEEIgLfP5TWmy6Z6RRRGOhBba18tSsX2_VdkdcI6xCu6cEzvSgPco1PwEAac5zRBWVH7quIuGCASSGDa1y-e1PN76WnL8ENkXlLkLTPlZ7_-V_c3G13aY034ofllAd5BRf2IWtzO7ZuOkt6-0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71544cd353.mp4?token=dU65xmVGLRZLy60KFd8ap5TppCf5L-k81TvR-U6iO2HfXbZf_39hY9FtFWqsvOAPbuMw-rW5ShRp35yGTUBefVvAoLpPZ8KikuyZSYgBAYWEw016YVSqigRMOa4AZ9QcdQi0Q1MZKbptjHEhV4T5_WFuUUGthmPsQBiNwUq7CiCecOkJ7_qPUnFN4EJIncrI5435oEEIgLfP5TWmy6Z6RRRGOhBba18tSsX2_VdkdcI6xCu6cEzvSgPco1PwEAac5zRBWVH7quIuGCASSGDa1y-e1PN76WnL8ENkXlLkLTPlZ7_-V_c3G13aY034ofllAd5BRf2IWtzO7ZuOkt6-0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درب‌های رمزی در بندر کنگ؛ میراث نجاری قدیمی
🔒
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/673828" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673827">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5Cha6FbafzcyaOs2Cdnt4DVfUerVxLvBhZVWHZERqEKlkouVenCnBY7Ka0GzkASW-TSYx8zseaqqXaAMj8SwyY69UsnlbLDNnKrTjy1Yn9LaJC-TWp71dwKKt4Yd9k9n8HRDx-VTqexh2OixKZhXdjhGoNVhsuivESraOX83c56AxrdLdOY_hIAWyrH7DKMb7Z5jFSpSVgzjJ6Rs_b8-c36RshdVOX69fg82e8XkSGGwH9kEUDllKE2YJUclfNxMNw9s7kkiRK-N5WDqJIQrcnAZOOR-LIdhtx310UBIF6qDdaz6VlyU189wuV2DaUTM2OxkI_y14bgv3jjkn6Jnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت ۱۴ ماه نقش‌آفرینی بانک صنعت و معدن در توسعه‌‌ی‌کشور
🔹
بانک صنعت و معدن در دوره ۱۴ ماهه منتهی به پایان اردیبهشت ۱۴۰۵،  با رشد شاخص‌های کلیدی عملکردی، مسیر حمایت از تولید، توسعه تأمین مالی، تجهیز منابع، گسترش ابزارهای اعتباری و پشتیبانی از اقتصاد دانش‌بنیان را با جدیت دنبال کرده است.
🔹
این اینفوگرافیک، مروری بر مهم‌ترین دستاوردهای این دوره و روایتی فشرده از عملکرد این بانک در مسیر نقش‌آفرینی برای توسعه کشور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/673827" target="_blank">📅 18:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673824">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163ba97ea2.mp4?token=L33CseHNS8KIKTn7CPPw002Sh7jY5mUzkFOc5A71_yspL7ymZt-K6PXiHVnss_XN2g98KHQMLKhkSc5mUa5RRL1AxToE6DZx6RlpIRBKpvpypZRrNHEyL6_hFwKJpbG3Va4hGwjW15Nha4l966thNBA5XBiZVpjC6OO-XbK1gcKysMQl0Qg5QRXZm-UpPRl6zf6kwfRe9-En5oNc-9IUtf8Y_A0BnMfa_lWWcUS0vB2HcbPaXkkZkcKSrgiEiHzuNeUprJMmFexXZLz7REJx-lGGqkZM8UG58cApNvh0iGRnEOC00GqJvwynSetp8emDzEx84uWmPVOsRVuC0dv1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163ba97ea2.mp4?token=L33CseHNS8KIKTn7CPPw002Sh7jY5mUzkFOc5A71_yspL7ymZt-K6PXiHVnss_XN2g98KHQMLKhkSc5mUa5RRL1AxToE6DZx6RlpIRBKpvpypZRrNHEyL6_hFwKJpbG3Va4hGwjW15Nha4l966thNBA5XBiZVpjC6OO-XbK1gcKysMQl0Qg5QRXZm-UpPRl6zf6kwfRe9-En5oNc-9IUtf8Y_A0BnMfa_lWWcUS0vB2HcbPaXkkZkcKSrgiEiHzuNeUprJMmFexXZLz7REJx-lGGqkZM8UG58cApNvh0iGRnEOC00GqJvwynSetp8emDzEx84uWmPVOsRVuC0dv1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترکیب جادویی آب داغ، جوش‌شیرین، نمک و کمی فویل آلومینیوم برای تمیز کردن نقره
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/673824" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673823">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6oqqmyOWxcre_R4rNm2mvClJDqrIlEHE6489iEI7_bgugSHA_S6NYQswXjH1ybQtXrZAXuTg25Z3BKqs3YLaVzD875yUOL_I-fNY6hcT2hlHYTCccLiro-Wx6od8qVdDjaEeTKwwaXplEDOtiMULJYNV-Ta1Y5uT0AwLrS7aAorlqsq3gAZ2oOY67BJKs0lp6sfva63OjJ3DRCeonhRzUyuIVS8xWton3U94qQMppciXFFp_wkSFXPL2TH8HGYayIhwEl1fKlcNmvALm45XXHnRA5Wnfr_9Rm661BBtuGL9MaRzyc1QyzDQs_xJ3GbykF2bSq2PM-wLkgQ2_VjYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بلومبرگ از تردد نفتکش‌ها در باب‌المندب
خاویر بلاس، تحلیلگر بلومبرگ:
🔹
برخی نفتکش‌ها در نزدیکی تنگه باب‌المندب تغییر مسیر داده یا سرعت خود را کاهش داده‌اند؛ با این حال، اکثر نفتکش‌ها همچنان به تردد خود در دریای سرخ ادامه می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/673823" target="_blank">📅 18:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673822">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9Z6k2Z4MBPMnOWIv09VbYXb11ZSQySsNT3--7cTUdsIzYG31H0VVvmLXFJrMNM1UHBWEuTHSzIvIB4Y7ii0uPyUwUzOsj9Jp65vsmIw1GaFF1WG1lQk7wDed_9sQXIV24Uy0_hCqTY8poZIddDgk9WoBkkpCSSAE3ir1GW5LG0T6awZHWSopwVzxNi3VJgcXS3hkv1b1t2DtuZFFqvmauwBb6d1eh2mwBC50tTnB_S_e7U4yO368BHYxcmZktC49EjTXUC3lBbTPvjLzoQtA8SS0Movp-4-IN-sy98Za_qFUKaiFT5ArM8739KHjA9wTf1FGNpA5rIwyw3m0qKplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیسعلی دلواری؛ مردی که جنوب ایران را به گورستان استعمارگران تبدیل کرد
🔹
وقتی ارتش بریتانیا به سواحل جنوب ایران یورش برد، رئیسعلی دلواری با تکیه بر غیرت و شجاعت، پرچم مقاومت را برافراشت.
🔹
او با جنگ‌های چریکی، ضربات سنگینی به نیروهای انگلیسی وارد کرد و در…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/673822" target="_blank">📅 18:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673820">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAvid Academy</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THfIP6__fvJvBV6GaGb5Hk6OZV1SpeKg2rhYiKLBysOI95aw19kOlH1SucgN3Gszm1A7HidpkxqDIyC9BIz3l5hJj9kYYPU5YTu-tLXFT31bsj3SJaJQlueOHnDPBoOM0uHmFDSDQhznOesv4Wp-A4FSSCtVT4_2a66IycwNwzG0Yxpju5GSkTUQjNBDn7rBA3BWGGKnuS3RYaRYl72VEmZMTrXNdteVhIqREatHTAF0lg9_cc5Aw1TWLOf6NqSl0d3UBM4-pbTPob3mYvlAEFY3fcAwS-TsvDCWosz5Ojv2L7wL5wm-wsxB-eNjf7d9YmSv3HgJ_6GyMLXGm3Qqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادگیری خبرنگاری از اساتیدِ تراز اول!
🎙️
@avid_academy
@avid_academy
۳۰ ساعت آموزش تخصصی با مدرسین هلدینگ «خبر فوری» و «اخبار مشهد»:
👤
محسن ناهید
(معاون خبر و مدیر تولید خبر فوری)
👤
سعید برند
(سردبیر اخبار مشهد)
✅
فرصت ویژه:
امکان جذب برترین‌های دوره در هلدینگ رسانه‌ای «خبر فوری»
🚀
شروع مسیر حرفه‌ای شما از اینجا کلید می‌خورد.
برای مشاوره و ثبت‌نام سریع:
📞
09981897105
@avid_support1
@avid_support1</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/673820" target="_blank">📅 17:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673817">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw2F5hg_KCejZk5eOl3G7S41LfCW_r67MkDNwMklDGZxHUbq3fAMi8_3j3CjZ_QxRua--be7k3bY5k1ZQ8DHLBqqcQwOmf0RJtZpQ3A_eXKI7C23sSRqOpIteuRHkKDXUSG5xJacgqmpw8XGAdYuevhFS-rPON5d4_QwVFJQb4JgaEpl26VtU0_7ULJVuIQTLAJlV7Y49IS3YRMfvZ-JxjqF69OtkGSqs3-K2_20lyNmaCwGAQHRKl3t8gfKcexi0BXC5qNcTXpPaep540zxAlk-WqtJ9uTy9hSmXDt6JQhu4OwiBTmlFaS8Fk9oi_AbTSDWenuKbh6VEoaOCivscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت ۹۱ دلاری با بسته‎شدن باب‌المندب
🔹
پس از بازگردانده شدن دو کشتی پاکستانی حامل نفت عربستان، قیمت نفت به بالای ۹۱ در هر بشکه رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/673817" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673816">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6973d0cf51.mp4?token=I6VtBJrPyUX2bCFHr54KJVYddtrCrdgBLEWh6aaAwRLPgfQwCpPr851tqwVB3IWVHkvPnjjIHuSU51VRXOetFJCkVKDY17hKD2KU4KjUJcL1iExXirfeYq0NJ37rIYqlcCjGe0Qy9SpPKjqQMtdRrhIFMZZTli4C2SmZPLfHHPonKPIVT7gfJB8vy2wqWweZx95RMx-mwR-O3JDmfQYnh3S1k_i5BRfEts1_5oRkf80lGNwgdg2qMvMOOEdhVrNop0Y6qjrMkmpGBr3bL6O6kxWMDHsdN4X1lDKuXnrszSgJzfmZhxOGRG_DUVU9x-vmmvzRLl4JqkwrDmrBnGaiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6973d0cf51.mp4?token=I6VtBJrPyUX2bCFHr54KJVYddtrCrdgBLEWh6aaAwRLPgfQwCpPr851tqwVB3IWVHkvPnjjIHuSU51VRXOetFJCkVKDY17hKD2KU4KjUJcL1iExXirfeYq0NJ37rIYqlcCjGe0Qy9SpPKjqQMtdRrhIFMZZTli4C2SmZPLfHHPonKPIVT7gfJB8vy2wqWweZx95RMx-mwR-O3JDmfQYnh3S1k_i5BRfEts1_5oRkf80lGNwgdg2qMvMOOEdhVrNop0Y6qjrMkmpGBr3bL6O6kxWMDHsdN4X1lDKuXnrszSgJzfmZhxOGRG_DUVU9x-vmmvzRLl4JqkwrDmrBnGaiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
هر آقایی یکی از این جاروها توی ماشینش نیاز داره
👨‍🔧
🎥
برای دیدن کاراییش ویدیو رو حتما ببین
❗️
قیمت با تخفیف
❌
فقط 899 تومان
❌
✅
سه روز ضمانت بازگشت
✅
پرداخت درب منزل
🚀
عجله کن! لینک خرید اینجاست
👇
asrefardabale.affdn.ir/lead/44273
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
asrefardabale.affdn.ir</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/673816" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673813">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای العربیه: ترامپ از نخست‌وزیر عراق برای میانجیگری میان ایران و آمریکا کمک خواست
منابع آگاه به العربیه:
🔹
واشنگتن به نخست‌وزیر عراق چراغ سبز داده تا با تکیه بر روابط بغداد با تهران و واشنگتن، در تلاش‌ها برای کاهش تنش و پایان جنگ میان دو طرف نقش‌آفرینی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/673813" target="_blank">📅 17:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673810">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTgermHOrJ9FMWP2F1Hw0lElWiXS7dvzTQQJxC-Uknxqph8Gk2BwMBdbh7bgv6hUDq_soFczbxWg13pxZVTNOjy-QKzuCHdNhJiMhbfxxwGxJFB5UZ65WJVi7Axd2D6KDZXWXjtzAQzycvlI1DqXKmD6Kdub8PzUINU1yQcUfrGBC3FhakI5VHdS639mpD9nMWg6dKQr3_PJh9WC-eQVaN2aPNXJs4pGdA_WIQ37J4CwrYPGQyC2gWGLE4q5FAOJPaSesIL55uw_M4WdkmKAJrt-YAZmSZYx-S5Pdiknaze3u15K9saOepWydJnxXJtEyYP0xWB3HYeZm2Kto8fWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nI9M8Hl9fbG3oK_3PMAbv4t4S85l1zG0Rr3l7l4F_013WdgzCD3rYuQQvz_aZKlrEgcdrAzDF7_XwTMLmZ796xHWcwAHHRKYs1wFghsXHDKONhMkESjBYoadG9kF-0AbPaZ_okYB69ajG3iCCVklfrfBgxs5bObjBDoZ79aqbau_84dT0R6WoUDDWJ2JbgwaEjCAfKhXSK40X-W-wpjEC2-2QKUPQpagoe6MFVaNTCd7xqky6ppFLj7g2N-kBfy7nfc04ZKV8ncqL3ObEa4haiYA5aO-fLk7TxBU3hC4dZWlStmkaEhiZUdvp_uCTC-2PjO5SN_OpGs5BLdGrFBsgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaslKmFLQ7kuXALvtsY5BpdS_G__EuJLge0FN8FVMwlqH7suNUKmshHg7oDyMOlB8ECMAz4b89CIUQBusL1_KyvWZzlrAjVbYHzRgSb6vy1qBaZSSouNyOYM59mjSnY6KBNAbrYnHttcZY_FA0XdQB12uZc1h1yJ_gUfzZW6bhmf9T1uOlqr-vleHngeejZNJEW-0D-dJ_DfxTJZGom1BGGQWUXd0453kHR9reEz5LowTvnN1vQirMPiNl3-lgIQs5glRj1KMRhxtvfdXOMkLyriphjdTlkykgk4g_RmZ3ePwt8A-fjJYkYhjjTapxc_AxcH61j6ehnwMJMAvA5MfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی ۱۵ روزه: هوای خنک‌تر از نرمال در مرکز ایران؛ شمال‌غرب گرم‌تر می‌شود
🔹
مدل‌های پیش‌بینی نشان می‌دهد طی ۱۵ روز آینده دمای هوا در مرکز فلات ایران و استان‌های مرکزی کمتر از حد نرمال خواهد بود و فقط شمال‌غرب کشور شرایطی گرم‌تر از نرمال را تجربه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/673810" target="_blank">📅 17:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
پزشکیان: صداوسیما فقط بخشی از سخنان رهبری درباره عدم مذاکره را پخش می‌کند
رئیس‌جمهور:
🔹
رهبر انقلاب در جلسات خصوصی بر ضرورت پایان این وضعیت تأکید داشتند، ایران در مذاکرات با محور بازگشایی تنگه هرمز گام‌به‌گام پیش رفت و با وجود تخلف طرف مقابل، دستاوردها فراتر از انتظار بود و نباید با سخنان نادرست این دستاوردها کوچک‌نمایی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/673806" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673803">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkcwgFcxK7cc2PA5cZclxZTtD6-Lzu5mQTJpBw6uSjvjfNGpCgRUGt_BEhSkjUHSw1-GTWuSgd0UFhnDX2uc48QP80dMUjBxp6V2hpl5w-S3MqdqhnrElrqHM8JLg0X0iDlAMjSBqBocDeyz0JNyrmsgxV9k1SCKF2exnPQEeCMBtsnhnj5wDfam8hI-2UOqVhlqXlULX6DMG3tktwbLh1k_GSoFvw2bKE8C-TkoGvIlC0qhJy8lfaCgwRb3KFSUQNc779JoZMHvnatu94n7YUbdq59oIszpi_TepV_SUvgZOHVJbImY-cqjsOmsuQ_PC2bd8-gKGLaUe6wrys0pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه آمار مسی و رونالدو در جام جهانی
🔹
لئو با اختلاف بالاتر از کریس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/673803" target="_blank">📅 16:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673802">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f52b27070.mp4?token=Fb1hoCPBIACRT8JEX0OMFNSvfYQhXmhRFwgGsFCu4d_jMP1iAinXPxjxPoxZF5aNula54-7Y909cUhK4qJXwdsRujFPa69d1aM7hSlPqtkepoEKhtoGEIkNeIzSXGeyNdN9MybBo6Oz5E10U0sC9YVvQ55cQU86j3K3rY9ZRz7BhGylJLRh7Isxc-Blts5zsXv2joXVMZd86JHyhxKLIaPK1ralGusuzpO02ItvtfErtiQEQuyvg5E7W7M0-TPfjZ2_7dN2GTbJPoA_2bNgj6K5eGGhc8ZdQhmi5frUjajjEgu1oRDeZHaY7PPVLm7penBHw3uV-JqEjMHlpJcWvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f52b27070.mp4?token=Fb1hoCPBIACRT8JEX0OMFNSvfYQhXmhRFwgGsFCu4d_jMP1iAinXPxjxPoxZF5aNula54-7Y909cUhK4qJXwdsRujFPa69d1aM7hSlPqtkepoEKhtoGEIkNeIzSXGeyNdN9MybBo6Oz5E10U0sC9YVvQ55cQU86j3K3rY9ZRz7BhGylJLRh7Isxc-Blts5zsXv2joXVMZd86JHyhxKLIaPK1ralGusuzpO02ItvtfErtiQEQuyvg5E7W7M0-TPfjZ2_7dN2GTbJPoA_2bNgj6K5eGGhc8ZdQhmi5frUjajjEgu1oRDeZHaY7PPVLm7penBHw3uV-JqEjMHlpJcWvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه بستنی طالبی خانگی با شیر پرچرب و طالبی یخ‌زده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/673802" target="_blank">📅 16:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نقشه گروه‌های تروریستی/ احمدی: مرزها به‌طور کامل تحت کنترل هستند
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
گروه‌های تروریستی خیلی وقت است به‌دنبال فرصت برای ورود به کشور هستند، اما جمهوری اسلامی هیچ فرصتی در اختیار آن‌ها قرار نداده است؛ آمریکا در برنامه‌های خود روی گروه‌های تکفیری حساب باز کرده اما نیروهای ارتش و سپاه آمادگی کامل دارند و مرزها به‌طور کامل تحت کنترل هستند.
🔹
بر اساس اطلاعات موجود و گزارش‌های دریافتی از مناطق مرزی، هیچ تحرک جدیدی از سوی گروه‌های تروریستی یا تکفیری مشاهده نشده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/673800" target="_blank">📅 16:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyxvIyr4mV0lCVdZVcqrUxntK3Yf21L9TNDDDZI-PxgGOYNXqO5jeJb6hZ_7xghNflZ0RTgsn_eEXtuhcGgcMJD8F9ND1YpPrRaSsoOcQ5CMlQ62rH5VhGWc7RLdFaxS-XeOjIfYG0RYo5eAzitUU9zDfCL6LqTpny8zh2bmSVtpuuZB2eGagQnrPkKfefQr9G5ppSBQbprbQOQRvKRpaBoaVsEnL68wMG7WonvRqiCSwlBdX8ET8CGkG8QSQcRoP1p0ZFwVZLunrkj_9N07qIUAiJWob4kb7eBLgDqzwaWHwCB1pu5tFVSxBNZy409WIP0nuNkxnz4a93k850avmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور اهالی فرهنگ و رسانه در دل جنوب کشور
🔹
با حضور چهره‌هایی چون علیرضا دبیر، سعید حدادیان، یامین‌پور، خضریان، حسین پاک، خانعلی‌زاده و جمعی از فعالان فرهنگی، رسانه‌ای و اجتماعی، ویژه‌برنامه‌های در جنوب کشور برگزار شد؛ حضوری برای روایت از همراهی و همدلی با مردمی که این روزها داغدار حملات دشمن هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/673799" target="_blank">📅 16:29 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
