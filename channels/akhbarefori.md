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
<img src="https://cdn4.telesco.pe/file/XPfkhj0kr-pFMsqxHFhiW86i4nohER_4qs0rNvfIfJ7Y4uODZc0h_JfhFCDWGWliVyohipV4gQT-srIpscBC3juU5lMpEVvgara4x0kxuaYMge6VZQduQ1afOjdL1H3EyoF-K3eqlDjv9QtNmLIQ37t1pl_AAyazE-63qQ-8NKMhpmoCKXKCFRPRI9EFRoF8R9KJb9o8PFTQavLRX9qDns0SP9P-tYA4-12hOo83P5rVQP-1ezg3ewjsKBMUKtpP-m-ATvg1vlRwvQOaNW7C5g7EjYy88upx5hu18ekpPfdE4wfXljXWjW6dFxEnHvrzQW8T3mZ2SS6TAalnmz2bqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 23:21:26</div>
<hr>

<div class="tg-post" id="msg-684083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a63edf13.mp4?token=U3XihBM1WJpBVG8EtnG-xBGB22_k06ftOvwzXLWjnGA-nrPMg8G0ezMQqaLyl6pGfZmsGwf6xwgCp49LQBa85Bq04kGIKBItGuoucqpFpR1SXL55sCUhN81sP7uto2_lQPh-N4oZr5PTqxYL0khzWw1QkJeG8yuJqFZMgiHCPDLDLAOUg5K9kfWYapzCOqD7x21kyPb9jknzY-6W4_3th6aGXmwwWTQEJaBz_ojZ3HtEFVJwozSAaSGWk5ekIxVS7c7rZT1EQ42prftML5UNgC1yD3-Dq1IOVCXX3xkipmwrLg2GEpUr8SykDPWQrYv50TV3qyj11V2BNN93Zzmlxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a63edf13.mp4?token=U3XihBM1WJpBVG8EtnG-xBGB22_k06ftOvwzXLWjnGA-nrPMg8G0ezMQqaLyl6pGfZmsGwf6xwgCp49LQBa85Bq04kGIKBItGuoucqpFpR1SXL55sCUhN81sP7uto2_lQPh-N4oZr5PTqxYL0khzWw1QkJeG8yuJqFZMgiHCPDLDLAOUg5K9kfWYapzCOqD7x21kyPb9jknzY-6W4_3th6aGXmwwWTQEJaBz_ojZ3HtEFVJwozSAaSGWk5ekIxVS7c7rZT1EQ42prftML5UNgC1yD3-Dq1IOVCXX3xkipmwrLg2GEpUr8SykDPWQrYv50TV3qyj11V2BNN93Zzmlxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایگاه زن در خانه جایگاه مدیری‌ است که از قضا ریحانه هم هست
🔹
این جایگاه اساسا با هیچ جایگاه دیگری برای زن قابل مقایسه نیست نه به لحاظ دنیوی نه به لحاظ اخروی...
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/684083" target="_blank">📅 23:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684082">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای مضحک وزیر جنگ آمریکا: می‌دانیم که ایران نمی‌تواند فشارها را تحمل کند و اقتصادش در مارپیچ نزولی قرار دارد
🔹
ایران می‌داند که ما بر تنگه هرمز تسلط داریم، محاصره ما غیرقابل نفوذ است و نفت از این تنگه جریان دارد.
🔹
استفاده از نیروی نظامی در تنگه هرمز یا هر جای دیگری را بعید نمی‌دانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/684082" target="_blank">📅 23:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
نتانیاهو با استقبال از تحریم‌های جدید علیه ایران: به ترامپ و بسنت بابت تازه‌ترین تحریم‌ها علیه حکومت ایران تبریک می‌گویم
🔹
شما به‌درستی هزینه سنگینی بر این حکومت و کسانی که به ادامه اقدامات تهاجمی آن کمک می‌کنند، تحمیل می‌کنید.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/684081" target="_blank">📅 23:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
وزیر اقتصاد: از نیمۀ دوم سال حداقل برای بخشی از دهک‌ها افزایش مبلغ کالابرگ  خواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/684080" target="_blank">📅 23:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684079">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1a7200f9.mp4?token=B8eMQY7pP3NgUMaj7ZTHpkmAVzwnLX3VGUOoJnqICvHRJiHkFQrz1QslwET0dZQOWmyUmCFqpfw_9ijQP8DuCxpSOLJcNwR9AGj6lR3WhPTfkDtdU2pFKZWtT33qrNkFB-KVlEOIHdahv27UPqxmzACJYoZYjvAg-vgXH8PLkjCM_C6bf9S9DJzs-BRraQqMewYwMjFQL-wcbS9-BKGJ6cxCuGdncL3a3NO7-0h6LS25rQqh2k8RgKN-ycqH27oYQX1KTH4wp7c2GM_-cM64t-iQKWNk0JyQpw7hh__pO1E7I5tup7uclAYuquXyix-pd3-0U9PH1wq-xN5CykNbdK8-3x0WI5Yk2hKRWOSvFa4SHGyWV1CUEh859zBY4_XYGPxXQNN6swTcEnhuKr_dp7PD6LKB2zNWhyafCQxdktJHEOWebY0i5pW1G2MtNwzHnfF0HUCvMgSnV-OOyy3MQoif-FGDHvhWN13RPmJDqD4bm0j_qcIJ8u1wZcGr_nFU5-vovQUec84jOOOEc8Ous0ZhvOMFmCEFZw8hy9Y9qXx4GfH_yXvyk2yjv_toc2VTBQkBBOQbjYePwt3mRq_orHF29VYJVHwVJGBPYYVQty288psgTm8p5xy2hsif4F57be5VcbV2i9ofV_uxCqdw67g9UW3civz2WgVARnv2KvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1a7200f9.mp4?token=B8eMQY7pP3NgUMaj7ZTHpkmAVzwnLX3VGUOoJnqICvHRJiHkFQrz1QslwET0dZQOWmyUmCFqpfw_9ijQP8DuCxpSOLJcNwR9AGj6lR3WhPTfkDtdU2pFKZWtT33qrNkFB-KVlEOIHdahv27UPqxmzACJYoZYjvAg-vgXH8PLkjCM_C6bf9S9DJzs-BRraQqMewYwMjFQL-wcbS9-BKGJ6cxCuGdncL3a3NO7-0h6LS25rQqh2k8RgKN-ycqH27oYQX1KTH4wp7c2GM_-cM64t-iQKWNk0JyQpw7hh__pO1E7I5tup7uclAYuquXyix-pd3-0U9PH1wq-xN5CykNbdK8-3x0WI5Yk2hKRWOSvFa4SHGyWV1CUEh859zBY4_XYGPxXQNN6swTcEnhuKr_dp7PD6LKB2zNWhyafCQxdktJHEOWebY0i5pW1G2MtNwzHnfF0HUCvMgSnV-OOyy3MQoif-FGDHvhWN13RPmJDqD4bm0j_qcIJ8u1wZcGr_nFU5-vovQUec84jOOOEc8Ous0ZhvOMFmCEFZw8hy9Y9qXx4GfH_yXvyk2yjv_toc2VTBQkBBOQbjYePwt3mRq_orHF29VYJVHwVJGBPYYVQty288psgTm8p5xy2hsif4F57be5VcbV2i9ofV_uxCqdw67g9UW3civz2WgVARnv2KvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلن اکباتانی، فعال سیاسی مقیم آمریکا: ایران به ویتنامِ دوم و گورستان نیروهای آمریکایی تبدیل خواهد شد. ایران، باتلاق بسیار بزرگی برای آمریکایی‌ها است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/684079" target="_blank">📅 23:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684078">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🟢
داستان لگویی جدید منتشر شد...
ولی پایانش چیزی نیست که اولش فکر می‌کنی
🫨
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/684078" target="_blank">📅 23:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684077">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa13b21ef6.mp4?token=VkJIeXPFz7Izbw-J_qEDo6_3wxwJzbnCZywjbjxojIPj0KVsjAY3Ttv_AGKwJ9IY_M6mdjAhZWUw27Cur5Mf-DbEVegenWBxQBzyULUbdj2DznyrcRi0rl-P5149gQo_LHkJwjmUZk4Q1_76MC9qx0cd6quLhoHEjvruTfo-aLNM7AFoQJhdSG81UBp2xCCz-RzLET8r0dtUmiExXHtQuW85dPLq55hAOMxPNzkMVZibmh8p_WCica0SmH0Bz-z_fcxnagb2YlQb5kc9pi-p61nRfNGHKuVeqQ7Ll1oSJGotCxUL3VNHZew5vKfyVvTGf6yU6gaemXLCp6t3omvxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa13b21ef6.mp4?token=VkJIeXPFz7Izbw-J_qEDo6_3wxwJzbnCZywjbjxojIPj0KVsjAY3Ttv_AGKwJ9IY_M6mdjAhZWUw27Cur5Mf-DbEVegenWBxQBzyULUbdj2DznyrcRi0rl-P5149gQo_LHkJwjmUZk4Q1_76MC9qx0cd6quLhoHEjvruTfo-aLNM7AFoQJhdSG81UBp2xCCz-RzLET8r0dtUmiExXHtQuW85dPLq55hAOMxPNzkMVZibmh8p_WCica0SmH0Bz-z_fcxnagb2YlQb5kc9pi-p61nRfNGHKuVeqQ7Ll1oSJGotCxUL3VNHZew5vKfyVvTGf6yU6gaemXLCp6t3omvxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: افزایش فعلی قیمت ارز ناشی از التهاب در فضای رسانه‌ای است
🔹
تلاش می‌کنیم وضعیت بازار ارز را به حالت عادی بازگردانیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/684077" target="_blank">📅 22:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684076">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک پیشنهاد ساده برای صاحبخانه‌ها
🔹
گاهی یک تصمیم کوچک، برای یک نفر اصلاً کوچک نیست. شاید چند روز مهلت، کمی مدارا یا یک جمله ساده، بتواند فشار بزرگی را از دوش یک خانواده بردارد.
اما اینجا قرار نیست درباره بخشیدن پول حرف بزنیم؛ درباره چیزی مهم‌تر از پول است...
#چرخ_زندگی
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/684076" target="_blank">📅 22:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684075">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a6edfdc9.mp4?token=p7QGHxFDhxaAwODFOE_a0TzfIJZLvf8obpjdEu8qWIip7ZwOD3WvEgzcHbxe1EtB-Nt21-504iHFs8WcbAYIXHgqaruvMgVlYheM2CS3ip2AYSIoIPSHsmd4vgo_ZW4DUQEZ6wiau4fxWvqj-nyQh_2D7cmML9Ke_dAPg_Uzy6p3TyLGeS97Edn9qWAbBDFlUL0qVI7XMHjMxGfqKl4PqVuiW8FiC5HVhRvubakIQJohyqgaFv27k4rfhC60pJgHcR4qh0TRldjVO7-oCfHGGgJJp-jI-qPCS8H2zoi2mFUvCvqlVUVaH4StuL_oPbTBXO1vu2ECbwZkXVSX150_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a6edfdc9.mp4?token=p7QGHxFDhxaAwODFOE_a0TzfIJZLvf8obpjdEu8qWIip7ZwOD3WvEgzcHbxe1EtB-Nt21-504iHFs8WcbAYIXHgqaruvMgVlYheM2CS3ip2AYSIoIPSHsmd4vgo_ZW4DUQEZ6wiau4fxWvqj-nyQh_2D7cmML9Ke_dAPg_Uzy6p3TyLGeS97Edn9qWAbBDFlUL0qVI7XMHjMxGfqKl4PqVuiW8FiC5HVhRvubakIQJohyqgaFv27k4rfhC60pJgHcR4qh0TRldjVO7-oCfHGGgJJp-jI-qPCS8H2zoi2mFUvCvqlVUVaH4StuL_oPbTBXO1vu2ECbwZkXVSX150_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش وزیر اقتصاد ایران به اسکات بسنت: منتظر پاسخ ما باشید
🔹
آنها این صحبت‌ها را قبلا هم گفته‌اند، ما کاملا برای هر سناریویی آمادگی داریم.
🔹
شریان‌های مالی و اقتصادی دنیا به این سادگی نیست که بتوانند ادعا کنند ارتباطات مالی و تجاری ایران را به‌طور کامل قطع…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/684075" target="_blank">📅 22:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684074">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZimj8pqMThedJF9ysQsPat4a3jDg0-n03-ePpx5Ts_dp-BNfGuRxBAIyt1R_cO5zR5mKdNFKjdyIiM8FOUvETiR6tjt9mX8n5iN6FEP2XKUvn2HALWB0GgBqGSQCyDmhB7sDaB_myu8Zib7MqAz7ra9u9vgdKRbLGdAhBFlutNK4djpIVoYj4t7EaDRv7ACTrIeQUBIYtrckrXPzsc_mGz02lqyPW9sQp1Kk3HGLubmrVPyUv5YGkwoK1SEjWtjweVN1y8yh88jOOZ3fAxz_FGFFgt617gxINXSNFADf_dZrrnfWcwywz4zGC9KK2eMqE4ic38Cg-4j180JIvp-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر در پایان هفته سوم با صدرنشینی استقلال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/684074" target="_blank">📅 22:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684073">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1kMnogj1eMeeGyQlvwUwLH59pRncoW76KR4DyvkzgOwi5vzmEEHIPA1o-mRBRSaq8aZVCPbeb_XCxhNx-DvOyS5cqVa_89rB_GYL4DTX9UT6dt_YOazCZIA0_Q1TirHUWaQ11Yo74iLo4acNOl8C1g6oSPJa1SlU3riIRZuPjUWeo55aADkabuoZwinUd5MO0A3qvvRsIet9EZQBnhtwhZCxXGdh5N2U5xTNbjuoSdzirNDqXodVK6LInp9aWpEfVYHzvRmYwgQF_3u6lOZD6gNshGFhuNyZM0slBkuXAZZlB-Hf5cWxl0etv9alYxPboDcB05EnB2_R1neKHBNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: از زمان شروع جنگ ایران بنزین در ۴۵ کشور گران شده است
الجزیره:
🔹
از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران، شش ماه پیش، قیمت بنزین در حداقل ۱۴۵ کشور افزایش یافته و بار سنگینی را بر دوش مصرف‌کنندگان در سراسر جهان گذاشته است.
🔹
این ارقام بر اساس داده‌های GlobalPetrolPrices است که قیمت سوخت را در ۱۷۰ کشور و منطقه ردیابی می‌کند. قیمت بنزین در میانمار بیشترین افزایش را داشته و پس از آن بوتان، کوبا، امارات و نیجریه قرار دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/684073" target="_blank">📅 22:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684072">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پاسخ وزیر اقتصاد به اسکات بسنت: این‌بار هم شکست می‌خوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/684072" target="_blank">📅 22:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKqOC8UoynCUHd-52fbznI7g6Ow97ojrhdAt_M_jH7Ib81wn3xiC_N7O5_K9HyKdVAJCGcHIPQJBZD2z_1g0eA3DRfoh0CUsPOgBkNDLF_XfzdAg5CcVxk5iCU6rEEjESSh3oAWKa877xPw1WCyXzhqvLY2Ow7uQhI0wF3NUq8RH6PB2o0soQUhNvWhvcqBiqFn7Xw5BdpVOIQlud2U5PfG8vrXdMx4cFod0RQgudNd4ONXdxV5iZfJlgq-orU-XwUYkXBKTPcDOXyyam6QLAg-ONzcELSREM1nWpjkIA7k-mNI_15159kIYaEiSCfhE1blDqiD0yS_x-DsLraBoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAikv2BAEEMwXuPQtTvvjIp0Cty_6JjBgSw1r0YoBxO1w3AuC5sqoS-rO0SV0Bqz230Xfm4ickxJbaMquePmTMD3yaX1HEw2LzglnFRIkfit3cxbtAfd49U9-w16DUgb-vTmZU_ibLERfKzle9VGzFdQRx_97U6LW-k-I4KU8my1kWfndYK2BjexN8rUIpW-93TIpUhLB3xfbYerLHEIvFo3wtbGxa5bIFUEIajwjeY1_Ce9LO6fqXnk2Xdxk65w3LcqAzF-fdQNXFcab_XDDawI21TTUZ1RJMDTMRYH0ZLMntWWmY5vPEzxBlob2yfq0CvvHlyhQ6froZBWl3bcCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
‌طارمی زیرقیمت به امارات رفت
🔹
یک رسانۀ اماراتی مبلغ انتقال مهدی طارمی از المپیاکوس به الوصل را تنها ۴۰۰ هزار یورو اعلام کرد، تا او ارزان‌ترین لژیونر الوصل لقب بگیرد.
🔹
مبلغی که باشگاه الوصل برای خرید طارمی پرداخت کرده، حدود یک‌ششم پولی است که المپیاکوس برای…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/684070" target="_blank">📅 22:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مدنی‌زاده: افزایش قیمت کالابرگ برای برخی اقشار از نیمه دوم سال اجرا می‌شود  وزیر امور اقتصادی و دارایی:
🔹
در ماه‌های ابتدایی سال، به دلیل کاهش درآمدهای نفتی و آسیب به زیرساخت‌های گازی، تأمین منابع کالابرگ با محدودیت‌هایی مواجه شد.
🔹
با استفاده از منابع دیگر،…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/684069" target="_blank">📅 22:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
پاسخ وزیر اقتصاد به اسکات بسنت: این‌بار هم شکست می‌خوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684068" target="_blank">📅 22:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پزشکیان: زور و قلدری آمریکا راهگشا نیست؛ عاصم منیر: فرآیندها را با دقت دیپلماتیک پیش می‌بریم
رئیس‌جمهور در دیدار با فرمانده ارتش پاکستان:
🔹
آمریکا باید لحن و رویکرد خود در تعامل با ایران را اصلاح کند، چراکه تکیه بر زورگویی و قلدری، تنها فرآیندهای اجرایی را با پیچیدگی مواجه خواهد ساخت. ملت ما با اتکا به همبستگی، از هرگونه فشار و تهدیدی عبور خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684067" target="_blank">📅 22:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRJjz2akQ9zuebxzQcTepr04JRLflyonEGZ_xP1lw4zsQq0l2b--aFiTWK1aDA1odTGufqjY9DCQIgHD6o9uAIqh1L3s0LTZo854ar7Fbj0FPRlLJn9zrD2vke8R0CYM617-EsQGK0xO3YDsHOvZih8IynCSLPR7RAb4R_M-fURE8SYQmQUz7aEle7Sd7OWYCPgz8FDKnCxHzBBhPwivENwWFtyqbbk5SxSBkvyVOg0MS9mAdDUGDo9DTT5tLgn0KPf0bN48_ca0eSrvlwT3h3ywvQ-G9DGEulc4qJ1Gy9K3t23eFDILQID4ZZMdKvPDhmwgehyqibeTxfUTFd3ZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما زنده‌ایم به امید
🔹
تصویری از یک مسابقه فوتبال در غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684066" target="_blank">📅 22:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N512-4vSAzoT9l7P0FYVRyNGcynKkZj2JONlOSw_fqZ6D_Qjw61xnIFIZXAGY049mQI72alhYaYiYcxWmJN_arnw8NsR86MCXjx-5tuCmny89302hP12nRAGFEwlbuKABGNLqV7LefjTuTnXGck6YBgJ6X_havBO_eUGIFm0wR0kGkVmONu_CpDBOYZ_7SKNApnad9WRbs0Caa0wBgsR5rPOuHowJLgqiLTld3pTd7Etrs-1qdi6ypWXaTcTXshfes6G7LO5EEt1g-rdUJ1FlZr0QuJjwV-QGh2dep3uLEgH7XErEhRli_n0_LTawhRSYvPjwShDsMJ-UkXQ2OVcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدارهای غلط درباره رومینگ
فعال بودن سرویس یعنی مصرف اینترنت نیست
🔹
در روزهای اخیر ویدیوهایی در شبکه‌های اجتماعی منتشر شده که مدعی است فعال بودن خودکار «رومینگ» باعث کسر حجم اینترنت کاربران می‌شود. بررسی‌های عصر ایران نشان می‌دهد این ادعا مبنای فنی ندارد.
🔹
رومینگ زمانی کاربرد دارد که مشترک از کشور خارج شده و از شبکه اپراتور خارجی استفاده کند. بنابراین فعال بودن این سرویس در داخل کشور، به‌خودی‌خود باعث مصرف اینترنت یا کاهش حجم بسته نمی‌شود.
🔹
انتشار چنین اطلاعاتی می‌تواند باعث سردرگمی و بی‌اعتمادی کاربران شود./ عصرایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684065" target="_blank">📅 22:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
وزیر دفاع و رئیس ستاد کل نیروهای مسلح یمن: دوران نبردهای صرفاً تدافعی به پایان رسیده است
🔹
سرلشکر «محمد العاطفی»، وزیر دفاع و سرلشکر «یوسف المدانی»، رئیس ستاد کل نیروهای مسلح یمن اعلام کردند که ماهیت نبرد یمن از وضعیت «دفاعی» به وضعیت «تهاجمی و پیش‌دستانه» تغییر یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/684064" target="_blank">📅 22:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e560e021.mp4?token=PFgxzkBGeflpAMO3yDPJu6DdYwIIiEpcwoGrIEp3L_ryU13OdFt7NDVCy5JC-0gb-hgIjRaakdXfozeH9ckTv4nSzqiefWvKfV1ddiYRRvQ3qr9SgmZamxPRkrC9N2cDivfIZcMLWAwzhPml1U1vh56UB-fJu31vRDRcKVTxeC8UBA9gMBt26UKJsf8euB23Sa5fvacmuPz4NNQD81j5liE_MVWXBdCWFGKJh_pQyfygfWATsncgNbpcCcjwcL5kXs5TaygPoipcGDuREiaNVKsppKhMe0QsddPEuW6Wj0i6vKvCOj9RIZwGd8bsgAq6ptOoKnjTnrLYYO6t_0csBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e560e021.mp4?token=PFgxzkBGeflpAMO3yDPJu6DdYwIIiEpcwoGrIEp3L_ryU13OdFt7NDVCy5JC-0gb-hgIjRaakdXfozeH9ckTv4nSzqiefWvKfV1ddiYRRvQ3qr9SgmZamxPRkrC9N2cDivfIZcMLWAwzhPml1U1vh56UB-fJu31vRDRcKVTxeC8UBA9gMBt26UKJsf8euB23Sa5fvacmuPz4NNQD81j5liE_MVWXBdCWFGKJh_pQyfygfWATsncgNbpcCcjwcL5kXs5TaygPoipcGDuREiaNVKsppKhMe0QsddPEuW6Wj0i6vKvCOj9RIZwGd8bsgAq6ptOoKnjTnrLYYO6t_0csBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدنی زاده: زمان توقف کالا در گمرک از ۱۰ ماه به ۸ روز کاهش یافت  وزیر امور اقتصادی و دارایی:
🔹
طی ماه های آینده  زمان ترخیص کالا را به سه روز می رسانیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/684063" target="_blank">📅 22:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69aa0f9eb1.mp4?token=aTa8PhTGBj0XFewTurPVOJBhBOVXiUEXbAp5j08CPrVBPwwV5DSohinnsR2HLJgWDkoGViEnOnMUFX88PAiGTrzZWInTqvKjUSYQ1BAwt0xHW1tK-pSJXbvBe7BBZi3rXJQLvBp7N6grKCoUOt7_YeMebQaOHB9EeQdcve34Ii7N4vmPjYCRyQFi1_RYP_I-5ryMb45ki5HYY2D7i3ymez37iXJhqCrIRirgRO98L-1g4bpZaOuEybSn3m4G6ZYaOrMQJkCuAb-jqaDhnVAO_BuR2QcWuknRx7Bb5cmyN3AC9wVzBlV4qf6k4hxSSqj0iuX7DHF2xDAbiunkqsf73Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69aa0f9eb1.mp4?token=aTa8PhTGBj0XFewTurPVOJBhBOVXiUEXbAp5j08CPrVBPwwV5DSohinnsR2HLJgWDkoGViEnOnMUFX88PAiGTrzZWInTqvKjUSYQ1BAwt0xHW1tK-pSJXbvBe7BBZi3rXJQLvBp7N6grKCoUOt7_YeMebQaOHB9EeQdcve34Ii7N4vmPjYCRyQFi1_RYP_I-5ryMb45ki5HYY2D7i3ymez37iXJhqCrIRirgRO98L-1g4bpZaOuEybSn3m4G6ZYaOrMQJkCuAb-jqaDhnVAO_BuR2QcWuknRx7Bb5cmyN3AC9wVzBlV4qf6k4hxSSqj0iuX7DHF2xDAbiunkqsf73Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدنی زاده: زمان توقف کالا در گمرک از ۱۰ ماه به ۸ روز کاهش یافت
وزیر امور اقتصادی و دارایی:
🔹
طی ماه های آینده  زمان ترخیص کالا را به سه روز می رسانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/684062" target="_blank">📅 22:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSphtilliaeaEJI33GvNPkrnJqLvjM70zNpR6w9MgM5zFFzSuGRi8W-42Fhv4sBf4FIQ6sW9zIGuX51qkWbKZlZ8cOKaUhJNS9z02dcUXsrkG8Jkjj0YfmAJlNrZxwjfe8RdqjaLdVbsWvKrNqSpJnroLQFsZBaYEPvTNCJcY2j8u3stOJhy9cZ3uNvyADfG0utvQBFaOATLbyF0i77V-LAXGzJ5T-sB0x6Yli4ZV_vSoeN7k06oBIXAqRzXvSgU5k1BLeRwI5kneoUktnWfr9USS5aZyMBNuZhm8SF-9JtnpPyJo5qbfS_XtOv5geub99LebmSJLlEgsWzsWGec8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قمارباز: کانادا باید خود را با مقررات آمریکا وفق دهد
🔹
ترامپ در اظهاراتی درباره روابط اقتصادی آمریکا و کانادا گفت بخش قابل‌توجهی از برق، نفت و گاز مورد نیاز کانادا از طریق ایالات متحده منتقل می‌شود.
🔹
او با لحنی تند خطاب به مقام‌های کانادایی: یادتان باشد، بخش زیادی از برق، نفت و گازی که کانادا دریافت می‌کند از طریق ایالات متحده آمریکا منتقل می‌شود
🔹
یکی باید این دلقک‌ها را وادار کند که خودشان را با مقررات وفق دهند؛ وگرنه عواقب آن برای کانادا بسیار بدتر خواهد بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/684061" target="_blank">📅 22:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
آمریکا نام سوریه و «جبهه النصره» را از لیست‌ سیاه حذف کرد
🔹
وزارت خزانه‌داری و وزارت امور خارجه آمریکا رسماً اعلام کردند که نام سوریه و گروه تروریستی «جبهه النصره» را از فهرست‌های تروریستی خود خارج کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/684060" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2c709522.mp4?token=cc-7fRhlz4l58IpsRPnZf_nPXg1THFdG-VAxZLhA1aqi78io1uMHdiK-UHnMeCE7lLdJI6sKYidmUkH4bbZZte8FsDbPuysMXLe-bV8CPQ5tCtoJFREiFvzME5boFi0hFIWhuldEPnFGVUQ_7iyc3ImId-R7R2g69KD6SQCWWjCnZwPmYCf-uaeTc1BrYswT9GERI-q32GPSfITY_vYnyvX5tTO1o1G6J5PvXlLdFrtibx789sH6pZ0pvBK2eFIx-rE5NzxOLjhfFvv__v0_KLRn19m2lBAsDW_O1pJyUxw7B4TNfURc6PNVBMT1juWwtE6Eo-EIcxOsg62SxGaOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2c709522.mp4?token=cc-7fRhlz4l58IpsRPnZf_nPXg1THFdG-VAxZLhA1aqi78io1uMHdiK-UHnMeCE7lLdJI6sKYidmUkH4bbZZte8FsDbPuysMXLe-bV8CPQ5tCtoJFREiFvzME5boFi0hFIWhuldEPnFGVUQ_7iyc3ImId-R7R2g69KD6SQCWWjCnZwPmYCf-uaeTc1BrYswT9GERI-q32GPSfITY_vYnyvX5tTO1o1G6J5PvXlLdFrtibx789sH6pZ0pvBK2eFIx-rE5NzxOLjhfFvv__v0_KLRn19m2lBAsDW_O1pJyUxw7B4TNfURc6PNVBMT1juWwtE6Eo-EIcxOsg62SxGaOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کابوس مرگ ترامپ سر میز غذا
🔹
یک وعده غذای معمولی به صحنه‌ای مرگبار تبدیل می‌شود؛ اتفاقی شوکه‌کننده که همه‌چیز را در چند لحظه تغییر می‌دهد.... #کابوس_ترامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/684059" target="_blank">📅 22:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPvpuTpsmC8xIw5P_PPnzPpLgEyWC-iunlBCq1wU4-9xbbDsO6TNaR-1JyU941DKDC1qFhSmS164ZF8ypA0uRP_Kt9UguKTFp6MRtdvgSH6wM81wXDKMvpJFFR54x8-6dAMwERegdMBLWEyuYdxdv5Oi9NbfW0F7pjGZaL4t5nf8_FSlY6LsM9i6k7yKNAea5zgp7JvopXFCToWly9Q3-gV1PxxJsEndZsm9O2IEybv1yHlhJ-hhifv3UagmzTDk-cbo8yeJnMvYmcl0oAD0UKtV7adf9_LodxoCEpASedejbMWy-5nFHCo2DjKVw5IqspR9l4iYoXO8ZiKz12Ze1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رازدار بودن، فقط پنهان کردن یک راز نیست؛ راهی برای حفظ اختیار و آرامش انسان است
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید: «هر کس راز خود را پنهان دارد، اختیار کار در دست اوست.» گاهی نگفتن، قدرتی‌ست که به انسان اجازه می‌دهد سرنوشت تصمیم‌هایش را خودش در دست…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/684058" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16caf9a31.mp4?token=YCZDTrdXnoM0OuRkdteb0MHZSzyNZetPANCWb3-jpTpKBmt1mljGbm1z04ehdvrtn42KlPBgmOoO0vLuv6Ln7knZMpflQlvm95rcOLH9APkLdUXKxLswb_8H04KcBFYgO6wbeh4P7wkWf-73hBTcxhbCTgDRWmt7TreS5FkAiTsumLLd8gamC-kchF-QSkrEeMJKZAc_4oHn-auMufP80jvzjNR-INqc2upiA3H-awRkgmq2rSaObLoQqrYzyLxNiKlf6IxkoJ7IhogKejkmwyekAUZvRz63ZtyJKKmu7VHQiKt5C6qT0R7LWvkTwwCkzQ3bA3KC6YAumVLjhVwb1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16caf9a31.mp4?token=YCZDTrdXnoM0OuRkdteb0MHZSzyNZetPANCWb3-jpTpKBmt1mljGbm1z04ehdvrtn42KlPBgmOoO0vLuv6Ln7knZMpflQlvm95rcOLH9APkLdUXKxLswb_8H04KcBFYgO6wbeh4P7wkWf-73hBTcxhbCTgDRWmt7TreS5FkAiTsumLLd8gamC-kchF-QSkrEeMJKZAc_4oHn-auMufP80jvzjNR-INqc2upiA3H-awRkgmq2rSaObLoQqrYzyLxNiKlf6IxkoJ7IhogKejkmwyekAUZvRz63ZtyJKKmu7VHQiKt5C6qT0R7LWvkTwwCkzQ3bA3KC6YAumVLjhVwb1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال جالب خبرنگار از وزیر خزانه داری آمریکا درباره عملیات تحریمی ایران  خبرنگار:
🔹
شما این عملیات تحریمی علیه ایران را یک «روز D» اقتصادی توصیف می‌کنید، اما روز D یک تهدید به حمله نبود و آمریکا به آلمان یک بازهٔ زمانی نداد. چرا تحریم‌ها را امروز اعمال نمی‌کنید؟…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/684057" target="_blank">📅 22:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
منبع ارشد اطلاعاتی ایران: طرح فشار اقتصادی ترامپ، عملیات روانی است
🔹
یک منبع ارشد اطلاعاتی ایران، طرح فشار اقتصادی ترامپ را بخشی از جنگ روانی علیه مردم دانست و تأکید کرد آمریکا پیش‌تر همه ابزارهای فشار، از تحریم تا محاصره، را به کار گرفته است.
🔹
وی ادعاهای ترامپ درباره حمله به زیرساخت‌ها و تنگه هرمز را نیز عمدتاً عملیات رسانه‌ای برای کنترل قیمت انرژی و اثرگذاری بر بازارها توصیف کرد.
🔹
این منبع، طرح جدید فشار اقتصادی و حضور میانجی پاکستانی را تکرار همین الگو دانست و گفت اقدام میدانی جدیدی رخ نخواهد داد؛ ترامپ می‌کوشد مشکلات خود در میدان را با عملیات روانی جبران کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/684056" target="_blank">📅 21:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a62c30e2b.mp4?token=Z1D9F46B3WMElmh7GoD6G13gnJcD_lpfPWyLf-w9-wRe0DFmEv5ejLUL9Hnn0HAkKaRMGB_odHNkLzh33zR-P19ixEc7pDlDgklCgC8vB9VmsKiUXuGU1OUhj95-1P8sWXe6mlAvL-Jq-B3-n9gilH4Ci-yLCsDX3y4vC-bD1CkNX6iZwNFOcl2iRluzZJ1qqRMVu6yN4O27l8ew07EF068VPygfZQasnE-wfJ2BXkKFZobXmL-vlm3qT3HFQTGYOf32TDyEu31HaiGRfmZwQEI49UBiGOb2HW4zfIcHUBOnQpmA16MwEIkdqLLKdQE-cjT7_dP9UAtvzCdvU6CzSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a62c30e2b.mp4?token=Z1D9F46B3WMElmh7GoD6G13gnJcD_lpfPWyLf-w9-wRe0DFmEv5ejLUL9Hnn0HAkKaRMGB_odHNkLzh33zR-P19ixEc7pDlDgklCgC8vB9VmsKiUXuGU1OUhj95-1P8sWXe6mlAvL-Jq-B3-n9gilH4Ci-yLCsDX3y4vC-bD1CkNX6iZwNFOcl2iRluzZJ1qqRMVu6yN4O27l8ew07EF068VPygfZQasnE-wfJ2BXkKFZobXmL-vlm3qT3HFQTGYOf32TDyEu31HaiGRfmZwQEI49UBiGOb2HW4zfIcHUBOnQpmA16MwEIkdqLLKdQE-cjT7_dP9UAtvzCdvU6CzSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: به آمریکا بی‌اعتمادیم و باید رفتارش را تغییر دهد  سرلشکر رضایی در دیدار با فرمانده ارتش پاکستان:
🔹
آمریکا باید رفتارش را تغییر دهد و اقدامات عملی درخصوص اجرای شروط تفاهم‌نامه انجام دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/684055" target="_blank">📅 21:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684054">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df291ff75c.mp4?token=a1YF8vejgEdGha-bVs6qhVay6nak8mGBPzy9-tdXJnPR15CG5AFE-lMu-nkFa5kkqyiOqG_7a4kjmTkFm6r0HDzjtBhaqo1OWic2ltTacGf6CtbrV-eZ12fEx-JmRTd0DKgwMbLcaS_-bcc-9BbAuGCxSCkVzO6-cxDhP9CHtw4cc0-bDMqEkYLPdEvM6gb39JXbF6Whg1fALfJOiE66cnANRKfqC0Tgr7oFDUypM3d4bs-4mNrU0nBnJn2WHuQ5nz50BG6h_Pn3Z-skJXp0z0w78ZF0-kTrHucTSG8f1KOb3HM92uS8yaLcqTsbnYwbPbZ2BAraQNtiTQY2P05m1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df291ff75c.mp4?token=a1YF8vejgEdGha-bVs6qhVay6nak8mGBPzy9-tdXJnPR15CG5AFE-lMu-nkFa5kkqyiOqG_7a4kjmTkFm6r0HDzjtBhaqo1OWic2ltTacGf6CtbrV-eZ12fEx-JmRTd0DKgwMbLcaS_-bcc-9BbAuGCxSCkVzO6-cxDhP9CHtw4cc0-bDMqEkYLPdEvM6gb39JXbF6Whg1fALfJOiE66cnANRKfqC0Tgr7oFDUypM3d4bs-4mNrU0nBnJn2WHuQ5nz50BG6h_Pn3Z-skJXp0z0w78ZF0-kTrHucTSG8f1KOb3HM92uS8yaLcqTsbnYwbPbZ2BAraQNtiTQY2P05m1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/684054" target="_blank">📅 21:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smAqgrbPAr3bBBeT7GYNT3UjxU-RB5zmLkD7CFg4zOXuPXQ9y72MR6FsO-NxW-rp216cuU_qW6hRJIzCSal2OS4obKVLzv8XeS1eS9cpq6eSnXFky7h4XS8qwhLmmVUbqOkE9HYz3ORZNuay5uLkKngvDUOdUrR8aOJdi3Co8SfX5QOI6wMNRUClGJckdL_uIEgTUoX4mFq_bWdSHqwSpRdcs9d22cPz0m2dC2jraQLK4wQmG3fBVnIT_HPBhWyC0FGU0dFpzYxvh6f_MMVByQgIvzIi1fkWDd7aQL8KvqHiEUzWykpvxeVt89dUBEiNjZVBHVUB55zMs4z2J-Ovsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiOTdWMNySo2VhfNfThI-ywIXi7I-JOuXXEYZCNi37QyfKTMrOo2YD_l50MRnCnrK_hSdIa2coGKoRt6q6Yo5u8EDe7JFyce0-b_pAL9zbI3f9IXEkUP02jMf1XU4InE7vKe5nwSw9Z0u3FhoZm3-ZP3diPtKprhrITVBbYaRVedbMDwjKR2Kytt2aN7zSyafqYtusk8IlXDUGOvguK3OzPQvXS2sFU8ilO5m0LwwHvQdV9o-TAl7BTXyNS0A_llw3i-iDw19YkY0GZ4tPl4RdqTlB1Rp8qdmPrsdTrp1sOcO1t_0jVE1LsvctAY209Vp9_Y1WY9mbVRoUZFGlgOGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامدهای بسته شدن تنگه هرمز
🔹
بر اساس گزارش آژانس بین‌المللی انرژی (IEA)، تنگه هرمز شاهراه حیاتی انرژی و تجارت در جهان است؛ به‌طوری‌که ۵۰ درصد گوگرد، ۳۰ درصد کود اوره و ۲۵ درصد تجارت دریایی نفت عالم از این گذرگاه عبور می‌کند.
🔹
پس از آغاز جنگ و بسته شدن تنگه هرمز، آژانس بین‌المللی انرژی گزارش می‌دهد که اختلال شدید در بازار انرژی ایجاد شده است که آزادسازی روزانه ۴۰۰ میلیون بشکه نفت استراتژیک یکی از مهم‌ترین پیامدهای آن است.
🔹
بر اساس گزارش این آژانس، افت ۳٫۳ میلیون بشکه‌ای صادرات محصولات پالایشی و کاهش بیش از ۲ میلیارد متر مکعبی عرضه هفتگی LNG از دیگر پیامدهای بسته بودن تنگه هرمز است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/684052" target="_blank">📅 21:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1qT88LmZ2WDEC9LR88KgtTgDhkItybpUzXvcL0youJugjtp6q7tUbLmZmlyvnpx3axchaK3NxxZdyiWkQDagj3U8d8cmGHF1hbPcCicUxkdEzbuS7YxoERdgg-Ryz2CF9htzxWota_8j6JyVW-VHfomwDTBRjehAaXXN9MdbUBwW_5hkf-8hCaBnF76ZJo7S8kQDoKKqApJMJa1ZS8G59K10c_88LEXvtGc8WIs9lgnTRtqa50F8FFCuSBkDClGFJZMqiQ991X2TZkdE1_OXSxQwbhClHfsW80IWIBJ5sVDhAh5tixRVcTUH_CvdgXuSABOBL04ENb3xAl1c3LoDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhK6RI24KRqoXOamnIK-87lVbK8b05wFe2wy5gUS-cLAG-3-NJt4sJCkdUoX191czJd0hFksVZTDSx5dhzYACeFbnUQnHudywKRBEwCaGAQWxHwtMiMrgCmspEE-3npu0_RTy2p9xGNeTrSe2hYxCHFO9qwDgvBafmXFflNCLpdFz6X5EYxwISQ7NQ7pLmxcWOm2RTZeXkbsMF6HFJZhwZfQXq9ScFlnae-a7rkWN3sKferEub5PsTMi9Udg9FjjlqDdtD2Hp4sA-mSEt_YxfLbBsVDjfz8x1xsl8jGt24jhASw0-2LdzatBe0YNz2V0TZPCet423GWoxyHKKJdMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVzSSh_eJVhuHQBSsC634DQtni89cv2MYup8FH8Hk-fyPWgS37TmgVA4q9zNiLIWLjEvjvxoHDTzFhSFyRhu-CrxLU0NlIzybMhjIv36XHiMrTkeegiLFj_O7Ykc7DcFYPepsEaJ7DwxoQFz7_SPBk3Q9P43Yqhj-o4ytc-GIydYY_vRp2TOsidZvglK78A3EQl15QQ0lPi-s7IcEcJwwcEhHmBGL7tRqrlGPNGha4eAH10Al13VEqFB2n3gF2n090jJglLCMRVXjJPRiYQBXqQcXq_K-DRFZWi1niTVJR1H9fwDaTIsZO4bkHxm1yRn4TL-ilPjBdzDGES4AJRuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyNmAgWGxSkOPGp-wbMt2YpD8PXSSZ1mviUqEBftuDdELPlweXCuL-P_KQ4xwkvJ7JRAjBEcbD-84U93wyckx6F0GfXEsh2B03Nint_oSjjN5vyVbzU2WNnMk2D_GcDct8NE8_aF9wS7bIU0ia0kERy7mI3lYpMgxikKnjsBilp_7V3fo9njHEBnnQ4BTnL-LJQ7o5mSZJSFciNNuXtVTu-CwfuVuyMj_gw9TjFYiH4XNSXHZ_Om_jOBHoIHFsxEP32i3zlLeE1GubOhUwm6DQ6GVfnnfBmfGVAF2QuUcIAlZK-9epnegVqz10TV-m30RqfI4yKHYKr-R-aTBHO1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNRaNsKP_xng1sw4LmW2x7teGa4m11UCJP0Z7Gp7JSSiArUV0g44BbhIe3nP-lSQxrkG_Tydmhiw3kmsixgSyf_lBjabcAL2fIB5wxtKEf1wrhfNT0BR0NXWuvIOcGXHDG509yA6lFca3xUsZZHejZSsFUsyUIsNcr10LPvm_XeR5bw6Z5Du1YalevdvVa-cIi2IdGvHdMLR9aR_TxwbFOLOP06CCbStkAOkFo4M3BGb-YkySsIfiht-scd77V-8_EhaDSOgdS8quvq45IDRPGVGaNZqjD9QZSy6UV-rmiFEEpjTp0C--PxVfzpB__ldUiEGC4VcsITKse9KcvUQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIOcoTUrhauYmn4bgs77h5HRN3_8xoAT_oUaK8QrLaGM-2kxCYZErf2oZfapU3B9zf8MBCKaQO-D57kFrMD4-2Hfe19WY2b-fKx-HnhUevxFrZls-702iWJrv0gjuy3aKw_-kMF2-EfO177-xei67iw74Veb1Mi9uAUJ9-5vbvtaPUShUQtF9ma6Gs3E1zZTP5HR5B4XeVO0LQGR4mYMjk8PDFku9g0JraydbrD4hDIXWfPlztaYfM1cj94P_QBFbTNRaFjEsCxRqXLqv4zm_45HR0F1-kFVUMgBqCiM5UqmD2A4ZMAkQ8wJ8J53yLcSUtfdoBVndkXZQX4XOjfDPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار فرمانده ارتش پاکستان با رئیس‌جمهور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/684046" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684041">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1cqRIHeeDdTtON9y5RxbyMH9wixtvL4SlH19BuRibiUVCaTRZ1k5M5EXakjNuGnOpu9ul13_6NBhGCDwy4SWsqAIOHBTh76iBJoQCPks8Jpr7oEHILCyKoDQqaeLaVNeA6J6dQNN8eQn9FhSUoI4DR5Z9xsZNh8yVGJ6uuziTLiiXXHJEwz9LBH_X_4dUaY6x2ffg-kmafLuawUJI7o1qi4tg7xGiKIRiAyH6fmGSwMXU8Y6V-aMsyq3n3ATsp7hSWabz2_bdCguqDLR22lxZpqF0BZwqzUxvRSiqsAf5A5-Ax4B_whjSAicREtfcf15xovNRkYVUArmVPk9kdOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkV2GRcrxgCEk93amZL_4DZcBEOyk8Zl8ujJxKx0NMCpRpHfYWovLAbFoaJewew1MzUUvNiDiXkSv-fio74EqNZBi9EGYKhytZs05zh9g9MnxY7aade7XlbXl3YBCGWhLjYln-bSm5Ag4isubOoOrHnl3E9TlcJ3AycfM8SYpM97N4p2sfq65FHuXFR6GiA3A6VaZbTHIJClqXPq0y_5wYp5eeLk57RllC2YpBzFfUAwFiXU-KILglCVAoluTwZUZ13e3Z4JbjT0tbUE-g79Cm3YwW35bMQEtsTdFi9DhacylMaS__bmq0oH580lxtsTiQQCkY5hYbuOuDT1qc2QYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-A8x3OXoAH28S1eWEXez1SHFp4FkSP0PFwyEiOu86mqRlISBRxPiuo41LyGEwKT1F81_-wLHgh9SnsQ_mAITIqDYqIV0wTOjHlFi_4AP2dfc16AAPDGWVgKfh5OaliZiO-bB_1OfK7gRuI3TnFRh63NJt0YaC2uBZDxKj6LpQePDiPglWKYLwv9C85m-MQYA1vx-zLlgTZDruht_U5sZG18iSY6RT4sfxqkzJH8PZHEqJkhfOPq7yen6DRoiLwGfIxF6B2v6SwhLqHObl3QZe63xakIO0hSLC363-haygm0U7ttxpHBwgIMhxPKX6C6whP7bitsOzceSRqyaNmzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU6mnI2nLR0Y_iY1Bk15D5pWivQeqto5SL0bOGhcnDlOs3ogWg63tU4ZwfWwyW29Pu2ZQSUhkeswXzVUY9GCwcgiOoWhtx2Gx3VOra4fZquIMn1ued6ubPNlAHRo1V5QPZXg6LIglK0puS2NXht4os_RhUCCSuqeEkPHcgNtYVxtR8OZgEVkecugxS5IZDOhdexS6eKqsx5IrMO14KMmgCo6pBxmQFxoUKLKZv5y8dBF3NU6ioAS1DF7AHUhCOxPrTaabS0UCxvzY4tsr701eGUqYhe5oCT9S0yxljKCvSVLcK3aykWKAEoTV8tmzZTxKwkLFQHAffV8FeDddZECPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvM57MKjulVHFI4LKaJWhArq628brh3CCmSQ_EAI1RrmkA1eTGXNX_R_6EWttEAlol7ujWatPm_1w97bCWkZUVNDGVDsNh0dWz1reLp5CSutGXXU8uc8_PcxjsSYRH5PPgfhPxXInBwyxkTGtXRGQ8-Z5N8-BUNFUtG0uzYVtlDUu_wfww4_zBIzZMwEv2FgZxSsM3BCaLcm2stIJgysrsvoMrYE4cRrH2tOgTFEnWLA8nJpzBoV3DRQoz5BrtDVhhA_HEv6haAo_VQNOxkK3SseAn0fEHXeVbKKn1I1Evu_gAurG24tqP6hZDL8vitFgkI_c4DcxdCAEwEd2nYaww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این سایت‌های هوش‌مصنوعی پاورپوینت‌های درسی و جاری‌تون رو‌ حرفه‌ای‌تر درست کنید
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/684041" target="_blank">📅 21:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684040">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h226wuznLNTlTEivsHTKcPxuSEzETYXsnZdAFL8tncQ71frLGZR4LwvQrCTzSbUNIxs-IT__vuVgUKBOc-_bIsbDLWF2a4hu8qdYZ7_rrPT-wkDh11zQWm3U1WHz3XMNuVgyD0TfVYGe4KTGHUW5SCW6TkaXz2iiTQ5gzjaktiTGpR3c_r2mF_fWDZlP12_-B_TGCCJOJps1a7kmSBqRLx96y713TwKpmosfQktOZqDrFYXr5EYHftJqQKXwha4H1zqvLjgXaAVwRRJudfUWBZUC4BxFtiBG87SLDS4rw8TJkZ5Up5DK2TXN4Hr-CdcnF7-F9TFv-F6HD_AEEI6iHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: پدر ملوان ناو هواپیمابر آمریکا در بازداشت دولت ترامپ
🔹
در حالی که جاشوا آویلس، ملوان ناو هواپیمابر آبراهام لینکلن، بیش از ۹ ماه در خاورمیانه برای ارتش آمریکا خدمت می‌کند، پدر نیکاراگوئه‌ای‌اش در فلوریدا توسط گشت مرزی بازداشت و روانه بازداشتگاه مهاجرتی شده است.
🔹
ملوان ناو می‌گوید مراحل دریافت اقامت دائم پدرش انجام شده و فقط منتظر تأیید نهایی بوده‌اند؛ اما دولت ترامپ با متهم‌کردن او به ورود غیرقانونی، حکم اخراجش را پیگیری می‌کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/684040" target="_blank">📅 21:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684039">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guHK-hb6eM6iL1ULCjwe8Nmw9EUe2hH9c5LPYxgYBHg0T1IkZNCNhlBry6SuDzqbC9-rhGAYQC_le0aWTV1vpjRkiWQqACR9P7N4aGnkt2zouZGUiMHyy8ZHlO6gQCLIBvXDRcgbYomPM2pHq5nAL2EPsK2qsJQVkmte1M0oS_SfilKNF3170W_ddn0AY8eVHcGAN0D_ltlyde2-Au37A9hYX8PHbb12nEdcxlC2kgWF9kdd2a_HSFhMZdhMQM7-_LHXsdj7QyqH6aisVCJ0kVK2OfRVUAJMPd22AYRtCuggdcXOrjugJ0cMc5OGgKPByL-MPvCSQUoLaIeGRvKr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدای نسل Z تشریفات روی کاغذ نیست / دلیل ناامیدی جوانان «دیده نشدن» و «نداشتن نقش در تصمیم‌گیری» است
امیررضا احمدی، مشاور نسل Z رئیس شورای اطلاع‌رسانی دولت:
🔹
يك لحظه خودتان را جاي جوان امروز بگذاريد؛ تصور كنيد از صبح تا شب افرادي بنشينند و بدون حضور شما براي زندگي تان تصميم بگيرند، همه آيين نامه ها را ديكته كنند و درنهايت هم خروجي آن تصميمي باشد كه هيچ منفعت يا آورده اي براي آينده تان ندارد. اين دقيقا حكايت نسل Z و حتي فراتر از آن، كل جامعه است.
🔹
بزرگ‌ترين سوءتفاهم اين است كه گاهي در ساختار مديريت كشور فكر مي كنند نسل Z خواسته هاي عجيب وغريب، پرهزينه يا دنبال تنش دارد
🔹
تصور اشتباه اين است كه مديران فكر مي كنند با ارايه يك سري بسته هاي تشويقي فرمايشي، هداياي دستوري يا شعارهاي توخالي مي توانند دل جوان را به دست بياورند؛ در حالي كه جوان امروز فقط و فقط «حق زيستن، استقلال فردي، ديده شدن و حق انتخاب» را مي خواهد
🔹
ما دنبال لطف و نگاه از بالا به پايين نيستيم. ايران خانه همه ماست و فقط مي خواهيم حقوق شهروندي، اصالت و عامليت ما به رسميت شناخته شود.
🔹
نسل Z نه يك ابزار است و نه يك بحران، بلكه فرصت و سازنده آينده ايران است. صداي نسل Z يك تشريفات روي كاغذ نيست، بلكه يك جريان واقعي است./ روزنامه اعتماد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/684039" target="_blank">📅 21:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684038">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ایران رتبه دوم جهان در رشد جمعیت بالای ۶۰ سال!
🔹
شتاب روند سالخوردگی جمعیت در ایران بسیار تامل برانگیز شده است. داده‌های رسمی حکایت از این دارد که ایران تا سال ۲۰۵۰ در میان کشورهای جهان، دومین رشد جمعیت بالای ۶۰ سال را تجربه خواهد کرد. ایران در رشد جمعیت بالای ۶۵ سال نیز رتبه هفتم جهان را خواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/684038" target="_blank">📅 21:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684036">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0iXwaF4tyidsU9L6dvloh3aKtcSrNMD9JenbV6ONjQmjWEJFHOTCq94gRlwhLbmP5Iol1CHEpWfyL9veEKdT8KSKK1C7bdHXRZ3FBaEXCbDe_fpsTnCWEak52uluLHUamPS9c_9qgpfGEclCKhM9KiBTP1YjHyKlrpfUKAGHRtKNn0MoaxRe7qH2ZP2XypBVGRK5saIQou5bd47ukrRLmV_0lInniUu1HSOHroOaE6eCUwT12b-URW7EyKC_aOMUXjVwuXJrJ_51hbiaGXiR3ZvarwU0l0GlJTBrw9mSJHGqfHQr5LS8Oa1y6mnnQqGEb7GVXkp4CrVqogyhOcSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf7cd6c43.mp4?token=FGZWhY05Ydfn5LyocCzh6OSwp_UaQeTETrgnTzDY8ce-hDll22rt5qnaKc5ic-42MO2ptolVXdGSQnYGHHRaj2uCl8CV6bAVx4KtA_2vYqLCZnQP0vevNq2BthBqkm985XSioJlVF3O2QiPImoxA5O3-j3g5ZioIAKt5zyi8cfb-BeHxrpDH68_UkTZQ74uVW0Jy3DnoAVqA1ubCQGwxKpezo-BnewUG_KzkP3HGv5V5TutuVyo0Ccs9prYwtFeUXDhNg8gRqmVFZsTPw3OuNobJLBNJrKGA0yVcXOFDMRH7_i7KXxF2M9-fhLFh76nw1XcuspE1tMt70jnjKU18wF4MGEiB5dryWlnoyDA2u7v2dvjhFztn9fo0aHIul36LchmM08FnUa6h2aj7yIaCqzHr84DUfgkkNQC-tsexKAqhACiz4rBJN3zwgCcS_HxbPl3TNZI7VLHkP0wiH6wIZ7F0_di55vwaBb5G5eFupWh5ZXk-U8AoOW0bM-l3u_MZ23jiBKTYGRGeXJLtIGHrey-a25UsA0nIac7KGrVDeY7Er9RTtHSysMyLT3VTwAmcF6iQk7phcJ3eWwLpVeIByC26afpPHgIFhV_2T6OSve8-BsQvGLgK3ANvRFTzqJKc-5fwNvoENlm4RPSqCJVNNjJLISDWy7YdXjKpkHMy7UY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf7cd6c43.mp4?token=FGZWhY05Ydfn5LyocCzh6OSwp_UaQeTETrgnTzDY8ce-hDll22rt5qnaKc5ic-42MO2ptolVXdGSQnYGHHRaj2uCl8CV6bAVx4KtA_2vYqLCZnQP0vevNq2BthBqkm985XSioJlVF3O2QiPImoxA5O3-j3g5ZioIAKt5zyi8cfb-BeHxrpDH68_UkTZQ74uVW0Jy3DnoAVqA1ubCQGwxKpezo-BnewUG_KzkP3HGv5V5TutuVyo0Ccs9prYwtFeUXDhNg8gRqmVFZsTPw3OuNobJLBNJrKGA0yVcXOFDMRH7_i7KXxF2M9-fhLFh76nw1XcuspE1tMt70jnjKU18wF4MGEiB5dryWlnoyDA2u7v2dvjhFztn9fo0aHIul36LchmM08FnUa6h2aj7yIaCqzHr84DUfgkkNQC-tsexKAqhACiz4rBJN3zwgCcS_HxbPl3TNZI7VLHkP0wiH6wIZ7F0_di55vwaBb5G5eFupWh5ZXk-U8AoOW0bM-l3u_MZ23jiBKTYGRGeXJLtIGHrey-a25UsA0nIac7KGrVDeY7Er9RTtHSysMyLT3VTwAmcF6iQk7phcJ3eWwLpVeIByC26afpPHgIFhV_2T6OSve8-BsQvGLgK3ANvRFTzqJKc-5fwNvoENlm4RPSqCJVNNjJLISDWy7YdXjKpkHMy7UY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از پودر دست‌ساز تا ظروف سنگ مصنوعی؛ ایده‌ای برای کسب درآمد خانگی
🔹
این بار در
#چرخ_زندگی
سراغ ساخت ظروف سنگ مصنوعی رفتیم؛ محصولاتی دکوراتیو که می‌توان با مواد اولیه نسبتاً ساده و کمی خلاقیت تولید کرد.
🔹
ساخت و فروش این ظروف می‌تواند برای علاقه‌مندان به کارهای هنری، راهی برای شروع یک کسب‌وکار خانگی و ایجاد درآمد باشد.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/684036" target="_blank">📅 21:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684035">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab4e204fdb.mp4?token=Jwq5-Vy5ZKra68TklFcFmnGbZpMgwXdzP-9FjsEV43urNqgh3aY_CQIiAiC1YszlS2RCZDAwEXWT-eqdJtsQbBLoOJs73eJ8Qmo31Gi34nu9lkbt-KnVuMGTCizGsgM1IxQQ6S3NsSRqEb3X4LXSxfe7ImgHOGknKF5eSf-egnTK-vZmvPU3U8ER512gdWN73tXIrzRS5xEcdf0Q16pQDiNu49nosoVa_P7fE4hnVeCySzY70I8oDpG-5QJHaGwFMzY6kAS4Tm7hwZ4vuCz45OxxUuRX7691eYVk5BsUuSUQH7Z5UlyERM21NwaICRViJ9AIj9NJfo8Mewh8SaFX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab4e204fdb.mp4?token=Jwq5-Vy5ZKra68TklFcFmnGbZpMgwXdzP-9FjsEV43urNqgh3aY_CQIiAiC1YszlS2RCZDAwEXWT-eqdJtsQbBLoOJs73eJ8Qmo31Gi34nu9lkbt-KnVuMGTCizGsgM1IxQQ6S3NsSRqEb3X4LXSxfe7ImgHOGknKF5eSf-egnTK-vZmvPU3U8ER512gdWN73tXIrzRS5xEcdf0Q16pQDiNu49nosoVa_P7fE4hnVeCySzY70I8oDpG-5QJHaGwFMzY6kAS4Tm7hwZ4vuCz45OxxUuRX7691eYVk5BsUuSUQH7Z5UlyERM21NwaICRViJ9AIj9NJfo8Mewh8SaFX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملیات انفجار و تخریب بزرگ صهیونیست‌ها در شهرک میس‌الجبلِ لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/684035" target="_blank">📅 21:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684034">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دولت ثروت مازاد خود را بفروشد!
🔹
در روزهایی که اقتصاد زیر فشار تحریم‌های ناجوانمردانه آمریکاست، دولت بیش از همیشه به تصمیم‌های دشوار اما ضروری نیاز دارد.
🔹
یکی از همین تصمیم‌ها، فروش اموال و دارایی‌های مازاد دولتی است، نه به عنوان یک انتخاب فرعی، بلکه به عنوان اقدامی که باید با جدیت در دستور کار قرار گیرد.
🔹
دولت سال‌هاست مالک زمین‌ها، ساختمان‌ها و املاکی است که بسیاری از آنها نه برای مردم ارزش‌آفرینی می‌کنند و نه برای اقتصاد.
🔹
دارایی‌هایی که در سکوت، گوشه‌ای از ترازنامه دولت خاک می‌خورند در حالی که همان دولت برای تأمین هزینه‌هایش با کسری بودجه دست‌وپنجه نرم می‌کند.
🔹
در چنین شرایطی، فروش دارایی مازاد می‌تواند بسیار کم‌هزینه‌تر از خلق پول باشد.
🔹
چاپ پول، باری تازه بر دوش اقتصاد می‌گذارد اما فروش یک دارایی غیرمولد، می‌تواند آنچه را سال‌ها بی‌استفاده مانده، به منابع مالی تبدیل کند.
🔹
دولت هم‌زمان می‌تواند آن دارایی را به دست بخش خصوصی بسپارد تا شاید از دل زمین و ساختمان خاموش، سرمایه، تولید و اشتغال متولد شود.
🔹
اما این کار، مدیرانی شجاع و حرفه‌ای می‌خواهد، مدیرانی که بدانند نگه داشتن هر دارایی، لزوماً نشانه ثروتمند بودن نیست. گاهی ثروت واقعی در توانایی تبدیل دارایی راکد به فرصت است.
🔹
البته مسیر آسان نیست. بروکراسی، مقاومت دستگاه‌ها، قیمت‌گذاری، تغییر کاربری و مزایده می‌تواند این تصمیم را فرسوده کند.
🔹
اگر دولت دارایی مازادی دارد که برای اداره کشور ضروری نیست، باید آن را شفاف، حرفه‌ای و منصفانه به فروش برساند پیش از آنکه برای تأمین هزینه‌های امروز، از جیب فردای مردم خرج کند.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/684034" target="_blank">📅 21:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684033">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bedb53e8b.mp4?token=AXqvaUP8Q9vK3e3-gqudx5NJRK3NCt4nNkA5lQJvi3GUpJW55D-mhGlTjMJTvs6HhHaR6RRoRc_OvMOwNxuT-0Y7QjRYhNVeFdfJq9mcDP89wGGNObq8UatqxCuZI7jOWXLC1jKW9hhJbhxq__y7fw5kUJRYsF026L5r-tpaeB6K5j4IPaU1AIKdo88stzpsQIgUBumT-qjSkJhtZDpZvt3gnpXbC0sHGVxoZramnz-nK6jDa0qkGVU5x0bnUhzusf5IwVymrLRb_vXmEwhof4KlsKfk7soWgAh0Cq9lw7UJy-A4oICSUxvFI5Bru1_PLANywF9SL3fBXmAMKFCRzYviIjaYA6qTXyR9Wrak6694IZPL_JcG7zC-TbkzwcB1E69yw641MZQ4piku7NMYM8ndkZO2_nchjBJDXlUiIkZEYeq0QsKx8siF11tfFHQByZpvFXf-7BjC0zYZdSwb8qim_D7Sj1ofAabtg502B0TJpqUAau4sq506jMmaStE5e1u2IrD9GEYJaGKBspQSWT7xxO6_ftx_fw0Wf9ybKpXb5AyByHnC_V1p3WPf-Gb7wKMSfd-mi2Ua22Szz4T-48ApRTjUQw_HmPgwB1FI6RrnR0KGYsKvna8q0vr3czYqYUeFbvo4wM_XCB-5z8l2Zf25cA6nGEbqxFSu9GAwBP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bedb53e8b.mp4?token=AXqvaUP8Q9vK3e3-gqudx5NJRK3NCt4nNkA5lQJvi3GUpJW55D-mhGlTjMJTvs6HhHaR6RRoRc_OvMOwNxuT-0Y7QjRYhNVeFdfJq9mcDP89wGGNObq8UatqxCuZI7jOWXLC1jKW9hhJbhxq__y7fw5kUJRYsF026L5r-tpaeB6K5j4IPaU1AIKdo88stzpsQIgUBumT-qjSkJhtZDpZvt3gnpXbC0sHGVxoZramnz-nK6jDa0qkGVU5x0bnUhzusf5IwVymrLRb_vXmEwhof4KlsKfk7soWgAh0Cq9lw7UJy-A4oICSUxvFI5Bru1_PLANywF9SL3fBXmAMKFCRzYviIjaYA6qTXyR9Wrak6694IZPL_JcG7zC-TbkzwcB1E69yw641MZQ4piku7NMYM8ndkZO2_nchjBJDXlUiIkZEYeq0QsKx8siF11tfFHQByZpvFXf-7BjC0zYZdSwb8qim_D7Sj1ofAabtg502B0TJpqUAau4sq506jMmaStE5e1u2IrD9GEYJaGKBspQSWT7xxO6_ftx_fw0Wf9ybKpXb5AyByHnC_V1p3WPf-Gb7wKMSfd-mi2Ua22Szz4T-48ApRTjUQw_HmPgwB1FI6RrnR0KGYsKvna8q0vr3czYqYUeFbvo4wM_XCB-5z8l2Zf25cA6nGEbqxFSu9GAwBP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکات بسنت، وزیر خزانه‌داری آمریکا: هر نهادی که به نمایندگی از ایران پولشویی کند، از نظام مالی مبتنی بر دلار آمریکا حذف خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/684033" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684032">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5ae27fa7.mp4?token=FaWg41RJZckGgzD6PLM7cFToiJD0ud_OHHiwxhFeDBNUPf808XaoV5e8oPtl1QeZFvWI3LWDZaAo5HZSwZSHHNHJ4mTnMv6GwctUSIpq2sgnV8qKuC7R8AGPNNj_-J8f4i42aEDQlqVTSAUJBSubP_sT3dEuVokEu-i-AK1ajXCerVPmG3T4EY4aahaFgSf4GdodrSVhTLVUauvLp1Uko1ys0t80dSQePgj3CsiMdtnNsR08t3rdMknVmTM15tip7rJWwpYGLZ0rImOU069U_tpPgHkXT61t-iRJ9d9_NSLwAfTjOd0jxxhJHiX1pl3nZGCPGBYMulbCoEOZ4_Sicg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5ae27fa7.mp4?token=FaWg41RJZckGgzD6PLM7cFToiJD0ud_OHHiwxhFeDBNUPf808XaoV5e8oPtl1QeZFvWI3LWDZaAo5HZSwZSHHNHJ4mTnMv6GwctUSIpq2sgnV8qKuC7R8AGPNNj_-J8f4i42aEDQlqVTSAUJBSubP_sT3dEuVokEu-i-AK1ajXCerVPmG3T4EY4aahaFgSf4GdodrSVhTLVUauvLp1Uko1ys0t80dSQePgj3CsiMdtnNsR08t3rdMknVmTM15tip7rJWwpYGLZ0rImOU069U_tpPgHkXT61t-iRJ9d9_NSLwAfTjOd0jxxhJHiX1pl3nZGCPGBYMulbCoEOZ4_Sicg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: ترامپ با رهبران کشورهای مختلف جهان تماس می‌گیرد و از آنها می‌خواهد تعاملات خود با جمهوری اسلامی ایران را متوقف کنند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/684032" target="_blank">📅 21:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684031">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10b3915dd1.mp4?token=aeN60B7bcHQoyxtUG6mO2S61Og51qW0W_qzov_snD_Yq4fSk3lk2sh4HZOfp-bKy47EjdSCQ6KR9JKJ-sPRLXEv_uKMXBUEE2H-Mmr3WEridPkgcUzt5cAXQDEpI00MHt3TY6GV87ljIMorz5HHDDWfi7ccgrh_CT5SyOwVRGxbWtVJCMYnYmM1LoC2Vl_YddgvTVrNctiVaa7-UGnXf4kVPY96GsvATHvw5oIekz2VeifCDvxj9OTvmk8KqFJJhOVU2uzCl1NhXWfmdled8YXAh2nfxHlM1QqyP5GCjiZ0HSXr-iweW37EDkmNKYl5CitC-ymZni2ktT8IZcKhvPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10b3915dd1.mp4?token=aeN60B7bcHQoyxtUG6mO2S61Og51qW0W_qzov_snD_Yq4fSk3lk2sh4HZOfp-bKy47EjdSCQ6KR9JKJ-sPRLXEv_uKMXBUEE2H-Mmr3WEridPkgcUzt5cAXQDEpI00MHt3TY6GV87ljIMorz5HHDDWfi7ccgrh_CT5SyOwVRGxbWtVJCMYnYmM1LoC2Vl_YddgvTVrNctiVaa7-UGnXf4kVPY96GsvATHvw5oIekz2VeifCDvxj9OTvmk8KqFJJhOVU2uzCl1NhXWfmdled8YXAh2nfxHlM1QqyP5GCjiZ0HSXr-iweW37EDkmNKYl5CitC-ymZni2ktT8IZcKhvPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گنده‌گویی بسنت: آمریکا منابع درآمدی سپاه و حکومت ایران را مسدود می‌کند  اسکات بسنت، وزیر خزانه‌داری آمریکا:
🔹
از امروز، حلقه فشار را تنگ‌تر خواهیم کرد و هر منبع درآمد احتمالی را که به تأمین مالی سپاه پاسداران و حکومت ایران کمک می‌کند، مسدود خواهیم کرد.
🔹
ما…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/684031" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684030">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منبع عالی‌رتبه امنیتی به شبکه المیادین: واشنگتن تمامی ابزارهای فشار خود علیه ایران را سوزانده است؛ چیزی برای اجرا نمانده!
🔹
شبکه المیادین به نقل از یک منبع عالی‌رتبه امنیتی سیاسی در ایران، اظهارات دونالد ترامپ مبنی بر اعمال فشارهای اقتصادی جدید علیه تهران را پوچ و صرفاً تبلیغاتی دانست.
🔹
ایران معتقد است ادعاهای ترامپ در واقع پروپاگاندای رسانه‌ای و طرحی برای افزایش فشار روانی بر مردم ایران است که توسط تیم تبلیغاتی او تدوین شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/684030" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684029">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXivjl0jk_IZ1ocgHGESUNwpOUimAN-VLzL_UwSFq4HLWrhROV-GUYzN6mOD9oAEEW6SMv_CY7-FwCHApVm3qD7oCFyJH8gOHrIPMRrlxLxL7qxFiijgrAB7hHtVX-k6QtP1-QxkC02d4eINUkGikR-0bKwprs-xsDnVBaHLfct7pEBXF4kJqhF6Bhf7HGoinhFHFZXkoZVll7oflSU1s3NvvLknZ3NYlvAJiTzJk6SOKRDm2uOboMFIEn43TtRv_Dt67zqf9k5CtY-3skBWbMF82WYf3Fl09eoR9Yi7_D2QCCZDClPmLE7oe3w1-SBu5Bl-KXWKEKx_2JBoNLGHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا ۲ میلیون تومان تخفیف با کد PNTHRD
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/684029" target="_blank">📅 21:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684028">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: به آمریکا بی‌اعتمادیم و باید رفتارش را تغییر دهد
سرلشکر رضایی در دیدار با فرمانده ارتش پاکستان:
🔹
آمریکا باید رفتارش را تغییر دهد و اقدامات عملی درخصوص اجرای شروط تفاهم‌نامه انجام دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/684028" target="_blank">📅 20:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9efd624f88.mp4?token=iHuJFkxDoImp7kiQurJR5CXnEiSTMUt5eRzEFppKD7aIbqEdWKsngAzxZotf6xR9Qaouxl3hVULOQ6M7moddFdjHBYFxsqYzbBTZg7gcVnEaP_MRWmu0EvJo4GRqroc36UXbtxwKYzCrGHKMbRLpEdhqumuZXtiKarEMKZcY5oDlhbxbALsVmebv39NTxKTtz_ZtvDaC8doWZHlp48IPSFNTLtswgIkm8gVt5zaVEz2DdPjdgAbCoupX7NxygfWUq5N5lz0rJDwEuOcT0LXLQBBHe0tPvF5IJ_o1xVUqd44rgqyc5ib1M83_Uue6IexVmK5ZtEA-l2KrOLDHtyvH7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9efd624f88.mp4?token=iHuJFkxDoImp7kiQurJR5CXnEiSTMUt5eRzEFppKD7aIbqEdWKsngAzxZotf6xR9Qaouxl3hVULOQ6M7moddFdjHBYFxsqYzbBTZg7gcVnEaP_MRWmu0EvJo4GRqroc36UXbtxwKYzCrGHKMbRLpEdhqumuZXtiKarEMKZcY5oDlhbxbALsVmebv39NTxKTtz_ZtvDaC8doWZHlp48IPSFNTLtswgIkm8gVt5zaVEz2DdPjdgAbCoupX7NxygfWUq5N5lz0rJDwEuOcT0LXLQBBHe0tPvF5IJ_o1xVUqd44rgqyc5ib1M83_Uue6IexVmK5ZtEA-l2KrOLDHtyvH7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده گویی بسنت: آمریکا حمله اقتصادی به شبکه‌های مالی ایران در سراسر جهان را آغاز می‌کند  اسکات بسنت، وزیر خزانه‌داری آمریکا:
🔹
ما یک تهاجم اقتصادی علیه ارتباطات مالی ایران در سراسر جهان آغاز می‌کنیم. هدف ما قطع کردن تمام شریان‌های اقتصادی است که این رژیم…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/684027" target="_blank">📅 20:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc411dd662.mp4?token=LsuPYOJym4vXhBwbb6B0iMFEWYwIMXTp6aBMlhyadQBCoR1NHKqaXGPkhK6N5lClgGK3TiszGG7UfRhI01g-jezKf4jQjydc67FqoBzHQbZDWZX31HGbVOaU51nyp6IfopCv0msAYXVfMwOxhdyhrdV-DHI_BlxiOaIIYGYN3k7GTVtMZlGSSNSv-XeoBfC587ANW7bE0210Y8j3QfDDXLEbjNG2ZJTPMrx2C3GFYcG09zhnQk399Ohry3Vf_L3wAOfHV8MbU-kgIsvMWvBOW5phFM7bqY-3WYh_G3ZMJ2LqO8-__HBXWdoPvC-T5gus2s4vw9ehj59ktKkdBauuJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc411dd662.mp4?token=LsuPYOJym4vXhBwbb6B0iMFEWYwIMXTp6aBMlhyadQBCoR1NHKqaXGPkhK6N5lClgGK3TiszGG7UfRhI01g-jezKf4jQjydc67FqoBzHQbZDWZX31HGbVOaU51nyp6IfopCv0msAYXVfMwOxhdyhrdV-DHI_BlxiOaIIYGYN3k7GTVtMZlGSSNSv-XeoBfC587ANW7bE0210Y8j3QfDDXLEbjNG2ZJTPMrx2C3GFYcG09zhnQk399Ohry3Vf_L3wAOfHV8MbU-kgIsvMWvBOW5phFM7bqY-3WYh_G3ZMJ2LqO8-__HBXWdoPvC-T5gus2s4vw9ehj59ktKkdBauuJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده گویی بسنت: آمریکا «عملیات طرد اقتصادی» علیه ایران را آغاز کرد  اسکات بسنت، وزیر خزانه‌داری آمریکا:
🔹
امروز، وزارت خزانه‌داری آمریکا عملیات «طرد اقتصادی» را آغاز کرده است؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.»
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/684026" target="_blank">📅 20:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abecb4465f.mp4?token=nvQZ8Rjp5lVfQnw9yda149hjnNK3LNf5LTtOXO25yFGLtZHX3QT4iQ0vxxg01-Y-HJ2dTo4O4UPVPd_wkgjfYhqf7XFIBie6jMPQxDAJ3h5MK5eJLf5iYG9vHwz6q34P6pNmJ_XREsKSnZ3bnfPZFfRSuq2T4f2dGvAyOCymY9x8TpU2WeMhUhYLlWgh_7LAA0YSKwT2yfCLllU_nB1Zr24XH7csdOR9JeItfEq0P7oGB5ChTcH0XNTxc4ZXFaASD76vVK07LtCwI5ajas91PM-uL6TfkRFauNYV0YFtRfo75ua1I03WHgB3aNmhJ8LDWoGxzdhkGHRB82TnSDIaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abecb4465f.mp4?token=nvQZ8Rjp5lVfQnw9yda149hjnNK3LNf5LTtOXO25yFGLtZHX3QT4iQ0vxxg01-Y-HJ2dTo4O4UPVPd_wkgjfYhqf7XFIBie6jMPQxDAJ3h5MK5eJLf5iYG9vHwz6q34P6pNmJ_XREsKSnZ3bnfPZFfRSuq2T4f2dGvAyOCymY9x8TpU2WeMhUhYLlWgh_7LAA0YSKwT2yfCLllU_nB1Zr24XH7csdOR9JeItfEq0P7oGB5ChTcH0XNTxc4ZXFaASD76vVK07LtCwI5ajas91PM-uL6TfkRFauNYV0YFtRfo75ua1I03WHgB3aNmhJ8LDWoGxzdhkGHRB82TnSDIaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هفته سوم لیگ برتر؛ تعویض طلایی نکونام و پیروزی لحظه آخری تی‌تی‌ها در دومین بازی بزرگ هفته
🔹
تراکتور بعد از ۷ سال در یادگار امام پرسپولیس را شکست داد
🔹
تراکتور ۱ - ۰ پرسپولیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/684025" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تجربه تلخ خرید طلای تقلبی در بازار!
🔹
«از ۴ تا سکه‌ای که میخواستم بفروشم ۳‌ تاش تقلبی بود.»، «با هر برند و هلوگرامی توی بازار سکه تقلبی ریختند.»
🔹
با افزایش قیمت طلا و علاقه مردم به سرمایه‌گذاری در این حوزه؛ شاهد موج جدیدی از طلای تقلبی در بازار هستیم
🔹
مسئولان اتحادیه می‌گویند مردم خودشان باید زمان خرید دقت کنند و امکان نظارت بر همه فروشندگان نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/684024" target="_blank">📅 20:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b49fad62e.mp4?token=oLsLdKLARYtyYLLeTruNrMbvMjgIdH3fR8ioXeHT0gRHpNENi5PH_4nNXrdeH5ItblwQypFxnKqENkXUJmDn28RIdQMdid0tUrm6Nf-LgHT4HoVdECpGMzSdA2s6KUGh7BHMX9DFZoGWTN3BbRfrTXWIkJQuGDvOVJbfqkwCqtIQhNcrzJGa6RtvPncJTrIRbi3FCWl3VN9Q1xgkYh8I6kEAcPnMI0_DPp3c2oam6wwiKXj8N2fatkKF2Yu-J4HvXVEUjh-IO9w-lPkqwEx2u7-JhEG-6xkPmPEOB0JLsaqQxM3xmfmFtH5kDF3nO5V9xpHTBqISpwHRf7grbM16Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b49fad62e.mp4?token=oLsLdKLARYtyYLLeTruNrMbvMjgIdH3fR8ioXeHT0gRHpNENi5PH_4nNXrdeH5ItblwQypFxnKqENkXUJmDn28RIdQMdid0tUrm6Nf-LgHT4HoVdECpGMzSdA2s6KUGh7BHMX9DFZoGWTN3BbRfrTXWIkJQuGDvOVJbfqkwCqtIQhNcrzJGa6RtvPncJTrIRbi3FCWl3VN9Q1xgkYh8I6kEAcPnMI0_DPp3c2oam6wwiKXj8N2fatkKF2Yu-J4HvXVEUjh-IO9w-lPkqwEx2u7-JhEG-6xkPmPEOB0JLsaqQxM3xmfmFtH5kDF3nO5V9xpHTBqISpwHRf7grbM16Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیاده گویی بسنت: آمریکا «عملیات طرد اقتصادی» علیه ایران را آغاز کرد
اسکات بسنت، وزیر خزانه‌داری آمریکا:
🔹
امروز، وزارت خزانه‌داری آمریکا عملیات «طرد اقتصادی» را آغاز کرده است؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/684023" target="_blank">📅 20:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21936b253f.mp4?token=JR71aA4Hu6eD38r27giJ8TnyFXAn9_oHiX-5Pjqr1yu4H0sQcnmWNbQKUNM6yyRCpbWNLSMfeQ9lEyGniNkIQ9JpTLS7PjlLgKeiDiFVKhJJkB5OcCNFXyb3AyotYSaXhDzpkeiPd9ms0Zs2mh7DCSpRwB64G1oZfrtap1VDkrXqpb_uGso9S56sQ3eRxEy61Yy4jnOxwnAFd9gdnTe5JSNZncP0sh-LX0tYAM04KhzFvG1Ws-eeAtjkhaISFIa_cQ3BxkwLi9NZ1nAJTZIGQvmj43z-QySR8KaPSv3koNDcdAaA_La91tapIrgkQdg496S6hMtDjGzhtZI-6pYiEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21936b253f.mp4?token=JR71aA4Hu6eD38r27giJ8TnyFXAn9_oHiX-5Pjqr1yu4H0sQcnmWNbQKUNM6yyRCpbWNLSMfeQ9lEyGniNkIQ9JpTLS7PjlLgKeiDiFVKhJJkB5OcCNFXyb3AyotYSaXhDzpkeiPd9ms0Zs2mh7DCSpRwB64G1oZfrtap1VDkrXqpb_uGso9S56sQ3eRxEy61Yy4jnOxwnAFd9gdnTe5JSNZncP0sh-LX0tYAM04KhzFvG1Ws-eeAtjkhaISFIa_cQ3BxkwLi9NZ1nAJTZIGQvmj43z-QySR8KaPSv3koNDcdAaA_La91tapIrgkQdg496S6hMtDjGzhtZI-6pYiEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه ونس به شرکای آمریکا: کانادا و چین در سیاست‌های تجاری بدترین هستند
جی‌دی ونس، معاون ترامپ:
🔹
کانادا و چین بدترین کشورها در زمینه سیاست تجاری در جهان بوده‌اند.
🔹
چین بزرگ‌ترین رقیب اقتصادی ماست و چنین رفتاری از آن قابل انتظار است؛ اما من انتظار چنین رفتاری را از کانادا نداشتم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/684022" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
زیان انباشته بانک‌ها ۳ برابر شد
🔹
ترازنامه بانک‌ها یک هشدار جدی را نشان می‌دهد. زیان انباشته شبکه بانکی از حدود ۱٬۹۰۲ هزار میلیارد ریال در سال ۱۳۹۸ به ۵٬۸۸۵ هزار میلیارد ریال در نیمه نخست ۱۴۰۳ رسیده است.
🔹
یعنی در کمتر از ۵ سال، زیان انباشته بیش از ۳ برابر شده است. اما نکته نگران‌کننده‌تر، تمرکز این زیان‌هاست، بخش بزرگی از آن در چند بانک ناتراز متمرکز شده و بانک منحل شده آینده با فاصله در صدر قرار دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/684021" target="_blank">📅 20:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmszuJ1fZSLtEJAlZYuvuMftDk4hlSaVLtYwwPuaSqRrGNMFgEiDQveYuk8RX1MDiKVmufodoIO34nCF4xAfGr7lh2qlAhP8Ml6WK9fTjcCQ5h0QIjDc3PXeQM8uRcIAq3MbXy1vFEPRAA68IZCQKiNIyE7x2n8A9L9BES-CuxuJkPb2JYy1JBPpoYfWL4ll9ZUDarDRyGROSrpRgBxXiH80nAnssiBwnc98_XG7En4uIRfCQ7XmLj3XhZR4ctF1G21yZe9fmHTsesVcdXoOxGVrWIpd0-UgXP7YWh-qxgkaGnG7GOel-nJtrqR3lKW8VQ7ZG7_XuK9yxR7qNFotEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: کسی گُنده‌لافی‌های آمریکایی‌ها را باور نمی‌کند/ شرکای تجاری ایران به ما پیام داده‌اند که تهدیدهای آمریکا را به هیچ جا حساب نمی‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/684020" target="_blank">📅 20:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40949b4013.mp4?token=ZeEekAlqMZ6VwCjLctWzuDU5Bfh0K8ANvJTmNx0hmdmlAFanFQh1gCE2RQWz0IJsW9yohQfqUgnwox_cAl9yrD9iw35H_rW2v1ReWhJ4NJd2gNE6P5ppK-ya2LNfMje7q0wjmC6hAh2NZ0DKEgW8xqGIuA9t1TExdnUPXnyULMejuFX8FfB1b7JGoXqrwmbX5TinoiENu9coqsCUfab1rsCFJE8rSE4yAoFEByQd0MlbQO_b5-Nm_bp3z5xgPX9kV245oQV85llZbRNb0aJdD24C1SBNxwMvokC4AE1_tAp3gVRl0Q62Xd3d4vXhIwJwTWLG4GqB_OF4GTB8h6AKJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40949b4013.mp4?token=ZeEekAlqMZ6VwCjLctWzuDU5Bfh0K8ANvJTmNx0hmdmlAFanFQh1gCE2RQWz0IJsW9yohQfqUgnwox_cAl9yrD9iw35H_rW2v1ReWhJ4NJd2gNE6P5ppK-ya2LNfMje7q0wjmC6hAh2NZ0DKEgW8xqGIuA9t1TExdnUPXnyULMejuFX8FfB1b7JGoXqrwmbX5TinoiENu9coqsCUfab1rsCFJE8rSE4yAoFEByQd0MlbQO_b5-Nm_bp3z5xgPX9kV245oQV85llZbRNb0aJdD24C1SBNxwMvokC4AE1_tAp3gVRl0Q62Xd3d4vXhIwJwTWLG4GqB_OF4GTB8h6AKJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک ترفند ساده میتونی شارژت رو درست کنی #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/684019" target="_blank">📅 20:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb175d00c.mp4?token=i9Ws1SW6fFa4VdvgXMlJKYH4WBxlnXOIwlzgCUf0T-lzUBTriJK52BTdUcXWFm9up3zqHVK2bzjZCtMVrR9F8JChFjA6iupEJBwPe4R6w49e_Ih6RgHQbUlipIbhP5ytZWAWZeT5EGezHjZG9KJL1Saj_4Dp60ZZOt8YBmMSzxJgfQY9o42RpSVob93Sn8MCRQdasa-PnACiCBQJ7Tt6Hep-x_UsoE6I4ExDuJS1MhRuk7b72DVa_o_hrUrbCPuMO1HAOe1F3ZVS-blfGhNnafHGKS-qI4MPqmjJS4YKir3R1FmqomjYG2qMGWRB8rxL7L6IQfw8wxLhNFBgOVwdIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb175d00c.mp4?token=i9Ws1SW6fFa4VdvgXMlJKYH4WBxlnXOIwlzgCUf0T-lzUBTriJK52BTdUcXWFm9up3zqHVK2bzjZCtMVrR9F8JChFjA6iupEJBwPe4R6w49e_Ih6RgHQbUlipIbhP5ytZWAWZeT5EGezHjZG9KJL1Saj_4Dp60ZZOt8YBmMSzxJgfQY9o42RpSVob93Sn8MCRQdasa-PnACiCBQJ7Tt6Hep-x_UsoE6I4ExDuJS1MhRuk7b72DVa_o_hrUrbCPuMO1HAOe1F3ZVS-blfGhNnafHGKS-qI4MPqmjJS4YKir3R1FmqomjYG2qMGWRB8rxL7L6IQfw8wxLhNFBgOVwdIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادتی که باعث می‌شود شما پولدار نشوید!
🔹
یک دام ذهنی ممکن است شما را سال‌ها بدون اینکه متوجه شوید گرفتار کرده باشد.
🔹
بعضی‌ها فکر می‌کنند پولدار نشدن نتیجه درآمد کم است؛ اما گاهی مشکل جای دیگری پنهان شده.
🔹
این ویدئو را ببینید چون باور داریم که حتما کمک‌تان خواهد کرد!
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/684018" target="_blank">📅 20:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684016">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">03 Ane Manaee (1403-07-26) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684016" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه سوم
حجت‌الاسلام امینی‌خواه:
🔹
شهید ۲۱ ساله؛ پرواز عارفانه به سوی حق [2:22]
🔹
سیر و سلوک در عصر شتاب؛ شهادت، میانبر راه آسمان [3:59]
🔹
جهاد؛ عرفان عملی در میدان نبرد [5:33]
🔹
کافران؛ بازیگران نقشی شکست‌خورده [9:20]
🔹
چرا مؤمنان در دنیا و آخرت پیروزند؟ [12:41]
🔹
قرآن؛ چراغ راه مؤمنان در فتنه‌ها [15:16]
🔹
آزمون صبر: تا کجا باید منتظر ماند؟ [23:41]
🔹
حکمت‌های الهی در مسیر آزمون و اعطا [31:33]
🔹
فتح پس از مقاومت: مسیری روشن به سوی آینده‌ای بهتر [34:21]
🔹
خداوند انتقام گیرنده: وعده پیروزی بر ظالمان [38:28]
🔹
وقتی ملائک، سرباز شهید سیدحسن نصرالله می‌شوند [49:52]
🔹
صدای حق در برابر باطل: داستان شهید آرمان و ایستادگی او [50:26]
🔹
مکر الهی: فیلم‌هایی که پرده از جنایت‌ها برمی‌دارد [53:23]
🔹
از کوچه پس کوچه‌های محله تا کتابخانه‌های جهانی: سفر کتاب سلام‌ بر‌ ابراهیم [58:08]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/684016" target="_blank">📅 20:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684015">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqA6Y5Y0ZqamT2ihaXtpd6RecqfMqFAHlQmeqjBnFknksovDKx9ERDZj_7P76pYzD2YTy_cm6fI1Kjk7M3jdhcClnDSEx6iKJVzzxyI2YCGWWARMxscZrBkHsjCcS1NlAWqdkt6GMmjj7Jadh0q3R6EzAgG1kFwfkrLj4Gg_t5fZVuraaAIlmKVrldDjnzkTPCXT3zWqJkZrDxAUUXMJOLD4HrOjUmRVi04XRGfCC8X_1mI-45ajews3NPh4lGkZio8OrUDf_XhHIALVAOwIJ0KanjWh1lmF1nC0k0_jGSGGFSRdWPQUr3kkIhwR5-gH0oXFtPEHQ5wrS6MsDiq_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفن ابری فونیک، بدون دردسرهای راه اندازی
برای راه‌اندازی تلفن شرکت لازم نیست سرور و تجهیزات بخرید یا متخصص VoIP داشته باشید.
✓ بدون خرید تجهیزات
✓ ضبط و گزارش‌گیری تماس‌ها
✓ تلفن گویا (IVR) و صف تماس
✓ بدون نیاز به زیرساخت پیچیده
✓ مناسب تیم‌های دورکار و چندمکانه
✓ مدیریت ساده‌تر تماس‌های پرتعداد مشتریان
تلفن کسب و کارتان را هرجا که هستید همراه خودتان داشته باشید.
🎁
تست رایگان ۲۴ ساعته فونیک
https://isp.abrenik.com/fonik</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/684015" target="_blank">📅 20:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684014">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای جدید نتانیاهو: ایران قصد ترور یکی از اعضای خانواده‌ام را داشت
🔹
بنیامین نتانیاهو، نخست‌وزیر درمانده رژیم صهیونیستی، در چرخشی تازه برای فرار از بحران‌های داخلی و شکست‌های پی‌درپی میدانی، مدعی شد که ایران برای ترور یکی از فرزندان او برنامه‌ریزی کرده بود.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/684014" target="_blank">📅 20:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684013">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe1319de9.mp4?token=ARVlJ7tDLH2ZmZ-5t3aYzKNSN-o5_VMxdGUF3YBr8b2EdcTl1Hfy5yKVdE6Y8T-fv4FYfGRP_NylLllItFkjeaTqWZWLQ1lSdKsM6YKLh_twahIfXpRx7V8XDytIzrqsvaOqEkyZZY9bANHdMG_nLplqGemp_b1aFCKywhQgOMfczxg54qq8zeXxtQpt2SjbxG2DqHeaduLob5_SgsDjgoLCCWa3ZqYpPcWSPqQCCH1GptPTPuprJhpLqPcYuir_F8azvqdWoW89UzFlXMTBWfGtZqKTlaJOM3ScWJhoZJkMMoiDQT10F2WEvkUE-Zond6iu1e09F7gVXkHGD0i617RZcy4_U1HOLOsoufEkJ5fRPkDUPzGvpBv8abLqG75IAxW0Ej7nJacmFXAHaC1BxjYl4_WI6SID23TxnFWtfSNV5K5aaUNT6mS76YatjCs-zOx9VrnvacNRUW6SI7uUHCwFeOw4W0gZesAeaU4RBqOLIqLnYwSjZ6nXqY5BBkJnlMM9SSHZklAqJumGPTzm3PSYhw-UaVNh3Tww-9VhhTdcrIS_TpRx8BIwA5i77dtaNqVYRsC9Orx_GRqu5y2xMEaCUTsooTxzcVz_ptraGnvLgxLNCkcc_UlPMuSsN6I9QSYTZfxG8VI8AftWUDU8hU5dOqX_BS_xrpnRNoIctRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe1319de9.mp4?token=ARVlJ7tDLH2ZmZ-5t3aYzKNSN-o5_VMxdGUF3YBr8b2EdcTl1Hfy5yKVdE6Y8T-fv4FYfGRP_NylLllItFkjeaTqWZWLQ1lSdKsM6YKLh_twahIfXpRx7V8XDytIzrqsvaOqEkyZZY9bANHdMG_nLplqGemp_b1aFCKywhQgOMfczxg54qq8zeXxtQpt2SjbxG2DqHeaduLob5_SgsDjgoLCCWa3ZqYpPcWSPqQCCH1GptPTPuprJhpLqPcYuir_F8azvqdWoW89UzFlXMTBWfGtZqKTlaJOM3ScWJhoZJkMMoiDQT10F2WEvkUE-Zond6iu1e09F7gVXkHGD0i617RZcy4_U1HOLOsoufEkJ5fRPkDUPzGvpBv8abLqG75IAxW0Ej7nJacmFXAHaC1BxjYl4_WI6SID23TxnFWtfSNV5K5aaUNT6mS76YatjCs-zOx9VrnvacNRUW6SI7uUHCwFeOw4W0gZesAeaU4RBqOLIqLnYwSjZ6nXqY5BBkJnlMM9SSHZklAqJumGPTzm3PSYhw-UaVNh3Tww-9VhhTdcrIS_TpRx8BIwA5i77dtaNqVYRsC9Orx_GRqu5y2xMEaCUTsooTxzcVz_ptraGnvLgxLNCkcc_UlPMuSsN6I9QSYTZfxG8VI8AftWUDU8hU5dOqX_BS_xrpnRNoIctRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جهانگیر الماسی: پول غذا ندارم؛ هفته ۴ بار غذا می‌خورم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/684013" target="_blank">📅 19:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684012">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFu7VFiyLnMOJ6H3gdCOoBe52MOuezutlwS9aukLfMXBFUlz2dA7uTc5wB3vsFP87k1W8o-1PXoy7jkbzDFvUIT1ZGzMYb2XK_tbnXbM8H8akK8ngyzoI64UHpIjYJEWvPvcyySD_YH__bU5OiQ02Blom9Xw71ZDJgNZDR7ucE5u53TEFDFkbTvUpoBA94NDLNGVN8NHgrL3msaP8a10GJyARDB1-R487QR2vEkR_CQJ5aE_Z4ckuQAHdzJcldRR1sbricZUabPUI68bOohxoHSUMprP9iAwY2gbEbW7_F8Nyc1EIRhleokPIt3ObwDnTGHv8r8mgph15CY7x6gTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت کودک فلسطینی در حمله صهیونیست‌ها به غزه
🔹
در ادامه کارزار سیستماتیک نسل‌کشی و کودک‌کشی ارتش رژیم صهیونیستی در نوار غزه، حملات هوایی جدید به «دیرالبلح» جان یک کودک بی‌دفاع دیگر را گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/684012" target="_blank">📅 19:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684011">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
فرار رو به جلوی ترامپ: دموکرات‌های افراطی نظرسنجی‌های دروغ منتشر می‌کنند تا ما را قبل از انتخابات دلسرد کنند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/684011" target="_blank">📅 19:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684010">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGvgNpG1mrxjf_QEFz1qMBZJAqWLiDTOhmDQRHpcFeLJgbajTNLdkhTCkDapEUrenwJoNiwJ_qcr4B0tGS5lV-URGbQ7x3Q5QlUHYAGht2JMoNSDEKDUVezX9j3H6We_BDAkvgpnwmYjI4sCsAsK_Jpugcg_ykExGFxIIfqvVcyiCeANB4RawFgJzpGcQgls2zoQNLxQj9VPICBJHXoUGZY5af6WnPB6O1FrrzWF1y7DFV4v4MKQS6Mbw0VGOLzFJVN22yemzQmDANOex3ucxfPMDbKVQnripMGx-wUFjJqaj1tgllKrzW4Xv2qleaPVQpxXlNpKDHg1PrNaZu4QRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاهای خسته‌ای که جای چرخ موتور را می‌گیرند/ «پیک پیاده»؛ فرزند جدید فقر و فشار اقتصادی
🔹
در پیاده روهای کلانشهرها افرادی را می بینیم که کیسه هایی به دست دارند و می آیند و می روند. برخی از این افراد، خرید کرده اند اما بعضی دیگر پیک هستند. شاید تعجب کنید اما چند سالی است که «پیک های غیرموتوری» در بازار رواج یافته اند؛ افرادی که موتور و ماشین ندارند و بسته ها را با پای پیاده یا از طریق مترو و اتوبوس جابه جا می کنند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239896</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/684010" target="_blank">📅 19:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684009">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
۱۳ درصد تورم ایران به خاطر مسکن است!
🔹
یک عدد در اقتصاد ایران به‌سادگی قابل چشم‌پوشی نیست، حدود ۱۳ درصد از تورم کل، مستقیماً به بخش مسکن مربوط می‌شود.
🔹
این سهم طی سه سال اخیر تقریباً ثابت مانده، چون قیمت مسکن به‌عنوان دارایی سریع‌تر از اجاره رشد کرده و همین موضوع باعث شده این بخش در برابر کاهش تورم مقاومت کند.
🔹
مسکن همچنان یکی از سرسخت‌ترین موانع کاهش تورم باقی می‌ماند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684009" target="_blank">📅 19:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcuQVYl0RMcyOqTjFiQdUWEV0Gb1khDqPYLp6ZUwQbO7dZ5BzfbOCzhPak_3_inNI7JMl28GGS9-eZzbLX_Hv8pHsamgyLIKwnO1nmJ_o_jmh6rpl_1P_rlCwCUkjOuW25GldXUrA-LqaBw_SieWSXmolr6INCE1k6H5H2Wz1abe850Sr0XWAZ-KJ626mHgNzkCfjWcnbjYkxmBqzCcRtgpiTCXsMibUkzRmAEbVf1Xl1frWFwlSRSa0DeY3UwwwIdTQg4aPDuW0jFnGYnUNqqNyR4GQbFQPZcmMyy3_rmVRfqW4UUu8Ut1V59Lfj2sTgjsP_cuaeWHXLB-ul9aguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jbhiu3gmXNxU_LMRz8DrvVH3mw_Vrca3vu1Gi6BqCzA5pD8ZKNBX7ZowS9K6CKt0DYl_iWTYzgKQnJALXHGQyxh-BxEjtkrDnSnzrxG-tu_OLElEnHEPaxoZeW8QJENIs1v0cQWiNOresCk-Yxl4z7U_CXBnr-X5scC6qHV_pSKlm9l0DhinMOPTMaMTT9BWxg6633H1wAL58jMSeqapxht1Owo5ms5Pbq5DSGe8wf5xpn-NKzvOQfOTdIaxNhszJxDNfoyas50wFbLL5e4w_2xNCPUbfeD756KaGRVDhCJ8xQUH2zP_0MOGWgWiZuQGHlKK_Gc59eEUBPOKbUSpdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ورود فرمانده ارتش پاکستان به تهران
🔹
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/684007" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aScJzd2zBrnalLnyjxrqpZN2ljz0VMlIVcU9kqNOCk31UXbaL8MxhUYEQDbvHRORzU4DM_Zy05rOnr-EhB1wiVQ4zGdAeCxKtLvDaOpgLTSkDGRN3h2elTV__2jMZmkUK8OA5i0qkVE8q24UFF9xCxOG_LNI8YnkzZ9vQEYwf1EN1HZs1T_yCHeYuppU4HVpeqzaIU4sGVrRKSZJZZnY7sDuXmVLLXFhws7ROrq0dn6yFKOmwfd72hqQ9e_NFXRDAX15Atrrp3zL_keDPeywS_XHcwX4ygG-ymcxBLkDNKySzwzhAek5JS2gPgBrp3vt_TqGXJ1G0yE_Nh3EtefDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو دو بازار
🔹
بازار امروز در ادامه روند رو به رشد خود قیمت‌های جدیدی را ثبت کرد. دلار در بازار آزاد به ۲۰۲ هزار تومان رسید، طلای ۱۸ عیار از مرز ۲۲ میلیون تومان عبور کرد و سکه امامی هم فراتر از ۲۲۰ میلیون تومان رفت. با این حال همتی رئیس کل بانک مرکزی در واکنش به این گرانی‌ها گفت که بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست و در روزهای آینده قیمت پایین خواهد آمد.
🔹
هشتصدوچهل‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/684006" target="_blank">📅 19:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGLNvUTrJBl6HC80-YAUMqtFIQ8qXpbjgqrMaGrjVydi9RxOusubm-NiAY9rftfWXaubi7tXO_gCDn-o6LQlgCB8glKVSE9d4PfnmHlJUsN36lHs6THNwQ-54kp94t_jzI4ZXE0_8uXzJ85m6ZsEiw0vf4snymDCI19s7zWqq2szwEVgYM7LwUJCjvzABMQvyvvRBWa2fTEt2T9N2soa2WJYBLnAaLJW1OtsTALRsBb2X24lFtE3J_hLkNcIQVzfEW4gbeyjDGJ_BjzCJHVA2cmKmsoeyVi_48KG_XzF9rGR_fFIxJyJsbcK4Mm1Nhgdgv8w8FXVulKXyym1ohQslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: بگذارید ایران تنگه هرمز را کنترل کند
نیویورک تایمز:
🔹
جنگ با ایران دو چیز را آشکار کرده است، ایران نمی‌تواند تنگه هرمز را به طور کامل ببندد و آمریکا نمی‌تواند آن را به طور کامل باز کند.
🔹
ترامپ باید با واقعیت روبرو شود تنگه باید بازگشایی شود، حتی اگر این به معنای دریافت عوارض از سوی ایران برای عبور و مرور از آن باشد.
🔹
این نتیجه برای آمریکا یک شکست خواهد بود. اما در حال حاضر، این گزینه کم ضررترین گزینه است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/684005" target="_blank">📅 19:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684003">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b94af2eb.mp4?token=r1fdJxx8ES4ailODJgVIcNcpl6n7mJr2R7_WXcyk1nvQIpyKZjPAkw20HdhV_dEIR5Xri1vpHi1u5wZWuYnVD_YBcrfFJ7kO33ntgdFwVyA2B8bXPP05s7ByU4heE5VXVuH8QTQy_ai--tyK_Orr5GIGC595-D_Y0TUxk5jQOabBnQAoul6ejyKF19dx1G7nLdU0IUapKU6fqWGpxv7Vq-q3z0SyBZx0CM_sgSayp1DMJatOwNudx69QlfYRsczpx3k1IOvCq9_Tb0vgStbSLJN2a0xy9TZwF4HcnWSJXtlzVpzjycnNBrIivCjrBcnqFnzSvyF6foSen7ymV9V_fEnlejkLet5B_v8ZyASyaIbGHI1BQp5PGD_YaUdU4C6pBNxc2HuUC2QKSvTCTbghYh4B2yrVB-54kOkxjtGOHMyTLwuT325OFWgvBA2TEnlwCE5arC9LwdrB1rM7GrN79iBLWosSrPUPOmE7I_SsXWlgHYeJ2OBFFgqlWVais7RcNVjTrw28iDGY5plcylsYJe9DLLV-r7TaQW3I_Uq1r0EJyDUOkWCoLA1ZDIqMUHCF37K6FLKy0Ae5aKGcqUlyogDKwzIv34gl3yMcgAlhXdBoHU9EmVA-flQ4jHBUF1_H56EfrLBwOhkIq4PgBKxSWQYzHAqHG0XILWz4sL7wIVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b94af2eb.mp4?token=r1fdJxx8ES4ailODJgVIcNcpl6n7mJr2R7_WXcyk1nvQIpyKZjPAkw20HdhV_dEIR5Xri1vpHi1u5wZWuYnVD_YBcrfFJ7kO33ntgdFwVyA2B8bXPP05s7ByU4heE5VXVuH8QTQy_ai--tyK_Orr5GIGC595-D_Y0TUxk5jQOabBnQAoul6ejyKF19dx1G7nLdU0IUapKU6fqWGpxv7Vq-q3z0SyBZx0CM_sgSayp1DMJatOwNudx69QlfYRsczpx3k1IOvCq9_Tb0vgStbSLJN2a0xy9TZwF4HcnWSJXtlzVpzjycnNBrIivCjrBcnqFnzSvyF6foSen7ymV9V_fEnlejkLet5B_v8ZyASyaIbGHI1BQp5PGD_YaUdU4C6pBNxc2HuUC2QKSvTCTbghYh4B2yrVB-54kOkxjtGOHMyTLwuT325OFWgvBA2TEnlwCE5arC9LwdrB1rM7GrN79iBLWosSrPUPOmE7I_SsXWlgHYeJ2OBFFgqlWVais7RcNVjTrw28iDGY5plcylsYJe9DLLV-r7TaQW3I_Uq1r0EJyDUOkWCoLA1ZDIqMUHCF37K6FLKy0Ae5aKGcqUlyogDKwzIv34gl3yMcgAlhXdBoHU9EmVA-flQ4jHBUF1_H56EfrLBwOhkIq4PgBKxSWQYzHAqHG0XILWz4sL7wIVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متشکریم به وقت ایران!
🇮🇷
🔹
تشکر متفاوت لگویی‌ها از عوامل «به وقت ایران»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/684003" target="_blank">📅 19:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684002">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFqlHKLUtKjb87ZiPgAsUkrzmZRLZ5tXSDzydoY7k6Ge0hX3VTNjZfcTa2IQjtHeQuG2Ind94wzbcR42DJTpBq-gk2enDAJ2KC_VBJisGL9Gk0n4V_3qVi451WbfCIBFvb_InfdkvE_ja2H_RfTO30b6VqwyKze8uw5yiFSHc_IvCK_ttui4BEeFJmzyzxjtONM8NN8L9dX8pbEdhFhuwFO6FRH4dUWrjizYw_SQsiya7v87Gic6QQkyMhVZQ5eYg0UTq06v_6NP7Jp3O6vRkSQiUsxq3zFgINdAoUFQoxLCjfMOo-ikb7CCkjfOxKkHacMep6GY9RwxYxjNvskseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطع برق در کمیسیون انرژی مجلس
🔹
کمیسیون انرژی مجلس تشکیل جلسه داده بودند تا علل قطع برق را بررسی کنند، که برق در همان زمان قطع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/684002" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684001">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367508c21f.mp4?token=S8Bau3DkRBZxWO6QczQgmMsQtkghBPPl7KrjK7f_zstYQl3R_CIdu0nf8yMo6MLKsUJlNxfMYebOZc10drOSHCNsbvyIDvXZLYozDpuTKHG6meaCdgqcUipiMOQT5b0qplbQQIBG6oOT3WVYFuh5j38slJ0x5u8AxyoT4oBngfTCLyNQYkr-kqweiQJAFrtT89xp6t_CRi3Mm0YYXuBOE2sTVJGlvTHWZ0RWEpy7FG8EoZxELZfdA6Kx3dpGRW19oLk73CyUKRWsijl1uQ8DKtg1Yc_fJ_Gm2D0uyptDROcDr94aItIe-lji6mygi8Z9aBdhckBbH7GP0oPhb7SzyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367508c21f.mp4?token=S8Bau3DkRBZxWO6QczQgmMsQtkghBPPl7KrjK7f_zstYQl3R_CIdu0nf8yMo6MLKsUJlNxfMYebOZc10drOSHCNsbvyIDvXZLYozDpuTKHG6meaCdgqcUipiMOQT5b0qplbQQIBG6oOT3WVYFuh5j38slJ0x5u8AxyoT4oBngfTCLyNQYkr-kqweiQJAFrtT89xp6t_CRi3Mm0YYXuBOE2sTVJGlvTHWZ0RWEpy7FG8EoZxELZfdA6Kx3dpGRW19oLk73CyUKRWsijl1uQ8DKtg1Yc_fJ_Gm2D0uyptDROcDr94aItIe-lji6mygi8Z9aBdhckBbH7GP0oPhb7SzyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام گلپایگانی: همسرم به معنای واقعی ام ابیهای پدر بود
همسر شهیده «بشری خامنه‌ای»:
🔹
بنده با همسر شهیدم ۲۶ سال زندگی کردم. به دلیل برخی مسایل ۱۱ سال آن را در جوار رهبر شهید انقلاب زندگی کردیم.
🔹
سیده بشری خامنه‌ای به دلیل رهبر شهید از بسیاری از وابستگی‌های خود عبور کرد.
🔹
او در کنار کارهای خانواده، کارهای رهبر شهید را پیگیری می‌کرد و مقید بود آقا هرگز تنها نباشند. به معنی واقعی ام ابیهای پدر بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684001" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683999">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کوثری: با برنامه‌ریزی تنگه هرمز را کنترل می‌کنیم
کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری :
🔹
آمریکایی‌ها به هیچ وجه فکر نمی‌کردند که گرفتار بسته شدن تنگه هرمز شوند.در حال حاضر با مدیریت و برنامه‌ریزی، تنگه هرمز را کنترل می‌کنیم.
🔹
ما ۴۸ سال است که با محاصره اقتصادی و تحریم، کشور را اداره می‌کنیم و همه دنیا پیشرفت‌های ما را دیدند و اگر پیشرفت‌ها نبودند، الان جمهوری اسلامی هم نبود.
🔹
آمریکایی‌ها بدانند با این محاصره اقتصادی، ضربات سنگین‌تری خواهند خورد.
🔹
سیاستمداران برجسته آمریکا دائما به رئیس‌جمهور قماربازشان تذکر می‌دهند که از روی نادانی، ملت آمریکا را دچار مشکل کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/683999" target="_blank">📅 18:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683998">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYHaJQ6UI42Fhdz4MkLpIsGuQ7lUpIQbUn0t-WNy_QPEf7f8Q7kIletgVe9EcGYPjT3q1G9BZdofcJNUpC5sdU-NkRJCgr3689Zj4YW4NN7afTjc7mokIEneuxUxAZWLZW7uSLEUjMb9tJAF61FkA5jW9yiVNJaFBGlUlXjihYcPunUWfEqheGwxnSnb6vO71CNBrUB0I3y4ZljWgx8VU1PKKlhLIMtpZjVD9bv4JIjgjRGz0aSSwWeCPnuq-8hO711nXZd5aWZwJ-I9K3-MtV5Qb9ysfmSbzFKWxRhy2RPBeuWfhgNWKOwO-b3wSbvT0ThioWS1G37nV5jRv4KkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ مدل قهوه سرد محبوب که می‌توانید در خانه درست کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/683998" target="_blank">📅 18:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683997">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7iVYNVaTe2iWQDAUDIT-AwEy1HAQLA6nBJL0opIr54qeG9K85MSadAVcMIBQuJVY69m-SoG7SqUNv2IKqQHz6ToWQq3i0QD3ndUGstULuND5yHOKA92qR_KPnNSW1KUgSwz0lu_5V-b3pBq0fBygy4eemg9O6OkAJylXD5ZMtfy45FYylQUWK3CwBomM2GR2tkYLMJCw0O4Y78UQeA3GAs9Vb4UTdh3XYN6TXMFqU-dMJ6OCs39aoa69N5P5x-ng5T5WJmgQMM47Kwlsre2WhzvmF_Xcn6mob6kht4CXHraWPcELitriv45jBgMaQqJu82JIa9PgdFEG_HZydmnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصفهان؛ آغاز سفرهای هفته دولت با افتتاح ۳۹۰ پروژه ارتباطی
🔹
همزمان با سفر دو روزه ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات و نماینده دولت، ۳۹۰ پروژه ارتباطی و فیبرنوری با سرمایه‌گذاری ۶.۴ همت در استان اصفهان به بهره‌برداری رسید.
🔹
با اجرای این پروژه‌ها، پوشش پرسرعت روستایی به ۸۵ درصد رسید، ۷۳ روستا تحت پوشش قرار گرفت و حدود ۲ هزار نفر به شبکه ملی اطلاعات متصل شدند.
🔹
در این مراسم، تعدادی سایت 5G اپراتورهای ارتباطات سیار و چندین پروژه ارتباطی در شهرها و روستاهای استان نیز به‌صورت برخط افتتاح شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/683997" target="_blank">📅 18:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683996">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyz_H0OoMWUPb0ZDLsNzqvtB9AGbV3mbkOzg_MkW83fWiamstu2itZQ69_y6tzKhpJhbMVaHLMK356KQgNCgl8jSyMhPae0cqdy7NiKwoXCG51mBSQMAomObTngiE5WrgHd5C_usuVVUvlKJ2XSSKYIJ-aJ31gTiaZFZlTBUJw9qznCfDX58ecQ-x-9YZUFeXpqbjNI12G4m-AAoBJp8d-irzG8bFuac6alxzZph3XpIzrtpkUXp5Zmjy8tqjYm-9zPp3a3GEkgsjY-te-EQYGvD9KGiBIccb086ONxgQyjtUfhmU5d_9My1tiMs1VDNi_bnWB8wIShM_3uHP7OiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکاف جنسیتی امید به زندگی در جهان
🔸
شکاف جنسیتی امید به زندگی به تفاوت طول عمر زنان نسبت به مردان گفته می‌شود و در هر کشوری که این عدد مثبت باشد، یعنی زنان بیشتر از مردان عمر می‌کنند.
🔸
این عدد در کشورهای اروپای شرقی نظیر روسیه به بیش از ۱۰ سال می‌رسد که ناشی از سبک زندگی و حوادث است. در ایران، این اختلاف ۳٫۸ سال به نفع زنان است.
🔸
در مقابل، کمترین شکاف جنسیتی زیر ۲ سال در برخی کشورهای آفریقایی و جنوب آسیا دیده می‌شود که عمدتاً به دلیل چالش‌های سلامت زنان و مرگ‌ومیر مادران است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/683996" target="_blank">📅 18:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683995">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای الشرق الاوسط: عراق مهلت خلع سلاح گروه‌های طرفدار ایران را به تعویق انداخت
ادعای الشرق الاوسط:
🔹
یک مقام ارشد عراقی، مهلت ۳۰سپتامبر برای گروه‌های طرفدار ایران جهت تحویل سلاح‌هایشان را به تعویق انداخت، بدون اینکه توضیحی در مورد این اقدام یا تاریخ جدیدی ارائه دهد.
🔹
عراق تحت فشار آمریکا برای مهار نیروهای طرفدار ایران قرار گرفته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/683995" target="_blank">📅 18:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683993">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZopbbwsHGJdcia43Dj8gv7IlBv_SPoOV_iOIT53QGrjnYY8MnEqJXDx9eq2Yyx_rwTuFL2H-A1xfiZpJZXUDqkv0kmzZ5xxIPQURr63T_PqZegxarnReVG_6CSGcOj5qO0zxwxX82VWBxJ9T_SygjRmvPeDY0JR8B4tAzGbq1yYIX3_K0SBHMgLCA1vY4mCzt0jYRXNuIw8tJxEOGVFnV_Tp0ecSL1f522wzE-vX1f7L1DC6Gfj10OOXymLNFIG3esRaCF7QN-f0sMQMYAy-4ESPH9fAGyDzfD3dJIX44O-VPFJZ6CKO0swRnUnfmxkCqvpjr29BMnMTr8kzuKVGPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیلی محکم یمنی‌ها به سعودی؛ نفت‌کش متجاوز در دریای سرخ به آتش کشیده شد   سخنگوی نیروهای مسلح یمن:
🔹
نفت‌کش متعلق به دشمن سعودی با نام «أمزان» در مقابل سواحل «ینبع» با یک فروند موشک بالستیک هدف قرار گرفته است.
🔹
اصابت موشک دقیق و مستقیم بوده و منجر به وقوع…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/683993" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683992">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
جزئیات نسخه تازه مصوبه مجلس
🔹
بر اساس ماده‌ی ۱۵، همه‌ی اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند.
🔹
تولید اثر هنری بدون مجوز از نهادهای قانونی کشور،…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/683992" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683991">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb1915b85.mp4?token=B4YnTwhIbKycLklMWJUl0uH4Op1I75crWtHdm_aJg4Cuo6A29BRBJJjBEdC4JuPm7RFeLLmPVtFweqombSWSP-HmLqPQi80Du8M1M0gXYaP4dJybFmnikwa6aWWbRJVRqqpjnEDRSs8ymYSUsIz_iXHGxh_pyT3RWzEM-etFyx0g5EgukuHX1NZJPyhyspvNkdJVM57KL3FTVVE4bbNcGMfV5BlKvo0m0gxZteH3_R7L2vCc-YbiUKV0YyHhJvBZUfI3UyNa9sVSCVJ0eF3-SifJiBjxVqNb_2slwyhHVKjgMwrYk6HK70lX4YT-U8dgt9XReNLoTOqM3eAfiTdnHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb1915b85.mp4?token=B4YnTwhIbKycLklMWJUl0uH4Op1I75crWtHdm_aJg4Cuo6A29BRBJJjBEdC4JuPm7RFeLLmPVtFweqombSWSP-HmLqPQi80Du8M1M0gXYaP4dJybFmnikwa6aWWbRJVRqqpjnEDRSs8ymYSUsIz_iXHGxh_pyT3RWzEM-etFyx0g5EgukuHX1NZJPyhyspvNkdJVM57KL3FTVVE4bbNcGMfV5BlKvo0m0gxZteH3_R7L2vCc-YbiUKV0YyHhJvBZUfI3UyNa9sVSCVJ0eF3-SifJiBjxVqNb_2slwyhHVKjgMwrYk6HK70lX4YT-U8dgt9XReNLoTOqM3eAfiTdnHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وسیع‌ترین کشورهای جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/683991" target="_blank">📅 18:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683990">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280cc51c55.mp4?token=aklKxO_sGwwHlx_806pHFpDfaU4TbDVvgfb91siFE2OZ9tB9TKJ0ajYNtHHb6c2jeAFtpclv2hoCQPQp1ePv1QYsYU2LZrvZ6NGe23sg-CxwboUoG0GTPwOrneYuKnTvpd2qk-gUF-GHxMa8sZvJmpqvHKKsTebRjz5Cwwfq-ydZvBVmVPdSR8VqGKuNSoc_gsO3Wmd3GmK0mp8mw-mMKSD8uWuTGFd1cAwfpMVpU9CiI1Ow0oO066lj9YPZn80ODowVi8xK29JMfA9dnr4jLOb8B1ir9I_mKYtDwm5dKCl6g1eQsYUHfZc8GlCJNPg4MObgUwQyLaIixRZR2AHbKhJDIfs-6wYjEGGx4H49f0L-pt7MAJGx9YlKAJm1sL1iM7d6AX28xJTBMmcZW9xwnwquq_PAkRWlWGRHiwPLNsAoe9NeePZ1Kp4XKt72Ioxgu8o8QrPjFSvgj-rZDidxMEQLxxtZV842Jr-Z2VzSgzyPJMDz3pf62k21KLs2btnMeqFGfTsTsD6MMAmUcSvVIyh1mq8Af8lLZOD6A57FKPHipRMM5qScaWzyPWqjGVZktECSDTEFydMRNsmnYlsT6iInsvrH7djqkGanU2quX-FwLi1VG9U8fMG1E7S009C_M05VdJDXcMm4UyeueBWGaTlAP8DSYgRIm2DSwvOeGHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280cc51c55.mp4?token=aklKxO_sGwwHlx_806pHFpDfaU4TbDVvgfb91siFE2OZ9tB9TKJ0ajYNtHHb6c2jeAFtpclv2hoCQPQp1ePv1QYsYU2LZrvZ6NGe23sg-CxwboUoG0GTPwOrneYuKnTvpd2qk-gUF-GHxMa8sZvJmpqvHKKsTebRjz5Cwwfq-ydZvBVmVPdSR8VqGKuNSoc_gsO3Wmd3GmK0mp8mw-mMKSD8uWuTGFd1cAwfpMVpU9CiI1Ow0oO066lj9YPZn80ODowVi8xK29JMfA9dnr4jLOb8B1ir9I_mKYtDwm5dKCl6g1eQsYUHfZc8GlCJNPg4MObgUwQyLaIixRZR2AHbKhJDIfs-6wYjEGGx4H49f0L-pt7MAJGx9YlKAJm1sL1iM7d6AX28xJTBMmcZW9xwnwquq_PAkRWlWGRHiwPLNsAoe9NeePZ1Kp4XKt72Ioxgu8o8QrPjFSvgj-rZDidxMEQLxxtZV842Jr-Z2VzSgzyPJMDz3pf62k21KLs2btnMeqFGfTsTsD6MMAmUcSvVIyh1mq8Af8lLZOD6A57FKPHipRMM5qScaWzyPWqjGVZktECSDTEFydMRNsmnYlsT6iInsvrH7djqkGanU2quX-FwLi1VG9U8fMG1E7S009C_M05VdJDXcMm4UyeueBWGaTlAP8DSYgRIm2DSwvOeGHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لقب متفاوت مجری شبکه سه برای محسن رضایی؛ «سرلشکر فیلدمارشال»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/683990" target="_blank">📅 18:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683989">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3296509c0.mp4?token=Lb09gPQKWcPuIVGNqn854HXY9960l2BGYwtGmDqN-d7zFCYTifqq6QPffhuCCbSH0Kq3mt3UbMyyPNRiy9m3kUAihcCx4AOiXv66aApE_xZcpi5OOAgjDbv7SUVJSjcDWX_RORWllC1Le1V03q0ymTAW-Za4CqZty2TNTWuIpWREI0KAXHwW5Ems1vVwbY_oxP_1Rn009JE0g23pg6cqhAf_8nGaGrYAx_4HMHwiYGo_DqiXzdGhykiJNNb2n2d5tBzB8r2b7xtXwqvYy-d6-9MHSwsPlYEpulfBOAtTj1Ie1tl1bngMKV8TXRtd3q7jg5-GFYYh_ugMvM__oI9CD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3296509c0.mp4?token=Lb09gPQKWcPuIVGNqn854HXY9960l2BGYwtGmDqN-d7zFCYTifqq6QPffhuCCbSH0Kq3mt3UbMyyPNRiy9m3kUAihcCx4AOiXv66aApE_xZcpi5OOAgjDbv7SUVJSjcDWX_RORWllC1Le1V03q0ymTAW-Za4CqZty2TNTWuIpWREI0KAXHwW5Ems1vVwbY_oxP_1Rn009JE0g23pg6cqhAf_8nGaGrYAx_4HMHwiYGo_DqiXzdGhykiJNNb2n2d5tBzB8r2b7xtXwqvYy-d6-9MHSwsPlYEpulfBOAtTj1Ie1tl1bngMKV8TXRtd3q7jg5-GFYYh_ugMvM__oI9CD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۰ تا رنگ کاربردی به انگلیسی رو خیلی ساده و راحت یاد بگیر #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/683989" target="_blank">📅 18:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
💰
📣
✨
نسیم سرمایه
۳۰۰ میلیون تومان وام قرض‌الحسنه
با کارمزد ۴ درصد
‼️
📅
حداقل مدت میانگین حساب یک ماه و بازپرداخت ۳ تا ۶۰ ماه
🤩
🧮
لینک محاسبه مبلغ وام و اقساط
📱
لینک افتتاح حساب از طریق اپلیکیشن سرمایه
🔷
اطلاعات بیشتر
‼️
وفق ضوابط چنانچه حائز شرایط ­باشید
تا یک میلیارد ریال بدون ضامن،
تسهیلات دریافت نمایید.
#تسهیلات
#تسهیلات_بانکی
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/683986" target="_blank">📅 17:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683985">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سیلی محکم یمنی‌ها به سعودی؛ نفت‌کش متجاوز در دریای سرخ به آتش کشیده شد   سخنگوی نیروهای مسلح یمن:
🔹
نفت‌کش متعلق به دشمن سعودی با نام «أمزان» در مقابل سواحل «ینبع» با یک فروند موشک بالستیک هدف قرار گرفته است.
🔹
اصابت موشک دقیق و مستقیم بوده و منجر به وقوع…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/683985" target="_blank">📅 17:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683984">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
عراق به ایران و عربستان پیشنهاد تشکیل یک شورای امنیتی مشترک را داد
عراقی‌نیوز:
🔹
عراق رسماً پیشنهاد تشکیل یک شورای هماهنگی امنیتی مشترک با ایران و عربستان برای رسیدگی به آنچه بحران شدید اعتماد بین دو قدرت منطقه‌ای می‌نامد، ارائه کرد.
🔹
قاسم الاعرجی، مشاور امور امنیتی نخست‌وزیر عراق، این ابتکار دیپلماتیک را از طرف دولت علی الزیدی، نخست‌وزیر برای آشتی دادن تنش‌های جدی بین ریاض و تهران طرح‌ریزی کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/683984" target="_blank">📅 17:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683983">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24152d0a7.mp4?token=P7oRsmZGdQiEAU9Iaj975wwR6kzu406VsLcUMai67zvOYnMxFpe0JIovKhMrjPywzPmIhP-Oox_KKUicSfwkJ3-oB6evi6QCgqdqkszSILcnLv-hxM7u8q2WdKbi4BuNDu1sq6HTTU0X4ZiMgNB-x2Vn2PTX-Ku868EnbgnUu6Ip_iBXZzKTziqmyqhKhKKG43I4QdkiCOaoaLtQbWZSUcdr_PbQfuxpATTbBdkb_MlVG7fp_bsUrjJezN9z63qXNf087XglKTx1BiU4YNJk9DHFpkUTdNv3e4wrv1xovHE-T6VJc89CCURfkZyn4RrHLmM8kllRDS3y-2CSwy0WcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24152d0a7.mp4?token=P7oRsmZGdQiEAU9Iaj975wwR6kzu406VsLcUMai67zvOYnMxFpe0JIovKhMrjPywzPmIhP-Oox_KKUicSfwkJ3-oB6evi6QCgqdqkszSILcnLv-hxM7u8q2WdKbi4BuNDu1sq6HTTU0X4ZiMgNB-x2Vn2PTX-Ku868EnbgnUu6Ip_iBXZzKTziqmyqhKhKKG43I4QdkiCOaoaLtQbWZSUcdr_PbQfuxpATTbBdkb_MlVG7fp_bsUrjJezN9z63qXNf087XglKTx1BiU4YNJk9DHFpkUTdNv3e4wrv1xovHE-T6VJc89CCURfkZyn4RrHLmM8kllRDS3y-2CSwy0WcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقابل جنگنده‌های J-16 چین و رافال‌های مصر در رزمایش ۲۰۲۶
🔹
جنگنده‌های چینی J-16 برای نخستین‌بار در رزمایش «عقاب‌های تمدن ۲۰۲۶» در مصر، در تمرین‌های شبیه‌سازی‌شده با جنگنده‌های رافال مصری روبه‌رو شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/683983" target="_blank">📅 17:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683982">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KapISF7rPQtYAfhrS-2oYXr1H6ks5zlQMoagY76icheEgTJ1POqpLJajKPfNJK05d0QJfD2tFZK6JJePkpUVZIC6d9n3jwFZMUbYgPW6p2Q0pLk2yJuVFUfUKSBB8_psXp6EWpkDRPibWPRgTFzrRRkONovgsTi34R9vNWCcinQZ7YoCS1WJtgrEuU5DElWzRpEoow_j-D_KyWvexBSTbql0bDRcegFm7hWcIKHh4CEIAA4LcA9npiSBBJ4aAHW8rrz5Fy8M5BnF2qxV8lBRYkcYyT7150rqD2miK7_1SyCFZBaCIlO80EMruMO07q3-MWNjOrb_4G0GPqovPztTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: از سحرگاه امروز، گسترده‌ترین و بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد.
📲
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/683982" target="_blank">📅 17:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683981">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFSOctC-5_-vhZrjctbrkwLgOsBaDxUiw7I_ripHGBkFwJUrb-dIHcpIDndAwwyofRIG6tzKJHIMaP2vHmg8fCpGmUOlWRhQ86Wd9lUXVahtYTDU273KtfTfxOZm0WmgWv3B_l3LifXqEg5RDSHVERftdnMDwKT3qpsO9v5APMYWusAG9MpnS2Lj3g8LH7C9gJtep1q0hN8xjDHG9KFWRB9UYw4tBnb-tUceELlXU2SbcoKRwECF1i25wruu4wC_d9GiWJmx--Dde38hAGfKlFC2d-iT_SWFwr4p3NKU1n1sPOy_Ycii_67eJuPNALA9UlavPfecMz7YKsE53dFG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی جدید فولاد خوزستان؛ بازگشت به تولید تنها در ۳۵ روز پس از حمله دشمن
🔹
امین ابراهیمی، مدیرعامل گروه بزرگ فولاد خوزستان، روز دوشنبه در جریان بازدید وزیر صنعت، معدن و تجارت از این شرکت با اشاره به روند بازسازی خطوط تولید پس از حمله به این مجموعه گفت:…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/683981" target="_blank">📅 17:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683979">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سیلی محکم یمنی‌ها به سعودی؛ نفت‌کش متجاوز در دریای سرخ به آتش کشیده شد
سخنگوی نیروهای مسلح یمن:
🔹
نفت‌کش متعلق به دشمن سعودی با نام «أمزان» در مقابل سواحل «ینبع» با یک فروند موشک بالستیک هدف قرار گرفته است.
🔹
اصابت موشک دقیق و مستقیم بوده و منجر به وقوع آتش‌سوزی گسترده در این شناور شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/683979" target="_blank">📅 17:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683978">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3d5fbbed.mp4?token=etQ5FwsBUq0YZ0WZRMIDL7wLTJSdV_-14QypEJbPtmM0-rxAirGNQ-QO3RwVTFwzaccO8LA78-fiqmtkfxjJqyogF1hCGklmuc1q5VFB3LveUtrccvYqhAwk7v6XCaELlLMUOYG8_L1Feye28fufS1gN2OF7fbJRxPy1ZcrTDKX-u36O49g1OY70_pQ0HVcONzhCg2Z5DjO1VUbM-3znI01aDJ5h5jIPXPbnn6_w15S8TYj_NnjRF16O1JCh9U3G_aYIX-brRTaMNZLZ2pFQk9rjtBnaf2Yec-xI8L1gf6LxCtnjewbkimG9pMk2ynq8kx5Bymq-QbPioI2BXKgn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3d5fbbed.mp4?token=etQ5FwsBUq0YZ0WZRMIDL7wLTJSdV_-14QypEJbPtmM0-rxAirGNQ-QO3RwVTFwzaccO8LA78-fiqmtkfxjJqyogF1hCGklmuc1q5VFB3LveUtrccvYqhAwk7v6XCaELlLMUOYG8_L1Feye28fufS1gN2OF7fbJRxPy1ZcrTDKX-u36O49g1OY70_pQ0HVcONzhCg2Z5DjO1VUbM-3znI01aDJ5h5jIPXPbnn6_w15S8TYj_NnjRF16O1JCh9U3G_aYIX-brRTaMNZLZ2pFQk9rjtBnaf2Yec-xI8L1gf6LxCtnjewbkimG9pMk2ynq8kx5Bymq-QbPioI2BXKgn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اخبار تائید نشده از حمله سنگین یمن به مواضع حساس و انبارهای سلاح مزدوران سعودی
🔹
بنابر گزارش منابع خبری، نیروهای مسلح یمن با اجرای حملاتی دقیق، مواضع حساس، انبارهای مهمات و تجمعات نظامی مزدواران سعودی را درهم کوبیدند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/683978" target="_blank">📅 17:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvWYBjz39FTcxywlFkUP1yoAL4VM8GsYzD5pIWIU3eF10wQGRGKzaG3ZtrvH9E1-6baS2-gja1lTk4Y5VSpNDLYBrTMh98-GQ85TRx9ZVQYiZ6YWDo0nqSXICezRd01agoKslKxLs7GBuM05CE7nOkzTAP4TQPO9wiHOJSvGgnuTr7I5A_HIy8UxKczgUbLypH02z7FiPE-n-0ZuQDvA0zc_LC5zR1Jve0B8phYsG7TvEucnqrmx09E7VGHJLY1z58I0E-cNNN_MYABt_MpD3KiKyKHX3kUJHvrcIW8SWujapdv5aPHHPtJhZIEvistyryIeVunaKjmjWpPH4mmOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۶
🔹
کاهش۷درصدی ریسک اعتباری بانک کشاورزی در سه سال اخیر
🔻
بانک کشاورزی در ادامه روند رو به رشد شاخص‌های عملکردی خود در سه سال اخیر، موفق شده است همزمان با افزایش حجم تأمین مالی بخش کشاورزی، ریسک اعتباری را نیز به شکل محسوسی کاهش دهد؛ دستاوردی که از افزایش اثربخشی سیاست‌های اعتباری این بانک و ریل گذاری موفق در مسیر حمایت از امنیت غذایی کشور حکایت دارد.
🔻
شاخص ریسک اعتباری این بانک طی سه سال اخیر وارد مسیر کاهشی شده و از ۱۴.۹ درصد درتیرماه ۱۴۰۲ به ۸.۷ درصد در تیرماه ۱۴۰۳، ۸.۲ درصد در تیرماه ۱۴۰۴ و ۷.۹ درصد در چهار ماهه نخست سال ۱۴۰۵ کاهش یافته است؛ دستاوردی که با وجود شرایط بحرانی جنگ و چالش های پسا جنگ در سال های اخیر، بیانگر ارتقای کیفیت نظام اعتبارسنجی و بهبود مدیریت اعتبارات و مطالبات است و روزهای روشن تری برای پشتیبانی پایدار از تولید و امنیت غذایی کشور را نوید می دهد.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/683975" target="_blank">📅 17:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683971">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVeUocX9C1k1aiv_XQhMyWKH9jEarP3PWxmERpyhqrn5SHB6vbw1QA_fbR6_CR0FNxZunw1Vqtl8O3TSIrZgLAtvyXSPjpz-yVYr4kb7e3EUaa44gvO1_fq7WFek2Progz6UxuMFjjatc6qHQfT-wV0CqDGA7xUXuESErt3Hd1YDg-t7_6gctu0n5TEEZIZN_Z0rJSzzbglsYJLcR1RWoM11i-o0dHnYVUNo7rSVkz1v3MCvhvtYcLnW-fJHStyIHZ8mVCWBwZGioWMpEUm5wl0fEVPm6_7Tdi_5_S6ZmCXVJ0nTijYgYs2nPPLx8pjr3Tgs_a0COXvuXbD2YKTJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آموزش آنلاین ۸۰ برابر شد
🔹
در رویداد «تخته سیاه» درباره آینده آموزش آنلاین، یک آمار قابل‌ توجه مطرح شد: استفاده مدارس از اسکای‌روم در بهار ۱۴۰۵ نسبت به دوره قبل ۸۰ برابر افزایش داشته است. آماری که نشان می‌دهد آموزش آنلاین دیگر صرفاً یک راه‌حل موقت برای تعطیلی مدارس نیست و به بخشی جدی از آینده آموزش تبدیل شده است.
🔹
اما بخش جنجالی ماجرا جایی بود که کارشناسان درباره کیفیت این آموزش هشدار دادند. فاطمه مقدس، مشاور وزیر رفاه، اعلام کرد باید درباره تکمیل آموزش آنلاین و حضوری هم حساسیت به خرج داد.
🔹
از سوی دیگر، کمبود ۱۲۰ هزار معلم، ۳۰ هزار مشاور و بیش از ۱۰۲ هزار کلاس درس نشان می‌دهد آموزش آنلاین می‌تواند در کنار مدرسه، بخشی از پاسخ به بحران‌های ساختاری آموزش کشور باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/683971" target="_blank">📅 16:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683970">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp0jzG7hugztrBPv4fWI2IBtteEgNXbMK8m37XW9Z3CMfv2nf9_yXt_PYulwMcm-FvR_-I3uDM7MdnIeD617aH6J0G0FAYGY55gAIc10isGoKAk2f5W5VwmnltWsq68G0_APlJfKxgSsZq1FkarDRI1KQ0gEVJ6Jvh0ry9xDIlvJvqOD6Nkal9eKjNFdTXtMrH1YaC_wYNZwzJHi0L9MO1Bb_6ql-qoriSGzx9XWpO_meMkpiTSGl6ljr-AC3GEI_coDWeTIbzJVCW3w7rxEJ-4cwvIB5fiqBrtyfjxoBLyl6WveU9eHfIa8BwiQ9lM4294tnXrRr-ZZqMwuWTR6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لفاظی‌های جدید رئیس‌جمهور مستاصل آمریکا علیه ایران
🔹
دونالد ترامپی که با وجود روزها درگیری و عملیات نظامی علیه ایران، حتی نتوانست آبراه حیاتی تنگهٔ هرمز را باز کند و همچنان هیچ دستاوردی از جنگ ایران به دست نیاورده است، بار دیگر در یاوه‌گویی تازه‌اش مدعی شده که «ایران به‌طور کامل در حال فروپاشی است.»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683970" target="_blank">📅 16:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683969">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7VxZhQN9Ej9qLZ0plf0FlXiM6YZ3qnJHnPfpl-621RlTSc8aLWEok0-GWwJc2DFCM6cQ32Qe5ebu3eVdTrnTwJEiUYo9NrhSKt9w1AsqMaIlpF0nlio9O0KpOkWf7tFobtjGBL1KYpV__HmfZfeqjY3GuR6Ib9VcbSuTLka4Kdcr2BXMBdFLrpsn7GrOUXWG6hRiuCDakSuQZg945TsgKjXy74d85nm2xTh1QKoo7n9dIW_ifuo3ioGlKjO6sE2tS-XHPHajQameeaRzpwq5J28wNNy2Cp08HGB7bnszUL50C27pl2bzAIs0mauWcE7T948ZryguFh25MTXU7WxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاجیکستان تصویر ابن‌سینا را روی اسکناس۲۰ سامانی چاپ می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/683969" target="_blank">📅 16:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683968">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8vny2C4aUXYx45Bk9uMsX1UKQPcVLaE1tsD2kY-2PYYeZRpbfqOiZw8o39JsY79dOM0mEG-nLBwGx8Vbtpjn4MuGadejvp8U2ND6B0d7bch-PzK_DffhIpDBHVEz03eJQWKlKcZc75yAhz2G_Oayi8xMNkNjGxV9Qa-kEig66eCoocCIUUX4A6tjcKHr88aoq6cEAePH4EwuQAz1RdugrwCVLhDFcXDzdFD5T8otreDcmyvLFzFfrbCSQB5v1dSQsb2cfbLzE3y31PUYptPQkiiag-_3y_jMVxRz-5xGjhc9DnaRhVuxx8xuPA_ApJbn6MCe3Xiry6ZLsRiIz86IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایش توان فناورانه کردستان در حضور معاون رئیس‌جمهور
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در جریان سفر به کردستان و همزمان با هفته دولت، از دستاوردها و توانمندی‌های شرکت‌های دانش‌بنیان، فناور و خلاق استان بازدید کرد.
🔸
در این نمایشگاه، محصولات و دستاوردهایی در حوزه‌های
کشاورزی، تجهیزات آزمایشگاهی، سلامت، خودرو و ماشین‌سازی، فناوری اطلاعات، نفت، نیرو، صنعت و معدن
عرضه شد.
🔹
از جمله محصولات ارائه‌شده می‌توان به
پودر ثعلب، فیکسچر دندانی، دستگاه کشت خون اتوماتیک، سامانه هوشمندسازی گلخانه، کربن فعال، بذر هیبرید توت‌فرنگی، تجهیزات هیدرولیک و آفت‌کش زیستی
اشاره کرد.
🔸
همچنین چند شرکت فناور استان، نیازهای فناورانه خود را در این نمایشگاه مطرح کردند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/683968" target="_blank">📅 16:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683966">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtgkhvvvIGKd7i5xvMOwKdrvt6bFl7MV1Cm8o9gcWEpYnBFNg30VYfm_EnTFprS4jLs0nHvjk2aEOm113pzIna_Hbxk_8wdrGsydCEpXLvWK3PKbKQZXlpwxyhaNO6COplLWhvdn4fERXcYZwp7NG5EKPu1m8b1PxR44159dgmtooRyswU8WM5taCWMnAM42CY3keaZqQNfwnAPiK23Z_anRAcfFktO8wUdg84UKdIw8jbax4IWKoP2D5r9MzGPFXH3yF7Sg-4UY6MM7VeQ0Gh_Mh27mnWL-rL3Vlh31RV1S-gNFmuta7usOsHKZq34-QKiwmfLymqv-A9UWTcrOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی جدید فولاد خوزستان؛ بازگشت به تولید تنها در ۳۵ روز پس از حمله دشمن
🔹
امین ابراهیمی، مدیرعامل گروه بزرگ فولاد خوزستان، روز دوشنبه در جریان بازدید وزیر صنعت، معدن و تجارت از این شرکت با اشاره به روند بازسازی خطوط تولید پس از حمله به این مجموعه گفت: فولاد خوزستان با وجود روزهای دشوار، با تکیه بر توان و تلاش کارکنان خود توانست در مدت کوتاهی بخش قابل توجهی از ظرفیت تولید را احیا کند.
🔹
وی با اشاره به حمله فروردین‌ماه امسال به کوره‌های فولادسازی اظهار کرد: هدف این حمله ایجاد اختلال در روند تولید بود که در پی آن، ۱۱ میلیون تن از ظرفیت تولید تحت تأثیر قرار گرفت. با این حال، فولاد خوزستان تنها ۳۵ روز پس از حادثه توانست به ۶۶ درصد ظرفیت تولید خود بازگردد؛ رکوردی که حاصل تلاش شبانه‌روزی کارکنان و سرعت در عملیات بازسازی بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/683966" target="_blank">📅 16:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683965">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuWpajRnxnwaM33xZ2-uQogwnS79iubIjWmonVZBWm-cqRGfvGHoKlhPpQxYDKy_tGm7PzaDcMsQ5WDPGKxfmU5nNumpmb2_WwhdG2QO79wX5pDd1vfndDKBObQBhpoeJKVaCnBPjpX1jh2HEQA68xyLC3YVSIRhUdBDEsCYFaiEAF6l4GTRMZ5nVITHaoiIdVSrk_BuyprKMrOT4juxKdCcqwSQtzkpWhLJfKl-Jeg0rPO8oXLl3tafsI3KS1goOZqaKryUAVR7OPdLxARmhcRx8EBJcxS9kMFwR8KyAPjVtdy1AJgds_a0O2leifeL-L_XeKCiWYIIV5Wv-6YWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: ایران ۴۵ نفتکش را در تنگه هرمز در فهرست سیاه قرار داد
🔹
ایران ۴۵ نفتکش را به‌دلیل نقض مقررات عبور از تنگه هرمز در فهرست غیرمجاز قرار داده و این شناورها ممکن است با جریمه، توقیف یا ضبط محموله مواجه شوند.
🔹
کشتی‌های مرتبط با شرکت‌هایی از امارات، عربستان و کره‌جنوبی نیز در این فهرست هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/683965" target="_blank">📅 16:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEwWHauN_Bi2r9v6WMOBGCx_dNBk3FKfSfm_IUNoEs7LX5aWEJkIREpzCFfPx_KJmJr8Ji2Ls7B6JDzhS_0oSBfhJiEhZDzPCqXsm_9DewRCC2bMwUPStLh8ClQk0YhEUmHtniTxhyT6sHzzggkd5io6GTf9YMurbIv5ngIwK_JV8xPBiOGwzbCq9tjW1X1AfANG2NPkuWVuHcX1IO9m02Z7naVZtw_I7IBcw9QUwBtdHwRSs8kJQFLO9SjAWgzISat0lRqnuTaqq6nYKSpcVKG9-ID66wr0vAgs8827tuUhdIj5dNotMq6bSjK0ojZZQuZtt9n9tt99jZMIvWZoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qe2Quf2p-Xr361ENBixx-RDUixn9G1Nlb3nnmfgQBWpcihPNqo6jXiKLC2ju1T55-owIrUSJM-W4JZAjCXbwvDoPpG5BnVq-IL6xIf5rhsSTC_fOHfqo9Qy9IhGrlSAoUjPTGd6mX2ULuRL7X2Om2B9uJLCA7OPPjmh_JvZSQe__-D9kTqGhYvZ4fwLGqMRTB7ZMds957nizAQGoAk4iVYA0Sufbhzg9rt03mJt-SxZqPQBG4ooa809niqLnFAnyKekou_34LSwpumSZCToReTES9YoT329bE2PvyehUwSU-JPwRdf5T7sKMEfqWqf2I17G_B2A9EL-84AxhebLjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMkK_iROHp9_ymyHg0yrcCZfZU3XLDY4atsgmENRBD5nOI-nS4rUfg82yH1ikS238j_K6uTMhYPiK7xEie2WBv_Ffin5fx8UYsUfhMUe5o7CVGWweRzdLqndIjO7NvAAMr5DPyyS0On6ANAGSQ4Z3mwkAIjym7W2TAWnbq3_y_d2DoTG7lIYlrF12KdIvdZHEqHzz9f88lhumGc_GCtY5RmN8roACXd9_NlggdZpWPqquewWtzqE79G3wVtbGPlMdCgtt9P4SCRsmEoaifAbN2vlbXMLhxoPnOMpHCcAEZsi9ZhjMEPuo_i6E8fp_8cnBUaRh_ylrgaVTky8oxR0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3_rveQOt4ELU417tz2jPQMAB0ku4nzYx8oVJBPmNC5XxiePL91iwzDoIgzkoU39eEJrM3f5AWXQj6PtawDuxsay1UdXdyEfmWLBpw8Uns6YkB8Ljzy7F3dyxzZKX8nd62RAQMemyvHfTdEz7TiylKWJMFtpUZi6jTNFbNQe13ADMKlt7XLBfucTeDf3JpgvM-PpNv6o-ZTvJ_O2Ie_pTu6JbKcRjjGGV3LbxcVsLFLsGF0JCCXFImINNlTWAQLe210BsWwMH4xpmSXhvG07iNnl7wALiGSzvBzX2_0fG1w4yNtPRj9cOuZgOjRRHfOmco2W01jHg4eDIMkt3c3Dxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wplpz4mqarsUYFZSuYT4m9VK4Bxzmb8bWnyZr15cPH6tht4Uk14QH_yhTraIZaruBEQmWCYqtBQsAEbJeledUlQIxt3sHeIdiZLBU2Fy6gensU4vf0UcdJvN8CtEk-Nt1Y9lGRXhDmLdU4oWZvbYvvemYLlZuiFrs9cwPQOXYrD0CB5xyqEqtXYlYF_lsmw1uY-snb6x5XTpOlo5R6aLlzJdXfvpk0qUFhuXVTQwYcm00YxatV8N6WOC0RISWVxuBXy6eBhDrRxAhzd1ldjEQfQmbieU1vHyPCCnG9KMyfQ1Om6kHIh7N5V1f9AIPWu_afadK9JxcRYAkzAL3Un_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdXuLRzQ8Rrezd0liMTYnR-CvWiodxfP2CedbUshNiQMVQYKicX48o-IBtBg8L7SHzOO0jFt4Rm2O01OMpZb_Xb32lrh5hmBdq6vl4GiSNXnsfWYT8QoCg-GIzIAR6NPH7iFoQ4jiUMGdeX1kIOXHpRpjGmO2R8B7acj4TQkB7ZPaScIPsR75sXgvS2AF-hm-emfHAbZ4OPKNFv3YiRSlPKKH1cQ9M2aeOMibzy-xezpl2PkKeJvPidn5w91wllWNRvZ5LiKb4Ni9rR5bep2Ou2-OMeIVpCnDTJlfxx8mHEks_E8uGMo8TVjdu_QMDt6-hMUvL7GiNdJBkb8-hVioQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سکه که حباب داره، بخریم یا نه؟؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/683958" target="_blank">📅 16:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
چین و اردن در بیانیه‌ای مشترک: باید کشتیرانی در تنگه هرمز به‌طور عادی از سر گرفته شود.
🔹
نیویورک‌تایمز: کنترل ایران بر هرمز با عوارض کم‌هزینه‌تر است.
🔹
دادستان شهریار: یک نفر از اعضای شورای‌شهر فردوسیه به‌اتهام دریافت رشوه دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/683957" target="_blank">📅 15:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683956">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس صداوسیما: جای یک نفر مانند محسن رضایی خالی بود تا حریف ترامپ در جنگ نرم و عملیات روانی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/683956" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683953">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d432a1bcd1.mp4?token=GK_iB2A5e2DIsvhBLK84lfznPc2HWZ1cjUsBp0Ab0btscDgEorXsSk2frqE6tg1zQdyAKXXe9Cut24tEmPr6YR-UiAVzmCLJwW24JsfqwjYst_X46f2JCabFdJCRhtriOAmgau_gJPVuqB3ov3PCQWicz_6-7flVKRmydD2dnrcvHx65yzFlPdbXsrx1z0g6uFQrQllyl1PK6CzybBo2a8AMzthCHm5E-k2PLBYM2Tb_zT5GONnF8d-OxpjqEMoXsu6jqpsgnKP6RgonI_6tmqxJgs48ZN0LjJi5Qy79d7L1QNQak54Duq10SJ2qc9iI5zI32Cy32ce83YFi-Z9XrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d432a1bcd1.mp4?token=GK_iB2A5e2DIsvhBLK84lfznPc2HWZ1cjUsBp0Ab0btscDgEorXsSk2frqE6tg1zQdyAKXXe9Cut24tEmPr6YR-UiAVzmCLJwW24JsfqwjYst_X46f2JCabFdJCRhtriOAmgau_gJPVuqB3ov3PCQWicz_6-7flVKRmydD2dnrcvHx65yzFlPdbXsrx1z0g6uFQrQllyl1PK6CzybBo2a8AMzthCHm5E-k2PLBYM2Tb_zT5GONnF8d-OxpjqEMoXsu6jqpsgnKP6RgonI_6tmqxJgs48ZN0LjJi5Qy79d7L1QNQak54Duq10SJ2qc9iI5zI32Cy32ce83YFi-Z9XrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس اوقاف اهل سنت عراق در حین سخنرانی از حال رفت
🔹
عامر الجنابی، رئیس اداره اوقاف اهل سنت، در مراسم جشن میلاد پیامبر دچار افت قند خون شد و از سکو به زمین افتاد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/683953" target="_blank">📅 15:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84e839840.mp4?token=qQZhBdg2NY_DcaKnN-A50q8LnpyFQqxZYbHjdqSitNfXdLqzjxwxdU9IHZB-s9hqvYHxa-CxnV_6ae7RIlVVnerDCIuz3aEBywtXKw9vdD5U-3L1g28_qhrTtFkT60yeCKsJWds7_4Zuw18L8sIItkPD1Era6GOV6qnueQf4i4DnymyaDpiRfN_0CI4YqDaOmisGCKx4Js00JHsUViyr9zlQ9BZnsQeyhwtRIEzEeFzfluei4htsiVE36tLtbaaei67-myJE30rdksVW9VswuSnyfASBNg11nBl0yhHbGC914o6adEVkZ2_TVk1p7Ru12PYgbD8QMPL-gI2LILMZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84e839840.mp4?token=qQZhBdg2NY_DcaKnN-A50q8LnpyFQqxZYbHjdqSitNfXdLqzjxwxdU9IHZB-s9hqvYHxa-CxnV_6ae7RIlVVnerDCIuz3aEBywtXKw9vdD5U-3L1g28_qhrTtFkT60yeCKsJWds7_4Zuw18L8sIItkPD1Era6GOV6qnueQf4i4DnymyaDpiRfN_0CI4YqDaOmisGCKx4Js00JHsUViyr9zlQ9BZnsQeyhwtRIEzEeFzfluei4htsiVE36tLtbaaei67-myJE30rdksVW9VswuSnyfASBNg11nBl0yhHbGC914o6adEVkZ2_TVk1p7Ru12PYgbD8QMPL-gI2LILMZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس بانک مرکزی: کشور در شرایط سختی است اما تلاش‌ها برای ثبات اقتصادی ادامه دارد
🔹
مردم باید بدانند که مسئولان سختی‌های آن‌ها را درک می‌کنند. معتقدم با مردم باید صادقانه صحبت کنیم.
🔹
فشار آمریکایی‌ها نمی‌تواند ادامه پیدا کند و با اطلاع می‌گویم آن‌ها بیشتر از ما نیاز دارند که این شرایط تمام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/683949" target="_blank">📅 15:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683947">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b4be905f.mp4?token=Wh9DSKzdqKAByYOeuTXzhFhJ3z__inQL0-Ozahl-8f-h0fzVgKr2r4jmt6rhfqgW76K8H8TogvsKXvuBoFHPLqDIvuOgDQty9TZPZPetEbZ7F2eFslihz6LwtCbs7JT1aywA_IFdeD0bY-kcDsDV09iHs4lyquhIH0E744DEETRQl2LmezXAaX-OGmLFh90DnU7JK4H_WTr5NGyk9_xRnjxY8ObS5M_bImwAJMQ5-7tgpaoqPV7oLNpwweoPvqS3PQw_PQFNqGoZuJT0o_4EpKEO0kAG_Edn8Z7uyY9TLbmBmlon0xIe6LoRo9qoVH_gtAxXRzgDjrrRX5tcqGEjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b4be905f.mp4?token=Wh9DSKzdqKAByYOeuTXzhFhJ3z__inQL0-Ozahl-8f-h0fzVgKr2r4jmt6rhfqgW76K8H8TogvsKXvuBoFHPLqDIvuOgDQty9TZPZPetEbZ7F2eFslihz6LwtCbs7JT1aywA_IFdeD0bY-kcDsDV09iHs4lyquhIH0E744DEETRQl2LmezXAaX-OGmLFh90DnU7JK4H_WTr5NGyk9_xRnjxY8ObS5M_bImwAJMQ5-7tgpaoqPV7oLNpwweoPvqS3PQw_PQFNqGoZuJT0o_4EpKEO0kAG_Edn8Z7uyY9TLbmBmlon0xIe6LoRo9qoVH_gtAxXRzgDjrrRX5tcqGEjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
روایتی از همت و نوآوری در محیط خانه؛ انگیزه‌هایی ماندگار که ایده‌های ساده را به درآمدی پایدار تبدیل کردند.
🔸
اگر با تلاش و سرمایه کم کسب‌وکاری راه انداخته‌اید، داستان کوتاه خود را در یک صوت ۳۰ ثانیه‌ای بگویید و عکس کسب‌وکارتان را ارسال کنید. بهترین روایت‌ها در خبرفوری معرفی خواهند شد
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/683947" target="_blank">📅 15:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683946">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeXkiLaWEHdNMYsl3VN074zM3NXGn91o3Jm2XxybNhprI81DBLaugmfEAG7cX7jIW0q6djVenD6DghUR3UAZr4C0gNoWivIAUiuwq3wxxfKwQ4s0n2c8tTkvzmA9DU77BEezjtObrrEsF8r-b9XUyjqBP6RGHvS1kSx5lYQOz9v4KWL4FstdGiHY7vxdn8oZgCGwcAamlOI6ayZZi-fAjtNINRMRkJRs7PeZT5j258iRscxrDzdahyxk5vegkHHXPEiMcALtZhpwVXvbsyLPlfZlgReDMNNFFqZuD5aoI3973Cn7TquWVYLxFSMifjBlsDFsm9SNuwsszAWsCZPtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشروعیت‌بخشی به تروریسم در پارلمان استرالیا!
🔹
مریم رجوی، سرکرده گروهک تروریستی منافقین، اخیراً به‌صورت ویدئو کنفرانسی در پارلمان استرالیا علیه ایران به اتهام‌پراکنی و سیاه‌نمایی پرداخته است؛ حال آنکه این گروهک در کارنامه سیاه خود، سوابقی چون ترور و کشتار مردم بی‌گناه ایران، همکاری نظامی و اطلاعاتی با صدام در جنگ تحمیلی و اقدامات تروریستی و خشونت‌بار علیه کشورمان را دارد.
🔹
با چنین کارنامه‌ای، سؤال روشن این است که پارلمان استرالیا چرا تریبون خود را در اختیار سرکرده یک گروهک تروریستی قرار داده و برای ادعاهای کذب او اعتبار سیاسی می‌خرد؟ چگونه گروهکی با این سابقه که همچنان در رسانه‌های خود بر فعالیت‌های مسلحانه تأکید می‌کند، در محافل غربی «دموکراسی‌خواه» معرفی می‌شود؟
🔹
این اقدام استرالیا عملاً به تطهیر و مشروعیت‌بخشی سیاسی به منافقین کمک می‌کند. انتظار می‌رود وزارت امور خارجه ضمن محکومیت این اقدام، دولت استرالیا را پاسخگو کند؛ چراکه سکوت در برابر چنین رفتارهایی، راه را برای تحریف تاریخ و تطهیر تروریسم هموار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/683946" target="_blank">📅 15:23 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
