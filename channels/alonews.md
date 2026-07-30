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
<img src="https://cdn4.telesco.pe/file/UfOLw8wz2SSj1zYvy0gstIFzHjBkCcvlDGj3L1masitDbd7J3ajmiFJ9hKQVKpy1XMA44f5zTcPf_9aCNIoAo7b-l2ueCFqDGs9ssh3Dn6DZJYO2p9ckuhHbZNwSs94PxgvA71v9oz7rI0ntw653Jr7eI0yw95oD4ikMBTnu1zt_YIIViPixudNxbaE3OB8kx2BwVGR3wNtWH-gHVKwYsHFX9JcnS_8Cpkpb0JVmQxBxL4TO-pLtWVqu1Xw42aIBR7ISmY01vvffA5JW_5AgB9X6OofU7B-YrRAB_1L85mlWAX6ZmKb3H8feLxm5OO3DEVMQ3EiU-9udfEqbqcru3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 16:59:30</div>
<hr>

<div class="tg-post" id="msg-138695">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/140b26266f.mp4?token=jkhKW94Y9RWlgWuwRk0yWDnrfg7xQloCBU8LnlVgl7Xf3oYqva8s6B-fvbZMKfxpADzcjlGPqKEgbhudBb3CI-K239RsUsZzWqwqL0W1fjbDz_iopo-WM3g6eoNKbhjvs5NJHJIoCHHOFFxSxXPSYLRJFEc19MacDLLokQYZteiyFGnvczwKXAY-KBb2gCDHxwP3sGJyvzkSh36CJ125XPfQRfVRl5wlv9bR2tgrHliRJbrP5ihjvpSpQubBFfC56lgx1z3-R3FVgZEURc0qIPK6nCHcQZH7N8YvnDtQRJcW5lmnRQnuzf-b9QcK87wJ6WjBf2b0odFBCJO9XYoLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/140b26266f.mp4?token=jkhKW94Y9RWlgWuwRk0yWDnrfg7xQloCBU8LnlVgl7Xf3oYqva8s6B-fvbZMKfxpADzcjlGPqKEgbhudBb3CI-K239RsUsZzWqwqL0W1fjbDz_iopo-WM3g6eoNKbhjvs5NJHJIoCHHOFFxSxXPSYLRJFEc19MacDLLokQYZteiyFGnvczwKXAY-KBb2gCDHxwP3sGJyvzkSh36CJ125XPfQRfVRl5wlv9bR2tgrHliRJbrP5ihjvpSpQubBFfC56lgx1z3-R3FVgZEURc0qIPK6nCHcQZH7N8YvnDtQRJcW5lmnRQnuzf-b9QcK87wJ6WjBf2b0odFBCJO9XYoLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تهدید ایران توسط نیروهای اوکراینی!
ما با شیاطینِ شیعه صحبت میکنیم، انگاری یه کشتی که زدیم براتون کافی نبود، پس دوباره نابودتون میکنیم.
شما برا دنیا، مثل کونِ خوک هستین، ما و برادران آمریکایی‌مون قبلا حسابی کتک‌تون زدیم و بازم ادامه میدیم.
پس بهتر از اون رهبرتون که کشته شد، قایم بشین.
مرگ بر ایران
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/138695" target="_blank">📅 16:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138693">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkgqBuuI1PBiakxixbN_pRZ8x6a5zWutZI-egSX6CVhpdYtdogdeEOnvtt6xXqrfUuEpB1kLV2xd9YdFT6fTQfSN7HjC2AeIXZ5L2S48hBXMP7YaCaXQpJ-R0XDZ7EV7TQjm-d78U3aMsOk4znZrZW6ogZLYZRAey1qHq2E3NixK0LhjuFDMhOndSWqx2GK4tFFfXmq8Ln70He_v8lS33gHLpX5F4t8SOcCPQiDYJPGE2uPVAk3XNOUl-q5N8tZsTZhNEni28NoEua1LsaUvczH3ocQp_S3od0R8YjpVRzubCp55jKQgctHG96qin4fZIUa3skHU0ysOIgCNXgn0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3KgiN_gDbau01n_S4QZhwMJGLJcVFheHifdRIybq3zi0RHjR6FPyNbs1UQ5ZtzYH7iTMUbygSOSP3Zmq7V7bPmBTzvIB7PqZ_nW_hXBAJOk4wCPJvy487U2kukxkkIc_Sr6ejMbS3R2BKg0WlALhGP1hSTAnRfUcnPYdji52W5vF-CoMesK08qf_e7c8b4S8ZfBPMcTcn3nIodNyb_INnZFrVna2Jp9CyUwtf8nztE3RAkbRWAM7tldm35zg1WIR4AoZfydPxrVm_AvPY3VeCPQq7wfXxFu0DwjsDaJEiN2hMt2BGuvP00ZBZPmEMmfZKzqj1CGOI3SgVJ9zjOrtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پیج اینستاگرام "افشین فدا" بلاگر مازندرانی بعد اینکه یه استوری با کپشن "هم‌وطن
❤️‍🩹
" بخاطر جریان اعدام‌های اخیر گذاشت، امروز توسط مراجع قضایی بسته شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/138693" target="_blank">📅 16:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138692">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بهرام یوسفی، فعال اقتصادی نزدیک به دولت:
ایران و عمان در آستانه توافق بر سر بازگشایی تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/138692" target="_blank">📅 16:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138691">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
اکسیوس:
چین با ۴۰ درصد کاهش خرید نفت موجب جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138691" target="_blank">📅 16:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138688">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q3rVK-NG_gN9yrdu7VyL1rhosteE5H1UG64GkCyhTvKLkLME9HJvs2uUxgtW8V5rZy_oVmjHCL9nQRTfQFA_XZ_A5vfyJhi3a3CzWNXiJhoi2pzzbU1xLO58GqxUhjKlDxQ6pyMTr_d-rjZfeMP9tfHSv7Wl-LbBLVjsfXrR6tzpUsWGg-sPpqiKZYTkkqQAjrvHNGIMenf94cbz2UQmiO5_IP9j18sC9nu7uuwPEGHTmxDtb_gPtW1flfYGNI7_JH2l3wBSI7JxDU3LxTopNXNgPWLHjqy3dLW0CpUCg_XaqMJfTQaipjRcwGGiGa4RzdTO1aQ9qEvMQ10YdNY95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jjU0Iotv54KisJBNsUuw8X6REe6WRtVVNYCJe2e8Mz8xgltZkWn3nhdSJx9wb2X4efDAt-QTEEv3IrMjBSLIGVxdGalKhnHSKQ7RctkCQmHZs3m1J1otvjY1PSRGbwKE91daNWa8KwIBBQDAxu-1sJG5vy1RWGFSbsjGOPK-X6UbBNwWY9DorLQimKjXj5D0FCfBomZIoDWRYlEax9Ak8zeO6_YNHdzZzAaXmBXH-ubDfLpKROnTZdHOi3O3hq46FfT1WmWjyX8WLPs1HG5EL49inVexT1tpQvrqa0dEAo55eqbmX-Qy7fTFDdX-Wsq_2KkVAALTdr9_GmLtnBuNtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9118459d29.mp4?token=gwFcqZZ7pvcTkK6HAqrFF3xfil3wFOYcz3dbuLmEyJnuPZ6ufH9aQV0ajt9O3Li9KDa_yUMOnElO8PgEj8SCu9zacwm7rP5J1R9XkmYfWo51rUHV_sDGtp-smr_LdV-G1xwcrfnmfQ2BuBu1SQcEIZjxdcQ3uUaO3AjGFXsJvZUnc8rYBot9Uq86fADwnT9nYdwhfo1JPj1UX0Q4amDoWiWrolmfSoW54zwWRDMM7J_d4shsYN8O2Ae1-pPOCfdM1rU5Emt1MhXImr8QuGXfB1XihqGuhFCSWfC8BYBF3E3IbLVhMLjguWu6kZewjIx1HNrWr4ajDQ-_o5QPXog2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9118459d29.mp4?token=gwFcqZZ7pvcTkK6HAqrFF3xfil3wFOYcz3dbuLmEyJnuPZ6ufH9aQV0ajt9O3Li9KDa_yUMOnElO8PgEj8SCu9zacwm7rP5J1R9XkmYfWo51rUHV_sDGtp-smr_LdV-G1xwcrfnmfQ2BuBu1SQcEIZjxdcQ3uUaO3AjGFXsJvZUnc8rYBot9Uq86fADwnT9nYdwhfo1JPj1UX0Q4amDoWiWrolmfSoW54zwWRDMM7J_d4shsYN8O2Ae1-pPOCfdM1rU5Emt1MhXImr8QuGXfB1XihqGuhFCSWfC8BYBF3E3IbLVhMLjguWu6kZewjIx1HNrWr4ajDQ-_o5QPXog2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حکم اعدام بنیامین نقدی در دیوان عالی تایید شد
بنیامین از قهرمانان کیک بوکس بود و کلی مدال کشوری و جهانی داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138688" target="_blank">📅 16:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138687">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت کنید.
۱. برای دریافت جایزه پول واریز نکنید
اگر به شما پیام دادند که در قرعه‌کشی، مسابقه یا جشنواره‌ای برنده شده‌اید، اما برای دریافت جایزه از شما خواستند مبلغی با عنوان مالیات، هزینه ارسال، کارمزد، فعال‌سازی حساب یا آزادسازی جایزه واریز کنید، به احتمال بسیار زیاد با کلاهبرداری روبه‌رو هستید.
برای دریافت یک جایزه واقعی نباید ابتدا به حساب یا کارت شخصی کسی پول واریز کنید. قبل از هر اقدامی، موضوع را فقط از طریق شماره تلفن، وب‌سایت یا صفحه رسمی برگزارکننده بررسی کنید.
عبارت‌هایی مانند «فقط چند دقیقه فرصت دارید» یا «اگر الان واریز نکنید جایزه شما لغو می‌شود» معمولاً برای عجله‌دادن و جلوگیری از فکرکردن شما استفاده می‌شوند.
🔴
۲. مراقب تبلیغات وام فوری باشید
بسیاری از آگهی‌هایی که وعده وام فوری، بدون ضامن، بدون چک، با سود بسیار کم و پرداخت در چند ساعت می‌دهند، ممکن است کلاهبرداری باشند؛ به‌خصوص وقتی قبل از پرداخت وام از شما درخواست پول می‌کنند.
کلاهبردار معمولاً از شما می‌خواهد مبلغی با یکی از عنوان‌های زیر واریز کنید:
- هزینه تشکیل پرونده
- هزینه ثبت‌نام
- کارمزد آزادسازی وام
- هزینه اعتبارسنجی
- بیمه وام
- مالیات یا حق تمبر
- خرید امتیاز یا افزایش رتبه اعتباری
- سپرده اولیه یا تضمین پرداخت
پس از واریز مبلغ، ممکن است دیگر پاسخ شما را ندهند یا با بهانه‌های مختلف درخواست پول بیشتری کنند.
برای دریافت وام به حساب شخصی افراد پول واریز نکنید و تصویر کارت بانکی، رمز پویا، کد پیامکی، اطلاعات حساب یا مدارک هویتی خود را برای افراد ناشناس ارسال نکنید.
وام را فقط از بانک‌ها و مؤسسات مالی معتبر و دارای مجوز و از طریق شعبه، وب‌سایت یا اپلیکیشن رسمی آن‌ها پیگیری کنید.
🔴
۳. برنامه‌های ناشناس را روی گوشی نصب نکنید
اگر فردی از طریق تلگرام، واتساپ، پیامک یا یک سایت ناشناس از شما خواست برنامه‌ای را خارج از فروشگاه‌های رسمی نصب کنید، بسیار مراقب باشید؛ مخصوصاً اگر فایل ارسالی دارای پسوند APK باشد.
این برنامه‌ها ممکن است به پیامک‌ها، تصاویر، مخاطبان، اطلاعات بانکی، رمزها و حساب‌های شبکه‌های اجتماعی شما دسترسی پیدا کنند. بعضی از آن‌ها حتی می‌توانند صفحه گوشی شما را مشاهده کنند یا کنترل دستگاه را در اختیار کلاهبردار قرار دهند.
برنامه‌ها را فقط از منابع معتبر مانند Google Play و App Store دریافت کنید. حتی در فروشگاه‌های رسمی نیز نام سازنده، تعداد دانلودها، نظرات کاربران و مجوزهای درخواستی برنامه را بررسی کنید.
هیچ بانک، اداره دولتی، پلیس، شرکت پستی یا مؤسسه مالی معتبری برای انجام کارهای بانکی از شما نمی‌خواهد یک فایل APK را از تلگرام یا واتساپ نصب کنید.
🔴
۴. فایل ارسالی از طرف آشنایان را بدون بررسی باز نکنید
ممکن است حساب تلگرام، واتساپ یا شبکه اجتماعی یکی از دوستان و بستگان شما هک شده باشد و کلاهبردار از طرف او برایتان پیام یا فایل ارسال کند.
اگر یکی از آشنایان برایتان فایلی فرستاد و نوشت:
- این عکس‌ها را ببین
- این آلبوم شخصی ماست
- عکس‌های عروسی یا مهمانی داخل این فایل است
- این فاکتور را بررسی کن
- این برنامه را نصب کن
قبل از بازکردن فایل، حتماً با آن شخص تماس بگیرید و مطمئن شوید خودش فایل را ارسال کرده است. فقط از طریق پیام سؤال نکنید، زیرا ممکن است حساب او در اختیار کلاهبردار باشد.
به نام کامل و پسوند نهایی فایل دقت کنید. کلاهبرداران ممکن است فایل‌هایی با نام‌های زیر ارسال کنند:
album.pdf.apk
photo.jpg.apk
invoice.pdf.exe
ظاهر نام فایل ممکن است شبیه عکس یا PDF باشد، اما پسوند واقعی آن APK یا EXE است. این فایل‌ها اجرایی هستند و ممکن است برنامه مخرب روی گوشی یا کامپیوتر شما نصب کنند.
🔴
۵. در سایت‌هایی مانند دیوار پیش‌پرداخت نکنید
برای کالایی که هنوز از نزدیک ندیده‌اید و فروشنده آن را نمی‌شناسید، بیعانه یا پیش‌پرداخت واریز نکنید؛ حتی اگر فروشنده بگوید مشتری دیگری دارد و باید سریعاً پول پرداخت کنید.
در یکی از روش‌های کلاهبرداری، کلاهبردار هم‌زمان با شما و یک فروشنده واقعی ارتباط برقرار می‌کند. سپس شماره کارت فروشنده واقعی را در اختیار شما قرار می‌دهد تا پول را به آن حساب واریز کنید.
شما تصور می‌کنید پول کالای موردنظر خود را پرداخت کرده‌اید، اما فروشنده واقعی تصور می‌کند این مبلغ بابت خرید کلاهبردار واریز شده است. در نهایت کلاهبردار کالا را تحویل می‌گیرد و هم شما و هم فروشنده واقعی متضرر می‌شوید.
برای جلوگیری از این مشکل:
- تا قبل از مشاهده و بررسی کالا پول واریز نکنید.
- معامله را در محل امن و به‌صورت حضوری انجام دهید.
- مطمئن شوید نام صاحب حساب بانکی با نام فروشنده مطابقت دارد.
- دلیل پرداخت را در توضیحات انتقال وجه بنویسید.
- از روش‌های پرداخت امن و مورد تأیید همان پلتفرم استفاده کنید.
- به رسیدهای بانکی ارسالی اعتماد نکنید و حتماً موجودی حساب خود را بررسی کنید.
🔴
۶. کد پیامکی و اطلاعات بانکی خود را در اختیار کسی قرار ندهید
هیچ‌گاه اطلاعات زیر را برای دیگران ارسال نکنید:
- رمز کارت بانکی
- رمز پویا
- کد پیامکی ورود یا تأیید
- رمز اینترنت‌بانک
- اطلاعات ورود به شبکه‌های اجتماعی
- تصویر کامل کارت بانکی
- کد بازیابی حساب
- کد فعال‌سازی واتساپ یا تلگرام
بانک، پلیس، پشتیبانی سایت‌ها و شرکت‌های معتبر هیچ‌وقت رمز، کد پیامکی یا اطلاعات محرمانه شما را درخواست نمی‌کنند.
اگر فردی گفت برای واریز پول به حساب شما باید کدی را که پیامک شده برای او بفرستید، به هیچ عنوان این کار را انجام ندهید.
🔴
۷. به لینک‌های ناشناس اعتماد نکنید
کلاهبرداران ممکن است لینک‌هایی شبیه سایت بانک، سامانه دولتی، شرکت پستی، سایت پرداخت جریمه، ثبت‌نام یارانه یا دریافت بسته برایتان ارسال کنند.
قبل از واردکردن اطلاعات بانکی، آدرس سایت را دقیق بررسی کنید. تغییر یک حرف، عدد یا علامت در آدرس می‌تواند نشان‌دهنده یک سایت جعلی باشد.
برای ورود به سایت بانک یا سامانه‌های مهم، خودتان آدرس رسمی را در مرورگر وارد کنید و از لینک‌های ارسال‌شده در پیامک یا شبکه‌های اجتماعی استفاده نکنید.
🔴
۸. اجازه دسترسی به گوشی یا کامپیوتر خود را ندهید
بعضی از کلاهبرداران به بهانه پشتیبانی، آموزش دریافت وام، رفع مشکل بانکی، سرمایه‌گذاری یا دریافت جایزه از شما می‌خواهند برنامه‌های کنترل از راه دور نصب کنید.
پس از نصب این برنامه‌ها ممکن است بتوانند صفحه گوشی شما را ببینند، پیامک‌های بانکی را بخوانند، وارد حساب شما شوند یا انتقال وجه انجام دهند.
به افراد ناشناس اجازه مشاهده صفحه، کنترل گوشی یا اتصال از راه دور ندهید.
🔴
۹. مراقب پیام‌های فوری، تهدیدآمیز یا وسوسه‌کننده باشید
پیام‌هایی با مضمون‌های زیر معمولاً مشکوک هستند:
- فقط چند دقیقه فرصت دارید.
- حساب شما مسدود می‌شود.
- بسته پستی شما توقیف شده است.
- برنده جایزه شده‌اید.
- این موضوع را به کسی نگویید.
- برای آزادشدن پول باید کارمزد پرداخت کنید.
- سود تضمینی و چندبرابری دریافت می‌کنید.
- ظرفیت وام فقط امروز باز است.
- کد پیامکی را سریع برای من بفرستید.
کلاهبردار تلاش می‌کند فرصت فکرکردن و مشورت‌کردن را از شما بگیرد. هر زمان احساس کردید برای تصمیم‌گیری تحت فشار هستید، هیچ اقدامی نکنید.
﻿
🔴
اگر با مورد مشکوکی روبه‌رو شدید
🔴
پول واریز نکنید، روی لینک کلیک نکنید، فایل را باز نکنید، برنامه‌ای نصب نکنید و کد پیامکی خود را در اختیار دیگران قرار ندهید.
🔴
ابتدا با یک فرد مطمئن مشورت کنید و موضوع را از طریق شماره تماس، سایت یا صفحه رسمی مجموعه موردنظر بررسی کنید.
🔴
اگر برنامه مشکوکی نصب کرده‌اید یا اطلاعات بانکی خود را در اختیار فردی قرار داده‌اید، سریعاً اینترنت گوشی را قطع کنید، با بانک تماس بگیرید، کارت و دسترسی‌های بانکی را مسدود کنید و رمز حساب‌های مهم خود را از یک دستگاه امن تغییر دهید.
🤔
به یاد داشته باشید: کلاهبرداران از هیجان، ترس، طمع، اعتماد و عجله استفاده می‌کنند. چند دقیقه توقف و بررسی می‌تواند از خسارت مالی و سرقت اطلاعات شما جلوگیری کند.
#امنیت
#کلاهبرداری
#کریپتو
#وام
#دیوار
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138687" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JouFbVHB-gNLaHjwobe1CvE-V4Sf1Sy5tK_zBM3LIqzDaal8Uo8Fuagzstp1Dl160RJcuyF84nMJ5dd__1W341ClsiKzJGgll-hpiB39Wfs2HvaYbhkeFDKAS7V3NYaB261VNG3-6FWt47zX0hdwDvq4ESap5MY_2coL37uXU__V3g11AcT_iLxOK3VI74Cg2tUuRhJBX35wwEptI_LiK59HsgVjtJQWd46NpipS3LqVQB_6XEz9lKoWssMeDNt_XRnZ0lMQeNHoB7-E0Cyz1xJFjWYHabQOejdzCgK_j8fbABS6pYhhCAyIEgI193okqLeT07Cfb3B4JmO8Gq2SNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVqWXIxeUQmv42DvkBYCIcCmra-NyDLr-jsg89IQtja7RhNoTYPFukanPuP0__tJcxGHExx5Vs-fKK8fRfJmxqwnbpyZxNV9SukjC1jeBOTf9ysrzfADZnJ5vZp3qlxNqP9S5-mbjQVxK0m1yVoEYlzlsjTQW0CXTb_tdGviqmLdpVcTiwvJIQFBLZd8zb80OdVJbIMfpsVVL_UQyjamx2qS5zx972oq4TYsn0gvxfu8yQTq7RpCNdEHsOjYYIL5VaE2LkdIZy3ZykSIUXzS2nrqPiheXaIDzAPH7diTTSo4wdNkltmLZecovgX1PXyzgBCIpu61QuVCQ2JdTlzGcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjPcVqjJwMJAymLxBTDy3VXxM468Qj7EzjnQXsF8MLYvhKa8ybv8weTiNsl3BmP6pjmYwGHD3EPM2BcbsvZeh8g8beyXTrswIIqfXK-OUNFe4lrSdawnxO2IwIGOhdZoNDuW8qV-zR52_lqKZeoPsoD5I8qsXnH1ecnWh8e39cLyudkKI6Lhm2Zs-eVcqCMG1OBAQOMcFimt5Qw8we0eSrJhFeMRxj3vJKmoBgZIARmj3bojJ6mCQieJjAW2l4kyzo15hfCmXy0Z9Wa9cIUBU_4IqlFUH2cmNPBpFpo_wv4i1ZI4UVK4Rt1ptBuyoiRH0MjmDS7mbtuJ_oCTBkufmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرود چندین فروند هواپیمای آمریکایی در پایگاه هوایی عیسی در بحرین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138684" target="_blank">📅 15:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzoLF8MIbPFmJPUJ1Lyr6SzDE1dnGRyAii-7YaOhpdOrOR9w9lCT-3m3jDF0baeyzw_yKgG1g--JwGzMREQGB_wx7-i3jWQMA6rAzdT_lARuN-AQZUM3KDLdp-96XdG2H1x2Orw0evKCvg6URXO2HigXnoaDbRq2SlwHPQRcwxfZ3cmChV2rPfp4R1DKj3CwtXrAx9bF4hi0GumNjqGeTmfo7FNb02D_4Hz_huV8PouwyZkXWdu6bR_U1e-c6DyyJw2Ehak6QQya2voxqogZAk1K7r3rjB0buw755-OI_c9oBrKWkewgt1LvpVlWxYVoW50mC0-2w6nWY-Q3r-VjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چرا نمیتونم راجب این ۳ نیروی حشدالشعبی فکر مثبت کنم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138683" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت برق فرانسه (EDF) راکتور هسته‌ای «گلفش-۲» در جنوب این کشور را در پی موج شدید گرما از مدار خارج کرد.
🔴
دمای هوا در بخش‌هایی از اروپا در حال نزدیک شدن به ۴۰ درجه سانتی‌گراد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138682" target="_blank">📅 15:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138681">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نخست‌
وزیر لهستان :
دلیلی نداریم فکر کنیم لهستان هدف بوده؛
🔴
اما دو شیء وارد حریم هوایی لهستان شدند
🔴
یکی قطعاً این کار را کرده و مدرک داریم؛ دیگری هم مدت کوتاهی به مرز نزدیک شد و پیامد خاصی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138681" target="_blank">📅 15:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGnLtFkQHX-su7jLPCZFpHakA9LPa-tLKMkrAy_sSuZyXB2_HndCsEyawKjF4x_-I36qWmcAvzfYbiB3H-3FYf0WYKOexw1sB60rc1c7HI5Y3YwRZxql02_yQ0WYGb4JFFZcTNox6ThFCAwvAxXZzdNPkVqejpxWDWwwuIygb0a3SbicGcYEVsgs2rLlHS31e6p1xRT8ghyBoUm7IKshZx0iHvGv6ADOmu0sumv2UE6WHVuhAiz25wxUGJMDVNs7GpSUSfCNKUi1jrHKFtPXBNjVR3enRQ-39p1eHR3h0omNFL28CTsUkPILQSs-v9THHhuwptMJKIHL4hSY3UYuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی نماینده مجلس: استانهای دونتسک، لوهانسک، زاپوریژیا و خرسون و نیز کریمه را به عنوان خاک روسیه به رسمیت بشناسیم!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/138680" target="_blank">📅 15:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بلومبرگ، پاکستان با ایران مذاکره کرده است تا عبور امن حداقل یک محموله گاز طبیعی مایع (LNG) قطر را از طریق تنگه هرمز تضمین کند
🔴
نفتکش حامل گاز طبیعی مایع «العارش» که از اوایل ژوئیه در خلیج فارس منتظر مانده بود، تحت این توافق از تنگه هرمز عبور کرده و اکنون در مسیر پاکستان قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138679" target="_blank">📅 15:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
به گزارش اکونومیست، بخش‌های قابل توجهی از توافق آتش‌بس میان ایران و آمریکا عملاً کارایی خود را از دست داده است.
🔴
این نشریه افزود حتی اگر دیپلمات‌ها راه‌حلی پیدا کنند، احتمالاً این اقدام تنها ترمیمی موقت برای توافقی خواهد بود که از ابتدا نیز شکننده بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138678" target="_blank">📅 15:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2eXqRwd4g626KtVyv1iy4jlvOAgx9AKlbuSbE5c4cjap_C7TG8SNaaqZiuf_laqkRZkvxow9ago2h4M_kWmno6GGr9YlsOzelp0kVsxf554Rwf9biyfZS5HXmZYKKtn_xM2_HZZAlGN-6GPkPgMSc_yiYzp0P91vUV9Nh1wCXU-uTtzLE5Btuh99efTuAtvCZOPdO4JzE3jKLOuhzEvoPBUqsHVwbHoD5Wn34jo6XDvLaakwX2u_AfhFLKSsn2W1gOOLI_CbSgUwGIBaXhszRXiphdECazg4wnVmpEJtwdqIajZcJ-_DfS7sJUG6MYs-EE2VIzG5RODkOl6X68QPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: امروز صبح 6 تا جنگنده زدیم
🔴
3 تا F35 رو منهدم کردیم و به 3 تا دیگه خسارت زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/138677" target="_blank">📅 15:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd1748f78.mp4?token=vrfnFhT1M_eo1xRUzoDpYNFIefedz2ceyqu-dNlveS0iVBSYw_T2SF-eQ7yFdJIlzrQOb9Q9Bu7hlZqChSsZ8gWFPjUfCvTC9TTN2oelfqmq2bjclriymJLQeOMoSjBeZNsPgNnSxF9CSKzUZXiT8ncnhCTTQ-N-NG5HpaYCb7lFgvduUvBx1fQAhmQl4epJI2IXrjwJ-UcF0S9MUtd2gxTxI14KkbiWsl9RncKnjPhjOwrKkw8C5lrQgVKiGljp4-J7tAFkMYCf6NGww7iYkB_M-NOS0CaPHmc1XuL8mZYLKRchqmvHaFFTvgIiqb66WYJpexMA4meKXzsducDe0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd1748f78.mp4?token=vrfnFhT1M_eo1xRUzoDpYNFIefedz2ceyqu-dNlveS0iVBSYw_T2SF-eQ7yFdJIlzrQOb9Q9Bu7hlZqChSsZ8gWFPjUfCvTC9TTN2oelfqmq2bjclriymJLQeOMoSjBeZNsPgNnSxF9CSKzUZXiT8ncnhCTTQ-N-NG5HpaYCb7lFgvduUvBx1fQAhmQl4epJI2IXrjwJ-UcF0S9MUtd2gxTxI14KkbiWsl9RncKnjPhjOwrKkw8C5lrQgVKiGljp4-J7tAFkMYCf6NGww7iYkB_M-NOS0CaPHmc1XuL8mZYLKRchqmvHaFFTvgIiqb66WYJpexMA4meKXzsducDe0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین در مورد رویکرد اخیر یک شناور بدون سرنشین ساخت آمریکا به یک کشتی جنگی چینی: نیروی نظامی چین فعالیت‌های خود را مطابق با قوانین بین‌المللی و عرف بین‌المللی انجام می‌دهد.
🔴
ما توصیه می‌کنیم از نزدیک شدن خطرناک به کشتی‌های جنگی چینی خودداری شود تا از بروز حوادث ناخواسته هوایی و دریایی جلوگیری گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138676" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138675">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سپاه : تو آسمان بندر امام پهپاد زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138675" target="_blank">📅 15:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrilgjtdTnUGQbcRfIBBbmZYCCkeHCOUvCjJr1p92igy6Zl596x6zY5IMFCpe9xGnV-F806ojoyYSsV2xPlRTFOqRlZgXCrJYqyLPcbJQ43uW_Ah6Ns4rabenaDZ3UTqPsKKEVTklW5I3Kdvo2bHlAUGsynrHLYl64lDXOX7GkWZpqYFsUoczt2nxp24ptsC3GLAnrMht4JgxDvroMv7bn4Fb4sglqnI8GVS6Ll_UgT8zz1vy72MbQTDOvPd-801cgOKfuqjM0ntRoTqXRcmxcYIioSj9PLE5cEJuyyfKvhWGHelq5sk9XRuplOpDvQ0GEmsQAB1CjupxMYpmNlD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: ترامپ از عدم پیشرفت در زمینه پایان دادن به جنگ با ایران و اختلاف‌نظرهای موجود در دولتش ناراضی است
🔴
برخی از مقامات از ادامه عملیات نظامی حمایت می‌کنند، در حالی که برخی دیگر هشدار می‌دهند که حملات طولانی‌مدت می‌تواند ذخایر تسلیحاتی امریکا را کاهش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138674" target="_blank">📅 14:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ایران: مذاکرات با عمان درباره مدیریت تنگه هرمز همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138673" target="_blank">📅 14:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
صدها چهره سیاسی، حقوقی و عمومی اردنی نامه‌ای سرگشاده امضا کرده‌اند که در آن به خروج نیروهای ایالات متحده از اردن فراخوانده شده است، با این استدلال که حضور نظامی آمریکا حاکمیت کشور را تهدید می‌کند و خطر درگیری عمیق‌تر آن در درگیری منطقه‌ای را افزایش می‌دهد، به گزارش نیویورک تایمز.
🔴
نامه بیان می‌کند که حضور سربازان ایالات متحده «اردن را در معرض خطرات امنیتی، سیاسی و اقتصادی قرار می‌دهد» و احتمال کشیده شدن کشور به جنگی را که «در آن طرفی نیست» افزایش می‌دهد.
🔴
برخی از امضاکنندگان گفتند که می‌خواهند افکار عمومی را از سیاست خارجی دولت متمایز کنند که با وجود تنش‌های فزاینده منطقه‌ای، روابط نزدیکی با ایالات متحده حفظ می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138672" target="_blank">📅 14:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رویترز : دو تانکر نفتی که حامل نفت عربستان سعودی به سمت هند هستند، از دریای سرخ خارج شدند. این خروج با خاموش کردن دستگاه‌های ارسال و دریافت سیگنال انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138671" target="_blank">📅 14:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فارس : کشتی کانتینری نورا از خط محاصره آمریکا گذشت و وارد آب‌های آزاد شد؛ این کشتی پیش‌تر در نزدیکی قشم دیده شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138670" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سپاه : در پاسخ به حمله آمریکا به قشم؛
با حمله موشکی به پایگاه الازرق، ۳ جنگنده F-35 رو منهدم و به ۳ فروند دیگه خسارت سنگین وارد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138669" target="_blank">📅 14:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f178e085ff.mp4?token=Nh0EP62fPLWd-kH1-2tJ1p91Z9XLHWusPWcv4YDTLsVpHvkuQxMgUj1MZ2ArawY_gf1Iope06MLHvaytDvaK3cYYuf3r4QK7MRTjVOCtKxLLjlEwGVAom9qpSkZYysWH8zHAJKyb9HWybKPN54-_sBvgibntp3AyEb66KbEC6ZH4SR_fM4iZSL-ZhHSyify55cEbAATpMNVW8IH4roJZfHXpIircpajarubbAzMLw84hgpPJIPWcFeC0kY08ssZuEnEWYQNEmGRk-rT9hb9iwBxFh3T-jQEeO8Whx1kGzImuq7rxcppBOBCl3XrGZ_rfUUekXVptMCghxwAmQnJIJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f178e085ff.mp4?token=Nh0EP62fPLWd-kH1-2tJ1p91Z9XLHWusPWcv4YDTLsVpHvkuQxMgUj1MZ2ArawY_gf1Iope06MLHvaytDvaK3cYYuf3r4QK7MRTjVOCtKxLLjlEwGVAom9qpSkZYysWH8zHAJKyb9HWybKPN54-_sBvgibntp3AyEb66KbEC6ZH4SR_fM4iZSL-ZhHSyify55cEbAATpMNVW8IH4roJZfHXpIircpajarubbAzMLw84hgpPJIPWcFeC0kY08ssZuEnEWYQNEmGRk-rT9hb9iwBxFh3T-jQEeO8Whx1kGzImuq7rxcppBOBCl3XrGZ_rfUUekXVptMCghxwAmQnJIJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ارتش روسیه ویدیویی از هدف قرار دادند 3 کشتی تجاری اوکراینی توسط نسخه هدایت شونده گران ۲ در نزدیکی بندر اودسا منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138668" target="_blank">📅 14:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اتحادیه خط لوله دریای خزر (CPC) اعلام کرد که یک نفتکش در حال بارگیری نفت در یک ترمینال شناور متعلق به این اتحادیه هدف حمله پهپادی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138667" target="_blank">📅 14:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138666">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سپاه المهدی : تو حمله موشکی آمریکا به زنجان، ۳ نیروی سپاه کُشته شد
🔴
جمال امیری/ محمدرضا چراغی/محمود ملاجابری
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138666" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138665">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7319df0d.mp4?token=TftH9o7H5OksRB3R3M36eqkTWRIsUhISsrLywpAmfayAUJ1Rn8R6gdAZQcOlSdI6kyjQFjVhnXtmA7WgH7_-J47c0_7HkcX2idriMtJaMZ8cXTakchEBDqOPfbssQIu_y5EnVgXD4EzY9RnBkZFgORpt8kqUQxy8HqO1wneS21ycDQHbqa-i3FuhGbYlZ7axhYI-Udc4vX6hK1j9r7OCdhnxAMGXviyee9hdgt4sg9JItRVW0px5rECJT6xM7x5IuIj3-wRewUjgc2cxSfbyUTBIqSXYPRpQqsERK9nfOwOMQfLUNesU3iidZpHCEkdf329ylkRarBAbKFa1C24H4zdJXBZGvCfB8uk02IoVSM8oEeOGRm3mRxnsJV6-QE8_ZzjOavNHLYk_nHu9tfJvj-cxv628hK78MPiCkRLH1mT9ofkB4ujhW90qHY4JOTYQ2X7l4xbJqf3mfiFKgHcV8Q1Kv3XZoUHjgQ7ylhdwe7ujBsGcgyExMtlrh9jcaGP9_SQwIr_3FyWDQczF_aaY6mOYH7kLjtznBL4ysFhB1ilAG_DRstjzFL0glMoiccOF_2f7h4swNS-4Adq2EgL38JL599SVFqu82eIJmIMZytEZJ2rMMdSHtaQ5oUdYLT4xuZrjlKxHFBCAmpEeXboqk-MmxTkMmOhLHvWu_fjX1nU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7319df0d.mp4?token=TftH9o7H5OksRB3R3M36eqkTWRIsUhISsrLywpAmfayAUJ1Rn8R6gdAZQcOlSdI6kyjQFjVhnXtmA7WgH7_-J47c0_7HkcX2idriMtJaMZ8cXTakchEBDqOPfbssQIu_y5EnVgXD4EzY9RnBkZFgORpt8kqUQxy8HqO1wneS21ycDQHbqa-i3FuhGbYlZ7axhYI-Udc4vX6hK1j9r7OCdhnxAMGXviyee9hdgt4sg9JItRVW0px5rECJT6xM7x5IuIj3-wRewUjgc2cxSfbyUTBIqSXYPRpQqsERK9nfOwOMQfLUNesU3iidZpHCEkdf329ylkRarBAbKFa1C24H4zdJXBZGvCfB8uk02IoVSM8oEeOGRm3mRxnsJV6-QE8_ZzjOavNHLYk_nHu9tfJvj-cxv628hK78MPiCkRLH1mT9ofkB4ujhW90qHY4JOTYQ2X7l4xbJqf3mfiFKgHcV8Q1Kv3XZoUHjgQ7ylhdwe7ujBsGcgyExMtlrh9jcaGP9_SQwIr_3FyWDQczF_aaY6mOYH7kLjtznBL4ysFhB1ilAG_DRstjzFL0glMoiccOF_2f7h4swNS-4Adq2EgL38JL599SVFqu82eIJmIMZytEZJ2rMMdSHtaQ5oUdYLT4xuZrjlKxHFBCAmpEeXboqk-MmxTkMmOhLHvWu_fjX1nU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از رهگیری پهپاد روسی تو آسمون اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138665" target="_blank">📅 13:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138664">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8jJNyd-ALGHaRHxp7DGbxLdDQzNS8yqHsPFDtAMVW2XCDGFFQUwW0qSSDYVcrb5omUq0MzMDSMG_ggF2ZN670RFsWGBZBdn7uca01pR6cs3m3RzaOw4Loq9Q1foDriS821dU1blBrONHQr4oJXFe_XymureJ3CeSEmr_bHsdWdWUBZFxNgAuPP_SjehlnJ4yj33IJdU62fDC2WZ4xeJiMqCU-KMqYD4PvaAP445Engevw0fshvN8YoNCpOpUIndGkY4BRDL_x9RSdij63YszNpxJtGkrmM-JzdTYvNcLi8NlFCXuFzsg-U-5urqODDiEpd_DTszQ6S7n9xNm9namg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهار کشتی نفت‌کش/گاز‌کش از تنگه هرمز عبور کردند و از مسیری که ایران تعیین کرده بود، استفاده نمودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138664" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138663">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت دفاع روسیه : لجستیک دریایی اوکراین، در حال فروپاشیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138663" target="_blank">📅 13:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138662">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae07c4c25.mp4?token=DpXhKs8GS5w1-HSZotN4tWXOIU1W-sQvj0VLvhI5AVz29JWzQ_hwBrxDO-U0IaxXyQBNn3xKfibigyghXAQSd5n8S2aqpdOmHMcaXppoIK0JkIQGlfFRwra0PAbkfcqy7NZrEN02Tdd4D9sm1Vxqhtcvz0N1PvLF5sLeO6frf4NxoDuPd06AKmDpwGeykAS3FAihymPrvxOXXaKoAMJbkXf8MjLjIMNQ9Wux4S4k3rEM2_wM-GciQ_6xcq23uL27JyR1_8gXQs3iZmgMhwHuezHefXyZUQfbQ0-QvSwR_m6TVisJ8qcHZqWVyEKhCzvg3yjtuhXtF7_vu2y7wwO4SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae07c4c25.mp4?token=DpXhKs8GS5w1-HSZotN4tWXOIU1W-sQvj0VLvhI5AVz29JWzQ_hwBrxDO-U0IaxXyQBNn3xKfibigyghXAQSd5n8S2aqpdOmHMcaXppoIK0JkIQGlfFRwra0PAbkfcqy7NZrEN02Tdd4D9sm1Vxqhtcvz0N1PvLF5sLeO6frf4NxoDuPd06AKmDpwGeykAS3FAihymPrvxOXXaKoAMJbkXf8MjLjIMNQ9Wux4S4k3rEM2_wM-GciQ_6xcq23uL27JyR1_8gXQs3iZmgMhwHuezHefXyZUQfbQ0-QvSwR_m6TVisJ8qcHZqWVyEKhCzvg3yjtuhXtF7_vu2y7wwO4SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی بزرگ در یکی از انبارها در مسیر اربیل - کرکوک
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138662" target="_blank">📅 13:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138661">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzrHBy_gKGajJRRnlsPTkzJlcReza7Cxb-Y5j58SU5dfbOw6Tr3KDIq0bFQ_YHNPsOS1Tkcwl50RJEtZUNjNpkpXP1EpiCKCSnK5_rLgsWxXc_1yqWH8ZfZgyYqX5XV_rlxQiJWLu1hsXed3oe9dDwprze3xc523mZ1pv5fRKIEJa5vMZvNAmjyyWqANqwhR-As2ym8wO-RDI82saRedTGHeHX5ohNp1jJiB6YNboMthByvPlAfqF8UxpiZ8-PDYXucU-j62Qy0uEDmWMKHMJ_PpOhNz_Awc68VkMoGgiKd0MhfILEdKYJ6w2bGxnVEJE0Y22nb_ELWaLGE8ErC6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله کارشناس صداوسیما به وزیر امورخارجه به دلیل جلوگیری او از حمله به اوکراین: هر ثانیه حضور عراقچی به عنوان وزیر، خسارت محض برای منافع کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138661" target="_blank">📅 13:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138660">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a7dcb61f.mp4?token=HacV-QJSxmrEWxAm9YiK6KSc4E42soN8mRIA8uAt2dipg4MuaLFt4xskQnQauXHX1kW0k4945iITFhRp8MMlT_-oWbixSMaxdbDi50R7J8qqzrGU0i4sK7QQlorpw90cifrStXUFIjliIs52mSjHWTyMEVnnKG54_3xmIV2ZhTddpimL5Mnn0rXdxVGQr7lcSY6nMnzQKPg_PvQV3ZJcWwghDABL_y44B1gbiWONK0gUDa_JOYBlyTY-VW06ve_GZ6aABCEBwbeUI5WUGi1iyJvyMGsE9Hv_SKJSE_Seu6HT6FsCbaFDhHNPa5l3TN0Jup3pDmkY8COagUhOV-N3OnWwlB8cEH8pyiHt4g8533o2elAw57_uerb8rogqn-JFNi1ab88uRlVi3SNm9M1Aci7qVtELRa_WshLSXKodgcdUWr2KxmxehPRxIYZ6ll2AdrVhBL_ibSbjM9VaiD_yFGqCwZWAMnDxWNF_LqzWyvg5c7g1LYU9luD3NHZoG2euqV1tbW2sty3zddbOexR66tXLSjGU3uexINUxLaZPnw5BWky6DGMxAnxJZZLpS4xBUQrrwsZQBi3zaz0Eb-UeSnT3ez2xf0WdBv6emDajXhcXe6UrfiYHcXGWcQCn_BIslBFDlFZ731rSZE2DKLVLpPMUQr0Joyxf4m1nkF0OmE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a7dcb61f.mp4?token=HacV-QJSxmrEWxAm9YiK6KSc4E42soN8mRIA8uAt2dipg4MuaLFt4xskQnQauXHX1kW0k4945iITFhRp8MMlT_-oWbixSMaxdbDi50R7J8qqzrGU0i4sK7QQlorpw90cifrStXUFIjliIs52mSjHWTyMEVnnKG54_3xmIV2ZhTddpimL5Mnn0rXdxVGQr7lcSY6nMnzQKPg_PvQV3ZJcWwghDABL_y44B1gbiWONK0gUDa_JOYBlyTY-VW06ve_GZ6aABCEBwbeUI5WUGi1iyJvyMGsE9Hv_SKJSE_Seu6HT6FsCbaFDhHNPa5l3TN0Jup3pDmkY8COagUhOV-N3OnWwlB8cEH8pyiHt4g8533o2elAw57_uerb8rogqn-JFNi1ab88uRlVi3SNm9M1Aci7qVtELRa_WshLSXKodgcdUWr2KxmxehPRxIYZ6ll2AdrVhBL_ibSbjM9VaiD_yFGqCwZWAMnDxWNF_LqzWyvg5c7g1LYU9luD3NHZoG2euqV1tbW2sty3zddbOexR66tXLSjGU3uexINUxLaZPnw5BWky6DGMxAnxJZZLpS4xBUQrrwsZQBi3zaz0Eb-UeSnT3ez2xf0WdBv6emDajXhcXe6UrfiYHcXGWcQCn_BIslBFDlFZ731rSZE2DKLVLpPMUQr0Joyxf4m1nkF0OmE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جزئیات بازداشت عامل انتشار لایو ضرب‌وجرح دختر جوان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138660" target="_blank">📅 13:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138659">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPCMEKRsYvC2tIryYyrU7zWgLxYrJ0s-CqMVJduCizgSyUqrZK28DIAv7c8W_wXG6BCDR8fvMCAqV-V9DjpRftcDKeVAjH2N1KwnCvkDE28UwzOjPZP0Ojf4_z9jb2y6O6zCh1jtmdvKYMyAN1UvBir6QJ-uWnJFIEeh1PWG1nSXVLap6BzjxRZ2zGqSAQMiwCwArjtW2OJgWjaM0BEzboUI82b4iQJSOVk_8QDNFlkpDlgLH9CtxyoY_Lg0Zmgtc-HbtECNW9v6qIF-6hjnUGxs5thMC9l26-kNiOdmj1jMElu7pTaJxIFyHS0xECa8ZYM_yQoNy5qtZcMMnrVuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عطوان تحلیلگر جهان عرب: حشدالشعبی وارد جنگ شود، پایگاه‌های آمریکا در منطقه دوام نخواهند آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138659" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138658">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از فرمانده ستاد فرماندهی مرکزی ایالات متحده نوشت: "ما طرحی برای یک کمپین هوایی قدرتمند علیه ایران آماده کرده‌ایم که می‌تواند تا دو هفته ادامه داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138658" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138657">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
العربیه: تلاش‌های میانجی‌گری تاکنون به نتایج ملموسی در زمینه توقف تنش‌ها بین آمریکا و ایران منجر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138657" target="_blank">📅 12:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138656">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cfe0b1f3c.mp4?token=nnFOJweGcvo8MHk-4p12bYjwOXYYgJtekwjn7b8CJWXGfcvNWnoROnV2UxpNu1nsK8r5NN_9zwbNZZGPoK5kBbBvdGy4isQsg4Y3T6jhg4qD1fRNdZntCq2Rd-jOC50vQRNJsCfsYG-UFHeE-ovU792fr4mwwhRS_dSfa-02PGcyV0a4zWufZOC-11UnVRqhtsnWsy0NprB9YkPxfE6slWFwAbZRbuEvRDaZQqodxbUz0cRaAX5k1Km2ntAxFSkt4Z3IDl92eq5GoAOO38zIRd__ur7wvqcib4QTi3vW4gxWOJUStu0IvIaZtctaela3jDzWWhAOivrH-KrLmwJDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cfe0b1f3c.mp4?token=nnFOJweGcvo8MHk-4p12bYjwOXYYgJtekwjn7b8CJWXGfcvNWnoROnV2UxpNu1nsK8r5NN_9zwbNZZGPoK5kBbBvdGy4isQsg4Y3T6jhg4qD1fRNdZntCq2Rd-jOC50vQRNJsCfsYG-UFHeE-ovU792fr4mwwhRS_dSfa-02PGcyV0a4zWufZOC-11UnVRqhtsnWsy0NprB9YkPxfE6slWFwAbZRbuEvRDaZQqodxbUz0cRaAX5k1Km2ntAxFSkt4Z3IDl92eq5GoAOO38zIRd__ur7wvqcib4QTi3vW4gxWOJUStu0IvIaZtctaela3jDzWWhAOivrH-KrLmwJDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه دستگیری فردی که برای جاسوسی به
ایران
متهم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138656" target="_blank">📅 12:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138655">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نتانیاهو: ترامپ درباره ایران سه گزینه پیش‌رو دارد؛ توافق، ادامه محاصره دریایی یا تشدید جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138655" target="_blank">📅 12:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138654">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbc8eae3d.mp4?token=qAI0LitIdHAcOfX-gzAAzXLLmt1d1YbaMkCpwY9ZG9ezdhIhin9gTujR18kRjKfbLeChWrTG4u-_Q_h2A0Rmp7KI0FEhl301JGRS7HyCccRVQ5W99XZMtfYVbGVTALxcclyN0z2IOOyN1D8yjb1vLuVjelbWtu4n0L55lKBZAZXnT4uvIoOE7AwJ1YO5Q20aAAdYDVljMsbp-w6NWBjgZkq2ifX-wOM_a3poo0Ts8JXnc8C4kptcrm3WcPPbl3J6_yxqIivhjYt76T2zuAD0DaEQSn4sLdXC118gJA70fWaKu7LYoifKhBjNwr51EVeJ7Frea8HlWWZNbAPyqbozUHTIyxnrfkFAsH0srQAc9DZSKzCArBPm5TgGCG_sy6uiE6iKZuUp_bUG2kVAAi9VCj6WjzUWeronAQjJUNtIApg_dPcSaR92h1rckxEqT-Gz5ZnsRyYgnghrwnq4cEbeTwdEmzzLINzH7VdLbk8sBdJA7zMUuQ6mTYnjWbSJ_ivgGM0NcT0lw8a5KHVDBImayLvpHDJQnOaXFrMD_RhTG4WvYRlmTSYWK8QPblBSSWw5nZ_14yivKlqLMvP0bgCHd0tld5uHv2VwI4B_ebCPVUmr5q4nY4ROXWy59Q9aa2rMSuOIAFJrBUIfrVvzP6ZeHv4pnUyupOKaVptohPyjdSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbc8eae3d.mp4?token=qAI0LitIdHAcOfX-gzAAzXLLmt1d1YbaMkCpwY9ZG9ezdhIhin9gTujR18kRjKfbLeChWrTG4u-_Q_h2A0Rmp7KI0FEhl301JGRS7HyCccRVQ5W99XZMtfYVbGVTALxcclyN0z2IOOyN1D8yjb1vLuVjelbWtu4n0L55lKBZAZXnT4uvIoOE7AwJ1YO5Q20aAAdYDVljMsbp-w6NWBjgZkq2ifX-wOM_a3poo0Ts8JXnc8C4kptcrm3WcPPbl3J6_yxqIivhjYt76T2zuAD0DaEQSn4sLdXC118gJA70fWaKu7LYoifKhBjNwr51EVeJ7Frea8HlWWZNbAPyqbozUHTIyxnrfkFAsH0srQAc9DZSKzCArBPm5TgGCG_sy6uiE6iKZuUp_bUG2kVAAi9VCj6WjzUWeronAQjJUNtIApg_dPcSaR92h1rckxEqT-Gz5ZnsRyYgnghrwnq4cEbeTwdEmzzLINzH7VdLbk8sBdJA7zMUuQ6mTYnjWbSJ_ivgGM0NcT0lw8a5KHVDBImayLvpHDJQnOaXFrMD_RhTG4WvYRlmTSYWK8QPblBSSWw5nZ_14yivKlqLMvP0bgCHd0tld5uHv2VwI4B_ebCPVUmr5q4nY4ROXWy59Q9aa2rMSuOIAFJrBUIfrVvzP6ZeHv4pnUyupOKaVptohPyjdSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اضهارات نویدِ زیادخان:
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138654" target="_blank">📅 12:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138653">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
دولت عراق در بیانیه‌ای اعلام کرد که هیچ مدرکی مبنی بر آغاز حملات به عربستان سعودی از خاک عراق پیدا نکرده است و از عربستان سعودی خواست تا مدارک خود را ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138653" target="_blank">📅 12:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138648">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/452945470e.mp4?token=vPxGf2jSJjlEWml75elYkr0DeONudef4LQuKycTNLej0GUnwbMs_2g58oCJMDkuLN58n_3UfIkp-2Vs_R-P3ViNsjAVabO1Ozpl9vMra7oJ7qm9YGV3G8ZI7IWXOr5fQlM7MEMr6tEXznTowNQMiODXqNErFQQNZ8C4x_LMXgCM_c7NGQ7nnunlTrq07bjyX1B5iK2G96tOwdfWAS_v7Sh1sgCD7QYuzCmp2tswnpLSNPI6x6zjSX88AoLCXnsb7yYBkSz3ZsHu-M5tS7YBaqoUA_XqbCUwbcr_x7Btcq2UD1DdhO-v24z45DVzM9PVaXA34WYlh-5E1xY4AlxsM8w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/452945470e.mp4?token=vPxGf2jSJjlEWml75elYkr0DeONudef4LQuKycTNLej0GUnwbMs_2g58oCJMDkuLN58n_3UfIkp-2Vs_R-P3ViNsjAVabO1Ozpl9vMra7oJ7qm9YGV3G8ZI7IWXOr5fQlM7MEMr6tEXznTowNQMiODXqNErFQQNZ8C4x_LMXgCM_c7NGQ7nnunlTrq07bjyX1B5iK2G96tOwdfWAS_v7Sh1sgCD7QYuzCmp2tswnpLSNPI6x6zjSX88AoLCXnsb7yYBkSz3ZsHu-M5tS7YBaqoUA_XqbCUwbcr_x7Btcq2UD1DdhO-v24z45DVzM9PVaXA34WYlh-5E1xY4AlxsM8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم تشییع نیروهای سپاه قدس و حشد الشعبی که در حملات سعودی آمریکایی کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138648" target="_blank">📅 12:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138647">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد مقادیری سلاح و تجهیزات رزمی را در منطقه «مجدل زون» در جنوب لبنان کشف و ضبط کرده‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138647" target="_blank">📅 12:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138646">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138646" target="_blank">📅 12:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138645">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59dcbe8179.mp4?token=ZbTV1HWvKw15F7kNVnz-SqXLsCh2432ex_EA3oUUdDN7K1CizwmJRp-K99_BTCKObthanT3M6B_L8P3dzd5PS4je5pwL3GZvSItBa9LdGhK_EgPqlu-UfJn4G_cWo26Ijtonwm1JJkUVQ-umN7niluq1bppVxl3ZNnmug27_D7YVNEl3S1XpFnTJCd4hKJxetJHKJMTCvP3H8t2vHU7YvbfKjT811Zx5DL7k3ShYsb10DQlEd8lpih3D0lcMNfxWL5q0YQV9bbJbXnGJBPDbT5ub93WjALXxq6JC__x8NvuafyPlXhkTxSK3QZvnOSH2LhYAEs2Izm6EpF56Wqkgug5IrqmyamKZI4y7aPAbfJlUsxHwRKvflKysEuvrQhB7KZ6mM8wD7_kqYf1BjpOjL0_ZnSjbJVFhXFt5Ep7K1MWVxy34enSy53zu10cwuxyHh7dZvioEzouG7u8ncSgWDH-0KZhLRwjwSWpJmDzDQ2TF0TLFHxi0_aR7iH86nIbU3ZGpr0wH4EmKjqJZfQNHGr6KnNTV1aZkJUwWqJ0qJc29yn6ZEK5FjEhEY35j5uI8T3m7I_GCT-MqTk8MIaGlH2KPqRAIbCTQLO-oVMj6mVXEolCsaW7LzoVB82h7RXmGUEijBNmWYEPaG79HCk64MZ_J2WtWlmdXC1SW34blAFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59dcbe8179.mp4?token=ZbTV1HWvKw15F7kNVnz-SqXLsCh2432ex_EA3oUUdDN7K1CizwmJRp-K99_BTCKObthanT3M6B_L8P3dzd5PS4je5pwL3GZvSItBa9LdGhK_EgPqlu-UfJn4G_cWo26Ijtonwm1JJkUVQ-umN7niluq1bppVxl3ZNnmug27_D7YVNEl3S1XpFnTJCd4hKJxetJHKJMTCvP3H8t2vHU7YvbfKjT811Zx5DL7k3ShYsb10DQlEd8lpih3D0lcMNfxWL5q0YQV9bbJbXnGJBPDbT5ub93WjALXxq6JC__x8NvuafyPlXhkTxSK3QZvnOSH2LhYAEs2Izm6EpF56Wqkgug5IrqmyamKZI4y7aPAbfJlUsxHwRKvflKysEuvrQhB7KZ6mM8wD7_kqYf1BjpOjL0_ZnSjbJVFhXFt5Ep7K1MWVxy34enSy53zu10cwuxyHh7dZvioEzouG7u8ncSgWDH-0KZhLRwjwSWpJmDzDQ2TF0TLFHxi0_aR7iH86nIbU3ZGpr0wH4EmKjqJZfQNHGr6KnNTV1aZkJUwWqJ0qJc29yn6ZEK5FjEhEY35j5uI8T3m7I_GCT-MqTk8MIaGlH2KPqRAIbCTQLO-oVMj6mVXEolCsaW7LzoVB82h7RXmGUEijBNmWYEPaG79HCk64MZ_J2WtWlmdXC1SW34blAFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار ای‌بی‌سی: ونس اخیراً گفت اسرائیل در تلاش است تا پایان جنگ با ایران را تضعیف کند
🔴
نتانیاهو: امروز صبح گفتگوی بسیار خوبی با معاون رئیس‌جمهور داشتم و فکر می‌کنم که آن را حل و فصل کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138645" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138644">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان سعودی:
حمله ایران به اردن را محکوم می‌کنیم.
🔴
در هر اقدامی که اردن در برابر حملات ایران اتخاذ کند، در کنار این کشور هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138644" target="_blank">📅 12:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138643">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دقایقی قبل زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر در عمق ۸ کیلومتری امیریه در استان سمنان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138643" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138642">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در کمیجان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138642" target="_blank">📅 12:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138641">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گوترش: جدی نگرانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138641" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138640">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
بلومبرگ: اقتصاد عربستان سعودی به دلیل جنگ جاری که تأثیر منفی بر صادرات نفت داشته، به پایین‌ترین حد خود از سال ۲۰۲۰ رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138640" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138639">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نتانیاهو: قابل پیش‌بینی نبود که ایران تا چه حد می‌تواند تنگه هزمز را به اهرم فشار تبدیل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138639" target="_blank">📅 11:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138638">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: اخیراً عبور شهروندان اسرائیلی از مرز و ورود آن‌ها به داخل خاک سوریه به طرز چشم‌گیری افزایش یافته
🔴
فقط دیروز، ۳ شهرک‌نشین نزدیک به یک روز کامل در خاک سوریه ماندند
🔴
ارتش این هفته، دو نوجوان زیر سن قانونی را هنگام عبور به سمت سوریه دستگیر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138638" target="_blank">📅 11:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138636">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b3dbc650.mp4?token=J8UR2yw2h0NgeTUp3tBr7ueQBTWUj8uVf-UjiNfdQ7VCWUaNqKkOP5O1gb_QevmMjYXGnur6Jyu-vrBxzd3ZAecp4dTpI17kq9y3TYwH4bUYN9pd7P-b6S610QCknHBgC2GgrJv378LlVGHEawFWBZq0PWQe2ErbU_ZAy9gazRO0MsLWyUjQ9GRVVFicp28SXkvNLFuPbn9Qrt76Fc1YU2rzKHRTbuF2Itkw1aRATdn8smrCqKnzqJS8yIx4p_ZBgcN6SHY9sJcQUF2zg3-L-bxudpofp8TjF964A9I3Psuvjc2GO0kq8EIO2TPOS0CFX1q0pIu7wUw7akxnxVEKXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b3dbc650.mp4?token=J8UR2yw2h0NgeTUp3tBr7ueQBTWUj8uVf-UjiNfdQ7VCWUaNqKkOP5O1gb_QevmMjYXGnur6Jyu-vrBxzd3ZAecp4dTpI17kq9y3TYwH4bUYN9pd7P-b6S610QCknHBgC2GgrJv378LlVGHEawFWBZq0PWQe2ErbU_ZAy9gazRO0MsLWyUjQ9GRVVFicp28SXkvNLFuPbn9Qrt76Fc1YU2rzKHRTbuF2Itkw1aRATdn8smrCqKnzqJS8yIx4p_ZBgcN6SHY9sJcQUF2zg3-L-bxudpofp8TjF964A9I3Psuvjc2GO0kq8EIO2TPOS0CFX1q0pIu7wUw7akxnxVEKXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا از کویت با
HIMARS
اهدافی وو جنوب ایران رو هدف گرفت
🔴
سنتکام هم ادعای ایران درباره انهدام این سامانه‌ها رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138636" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138634">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiEFzPYDjOcC0p9bIhC9LoccrXTFTQYN1irJF49AR8xbgph47Z0Fco2IHhwgBQX8kGsu6z5TiPUFaxdEFJg7QpGZDrmiwiV_igNlnA_hycz7Cxbw0XYszMXiTrrAPMeJm4x5KSC9hFhgeJOlB1DJY2ylbXLTBtL9BIQD1FOf_NuZqzFZqic_Q3LZjoWhfrlF8nqJd7JjG5qvijou9hQuPJmiWkR1hele4VDEqJKKaZrNgdrXV5qB2N-ITlNdWolWkHlzHyoGseGeEzuGDGKtDGZNL_MwUYke2J2mi__WZYmM5wu3fj0g-X497vCSErjUYjfAGYNJCQydDqrFoV9yqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQjRUxKrOKR0J7_icuyc72ecPgdUOiYX7Gp9aX2GZ73pQ-ZmBTr06IpHxXk5EKKy1CaDMqq1zAccgypfKTE11kGM0Sd62RFkfonBWnonHPIJ_RbPtXNmbskpmLjkPyNp4hccwy6lJ0TCpWUje9M5Riuobvyyd8Ue00r8pxk3Wa83vWfNGPnlRg-ZYpyrMoVDyxIr4e0VhdUhvtY-UoX-wwxQ3SlKZd4qG5yU3xVrSZZ422gONlhhqjX4Y6RYvAKJcpJKEYiIu7vLMGpP7s2IWGJIUJcFoHnymbw9FfjoIrwIUixhM6ebjO8DyFOTcKlRGQjudTIGgkXyR1R6OpTGNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
این حرومزاده به اسم نوید زیاد خان قره باغی، با شیرین زبونی برا دخترا می‌برشون‌ خونه‌اش و داخل لایو می‌زنه و تحقیرشون می‌کنه.
🔴
تو این ویدیو که از لایو هاشه یه دختر اینقد می‌زنه خون بالا میاره و گریه می‌کنه و یه دختر دیگه اینقد می‌زنه بیهوش میشه.
🔴
روحیه حساسی…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138634" target="_blank">📅 11:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138633">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
منبع ایرانی به NYT :حمله به کشتی تو مصر، پیامی بود که، ایران توان به‌هم‌زدن حمل‌ونقل جهانی و بازار انرژی رو داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138633" target="_blank">📅 11:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138632">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز: با تشدید تسلط ایران بر تنگه هرمز، نفت خاورمیانه با نظم جدید و تیره‌ای روبروست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138632" target="_blank">📅 11:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138631">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs7PHj4NXLyjyfW8PMCIsMbFi-u6RwBDhbGmS437dt-lKaXhT86s2y3yKYrSVuHGPJuCIHms0LABlYYKIzseUxby-9y8bCcPyUPOIBtZNe3vlfFAve1P__PH3jDIpXdPmq2hEkn_aBuEllxJHoMdXPksey7YOMWw_L8T2ypzxhGH4uCRCn39RfPinQQgbDujksJAroie4kuLlMYVSXp85EDZyC9Eaz44O4VJiu_gIvMB8WYvcYiBSKoI5Y9uwAm7AxQKLhnfQpRIIH2JGyP7WqwLSUKzhrL8zXbwl6WIoYe-rlk9IHe2mjDSGFE_2fhXxBsR6EWe4m1NiiMhsc-eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گودالی که در اثر اصابت موشک روسیه در اعماق خاک لهستان، حدود ۱۰۰ کیلومتری مرز اوکراین، ایجاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138631" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138630">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رسانه‌های محلی در اهواز می‌گویند شدت انفجارها نسبت به چندهفته اخیر بسیار بیش‌تر بود و بسیاری شهروندان از بابت صداهای مهیب به خیابان‌ها آمده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138630" target="_blank">📅 11:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138629">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سپاه: همین امروز حمله شدیدی به مواضع آمریکا خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/138629" target="_blank">📅 11:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138628">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گفته وزارت دفاع کویت یک ساختمان چینی در شمال این کشور طی حملات ایران آسیب شدید دیده و یک کارگر نیز کشته شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138628" target="_blank">📅 11:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138627">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وضعیت کشتی آمریکایی هدف قرار گرفته در مصر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138627" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138626">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نتانیاهو: به متحدان دیگر شما که به اصطلاح هستند نگاه کنید، فاجعه‌بار است. وقتی ما با ایران می‌جنگیم، در واقع برای آن‌ها می‌جنگیم. ما با این رژیم که ترساندن را به کار می‌گیرد می‌جنگیم.
🔴
ما جنگ دنیای تمدنی را می‌جنگیم، اما اکثر کشورها بسیار ضعیف هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138626" target="_blank">📅 11:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138625">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b55112a2.mp4?token=JYv6AGXmDR54gtGjSlb3NwhSyVn8u36w7YKsPpSHg-Y60eMlqp4kNUWRbVpdvaNT7oaEkQljCrf99-DPYLQp5IV-wQ4XUuVMpWp6HxWqvR5JoxeaMDh2-49fhcayKICEZCYdyXw9xH1H10gMAzNk7iHFbzdmxiG1T_JMRp5TwF8T6R2Vc5JNfevUZREGWk5i3kiWywaXXvnXrZ1en7k2BdNdujd7ykJwtm17ysUxsmRSZHRHUT3oiNDxEsYE1skVG5eP5ENPp5CZ0fkJsiZv4beBFnJIrtRcWB5HjGCvn0M08rb1Td22enc1dAadPDc9qpGGIA5Q8IYcCKtlD0M4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b55112a2.mp4?token=JYv6AGXmDR54gtGjSlb3NwhSyVn8u36w7YKsPpSHg-Y60eMlqp4kNUWRbVpdvaNT7oaEkQljCrf99-DPYLQp5IV-wQ4XUuVMpWp6HxWqvR5JoxeaMDh2-49fhcayKICEZCYdyXw9xH1H10gMAzNk7iHFbzdmxiG1T_JMRp5TwF8T6R2Vc5JNfevUZREGWk5i3kiWywaXXvnXrZ1en7k2BdNdujd7ykJwtm17ysUxsmRSZHRHUT3oiNDxEsYE1skVG5eP5ENPp5CZ0fkJsiZv4beBFnJIrtRcWB5HjGCvn0M08rb1Td22enc1dAadPDc9qpGGIA5Q8IYcCKtlD0M4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: من حمایت دوطرفه برای اسرائیل می‌خواهم زیرا فکر می‌کنم این اساس امنیت ملی ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138625" target="_blank">📅 11:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138624">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82cc0cd33c.mp4?token=lmQ5CtIUZ8isI5nsAJKW2PfXWi0ZgMZxANX6iqXpfTmZHajgHjsklw6NVQXvILAzzhtkMpxbzGUcp7-6TogwqAFaevDJD0bK-aEQ0Ko58VL3lfk7h7YLzdgMkerWVTvDLMgvg5OlrMPGDYLHxJPVNtaOYwhb8G3xbkW8ofx-S37gsItYopFi7WSVBTBbzxQKT1CjLV49nhi_h4X3dnKqglB4KUIic8KZmYrEy4hKvNJN3Bi8zFL-LDJASn0443AqZYWFaFmcozjGTxd5BhNqVf_OaoZNMnjHVYP0fOCNRPJ1FrZ8Wq_tGX9eb-gKWcIO8yNQSQHVe-_UZ1cTIQIRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82cc0cd33c.mp4?token=lmQ5CtIUZ8isI5nsAJKW2PfXWi0ZgMZxANX6iqXpfTmZHajgHjsklw6NVQXvILAzzhtkMpxbzGUcp7-6TogwqAFaevDJD0bK-aEQ0Ko58VL3lfk7h7YLzdgMkerWVTvDLMgvg5OlrMPGDYLHxJPVNtaOYwhb8G3xbkW8ofx-S37gsItYopFi7WSVBTBbzxQKT1CjLV49nhi_h4X3dnKqglB4KUIic8KZmYrEy4hKvNJN3Bi8zFL-LDJASn0443AqZYWFaFmcozjGTxd5BhNqVf_OaoZNMnjHVYP0fOCNRPJ1FrZ8Wq_tGX9eb-gKWcIO8yNQSQHVe-_UZ1cTIQIRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو ادعاهای متوهمانه خود را درباره ایران تکرار کرد
:
ترامپ اساساً سه گزینه دارد: اول، موفقیت در دستیابی به توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
🔴
هر چیزی که به پایان برنامه هسته‌ای ایران منجر شود، همان چیزی است که مامی‌خواهیم. این هدف مشترک ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138624" target="_blank">📅 11:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d39ced1a5.mp4?token=BBFhQcjQvhr_Mss4VVhwwT2PMK2nw5aVaLJpc1cjjjnQxKVkgRZeqb-RHx0x-kRhXmrbXgj9Zbnxl5roeUlPGwqD75rTrMn3CeKMS931y2DkDidJwQlDQYpvIF3vBla6y-4IAKahZ90-aAyeW0ANTScjCg4xgRrlQw6jg3N7STRfiz0mmD_yTF8eCwS8ZFSXYRs1h0nbydDVqFUeSn4aaKLUxRf1M2seyWrvNgZzcfhB2KO2jYYYxsWIzuXAHsSzf9NBiAlQPvMm2ntYAMVOzozahJiVvMDxFMsrxcZsGq_5vll7OdgJ-xHK7INwb3sNsn-uAXA5DEJGIz_URxWQPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d39ced1a5.mp4?token=BBFhQcjQvhr_Mss4VVhwwT2PMK2nw5aVaLJpc1cjjjnQxKVkgRZeqb-RHx0x-kRhXmrbXgj9Zbnxl5roeUlPGwqD75rTrMn3CeKMS931y2DkDidJwQlDQYpvIF3vBla6y-4IAKahZ90-aAyeW0ANTScjCg4xgRrlQw6jg3N7STRfiz0mmD_yTF8eCwS8ZFSXYRs1h0nbydDVqFUeSn4aaKLUxRf1M2seyWrvNgZzcfhB2KO2jYYYxsWIzuXAHsSzf9NBiAlQPvMm2ntYAMVOzozahJiVvMDxFMsrxcZsGq_5vll7OdgJ-xHK7INwb3sNsn-uAXA5DEJGIz_URxWQPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره غزه:حماس باید خلع سلاح شود و غزه باید غیرنظامی شود
🔴
این طرح ماست: خلع سلاح، غیرنظامی کردن غزه و ریشه کن کردن رادیکالیسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138623" target="_blank">📅 11:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری / سپاه: متجاوز همین امروز تنبیه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138622" target="_blank">📅 11:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
اسلام‌آباد نهایت تلاش خود را برای احیای مذاکرات میان ایالات متحده و ایران به کار می‌گیرد. گفت‌وگو بین تهران و واشنگتن در مورد وضعیت تنگه هرمز و کاهش تنش ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138621" target="_blank">📅 10:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دقایقی قبل، زمین لرزه‌ای به بزرگی ۳.۴ ریشتر لالی در استان خوزستان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138620" target="_blank">📅 10:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47170f0680.mp4?token=eB_oQyrbLJrLvmKkfevIj-8KvwYU5-Ha2msL2DkZWlbd3QfiSElYdUb6bMWWcYX3U8FzS9hxj0RPekfNsdVVplphGwlNQJYxetNVunwHBaaCuDXmf-QzUm8prYxe__IMmx6pjyXyHvf0SqeuVHPXzQWdKOpqQtoJiAnq9rxShgp-r2rgukVVJ08s1GRM6jWXYOSkjaU98Xl-o2dsabc7ti3B59kK0Gzt99WkYvSWL5qEW2OnboW3JWhcD3sxn7kYvYFLH-UZZVll0-RF71BSTbhpL6_uOh3QmSvSPLpuuHdpUL7XM3HsR4TdmGvRolWuRCYrW7Iu7HPXlIr9-9dyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47170f0680.mp4?token=eB_oQyrbLJrLvmKkfevIj-8KvwYU5-Ha2msL2DkZWlbd3QfiSElYdUb6bMWWcYX3U8FzS9hxj0RPekfNsdVVplphGwlNQJYxetNVunwHBaaCuDXmf-QzUm8prYxe__IMmx6pjyXyHvf0SqeuVHPXzQWdKOpqQtoJiAnq9rxShgp-r2rgukVVJ08s1GRM6jWXYOSkjaU98Xl-o2dsabc7ti3B59kK0Gzt99WkYvSWL5qEW2OnboW3JWhcD3sxn7kYvYFLH-UZZVll0-RF71BSTbhpL6_uOh3QmSvSPLpuuHdpUL7XM3HsR4TdmGvRolWuRCYrW7Iu7HPXlIr9-9dyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله ارتش آمریکا به یک دهانه پرتاب در نزدیک بندرعباس
🔴
سنتکام اعلام کرده است که جمهوری اسلامی موشک های کروز ضدکشتی را از این حفره ها به سمت تنگه هرمز شلیک می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138619" target="_blank">📅 10:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138618">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d6fe82ac.mp4?token=sfctjZpeeoQcmCRP2ZNqtc3Lb2a2vLsgcBPc7l5eN0HAHg2WSHgtObspwETRSXYfdzY8mTI4_OXv5zUH5bgSZq3tmhjLbJHHFEgjOIScg-bNphZP7TlME4tIgqCdMSj6yaKQSScPvyxiPQVrpKpGnfUZ3BxAvRzmli_8Pdv-mTK-KwH-ybmI3YzUUuzc3YoUOVqmIGmr2yXt6X4eY3lBpiOg3VyO739EBpo8MVKw5Vd2fhe2TGb5CSHeYSFXmCf--FPEnfXnAaHoWzo7IsXJPqzYSdODW1M8nn_edqzQsCL5bsqu5Mk2HxSRAV-w4BYV1Fp8_a6L0UBXqgJ9JBjrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d6fe82ac.mp4?token=sfctjZpeeoQcmCRP2ZNqtc3Lb2a2vLsgcBPc7l5eN0HAHg2WSHgtObspwETRSXYfdzY8mTI4_OXv5zUH5bgSZq3tmhjLbJHHFEgjOIScg-bNphZP7TlME4tIgqCdMSj6yaKQSScPvyxiPQVrpKpGnfUZ3BxAvRzmli_8Pdv-mTK-KwH-ybmI3YzUUuzc3YoUOVqmIGmr2yXt6X4eY3lBpiOg3VyO739EBpo8MVKw5Vd2fhe2TGb5CSHeYSFXmCf--FPEnfXnAaHoWzo7IsXJPqzYSdODW1M8nn_edqzQsCL5bsqu5Mk2HxSRAV-w4BYV1Fp8_a6L0UBXqgJ9JBjrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی در اهواز  پی حمله آمریکا به این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138618" target="_blank">📅 10:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138617">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwCWl9Qg9wBNzyHsR6-QwsCbTgl7p1BitqFymwuhE77PiAtOuY4eqHDjtitC-ZrVhXDOzYs3W3fnj56zXayGBceojUTT1C_q2bXZQwxqJnZ5U1BJSzpiF3lQxuD6F2y1GqIugAEQxbd6vbrkezXw1l12wy9YOzFuNXqI9bh_jP2OfJ8am2TZNy9g2OMiHQjik-GvbVSY9XS0U0E2cC1PomnHIKkJ3B08q9gp2q2eVzONGiSsgDY65Fa5z6CspQQbhpD7uuuRX7HoNeo70WwskSTj-xM7OlMxrLglA_p4VCHemYP_df_cPo1WOrk_zzeJtZywdkCqAbp6JX9aUEgZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: در صورت دستگیری من در کشورهای اروپایی، نیروهای ویژه اسرائیل برای نجاتم مداخله خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138617" target="_blank">📅 10:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aixey4sdpRrp4OyDV9ZJnQJbhnxWt25KRUPEaExu4pYwHuCXw1oAfK9DkygjxJH13Ah0Rkj3qRaja-dAXJF94SvQQGr3FkospaWhjzfyNouJ3nz241OIiKk4fOeDeP9Q7MPiUTh6uBBxk3lPieApymhx0Z3YlMoCC7vbo548kkCCgvAQXEDJcPeQ_soqARMztlnp8clfB0aY3rlu_amJVo9wGksdk1JTnnRr42F6thHYZZTn5KBLIu7hGM-h1PHeCMOj_RNO1NRyS9Ooa6v3Q2V6ZKT5JTlFO_1ET8Tc_qalQfgFGdAUnx78pAyopeg1tOvrpbqjaODFA-JF_2vxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
آخرین قیمت نفت، ۹۲.۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138616" target="_blank">📅 10:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138615">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbbZro87JIwbCwiPNvpmzavbVwBnorxh1vR0TILqwMCclpe14_QEQIcGYqsibzpNoCWKuO_pHEcqRrxKy3ogniDsseG-gwYyaKKoXSwWBNe0C2BXrf5PcokFTktKqQHTub5K02rON3kvx5LjfeS6-2X_KlaHhAwU-5uC-WS8CEl4f35QyZ0GpzvCW_SNCy43CkOkJ3EzhqtBa--X1QPfGfLbmDHkHIik0upsfYIf2mHlZcNbYKqYreRfUtwBKIh294nqDEjiVFJlbFqNBl_hPUoI2OfpZID5zPijXH9ZARO6QBullTESPm9MWqLgL7k5NRde27NmgXdvP0d5vBlR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نایا: اعزام هواپیماهای نظامی آلمانی و فرانسوی به اردن برای کمک به نیروهای آمریکایی در رهگیری حملات ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138615" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
زلنسکی رئیس جمهور اوکراین اعلام کرد که در حمله موشکی گسترده روسیه به چندین استان اوکراین، هشت نفر کشته و ده‌ها نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138614" target="_blank">📅 10:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138613">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
👈
شهرهای مورد حمله قرار گرفته از ساعت ۳:۳۰ بامداد
‏
🔴
قشم
‏
🔴
اهواز
‏
🔴
بندرعباس
‏
🔴
آبادان
‏
🔴
اروندکنار
‏
🔴
شادگان
‏
🔴
فراشبند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138613" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138612">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3gclmx5EnOcDtWpdcKBbEVGXMcYrD524tERtj3klnYte198pSAvg5dh6qOyFSQM6SYI84RNBd_Q_07q3dGznGlSkVLqeA_9wqGd9JJY5LUeR19YXmiU_PHUdr9wbYTSIRulDOnO3Wsh7VXHuLNPtwo71UypO9hLc4I_opmv3ObNHu-ipQYpcxsU5Y1Pb7j4lqxcQkSXWaXKait6QTzHPXnIe4TbPkCMuLu7ns2Q4pI8sJnBMsFWaXQHOuGeCJKu7fFnwLahnFTYmX_vuObLT0rO_NDzGHh_5_AXUe14Ku9LCBO0h9TIkrizqJYOqOC1zdyISL9hTW-sATrqrbaGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۲.۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/138612" target="_blank">📅 10:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138611">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ای‌بی‌سی به نقل از نتانیاهو: من در دیدارم با ترامپ، سعی نکردم او را به ازسرگیری حملات علیه ایران ترغیب کنم
🔴
گزینه‌های گوناگونی را درباره ایران با ترامپ بررسی کردم، از جمله مذاکره با آن برای دستیابی به توافقی گسترده‌تر.
🔴
از جمله گزینه‌هایی که با ترامپ بررسی کردم، ادامه محاصره تنگه هرمز یا انجام اقدامات نظامی است.
🔴
من کسی را گمراه نکرده‌ام و هیچکس به ترامپ دیکته نمی‌کند که چه کاری انجام دهد.
🔴
قابل پیش‌بینی نبود که ایران تا چه حد می‌تواند تجارت از طریق تنگه هرمز را به اهرم فشار یا سلاحی تبدیل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138611" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138610">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
منابع آگاه به وال استریت ژورنال : ژنرال براد کوپر، فرمانده سنتکام، یک طرح عملیاتی گسترده را برای ایران آماده کرده است که مدتی بین 10 تا 14 روز طول خواهد کشید و شامل حملات شدیدی است که هدف آن مختل کردن توانمندی‌های موشکی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138610" target="_blank">📅 09:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اولین محموله LNG قطر پس از ۳ هفته  از تنگه هرمز عبور کرد.
🔴
سه هفته پیش تهران پس از نقض تفاهم‌نامه توسط آمریکا عبور و‌ مرور در تنگه هرمز را متوقف به تأیید ایران کرد‌.
🔴
این کشتی قطری با داده روشن و از مسیر تعیین شده توسط ایران گذر کرد و بدون هیچ مشکلی به‌سوی آب‌های آزاد می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138609" target="_blank">📅 09:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVfnn5PShqEDT_rWlKAwUHt4ini94RCtXX1bIeuaQM6hdsxDcSXCVBIDfFLlJor-HlufZXR66gOf7aZrPhFrhTtUxefrORzC-zvGh5WEcKOlWf78WvGcG2xOZQpCAZALInFecynB-TyJoFqOSbO0TJe_1Dxu4GDFz-Uftl__Nwbz-azsle8FWeGGuzUAsHtw2e4MPPaQ7fzNIh75QhM6phDNelZXlosav6lUtYPUwP18wXY4rnUa1FNWDe6h-Vc9MFfUfYLYwbqGqrnoF1kGc-93Ifi1VeecmnyMOq4dqYaQM9TyRiM1ejlTYgX4wSEHjddMn4s7Xiwao2JV-yB1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین در پی گسترش تنش‌ها در دریای سرخ،«مذاکرات مستقیمی» با انصارالله یمن داشته تا نفتکش‌های چینی بتوانند با امنیت کامل از دریای سرخ عبور کنند.
🔴
اقدامی که با هدف حفظ جریان صادرات نفت عربستان و جبران اختلال ناشی از بسته شدن مؤثر تنگه هرمز صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138608" target="_blank">📅 09:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138607">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: پس از پایان این جنگ، فکر نمی‌کنم تنگه‌ها دیگر این‌قدر قدرت چانه‌زنی داشته باشند، چون مردم خطوط لوله انرژی را از تنگه‌ها خارج کرده و به دریای سرخ و از آنجا به اسرائیل و مدیترانه منتقل خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138607" target="_blank">📅 09:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTKkVf7bQc7a2vsEiFigRPNNXbgU0euaxuZGtzINSLHhG_gzbf4_KCiXGa4wJTkOUmonqUzxIHvHMw-8dIDRl4bltUZjkhbPWwV-hL-7h7VX7dfKVSIy8NKJXZmbUFhYp92YYCIr0-b5cAADHh-SFn10SKD4ANGzH06fD0rkqmwImuVtJ0epsblLCa3jFNJ7Z81ttKBADQ5s72d-ZbEhvHnlYuZPz7TjXa8xr8JnhPNTvlBC_UB08wrVdLVK1YgiJInFxIfKRhDYSPoypbBlOAWLlnVogeP9DXTxE0Pry3qyOBmtLQRwbbtLUjKDHnVPL9086Uy56ZmnJEEJ3TMvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMt_vFvNxnWmgu_-oBKPeCJv11rybETeA2pgjL-Sz8X7k6u4KnFZCPtN2Vvrlv8kgNV68SaXSZa5hAAGBEdhdM0IHMaozU3bjgRFjpCcFoQKXdSuf1fO3HzCWS4TZhyP6ydlkR5I0EaCJC0xKAiWKZMie8YlhHFh96jt0eqMyVJFXRG6MLNiOpfNxkLSpyYlshSnBI9ln_DVwIkwwysh7GWfIMSgZHjmnIcmPb911mnkMSRhVnqvl7Ib5T8CwVPSzB0QNrRyPkyQBZaQhg81s5uz4Ui_Qy9tuBkCLJAGGa-SXw6ihsF9Na8_4e8Hn0bZcXmNOLTT87AhSaxjHjkDBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وضعیت قشم بعد از حمله دیشب آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138605" target="_blank">📅 09:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ روز چهارشنبه با شاهزاده خالد بن سلمان، وزیر دفاع عربستان سعودی، دیدار کرد
🔴
این دیدار پس از آن به برنامهٔ سفر وزیر سعودی اضافه شد که او با معاون رئیس‌جمهور، جی‌دی ونس، ملاقات کرد و به او گفت که عربستان خواهان کاهش تنش با ایران است، با وجود حملات مشترک آمریکا و عربستان در این هفته به شبه‌نظامیان طرفدار ایران در عراق.
🔴
منبع آگاه گفت هدف این دیدارها، انتقال پیامی از سوی محمد بن سلمان، ولی‌عهد عربستان، دربارهٔ جنگ با ایران و اوضاع منطقه بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138604" target="_blank">📅 09:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
الکسی چیپا، نایب اول کمیته امور بین‌الملل دومای دولتی روسیه در گفتگو با ریانووستی گفت که با سفر همزمان بنیامین نتانیاهو، نخست‌وزیر اسرائیل و ولودیمیر زلنسکی به واشنگتن، هدف حمله کی‌یف به کشتی‌ ایرانی در دریای خزر کاملا روشن شد: هدف آن پیوند دادن دو درگیری و تبدیل آنها به یک جبهه گسترده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138603" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b2815541f.mp4?token=gCxuKVzFWozTjHNGJ1t7RDi0GQT2CdgqQLUYEUe2BN6gltof-8GvnH52vnpJMidwhmI6A8eOkoO4Z8NrrVLMf0kTgHN7wQjJkuXP8QgT8OZiexXY3w9VWMXsVmfmRAaMRHesfNl7WHjB2lu8aPRjsiZwAkft9cat-652OOn-8bIHt8qVP7O8JUSFEKkr_4xSqgn-UyyyOQv9N95VK5HRReHNahETO5vpcet6WE9IstIcxhnf1nnrNY5FafDX66GmF1GUcz7JjO2pbB6IAlz-3xCqIFJsMqUwr8puWIJwufbRcOn6_GolmhmkDr7m8qBtgSE_U5MfICSyYKzNZMxvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b2815541f.mp4?token=gCxuKVzFWozTjHNGJ1t7RDi0GQT2CdgqQLUYEUe2BN6gltof-8GvnH52vnpJMidwhmI6A8eOkoO4Z8NrrVLMf0kTgHN7wQjJkuXP8QgT8OZiexXY3w9VWMXsVmfmRAaMRHesfNl7WHjB2lu8aPRjsiZwAkft9cat-652OOn-8bIHt8qVP7O8JUSFEKkr_4xSqgn-UyyyOQv9N95VK5HRReHNahETO5vpcet6WE9IstIcxhnf1nnrNY5FafDX66GmF1GUcz7JjO2pbB6IAlz-3xCqIFJsMqUwr8puWIJwufbRcOn6_GolmhmkDr7m8qBtgSE_U5MfICSyYKzNZMxvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از بقایای موشک‌های رهگیر که برای دفع موشک‌های ایرانی در آسمان اردن شلیک شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138602" target="_blank">📅 09:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a307c5f4.mp4?token=Nm_sTlqt0xCz9spWldZKNW4ZqK_uhIgepJs8bQ4-EruU72zHdH17mF1vIGDvwd0Tbvb40MlIegjgqchCcnxlTqQgmKeJGjDnzHmbxLBSw9r7fKUn5EvvIgJT3Gw8jvLoXRhn_MTy7G2Wu_dhWiSlI2h42E7S-9RQ9DFcjiHdUQNXPMywgiH3NhvjAaQU3hayI05f3Efj-AN4vhP5hs5I6IEm3KP_9x_faX8Yu7o3w-bSKVqXRlAq1Wh_ufair0AjHalcSvsKV5TMCM34OIHCmn-vDpwk8YHCyk8TrXD5MDiesGrOBfEsm4TUh7Qg9ay9d1fGu9WAsuvbsQkDt6VZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a307c5f4.mp4?token=Nm_sTlqt0xCz9spWldZKNW4ZqK_uhIgepJs8bQ4-EruU72zHdH17mF1vIGDvwd0Tbvb40MlIegjgqchCcnxlTqQgmKeJGjDnzHmbxLBSw9r7fKUn5EvvIgJT3Gw8jvLoXRhn_MTy7G2Wu_dhWiSlI2h42E7S-9RQ9DFcjiHdUQNXPMywgiH3NhvjAaQU3hayI05f3Efj-AN4vhP5hs5I6IEm3KP_9x_faX8Yu7o3w-bSKVqXRlAq1Wh_ufair0AjHalcSvsKV5TMCM34OIHCmn-vDpwk8YHCyk8TrXD5MDiesGrOBfEsm4TUh7Qg9ay9d1fGu9WAsuvbsQkDt6VZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: اگر ایران به اسرائیل حمله کند، چه پاسخی خواهید داد؟
🔴
نتانیاهو: فکر می‌کنم آنها اشتباه فاحشی مرتکب می‌شوند و ما خیلی خیلی قاطعانه پاسخ خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138601" target="_blank">📅 08:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=kP7IE3lD0_nGVPAPGHGVlJTeU3BNGL5M-cJYQtYfoyWaUbEE5kTlxffFnp-lPSsVROrwL-4pGPncEwHz_Fn1pT4lVINcOI2xzK2Zf_cav4h3vBxka50DwjUM0VR4ypGFSzHaBkVxYV9FT8NuSXJR0vJ56hDd0D-SBD3z9vd-FlFbtNCz_RM6O_V-wTc4miFz-5YvXKMcncHlBNzujWEyXdhYee4FiSw7or0rc3L2t4Yh0uW_tWvHdqrveYKg_F_yvX4xe7-tjZCiZwoeui1om8ko15cIsRMF_NZ9N1FmdWn2aUANxSlqoR2YFJNtf-GVlg_RrWv9mOH94p-jRrnk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=kP7IE3lD0_nGVPAPGHGVlJTeU3BNGL5M-cJYQtYfoyWaUbEE5kTlxffFnp-lPSsVROrwL-4pGPncEwHz_Fn1pT4lVINcOI2xzK2Zf_cav4h3vBxka50DwjUM0VR4ypGFSzHaBkVxYV9FT8NuSXJR0vJ56hDd0D-SBD3z9vd-FlFbtNCz_RM6O_V-wTc4miFz-5YvXKMcncHlBNzujWEyXdhYee4FiSw7or0rc3L2t4Yh0uW_tWvHdqrveYKg_F_yvX4xe7-tjZCiZwoeui1om8ko15cIsRMF_NZ9N1FmdWn2aUANxSlqoR2YFJNtf-GVlg_RrWv9mOH94p-jRrnk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز درحین مراسم ختم مرحوم اکبر عبدی، عادل فردوسی‌پور دست‌ سید عباس صالحی، وزیر فرهنگ و ارشاد رو بوسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/138600" target="_blank">📅 08:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ارتش اردن اعلام کرد که پنج یا شیش موشک بالستیک ایرانی که به سمت اردن شلیک شده بودند، رهگیری کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138599" target="_blank">📅 08:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339de1bf54.mp4?token=XcApzLMgU5yjOyeM_9BKiczj0CVsl5GHh2ApZ7m6AgQuxEiA-bXqjYK_ZRrHiq8yDFEz1seBz47_UUJ-KXOeZSurAiSRfMICjIGjJd6Rx7XF0lE8U9aGEHkcH9awZaCQqdmqdullW3KOfwId_bHK64e9GD6XFlHWMHdvRCSb6K_5s5zCJsqm0pEORdKJJLa6ifwH9AfradP2PPZZ2jNyz6mMoafAUamvaC37EFOSNw5bP844l5RjQFjcfKN80Ft0k4QisMKZc_7q36gdJ6iEcM5vpke-Ilo8mUeMKkffx3Zm4Y2Oy1ja6p9FX9bq6Ox-JyrvhdOXHHvUkP3WzmLdPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339de1bf54.mp4?token=XcApzLMgU5yjOyeM_9BKiczj0CVsl5GHh2ApZ7m6AgQuxEiA-bXqjYK_ZRrHiq8yDFEz1seBz47_UUJ-KXOeZSurAiSRfMICjIGjJd6Rx7XF0lE8U9aGEHkcH9awZaCQqdmqdullW3KOfwId_bHK64e9GD6XFlHWMHdvRCSb6K_5s5zCJsqm0pEORdKJJLa6ifwH9AfradP2PPZZ2jNyz6mMoafAUamvaC37EFOSNw5bP844l5RjQFjcfKN80Ft0k4QisMKZc_7q36gdJ6iEcM5vpke-Ilo8mUeMKkffx3Zm4Y2Oy1ja6p9FX9bq6Ox-JyrvhdOXHHvUkP3WzmLdPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138598" target="_blank">📅 08:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aE110ppJzI3VHw30bp7B5kzDUgxFbXqTDZAOEeHdoB1NtKS62a15_oR6Y_CCCqX6eXbGZ1nvDq5sTKP5l7ARHl68J98S5HY5uunTq_z0glkhQ_-R2QplXKr5AEWKP2PriLhz4DCRXZwIlFkkQNZ5wO7O30cSsbMVp-Z5SnwT-fbMdDFUldLaV5L_JCWy7yFtIEsWTcqROW1VHM11MDhNj70VYAUX6jNa6xSN4_QEhZH-Oy-INrf8nAnNnEh2mY-0COgflZwU7ih-d7ZYRURFBfnCYSg0t8dyfMQwPcb_6wylz6VYffPRdsq-vdsJ939P7YjQpnqwmYCaTwBV6uBT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنت‌کام): ساعت ۱۰ شب به وقت شرق آمریکا در ۲۹ ژوئیه، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در پاسخ به حملات موشکی دیروز به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند.
🔴
دارایی‌های فرماندهی مرکزی ایالات متحده (CENTCOM) ده‌ها هدف سپاه پاسداران انقلاب اسلامی (IRGC) در ایران، از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، سایت‌های نظارت و دفاع ساحلی و قابلیت‌های دریایی را مورد حمله قرار دادند. هدف از این حملات، کاهش بیشتر تهدیدات ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه خلیج فارس بود.
🔴
در ۲۸ ژوئیه، نیروهای سپاه پاسداران در یک حمله غافلگیرانه، چندین موشک بالستیک را از ایران به سمت نیروهای آمریکایی مستقر در خاورمیانه شلیک کردند. همه موشک‌های ایرانی با موفقیت رهگیری شدند.
🔴
بیش از ۵۰۰۰۰ نفر از نیروهای نظامی ایالات متحده در حال حاضر در خاورمیانه مستقر هستند و بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/138597" target="_blank">📅 08:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDWOAKE_xkVUO3mAnx3Xvz9jIeCxw60J2wuC-Kxn3tjCJoCOvqKY7OS5CCLxSO_V-dRmllLXRL5Kw3HlJlgegjZash8c4MXbza8fyl-QjqbdoXYZhs4XuI43KqNiJMV8bm7To9Xom93rHMFMWr9b5JKZHihBiL1tJlk8lApaouggjmQxpqV8uh-qLd2bdRiyU0XboNkOCUZSSiBQ-Vwr43viU3GqDnwCM0wIUHA7CG8E-ofAoSIYW1oUuf7ZKccdUzvA3Y0RTgLwQV-ZJ6NfPdPqE2U6_srYILfPTPifl_h7VvtrFiGhXttgMcsDTYv7YOZEHygj-1Gl7BMh3eNN_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: استانهای دونتسک، لوهانسک، زاپوریژیا و خرسون و نیز کریمه را به عنوان خاک روسیه به رسمیت بشناسیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/138596" target="_blank">📅 08:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3247c7e9.mp4?token=cCnQTNg9k8AlMcgHFKWqC1_b_RzYTptguvf5cXdwHxNSgyQ0w_r_rm-3LWHg8_fM_N6uDfI43ozTXkd7mhbQW_E4VVy_T5iZo7A0Ytlm8pmtwkg1XeJD3EIjyNC7toHYz6kLqzmZbLn5DZkZzr9gAETKgS2QfThRHnw3GK4-X8GAGTdLRawfm6fl4AFQ2vmDojv2ft9Ln0gSByeXzgMuZyWE7QBa5jeXmkpxhdTMpHge2h7TGRoMPEioviG-CLkMV5zmUqWn89k3EYI58ULRCQ2WiAcVWSte4V-hFRnIdYzg_lgljX2hy-fSDBmPGwbWtBeCkgEm38L97cTZuiJvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3247c7e9.mp4?token=cCnQTNg9k8AlMcgHFKWqC1_b_RzYTptguvf5cXdwHxNSgyQ0w_r_rm-3LWHg8_fM_N6uDfI43ozTXkd7mhbQW_E4VVy_T5iZo7A0Ytlm8pmtwkg1XeJD3EIjyNC7toHYz6kLqzmZbLn5DZkZzr9gAETKgS2QfThRHnw3GK4-X8GAGTdLRawfm6fl4AFQ2vmDojv2ft9Ln0gSByeXzgMuZyWE7QBa5jeXmkpxhdTMpHge2h7TGRoMPEioviG-CLkMV5zmUqWn89k3EYI58ULRCQ2WiAcVWSte4V-hFRnIdYzg_lgljX2hy-fSDBmPGwbWtBeCkgEm38L97cTZuiJvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور جلیلی:
اکثر مردم دوست دارن جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/138595" target="_blank">📅 03:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بندر کنگان رو زدن</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/138594" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
جروزالم‌پست: جمهوری اسلامی ایران به منظور بازسازی نیروی نظامی خود، موشک‌های دفاع هوایی دوش‌پرتاب چینی خریداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/138593" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سیریک رو زدن</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/138592" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
اهواز رو زدن</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/138591" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isIWcjlX8XuJg6VXAGqLCE31hlosqfJDXoM2AIZtF7bBP3qX6He4lcOGhYhwW3Fum-neuH3Tw2erExKgW-v2QMP1QDZ793upB1hOZYMTW2LABTyIe9jy5f0knlLu9FVV_76aGpyg_PqZOVvL91TEuskZyWxzFwfkT2Wt0LSWAassDcpiwMDkGuN2vveRrrXqQ85owiFWCXII7FVHb1Y8OBPB7qnZP4xIli6LZqU1VyHdINn2fx7ui46gTijlnNo-rSzornLj-LtxmM54xc8l79qTgGmYSRk3R9FrTDiKBMv1J6n1ZEIEXGqtw5tp5iPrwSRlFkle8q2UJ5U2dyh4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/باراک راوید: حملات آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/138590" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گزارش برخی کاربران از شنیده شدن صدای انفجار در فریدون کنار
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/138589" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
گزارش های محلی از وقوع انفجار های مهیب در نور آباد، فارس.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/138588" target="_blank">📅 02:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وال استریت ژورنال: دریادار برد کوپر، فرمانده فرماندهی مرکزی آمریکا، گزینه انجام یک حمله هوایی شدید علیه ایران را طراحی کرده که ممکن است تا دو هفته به طول انجامد و هدف آن فلج کردن توانمندی‌های موشکی ایران باشد، در حالی که ترامپ در حال بررسی میزان تشدید تنش پس از حمله موشکی غافلگیرکننده ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/138587" target="_blank">📅 02:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee0836091.mp4?token=CdKJYNdVi-VZ7n__OXVHdOuKWXASzlLhPqkEyJXmtA0FzgXgJNYpWFdS_91odpGdMqtH1eEAr59700v8NtIaNAWc1fXlJYVQOWJxkRDSg1z_tGCm7o7CCj1T5lFb85INf9Sb0yurKLxdxNLR2p8Os9ZyB1tdQeG2t4C4obPyxShZGGqwBjv1nzS_RTKDwwjQozV96P0XUXVmiNq6ftboOZwMRid4oufGDvcnRKi9ESAcTq2H1B93JwvsI0EtdCDVIi05mYrZUou22T1g_Zp0VoHU4Zg8p-gibV_dCBcI5durA49Xqwq8arL-O7a6kJNJHIVLrAaxyCvhaORODSbuTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee0836091.mp4?token=CdKJYNdVi-VZ7n__OXVHdOuKWXASzlLhPqkEyJXmtA0FzgXgJNYpWFdS_91odpGdMqtH1eEAr59700v8NtIaNAWc1fXlJYVQOWJxkRDSg1z_tGCm7o7CCj1T5lFb85INf9Sb0yurKLxdxNLR2p8Os9ZyB1tdQeG2t4C4obPyxShZGGqwBjv1nzS_RTKDwwjQozV96P0XUXVmiNq6ftboOZwMRid4oufGDvcnRKi9ESAcTq2H1B93JwvsI0EtdCDVIi05mYrZUou22T1g_Zp0VoHU4Zg8p-gibV_dCBcI5durA49Xqwq8arL-O7a6kJNJHIVLrAaxyCvhaORODSbuTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک زائر اربعین:
پشمام اولین باره میبینم یه آخوند داره کار میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/138586" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501b0b150d.mp4?token=Ktd9I1WpcW7BKd4z_Zh9APOVLmDtmuPK6EVou8smEdGhCKan3oYeJUPYhUhXYzM6g1e678sYnIrI7SYkQEppPlGyVeTLxU2WtcroGsTL_8sgSCO4r4JMnLHbWnmaX_xM5HkGP5y5WixLe5fgQJqOe-FYhC5pXLjkP46BfnHizlhzy_wb6yJidACL5q6KGY0owxDRRnY-LV9EUou-P46baRH6FKPVVOVvNVOWTba5_50mc48_RHWlr-zY-uSRECWyoHSipjJzyt-93_I-_wkGQGvbvvJbjYEDRxkkTEqttqENybvVJI2pulBt6UlMieUm6yDHSp4VCkt1NyUWUX24UbVfaf51k6kGRay4dQlkYn22tPoS8vYvan2QDtRCm541PrMZLe8aoxRu1fcAg-KabX1J78-mqr3rZ9fqZ-rzglWL-TBtqYXnJ3TtpVsmdFD2dgh2-AvkVE3KD1veF1M4NNmMlnHp3OBdKfAUYrKz2dlUnETSYk1QS7jYUkz1dVnl2rAU50RYD-BuzPJ1O_11Ba-MjbOaul1uSwicGS83qs48WcESvqBIzqRFAI621Rk-DENqUC90RiDQIz9d55fbmlQbbL1AJqbdfZDsUQyMZfAU-tF38TfjTVt565wdd2C_Gv5ffpvTdbb_92kLGvTw9CPr4BzJ67hfFEBpKFCFfXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501b0b150d.mp4?token=Ktd9I1WpcW7BKd4z_Zh9APOVLmDtmuPK6EVou8smEdGhCKan3oYeJUPYhUhXYzM6g1e678sYnIrI7SYkQEppPlGyVeTLxU2WtcroGsTL_8sgSCO4r4JMnLHbWnmaX_xM5HkGP5y5WixLe5fgQJqOe-FYhC5pXLjkP46BfnHizlhzy_wb6yJidACL5q6KGY0owxDRRnY-LV9EUou-P46baRH6FKPVVOVvNVOWTba5_50mc48_RHWlr-zY-uSRECWyoHSipjJzyt-93_I-_wkGQGvbvvJbjYEDRxkkTEqttqENybvVJI2pulBt6UlMieUm6yDHSp4VCkt1NyUWUX24UbVfaf51k6kGRay4dQlkYn22tPoS8vYvan2QDtRCm541PrMZLe8aoxRu1fcAg-KabX1J78-mqr3rZ9fqZ-rzglWL-TBtqYXnJ3TtpVsmdFD2dgh2-AvkVE3KD1veF1M4NNmMlnHp3OBdKfAUYrKz2dlUnETSYk1QS7jYUkz1dVnl2rAU50RYD-BuzPJ1O_11Ba-MjbOaul1uSwicGS83qs48WcESvqBIzqRFAI621Rk-DENqUC90RiDQIz9d55fbmlQbbL1AJqbdfZDsUQyMZfAU-tF38TfjTVt565wdd2C_Gv5ffpvTdbb_92kLGvTw9CPr4BzJ67hfFEBpKFCFfXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی بعد ۱۵۰شب کصخولت در میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/138585" target="_blank">📅 02:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ارتش ایالات متحده قراردادی به ارزش ۵۸.۶ میلیارد دلار را به لاکهید مارتین اعطا کرد که بزرگترین قرارداد تاریخ برای موشک‌های دفاع هوایی پاتریوت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/138584" target="_blank">📅 01:52 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
