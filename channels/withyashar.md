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
<img src="https://cdn4.telesco.pe/file/KvRRoHMgctw-ifpnNZYr_KLKb5rpm2pTmX66vDC0J0qK6iRlWdtDeLzwgBjF7fiNfyheALMoGH4YtyQXF0INRppfl3cAeXBiPIXTy-FeZuT4Akf4XCwi2YUJQF-pQtCzVxZNGVR9T_dWhwSSvP8CB786wbwM7mBBucSE5XA6MFBke3Ekr66wq03nsshsVhLnipybK9hnp8hncrGUxx7734BkrK2rUS8O9206PDLlkPdVmSiO6YkdPfgJAB556-yHtqmrDGbPJJ6tZMUPAH47ExE8hTTxCEYjqd9PllPaJibXTf4L_AoxyTBhuMgo0d52vZCspEL0wxbEeGucv1_0cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 371K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 17:32:06</div>
<hr>

<div class="tg-post" id="msg-17601">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ درباره جانشینش به NBC: یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه @withyashar</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/17601" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17600">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ درباره جانشینش به NBC:
یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه
@withyashar</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/withyashar/17600" target="_blank">📅 17:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17599">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ به سی‌ان‌ان گفت: "دیروز ما با ایرانی‌ها به توافقی رسیدیم و آن‌ها از همه خواسته‌هایشان دست کشیدند. اما ناگهان، بعد از دو ساعت، یک پهپاد به یک کشتی حمله کرد."
@withyashar</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/17599" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17598">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دونالد ترامپ به اتاق جنگ با یاشار:
بنده این توفیق را داشتم که پیکر شهید گراهام را بعد از شهادت زیارت کنم. آنچه دیدم کوهی از صلابت بود؛ و انگشت دست ایشان به حالت فاک درآمده بود.
@withyashar</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/17598" target="_blank">📅 17:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17597">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f6b3525c.mp4?token=ObGlEiWeeY-aUM9LBhB0OjGnkRY1NUf9NUBhiPP3a4B0nFYXczyLwJCyMDGj3UOBoEgaYftpOWZUkuhl9H-rW-8SH3ogL5RGKDmGhPKMq76ZuBXTuNbccMJnrm5NQifKdppQyEpZ7UQGgzBIPcVT77iIbopoBezofjfBomh5h6PzuG4zw5arFu5MW_EWv9Z4J62yPvdYXYHhGxZXzVfXOvYriG4keSKNu6o3O5SkLB4LZOWnY7lTakMW83Q3uhtNhqDOjwzX_EpDF9RJtuV7SO4DONuM8wNhkzVKqEeL_1WlgHDOOdSiLqgq3irrK98vQYUCVvxSpFgBJ67pL4CBcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f6b3525c.mp4?token=ObGlEiWeeY-aUM9LBhB0OjGnkRY1NUf9NUBhiPP3a4B0nFYXczyLwJCyMDGj3UOBoEgaYftpOWZUkuhl9H-rW-8SH3ogL5RGKDmGhPKMq76ZuBXTuNbccMJnrm5NQifKdppQyEpZ7UQGgzBIPcVT77iIbopoBezofjfBomh5h6PzuG4zw5arFu5MW_EWv9Z4J62yPvdYXYHhGxZXzVfXOvYriG4keSKNu6o3O5SkLB4LZOWnY7lTakMW83Q3uhtNhqDOjwzX_EpDF9RJtuV7SO4DONuM8wNhkzVKqEeL_1WlgHDOOdSiLqgq3irrK98vQYUCVvxSpFgBJ67pL4CBcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید ، به دستور ترامپ پس از اعلام خبر درگذشت سناتور لیندسی گراهام، پرچم خود را به حالت نیمه‌افراشته درآورد.
@withyashar</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/17597" target="_blank">📅 16:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17596">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: تنگه هرمز باز است.
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/17596" target="_blank">📅 16:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17595">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سنتکام : ایران کنترل این تنگه را در اختیار ندارد.  تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/17595" target="_blank">📅 16:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">😞</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/17594" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سنتکام : ایران کنترل این تنگه را در اختیار ندارد.
تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است.
نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ می‌شود، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران.
ایران کنترل این تنگه را در اختیار ندارد.
ترددها به روال خود ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/17593" target="_blank">📅 15:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">@withyashar
⚔️
شمشیر زن</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/17592" target="_blank">📅 15:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سر صف
😁</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/17591" target="_blank">📅 15:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTheFarhām</strong></div>
<div class="tg-text">اقا توکلی یه انرژی بده تروقران</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/17590" target="_blank">📅 15:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSepehr</strong></div>
<div class="tg-text">هییییچیییی داداش
😂
😂</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/17589" target="_blank">📅 15:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طبق گزارشات بسیار زیاد شما تو دایرکت، به تعدادی از مراکز نظامی شهر های بزرگ حکم تخلیه داده شده.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/17588" target="_blank">📅 15:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چراغ سبز آمریکا</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/17587" target="_blank">📅 15:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لارا لومر،خبرنگار آمریکایی نزدیک به ترامپ :سناتور گراهام یا توسط روسیه یا توسط سپاه حذف شده و مسمومش کردن
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/17586" target="_blank">📅 15:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سیاست</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/17585" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">من اگر تو (تیم خیلی نایس) شاهزاده بودم الان یه نطق مینوشتم با توجه به تهدیدات اخیر جمهوری اسلامی و انتشار لیستهای ترور و مدارکی که موساد به دست آورده و مرگ ناگهنی لینزی گراهام آتیش به پا میکردم. افسوس…</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/17584" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/17583" target="_blank">📅 15:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17582">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/17582" target="_blank">📅 15:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">باید تا میتونیم مرگ لیندسی گراهام رو در رسانه ها به جمهوری اسلامی مربوط کنیم منظورم جهانیه نه تو ایران(توییتر به انگلیسی) ! همین کار رو تندرو ها با تختی کردن که خودکشی‌ کرده بود و سینما رکس که خودشون آتیش زدن و گفتن ساواک کرده و از دلایل های بزرگ انقلاب ۵۷ بودن ! چرا ما نکنیم !؟ این فرست ها کم پیش میاد.. بزن بریم ! تازه این بار بعید نیست که واقعا روسیه و جمهوری اسلامی باهم کرده باشن !</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/17581" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18fcd6ecd.mp4?token=G3hwoKfs1FeEPcAVJj3OWVJpXWgdRVf-3WUf4AC61KN16xq0_WHhvahLY9sdWJT7oBpO-DegYkS6IfCBWUSpBJUx8Bpo-i6bdv7JlON9BJjFeVWafN0WKqSV7dJsIXO2-Tf-Uqrw1U-J1b86Z-zmpiGH4uBObXtkdO7hdyLt2j9trjsqMO1yBfN9HSR8C7mk_P3k4NFaw6tfhgAJTQfiDKK2snHRx4VRswvxNM9zGNJB8jFXGs04LRQF0aN75LooVg62CoWuRSSf-BLokr7mpKoymjWUjw5_mnDPtMTZqOULHdV9taCQ1wYBFL48BYDHf4jBP9EQAToWbq5lvEIGwmyONyP8ufQJwNpHHdJ8c8jNQhyzuav2h9glXvsbEACmQ_SVX8W-_naSMCzdcwdK3BtJF68BCS_2xAchdkIpkrmohp9N8OzHNklpbhc1KvvChIoRKZBYGdm_7BAgF48EgqPsO_91pUybmkexVcSCZq3VjddfBGSEI92Y8rFXxW_R0nHJPz83scyVHsW9sCAeBn-c4TRvsi53ZxRkIFxKANUVmxfEdpoJZlr4BSpbkLtx0PH2LOiXGCrd-DLl7m8ZsJAbL9bkFkzjADQWF_F9yjT0a0OdamWYOlluXY1HAaiHpoDV5YZrlBWMEjKRbIwHj3_Gy12K7nSM1-3tCYSZfGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18fcd6ecd.mp4?token=G3hwoKfs1FeEPcAVJj3OWVJpXWgdRVf-3WUf4AC61KN16xq0_WHhvahLY9sdWJT7oBpO-DegYkS6IfCBWUSpBJUx8Bpo-i6bdv7JlON9BJjFeVWafN0WKqSV7dJsIXO2-Tf-Uqrw1U-J1b86Z-zmpiGH4uBObXtkdO7hdyLt2j9trjsqMO1yBfN9HSR8C7mk_P3k4NFaw6tfhgAJTQfiDKK2snHRx4VRswvxNM9zGNJB8jFXGs04LRQF0aN75LooVg62CoWuRSSf-BLokr7mpKoymjWUjw5_mnDPtMTZqOULHdV9taCQ1wYBFL48BYDHf4jBP9EQAToWbq5lvEIGwmyONyP8ufQJwNpHHdJ8c8jNQhyzuav2h9glXvsbEACmQ_SVX8W-_naSMCzdcwdK3BtJF68BCS_2xAchdkIpkrmohp9N8OzHNklpbhc1KvvChIoRKZBYGdm_7BAgF48EgqPsO_91pUybmkexVcSCZq3VjddfBGSEI92Y8rFXxW_R0nHJPz83scyVHsW9sCAeBn-c4TRvsi53ZxRkIFxKANUVmxfEdpoJZlr4BSpbkLtx0PH2LOiXGCrd-DLl7m8ZsJAbL9bkFkzjADQWF_F9yjT0a0OdamWYOlluXY1HAaiHpoDV5YZrlBWMEjKRbIwHj3_Gy12K7nSM1-3tCYSZfGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر مارک سیگل: پدر او هم وقتی خیلی‌جوان بود بر اثر حمله قلب فوت کرد احتمالا پرواز های زیاد و پرواز
اخیر
‌به اکراین باعث مرگ ناگهانی است
از سوی دیگر، همیشه این احتمال هم وجود دارد که یک عفونت ناگهانی رخ داده و به‌سرعت شدت گرفته باشد.
همچنین، همان‌طور که اشاره کردم، پرواز طولانی از اوکراین می‌تواند خطر تشکیل لخته خون را افزایش دهد؛ لخته‌ای که ممکن است در پا ایجاد شود و سپس به ریه منتقل شود و باعث آمبولی ریه گردد؛ عارضه‌ای که می‌تواند به مرگ ناگهانی منجر شود."
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17580" target="_blank">📅 14:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">علت مرگ لیندسی گراهام ایست قلبی اعلام شده
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17579" target="_blank">📅 14:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشحالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17578" target="_blank">📅 14:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تسنیم: جمهوری اسلامی پایگاه‌های آمریکا در ۵ کشور رو هدف قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17577" target="_blank">📅 14:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تسنیم: سامانه‌های دفاعی سپاه پاسداران انقلاب اسلامی، یک موشک کروز متعلق به دشمن را در نزدیکی شهر خرم‌آباد در استان لرستان، غرب ایران، منهدم کردند.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17576" target="_blank">📅 14:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرنگار هرمزگان :
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات آمریکا در استان هرمزگان شنیده شده است
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17575" target="_blank">📅 14:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مرکز امنیت دریایی عمان اعلام کرد که
به درخواست کمک یک کشتی تجاری با پرچم قبرس که در پی وقوع حادثه‌ای در نزدیکی سواحل مسندم قرار داشت، پاسخ داده است
.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17574" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : سناتور میچ مک‌کانل (۸۴ ساله) هفته‌هاست از ۱۴ ژوئن به دنبال یک فوریت پزشکی نامشخص در منطقه واشنگتن بستری شده است. دفتر او تشخیص یا دلیل خاص بستری شدن در بیمارستان را فاش نکرده است، اگرچه گزارش‌ها حاکی از آن است که اولین امدادگران برای نجات یک فرد بیهوش به خانه او اعزام شده و احیای قلبی ریوی (CPR) را انجام داده‌اند خبر مبنی بر چند ساعت پیش فیک نیوز است
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17573" target="_blank">📅 14:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرضا میرعلمی</strong></div>
<div class="tg-text">عمو یاشار
انتقاد دارم
شما هنر ظریفِ به تخم گرفتن رو نادیده میگیری.
بیشتر روش کار کن لطفا.
این عرزشیا میان دایرکت ی چیزی میگن پای ما ننویس. فقط دایورتشون کن.
عشقی
❤️</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17572" target="_blank">📅 13:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شبکه 14 اسرائیل : ایران با کارتل مکزیک رفیق شده و بزودی خیلیا قراره ترور بشن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17571" target="_blank">📅 13:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSCfNshhJcEZsbexzIxRECZQvYtnK0UPSvJxbAU9VgqLEvXnJ2fcGbyS_mT7vI2gOJ91BwiuW0awSwnv-HqffsXdAHfTh2AMAhV0PZrTkml12clw-Ho-_i5E30qVEuOUeaqfUZMqD4oGYJEcfIerSsvsoDbVzzkOPJSUkJcnlnocY6ZT_sWNS7-TkZZfqVZnxmwKf7zjFpMpDLS7azwE8LEbgOTxrLVo_8yAsYypFCCqDwjgMYF-8rRpOvPf_4yAopt1hUn_S-2euekJYIJwDmtS_tfJOHnX1C4D3fjvllqpJDCJP6WxsUqYncTGWwe9s6usUVLoC-_-4XW_zy6ctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fb5sLcjV2CDwW_Gz1fTDbsUXKUZKa17aDQC6XZZxNLybtJOTDaHTorYm3l_-XL59ss0_DdO83JDZBnXiWkC6fSlmzdpdHdM5ommiyLKGUqFQF5uLxtQxDU3lwb73xskN4BwhoCDsLF_t4wA6aRS3csPrp9u4-63EwFPKY55np7xZpHh-qrmx8RlXagMPzHAW2N30rb9jcDA24TbE26cfU1-Goy3LlyvLJJeClf9TEXfbogztfTPQPrDDkUqMf2Ud7dvIxZmQpat1aS2tetp0iEuAj_rn0jDJ2P6NXZUB-D9fYaLyl9FxPsZyc521iSrJV6G3bV_JEQB8Pj-ix38xMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPJGA6325aUiMJutYRlG4ojlL4A57MZPpDIWQu2-RUhqovOdUPw1OSE7Z3tPqcZEKoROX-8RPl4R-0_mvaBm2YYaxTpqlX-VukQ6rm6kGd7nRfyWKnlLBwPfa0XaYh9mLz7uZoIM3dWtIGu0bRTaTP2-TKb8rRXUGbfyNnwgz-IOQUmf9CeavoWCy18x1ulmK1Jn_obR9I7pkPO7wJLXKaahLKBSxitik97TyWZrIhGebUulOCbgOY0Xot386LzM3CmthYzAbVs-hcuIjS6c72GZ9fFxtIr5O2A3O08NytHdzJ3JpZhJ3nl59ahxORHqVB-0e8LifAWeh4iqKYPc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeEiThNZfzhk9C_ygQI-9cfHy_XjelEHkFxx6ZZW1elXs_oirfJqxnXS4j237QXZX0aUpI6txjGBP2L2CEir1GB2FxPZwJrWTU4WapREnv5eliF17vhD1YozIlMtJyIh0Gx_h6MPJc_kzGh8XeU_5cZDNXy1S3RKEV7m6EzU5zm8L-L0uRLu97Z5VCo3USwkJIw9X8wdUcz2L9ZxrLAZOURWOEDC_6ENBRxVfXdWFzG3ujvOdTXiHPfevj9pFl84pydpyQdj2JKhOLHKwLI753LpyPuxf_XxZNIER7Zqt_EjW82-98lAH0uqCOhshZS12nNFMOiCNrdPO_a1Y3yo7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب یه موشک بالستیک سپاه در لرستان سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17567" target="_blank">📅 13:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عمو یاشار گل ما اصالتا ترک هستیم و اسم شما عمو «یاشار» اصالتا ترکی هستش
😂
❤️
و برازندته خیلی زیباس و اسم یاشا هم هست و جمله هست که میگه: یاشیاسان یعنی زنده باشی یا زنده باد سربلند و پیروز همیشه موفق هستش</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17566" target="_blank">📅 13:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA®∆§|•^H</strong></div>
<div class="tg-text">عمو یاشار گل ما اصالتا ترک هستیم و اسم شما عمو «یاشار» اصالتا ترکی هستش
😂
❤️
و برازندته خیلی زیباس و اسم یاشا هم هست و جمله هست که میگه: یاشیاسان یعنی زنده باشی یا زنده باد سربلند و پیروز همیشه موفق هستش</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17565" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">همین الان پارچین پاکدشت ۴ بار صدا انفجار اومد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17564" target="_blank">📅 13:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4352950692.mp4?token=V1R2YR08oXmImkZSp9RBtP2JFHC2Ewr1GtSx75mRZqKIev6sO7mVqmL3vA3TU6XFPUHP6iCdIkhQMLHLsl_cisqhrlEoxvfm0pIqrYi8uDxIq6MIccTA4fP8vtv-ZiFp2zdiwLXDShuY1TWTowqzjfl5IITfj1IuJFsylRgr1tqd0WqAUmXO24lPI4x74sehL2k0HnNxloR_CI7iMOQPbfvNJI2Rc69-ucWyZRSTAr-HAYCssm2vtk_YCKZ9o_hyWhHYPNY4nyWVWZYvmD7jlhMPsrVTBc5If8ZUhdgOkxf_8ccJlSLrjZJ-VxFrgHEBHQ3vBcefryH46AGFcppEG6saAUe7LtT8gpi1d250IKAla3CY9ltzkI-841ZwG8SiQl5EXevNoFzmZLBKrwZTKKbBMbh93G-YySk5wiBoEvt6ggSr6iBKlR5pCHvEkU29WKKqpfA3GzDIILPwsQeIw0V51-Q8r2M3rpI96Dae04wrRc_lSxWo01T0qZUoN6Z7qzz2j1gL1RHjv5Lt-BPaUvOLl0k-4NZUDyG_XSb_ZEVRbZ9sSg9kox7y3wcA-x8pnybDojjVp6V20C5Rf04335NrOCtt1K7-kURL2oH6MAFcZjxenaVM7uVvtqGV-hNG0CAbAMus1zAdCqgFfRtwbvbb_4lahx9Zsb55_K9UYuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4352950692.mp4?token=V1R2YR08oXmImkZSp9RBtP2JFHC2Ewr1GtSx75mRZqKIev6sO7mVqmL3vA3TU6XFPUHP6iCdIkhQMLHLsl_cisqhrlEoxvfm0pIqrYi8uDxIq6MIccTA4fP8vtv-ZiFp2zdiwLXDShuY1TWTowqzjfl5IITfj1IuJFsylRgr1tqd0WqAUmXO24lPI4x74sehL2k0HnNxloR_CI7iMOQPbfvNJI2Rc69-ucWyZRSTAr-HAYCssm2vtk_YCKZ9o_hyWhHYPNY4nyWVWZYvmD7jlhMPsrVTBc5If8ZUhdgOkxf_8ccJlSLrjZJ-VxFrgHEBHQ3vBcefryH46AGFcppEG6saAUe7LtT8gpi1d250IKAla3CY9ltzkI-841ZwG8SiQl5EXevNoFzmZLBKrwZTKKbBMbh93G-YySk5wiBoEvt6ggSr6iBKlR5pCHvEkU29WKKqpfA3GzDIILPwsQeIw0V51-Q8r2M3rpI96Dae04wrRc_lSxWo01T0qZUoN6Z7qzz2j1gL1RHjv5Lt-BPaUvOLl0k-4NZUDyG_XSb_ZEVRbZ9sSg9kox7y3wcA-x8pnybDojjVp6V20C5Rf04335NrOCtt1K7-kURL2oH6MAFcZjxenaVM7uVvtqGV-hNG0CAbAMus1zAdCqgFfRtwbvbb_4lahx9Zsb55_K9UYuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17563" target="_blank">📅 13:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حمیدرضا دهقان، افسر پدافند دریایی ارتش ایران، در حملات آمریکا در منطقه جاسک در جنوب شرقی ایران کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17562" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17561" target="_blank">📅 12:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17560">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">معاون امنیتی استاندار خوزستان: سه شهر در استان، بامداد امروز مورد حمله آمریکا قرار گرفتند و در حال ارزیابی خسارات هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17560" target="_blank">📅 12:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17559">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری مهر :  شبکه ارتباطی تو کرمان بر اثر حمله آمریکا دچار اختلال شد
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17559" target="_blank">📅 12:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17558">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دیوان امیر قطر: پیکر حمد بن خلیفه آل ثانی پس از اقامه نماز در گورستان لوسیل به خاک سپرده می‌شود.
از امروز چهار روز عزای عمومی در سراسر قطر اعلام می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17558" target="_blank">📅 12:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgs0RShng0GKO54Y9Cg6rbW0OyodryFt8eGmsI0icu5uzT_2CYL1jjdabGQwFnIfnR4fInSbuJo9gLiHq5f0xbpMmF1IZFhAVMgxzWIC_wz00o2UoByw0AHpCvy-k277VD58C_izZZQ4zrS2JkABffmacTe4qQEJHvSgIeOl3yfbj9c-DVUiyUGd4-XENFj_b03C_GNrM_VFACZtlHCSqgXhztfOkLVgYhd1Ri_Da7em8g41zDu5eXLGNditqvU1U-b9kaYiaKHPqaEDTkg7cqIv39_OJYSP_cJq0jxW191dSnJuHZsZTRxZlfPm0cNj79iifAtTPnPCjJQJGyRPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب
🫱🏼‍🫲🏽
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17557" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هنوز تو شک ام
🤦🏻‍♂️</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17556" target="_blank">📅 11:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سرویس جدید رو فعال کردم اگه بخوام یک استوری حالا ۲ روز میمونه
😂
🙌🏾</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17555" target="_blank">📅 11:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17554">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شاهزاده رضا پهلوی : از درگذشت ناگهانی سناتور لیندزی گراهام عمیقا غمگینم. او دوست استوار مردم ایران و مدافع سرسخت آزادی بود.
در لحظاتی که نیاز به شفافیت اخلاقی بود، سناتور گراهام همیشه در سمت درست ایستاد. وقتی دوستان کمیاب بودند، او در کنار مردم ایران در مبارزه‌شان با استبداد قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17554" target="_blank">📅 11:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">استانداری کهگیلویه و بویراحمد:
اصابت پرتابه پهپاد آمریکایی به اطراف شهر یاسوج در ساعات اولیه بامداد روز یکشنبه
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17553" target="_blank">📅 11:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17552">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو: اسرائیل و آمریکا دوستی بزرگتر از گراهام نداشتند
نتانیاهو با ابراز اندوه عمیق، سناتور لیندزی گراهام را دوستی عزیز برای خود و اسرائیل خواند و گفت در آخرین دیدارشان به او گفته است: «ما دوستی بهتر از لیندزی نداریم.» او گراهام را کسی دانست که امنیت اسرائیل و آمریکا را جدایی‌ناپذیر می‌دانست و تأکید کرد اسرائیل یکی از بزرگترین دوستانش، آمریکا یک میهن‌پرست بزرگ، و خودش یک دوست عزیز را از دست داده است.
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17552" target="_blank">📅 11:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGQGN95Ty8FDK1R4SWWNlH8OYVI680TSunfehytAlIglalrNFuny3x5GDKnWVVsWEWPvA13DYqHteEorRsEiori2OHTZbCAcTo64YbNyU7-t0Pg8ru9yNvwiMlJNEFBhXhMCx3e04r691_OhHtNJf7y25T2TOKw8glvb0NnrYKcdmtZLMs_i-qzeaCa0ji0gevdkwwRfgrsUnwmKy3oIAyFVOFuTMqqCG3Kw8eG2Fg51VhRW8R3YTonRWhPMs6h_bVGsohOQq3u1ZQJpsH6fMosvi3NI_BAkLsGoggNLvv2FkFubwvWuSElof1CiWn8oy5qmxGPb01iKSUcVpoAlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشحالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17551" target="_blank">📅 11:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش وال‌استریت‌جورنال :  لیندسی گراهام نقش اساسی در متقاعد کردن ترامپ در حمله به ایران داشته!  گراهام مکررا به ترامپ تماس میگرفته و پیگیری میکرده و حتی به کلاب‌های ترامپ در فوریدا سر میزده  گراهام چندین‌بار هم با مقامات اسرائیل دیدار داشت و حتی تا تل‌آویو…</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17550" target="_blank">📅 11:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اتاق جنگ با یاشار : شکی‌ نیست مردم واقعی ایران و انقلاب شیر و خورشید یکی از بزرگترین حامی های خودشو از دست داد ، عمو لیندسی عزیز …، خوشحالم که به واسطه این انقلاب با این شخصیت بیشتر آشنا شدیم و همه با هم کامنت های زیبایی‌ رو براش‌گزاشتیم
💔
😞
او واقعا مردم ایران رو دوست داشت و یک آمریکایی وطن پرست واقعی بود
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17549" target="_blank">📅 11:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtWzDX9IFU6k3lvdgO8lfusPw-HqLalVQV0V0FkmI1FmJ0_xWCpWZJpD-5pBhuLIOWGLBbI4ytEM326gOYt8eB9bcps32LM7JhiaqbJCZyo1h2jcaOYfWDqyTww3ngDjKv0EgX2hSv3XHpfXb11U9z3J2Hf31fqCIBSEqLSxJv3tzvIzZXuLAIslINjsSBW4LzX1yDZIVILWQQIiTbrsu54cqMBdbtKf6k4Pde0wab_5agRsyRQ_kvoE4c3FTDamVhB00P_OQMNoW08HQ6-gq5sGFp7JOoorU4RGmkAeFnK1K5QaEc_qAyNLW0FngFXu-WrQ3Y5BIH4f1JpOIX3GlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود.
جای خالی لیندسی بسیار احساس خواهد شد!!! جزئیات و ترتیبات بعدی. خیلی غم‌انگیز است! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/17548" target="_blank">📅 10:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سناتور لیندسی گراهام در حالی ساعاتی قبل از دنیا رفت که دو روز قبل در اوکراین با زلنسکی، رئیس جمهور اوکراین دیدار کرده بود. او همچنین قرار بود تحریم‌های جدیدی را علیه روسیه به تصویب برساند!
دیروز هم از کارخانه تجهیزات جدید و پیشرفته بازدید کرده بود !
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17547" target="_blank">📅 10:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گروه تروریستی سپاه فیلم حملات امروز را منتشر کرد
در این حملات از موشک‌های بالستیک، سوخت جامد و مایع و نقطه‌زن قدر، عماد، خیبرشکن، فاتح ۱۱۰ و ذوالفقار استفاده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17546" target="_blank">📅 10:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صداوسیما:لیندسی گراهام به درک واصل شد!!
@withyashar
🤬</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17545" target="_blank">📅 10:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دو انفجار در فرودگاه بین‌المللی بحرین رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17544" target="_blank">📅 10:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دیوان امیری قطر: با قلب‌هایی سرشار از ایمان به قضا و قدر الهی، درگذشت والامقام، امیر پدر، شیخ حمد بن خلیفه آل ثانی را تسلیت می‌گوییم
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17543" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حمله به عمان، رأس المسندم هدف قرار گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17542" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp24jMPaZyg-JmR-SpF6xYWXUbQhWz4Kw5cY67gjDebEafi-hNzpOv5fpmSBCMqTADQog8Cn9LGINPlKW8u__48Csy8V6XXSXia8CpRIstjvt6RZR42pKqRX9kxL5X4PWTm3b44_i24wVjuDOU1DdP9z8xxbMsiv3k9NgkD8FOy0cgSCLZNbUJnWnluCynRIb3wJlgTPL9RgH0ylEZTNT7YM42YaeVtROzoAowVjccQ8fjS263TS5Whpn6VWhz1urukNFj92rsg_GdhJVFw1WaaqedTmqkQrWIs6quhlw6nyPki24mRaFvLmYEoSIdFzeMxHp6UERQbZOAm5g0dK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت لیندسی گراهام که دوباره وایرال شده ….
حداقل از یک عکس خوبِ من استفاده کردند.
مرا از روی دشمنانم قضاوت کنید
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17541" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در بحرین و کویت، مجدداً اعلام شد که آژیرهای خطر به صدا درآمده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17540" target="_blank">📅 10:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزارت کشور قطر اعلام کرد که سه نفر، از جمله یک کودک، بر اثر برخورد بقایای رهگیری موشک‌ها و پهپادهای ایرانی ، مجروح شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17539" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">واکنش ایتمار بن‌گویر، وزیر امنیت داخلی اسرائیل، به درگذشت لینزی گراهام:
«امروز اسرائیل یکی از بزرگ‌ترین دوستان خود را از دست داد. سناتور لینزی گراهام در کنار اسرائیل ایستاد؛ نه به این دلیل که این کار آسان بود، بلکه چون باور داشت کار درستی است.
حمایت بی‌وقفه، شجاعت و مواضع روشن او باعث شده بود میلیون‌ها اسرائیلی برایش احترام قائل باشند. اسرائیل همیشه دوستی، حمایت پایدار و تعهد محکم او به امنیت این کشور را به یاد خواهد داشت.
صمیمانه به خانواده‌ی او و مردم آمریکا تسلیت می‌گویم. یادش گرامی باد.»
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17538" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد اطلاعات اسرائیل نسبت به احتمال وجود طرحی از سوی ایران برای ترور دونالد ترامپ هشدار داده بود.
با این حال، این مقام‌ها تأکید کرده‌اند که تهدید ادعایی در ارزیابی آمریکا «کاملاً معتبر» تلقی نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17537" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تکرار تاریخ؟ سال 1979 نلسون راکفلر بعد از فتنه این سال در ایران، که شدیداً از شاه حمایت کرده بود، به شکل مشکوکی از دنیا میره. راکفلر دقیقا مثل گراهام هیچ بیماری‌ای نداشت و کاملا سالم و سرحال بود. و با مرگ ناگهانی (که سکته قلبی دلیل رسمی اعلام شده) از دنیا میره.
حالا گراهام هم بعد از حمایت های زیادش از شاهزاده، به دلیل مشابه فوت میشه
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17536" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لیندزی گراهام، سناتور جمهوری‌خواه ایالت کارولینای جنوبی، در سن ۷۱ سالگی بر اثر یک بیماری کوتاه‌مدت و ناگهانی درگذشت. نیروهای اورژانس پس از دریافت گزارشی مبنی بر ایست قلبی، به منزل او در منطقه کَپیتول هیل اعزام شدند
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17535" target="_blank">📅 10:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17534">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش های جدید از انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/17534" target="_blank">📅 10:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17533">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سپاه : ارتش آمریکا به تعدادی از پایگاه‌های ساحلی و برج‌های مخابراتی در سواحل جنوبی ما حمله کرد تا شکست خود در تنگه هرمز را جبران کند.
@withyashar</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/17533" target="_blank">📅 06:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17532">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سپاه : ما مرکز فرماندهی و محل نگهداری هواپیماهای بدون سرنشین MQ-9 را در پایگاه هوایی الامیر حسن در اردن با استفاده از موشک‌های بالستیک منهدم کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/17532" target="_blank">📅 06:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17531">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فوری،کان نیوز اسرائیل : واشنگتن تصمیم گرفته که محاصره دریایی و عملیات نظامی علیه ایران رو از سر بگیره.
@withyashar</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/17531" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17530">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بندر ماهشهر ۲ انفجار خیلی بلند
@withyashar</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/17530" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17529">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apG0ZOtLu6GBTGrPrDtcVwjP_qFbRmzf1EiMQpQgKe76UzhA2cYIDE8rt0QeqwN42jKtlntEk9TYzMi0mhA6h2DxKLmEAVaIcIXcj96Td68v_mFbVcc6vGUpWv3L8jpX52YMtKmYy5A7q-5nDHMVm5YcazF_GKf1z35UKMREYvd-Bsd3iVVWRhDYb-ZK0ZIjDQZbh-_9huPxnm1Tnxb8KO7EWx2siipqmmWXmV3jmRUfZNbpqt5wh0w7qlq_j9VZcZtXT2HNSSRDPWA8gtwX-FqFFWmi9IynAQA-cONeFVhyyDKt68Lxp--cGk8GWxc-80dEtb_P8lA2XofpugFecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار پایگاه نیرو دریایی کنارک
@withyashar</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/17529" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17528">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدا و سیما: ۱۰ انفجار در جاسک در یک ساعت اخیر و ۱۲ صدای انفجار در استان بوشهر شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17528" target="_blank">📅 04:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17527">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مقام امریکایی: هم اکنون موج جدیدی از حملات علیه ایران آغاز شده است
@withyashar</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17527" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17526">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">در مجموع ۵ انفجار جدید بوشهر ولی از‌
نیروگاه دور بود
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/17526" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17525">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۳ انفجار جدید بوشهر و جاسک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/17525" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17524">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6654096451.mp4?token=mpL19UMZxuQptKlAn1H4ud80bpkA-RkUP6x37Mz3kl0jB43XxKMrm4lX2pZl0ps2Jpjxkdlo8Yt3_cILQaozSHW219g3MOAmHT2QmhrWEivw_1qux_3Gblqlq5XB6OslO9-QtIbjOoWospL0bMbEcJ5XQtEj2u-uO-WyvxQIuQiLECw2YuMS18DrCZiP8wy6UT4ZHJRyMDb1_XrTjJBrjlobQcEPS98WQEmK3pLucNfUtVSYateRIc9HhgdpbFKD2LHfRGbhRHhBLpMNhiTqABoXjxJwrQWzPSLgrva1bxx1282QG7GBYmGikIZzi-Wl_F4iIujWGqleJ26XDHwXwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6654096451.mp4?token=mpL19UMZxuQptKlAn1H4ud80bpkA-RkUP6x37Mz3kl0jB43XxKMrm4lX2pZl0ps2Jpjxkdlo8Yt3_cILQaozSHW219g3MOAmHT2QmhrWEivw_1qux_3Gblqlq5XB6OslO9-QtIbjOoWospL0bMbEcJ5XQtEj2u-uO-WyvxQIuQiLECw2YuMS18DrCZiP8wy6UT4ZHJRyMDb1_XrTjJBrjlobQcEPS98WQEmK3pLucNfUtVSYateRIc9HhgdpbFKD2LHfRGbhRHhBLpMNhiTqABoXjxJwrQWzPSLgrva1bxx1282QG7GBYmGikIZzi-Wl_F4iIujWGqleJ26XDHwXwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدافند تهران
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/17524" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17523">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پدافند شرق تهران درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/17523" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYUST5WimqZa0sHzwTC_FKNLyxq5kCIinsnprM6sf5zrDjMpIcHezIJxwnYgla3VRrQuxt0xtyrfLkrcSkbZtE5X4Ji5ssTbvnvd3eYoILXUFSRXK9VkHcoDM2WBO0lOoH2MQuOYA__kBAP4hw01wkf3BX9QoAm-K2G0pzSvsL62D-T1L-vUQX3jhRFFXXYp9elK1xal_809FtnH7cs3kdRt3SmLzmPtWsOuwCuLOYSdYr8bgzcLrt5wPEuwtKl17BFZ-jSYf8-BedcoL-ob-EOxDrdJRvsxMjO3kCpdSlm-8BBTWnzxKuIBxciqR1fILX5Cke8UVgkfc_YAqhtSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnwYuSHdr5DQePM_NwI4pdEZhZoM0D879vnfnY_6gwNn5-TKqezjJcInLuY84xQ1xueZwJSFtJeCJgU9RJfILqmCERjrwCEofpqu4_hHlk7uzZ-lqbGCPqbLqL45Gj8Z7yIQjRtFbDSmwZcjcVjUHGeGn5LeGWQpZXHQq_25xO5aFT3grv3E7YoI31JuRYz99edXsc3GUnvA9zkW2HyFkvyPuihvlYVxXJZCKKEG6MwS0rAL7jYlKZPsm4ffZqRmqc-yxq8fVmjQfceIvzfihatlCaoQOcu7KtejFZ1MAX4Ajfl2V7I7c7KKeMtNazipd58435Bz_j2oRPBKsgw9kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم اکنون تهران !!!!!
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17521" target="_blank">📅 03:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صدا و سیما حملات به بندرعباس و سیریک رو
هم تایید کرد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17520" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXVp04QXqay5oRuAZotyJm68Xm9zTYNsWoHFWGhxX2R0niujOdNaDyJ1x418lz-hsnVWTbI0CGfu4CZrR8w612xqQBq8Apq-YLJukC11EJpe4d3IdydrJqvDbyiApClTY5hoas9AI_DCdzXKQfgEYMhiRUpTKh7z-DaK0Gyaqre5Cc3q0GE0YdQBPhLm_3Ds-oi7FXJckr8IZ_b_E3Bdo11XmNTOVR-7Ih-hh0lo9X2Hj314D1LlCBR8JDo3W8LV-vLtwWcsgZLwyrt07qW4eVqOeX_e7UsjlU56917RsFlluzIcoLhyD1RwOlb02py-gxRUuxnjXtwq_ey2qwOreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه دریایی در ۹ مایلی شرق عمان
سازمان تجارت دریایی بریتانیا (UKMTO) از حادثه‌ دریایی در ۹ مایل ساحل شرق عمان خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17519" target="_blank">📅 03:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qW0hjf6iXN_1hOiQmQgvIpDPZvVNEwITJZgMZmk4jZJ1O3a0UlD08c0bV4NUvNyy041gPtBMFmMWmoXpKIpuHgfbvaF7Y51YsO5I7tf2E6RfwzPTopzhTMFZucsx9Aq_6iejB-1SH-y9xTPtevdYzTtatTlVYejyDzZJbI0N5y1JGaBpGN08YHZIkXkqGsh63ZC4gPD76je5mh08YJrfiHQnu4jBCBKTZ6-_Dpfo1wYQeGFlXqcEoj3Xb7oQ_aaGmvNYJcmO6KXj3OPbR-mn5j8dNJmfhWr1ctA9Bd6dJY7TyDfrRyyU_ODkmx1erq70L_Rl74biqReJR9XRyB6YWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGMhaflZ82-TKz-98mL9Ni_GIVujbXxHWsBTUXo80m50jn4Sy3VUqzcJqkuDQcCXzlOGOHy0Dnc3ThlKAN56KwCJVZUCj9KYIHQDQFXTVlm-HPkQ5eA9ShQoNi6QKnVoWp0F6w9NYHtDP4pCOqr74eDoLphNk-TzYi2C2NuNA0-lTk-MMLVmTZg8ykju8WsJwiDsfK86wq6V9WQ9kT9I4eRL8n35kHXvDA-5Os4JBX8RNMgtcsXmv8pxcsuZGO3Zg22isIPca_REb7noA2QT3IJeVP0XNyZWNrGewWX9-BF24xsFEdIj6HcqseJORAJX-GhYJzI5gvylzUSOCIc6BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنارک الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17517" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دو انفجار جاسک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17516" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجار کنارک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17515" target="_blank">📅 03:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هم اکنون شلیک موشک از سیریک به سمت تنگه @withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17514" target="_blank">📅 03:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم  امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17513" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دو انفجار چابهار الاننننن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17512" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجار یا شلیک ، سیریک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17511" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانال 14 اسرائیل: حمله امشب به ایران بزرگ و گستردست...
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17510" target="_blank">📅 03:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صدا و سیما : دو انفجار در شهرهای عسلویه و بندر دیر واقع در استان بوشهر در جنوب ايران رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17509" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم
امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از تنگه هرمز حمله کردند، سومین دور حملات این هفته علیه ایران را آغاز کردند.
یکی از اعضای غیرنظامی خدمه مفقود شده و کشتی به‌دلیل آتش‌سوزی در داخل و وارد آمدن خسارت قابل‌توجه به موتورخانه، قادر به ادامه سفر نیست.
پس از آنکه ایران به‌دلیل حملات پیشین به کشتی‌های تجاری پاسخگو شناخته شد، بار دیگر فرصتی به این کشور داده شد تا پایبندی خود به تفاهم‌نامه را نشان دهد، اما بار دیگر ناکام ماند.
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی به این کشور تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شوند.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17508" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbhNTOuyetvhd0QYfPRnLGdWs6zoMT9LG_lICM98na58mGJ1MmPZUmlf3kodIplfcpzXW_9Wtx5Eph97N5x1YsccWMNhnIBwYrbvquX2gTU9yqTiCJMdPAzJByU6QNpb-GdphfWnPh5jEeh7eom06BShnVL7cBsX83fkNGyVYrwI2Li8HUL_07T-SX5tYFxbnzNrrDLZ45zEKdShFrNZmVafIVzlbWc1BsbucS-GMZnSx5sRl8QlzHn0zsPYb26Nga67KAxQPdPis9LVCSixl-w5G8-ws2Aow6RIryD0TTjonW4uK3WzexSLiMkx-6bvVW94JhnCiau_ETPaGI9t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر عباس الان
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17507" target="_blank">📅 03:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اکسیوس به نقل از مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف ایرانی در تنگه هرمز است.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17506" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4298477e.mp4?token=I8Mp57KmjF5f4VvKSznh5akPvf2Zxi-jcpg2McEuXMs7BpRSuza5uyvwLCo_IW-HYFFmvwDyyM-ievhLjatI13nJSH50YEQIs0WwirIHIJIK6kmlxiBtgLmzHCpIX2FgEOiRsMKpT4swARvDgbucxxX65a15gz9aeD9HeRo1IFHhZynfe1l0E0wvCUsvp_lV61dvX_llGMkCcEfyskwY6aiT-kXWU55t4JSvzqKFPK5DmzL-_2JXjCMGtQLeHojsgCv2voLgNi8ntXFMhqORSknGFtLEt05zPIkfOnT481TY9hHof4VUpahMk148Ml7PvDNOq4Ii3WEaYlA561tb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4298477e.mp4?token=I8Mp57KmjF5f4VvKSznh5akPvf2Zxi-jcpg2McEuXMs7BpRSuza5uyvwLCo_IW-HYFFmvwDyyM-ievhLjatI13nJSH50YEQIs0WwirIHIJIK6kmlxiBtgLmzHCpIX2FgEOiRsMKpT4swARvDgbucxxX65a15gz9aeD9HeRo1IFHhZynfe1l0E0wvCUsvp_lV61dvX_llGMkCcEfyskwY6aiT-kXWU55t4JSvzqKFPK5DmzL-_2JXjCMGtQLeHojsgCv2voLgNi8ntXFMhqORSknGFtLEt05zPIkfOnT481TY9hHof4VUpahMk148Ml7PvDNOq4Ii3WEaYlA561tb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سپاه بوشهر
رو
زدن
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17505" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قشممممم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17504" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آبجو ۱ - ردبول ۰</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17503" target="_blank">📅 03:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17502" target="_blank">📅 03:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دینی ۰ - کنکوری ۱
@withyashar
🤣</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17501" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سی بی اس: حملات به تهران هم‌میرسد
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17500" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بوشهر رو جوری زدن که ملت ریختن بیرون
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17499" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بندر عباس دوباره زدن
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17498" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17497" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
