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
<img src="https://cdn4.telesco.pe/file/I7prIQhZP5BTnu9NtgpCwpYH1GDZ4g8EfQJIH5pYyc2oW0O6oT748SCbD4kdRIaEjGI4rtZJi0tTIqDS_Kce074OXnNSaNLTC8yVu6jyNlk0nsYT2VZonRmsiPEe99rJXGfNQvfpGXGM5B-oqUh-tbjtDsQe_kZ20Z-FVle6UiueyE6kWcNq1Yb_wVLxcRLhejESMxWjnU4JRkaVytn3wreRtxTr5m1KZCi47WnVjrLVAHp5n5t9Ks86KkcvOD0Ja6b8yOTOmvMI4KyianF59Dn2LNEoqkMc6JriFUz9l9WAJixufDoqiZoVVBTFzod9bWy99zosvzWjbpBhgsUO5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBBVBr7pehkuHfBntN6Cf3uOa9XmiEBH9gCA7McNOEPU0flqxBR88erj0B0WSuSsiH-MjMCuga8KUxjtN-pD8KO3C8vbxHn4y4a4LI2pVpOounlo-2MzoDbjO_4WttK4gCQw3kL7i4nEo1xDGQKdpHYMmHPHK5eY4I9vSIFKL355gTgFvxCTwi-RvisZUCVlB7D__LwJb9NWWHQx8ZBvxlcUwzE5ZKML-PFJrHzMNFCZeqyVrI3bJ5m4W4wPIqbLfehAxI-l2a0cfngCgyCkYKTJtsABv_FMYTBOvD-nwIWLMaT2cjGqsgRLOgVx7lBGrNLKATBJZjLGuy15RnFCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIcqPGj-aCSTfq7pLBgh5dntKN8sm0jHKlAMjoyGKsAjQhQDoze7QnSUO6TQbaq_Ynunz9EGIhyna0sKpvN9eqRG8bg6ozCzYxDnacn2Z3_WOM654o9NcIoKtkXXlwJq3JrG3lENQajQxNAZrS2s4krzvsoqVmhfjT4zXnUkrhxq6ZMFlPqWh5PwOcqWQwfK3-FN870D-tD660iLmEpa_slvkWhbnI6BA_FUaBjHFiJtZiyDbeqiy3KCLezpmoyYUogiptZIdTSd6D9933Ux_9nvVRt-0dTzi-lcrWU4mPhiTbJZnpOnB5PR3NPb8BnB5fi7T9LpYwzXA8WH6lxAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ridyQfrhsInQTZafCeiOHrLG3H2Oadj7Ql01cK84o1s8fv5ANRyFBAlQYsEaXqMk4dWbV_q--W8BSVjDyDjU3AIdutstHREW1y1pCDMK1bFuz3SrwoTVV_h8VT_D6ufDUSyznLPcj341zgVzbT3SeHfYxaSf0kqw2zZ-gH9S-8RRoobcv2u_6xdQ5POPNZOO7g72kM2m-6TKv53V1GE1o-xwO7POENdrOS8tPLZ5c5c57zjJ7v-BKMMhaWHAmnobhU7nM32FEmgNic3KgHK-9T6Lnwgd5tznGqjD42sg5zPRz1G_a50IZl1aSvF8DENU6XKdFpwtyjr7TyMN14LdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=upE0oUHVJ1IJyYCgB1OkgeolAxf-QD1g-S6hBWWRV6OBlBq6oZKqHQgALCrRPvbeck_idA-wJN5UXJM4raRUEVn7oo-plCGJTqlIe3RXd0p376Al8XHwd_QV0hB7ovnPZuBSAXv7zUCfI9eyq5WxE2MxJ1MmDqTvVgU-gN7RBJsLMtKrVIUPk-r31oiIme3UZBIOa_HumGgE2gO0OIyqgyo5pJn-crBZ6aAdTuUnHnQ1AyPaTL1DkZ3kFSacnp97IlXpCWuvI4_I_ugVFStGIVXbmHdlXiRJp7i5CjOO0KFWUchIXnglxD4FSA9Bp79tvYzpPTjeKq0m0WFKg42QQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=upE0oUHVJ1IJyYCgB1OkgeolAxf-QD1g-S6hBWWRV6OBlBq6oZKqHQgALCrRPvbeck_idA-wJN5UXJM4raRUEVn7oo-plCGJTqlIe3RXd0p376Al8XHwd_QV0hB7ovnPZuBSAXv7zUCfI9eyq5WxE2MxJ1MmDqTvVgU-gN7RBJsLMtKrVIUPk-r31oiIme3UZBIOa_HumGgE2gO0OIyqgyo5pJn-crBZ6aAdTuUnHnQ1AyPaTL1DkZ3kFSacnp97IlXpCWuvI4_I_ugVFStGIVXbmHdlXiRJp7i5CjOO0KFWUchIXnglxD4FSA9Bp79tvYzpPTjeKq0m0WFKg42QQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=NKypW9aFiG_YfRgv_z_rkKSlsNd3OqcZX5I8SUBZMJZMZ7vglrnnkZMiGd1nAU0VOYdZs2AXWTbRpRmf1V3qiLNBmiJXfNvbXh0JK4I3XqA-nCbSEp0CXysrv1QR_XRGPLLe1p1-J_8y8tzSE0dIpwwRJO8vFhKJ1wS2dEQ_XBpYw43klL_eWe8hiozfjPrpuHeegYPjk2ulU1VOHQVfUZzzDWRaAlCrAg6JgzWC0VbfC-kgHf5Vyn8gz0IdRvOrJBwocxIfyajETGjwb6Nwx5n3uDz5mZC-cpcFHHXZ-xCtWvKlkIYNIfW4BelG1mg2IeGCLj6NJxOqzavDEzGC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=NKypW9aFiG_YfRgv_z_rkKSlsNd3OqcZX5I8SUBZMJZMZ7vglrnnkZMiGd1nAU0VOYdZs2AXWTbRpRmf1V3qiLNBmiJXfNvbXh0JK4I3XqA-nCbSEp0CXysrv1QR_XRGPLLe1p1-J_8y8tzSE0dIpwwRJO8vFhKJ1wS2dEQ_XBpYw43klL_eWe8hiozfjPrpuHeegYPjk2ulU1VOHQVfUZzzDWRaAlCrAg6JgzWC0VbfC-kgHf5Vyn8gz0IdRvOrJBwocxIfyajETGjwb6Nwx5n3uDz5mZC-cpcFHHXZ-xCtWvKlkIYNIfW4BelG1mg2IeGCLj6NJxOqzavDEzGC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=KfveprG7_sjfh9BSL1OCvH2Z6yYyqN8jMUjh4SweBmXz4K-D9TXZSZ4hVrxc9OhlqhilvWlgsvdQK8ErdKO68oxUOeT8UPLNVGKENRGECUGVY4U73QP6YDXmsdUYky8MMWGRXd_2_goJX9IfLj1SDeATzifZBOE5goCxiOSLoTLdLUTmU54j1ajf1r828bgW6Eao1LyqYwYYEIz_odlANQLA2PAB43tUlJYxbENQ7Sy1cuqNN-skY546FgNyvdouIjrekEIHB4ACDOcDPMkKpZxZAy3LEKM5cAt73xC-WhxGkzWD8cgbhnnut5WE1IXaCUUAdIRRFUmFwQDCN01AzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=KfveprG7_sjfh9BSL1OCvH2Z6yYyqN8jMUjh4SweBmXz4K-D9TXZSZ4hVrxc9OhlqhilvWlgsvdQK8ErdKO68oxUOeT8UPLNVGKENRGECUGVY4U73QP6YDXmsdUYky8MMWGRXd_2_goJX9IfLj1SDeATzifZBOE5goCxiOSLoTLdLUTmU54j1ajf1r828bgW6Eao1LyqYwYYEIz_odlANQLA2PAB43tUlJYxbENQ7Sy1cuqNN-skY546FgNyvdouIjrekEIHB4ACDOcDPMkKpZxZAy3LEKM5cAt73xC-WhxGkzWD8cgbhnnut5WE1IXaCUUAdIRRFUmFwQDCN01AzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=fO5L6gncvLGwaXiMekO3KP_Cv3tqZWXs5VVOou_pUqt6ceUZmRYbXl4gHPNZS5bcfLie0tiNmrpndJNCM7LZwPqPfM7WcRdkHfT5oO-AGBwN-omuODrBiKfjaAj6puXsc3MQm9wuoNyTCSJOPWICm6OYGmfI5YHb5XDcpCbueV5lh_IMwW6cbfzMAnRZJG97MTThwsKzcJS2A5C3C4TS6dzNEayrgyhI-JnhQ9tB7m88Z5OnAKYcnO-NWy1ZtWXydV0bUZnzKwCzheTkISvjlDMtLe_f8QnHJt9_NL5VpncLVlKjeVBBN_TT6c1QCgTvoOEeec5CubrPm9K-nfkyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=fO5L6gncvLGwaXiMekO3KP_Cv3tqZWXs5VVOou_pUqt6ceUZmRYbXl4gHPNZS5bcfLie0tiNmrpndJNCM7LZwPqPfM7WcRdkHfT5oO-AGBwN-omuODrBiKfjaAj6puXsc3MQm9wuoNyTCSJOPWICm6OYGmfI5YHb5XDcpCbueV5lh_IMwW6cbfzMAnRZJG97MTThwsKzcJS2A5C3C4TS6dzNEayrgyhI-JnhQ9tB7m88Z5OnAKYcnO-NWy1ZtWXydV0bUZnzKwCzheTkISvjlDMtLe_f8QnHJt9_NL5VpncLVlKjeVBBN_TT6c1QCgTvoOEeec5CubrPm9K-nfkyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=SK22HcmJlcSwwEHByOB7AAih6nWPXFs6mEXpvPDgVBdLEP3cviPeKeS2mJVuhTnbDST21kph0w45zPopWJHbD0D9eJYNRQoHnaC8uUxVdxlCf443CtHg3CxCvZTf3H1R3xQhrycVIJp9lUx_4mU3kJ58dWRuQe0o30Ia9-4OsI8eHl4rvcCrDcEmXCmGsdX-7PFMTw8wsMKi0lcPFXSPDbb3oXV-jIVzMTYQEWXiGUZtnbV_Rcuj-kigwsSayOHsiTeYhgZ2BDkCVpcUVX40G5ZXISheMoM6RavpaWG1VYJkcNbrrSmCiRSmN0YX8l94ZeT4Qj7-pd2_0S958jLJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=SK22HcmJlcSwwEHByOB7AAih6nWPXFs6mEXpvPDgVBdLEP3cviPeKeS2mJVuhTnbDST21kph0w45zPopWJHbD0D9eJYNRQoHnaC8uUxVdxlCf443CtHg3CxCvZTf3H1R3xQhrycVIJp9lUx_4mU3kJ58dWRuQe0o30Ia9-4OsI8eHl4rvcCrDcEmXCmGsdX-7PFMTw8wsMKi0lcPFXSPDbb3oXV-jIVzMTYQEWXiGUZtnbV_Rcuj-kigwsSayOHsiTeYhgZ2BDkCVpcUVX40G5ZXISheMoM6RavpaWG1VYJkcNbrrSmCiRSmN0YX8l94ZeT4Qj7-pd2_0S958jLJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyThFtJs6oWSP2GuJvrZi4lI0nTUUzFun8EvFVR7GFvUl5ZcufzOosoMn9MuQDOE0eEaiqHjPC7K0ZxwSVRDCuS9K4EBu0e56q_zPr8nVH3lTlV-7S3PAmO58t4Kga-9Pil4es5aptIejrSSEBHKMDEg0TMc4DHmP5e-Bqr7Yn__s487Drqj0tkHKG_ouJa5AhbyiPqVzPMc5a9gCYHXvH7p6DIw1zHYHh_MtFSXw6HVugqHDhKQ_GnhbiqVbu8QTpJ__s1Qjiir1tlhn5A2M_N7WznLDOMBcA6So4aS6RJs4mdsjZ0NiNugYsiH4Kh8wtUVekSa4liZWC2j2nI_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVgGDOEyIWPTMU6VWJEvdv9kJTpvCgxDZZXmqwzSHbOyXo8iRZNRHCyqxn9AhPYHWoxKYr66Sx1M_LcqY8BWtRAs6NTHfRYjQkZHKnKZLfahs-DpCunnt7GykJGDYeLGqveZhuz31N2LbF6TrzKOzVPBkAj1JMm07xOrXL66xE0fwzMzw485DKNnMcDgcd5xkDkD2N3P91g0KWk_VaiDmQi2376tmaOuFtNUSoBYM-wVkEiYc0gMbqdKuPjNgG5uzeAzAvbpUxKO_MdpJem_dE2BjhBHSk0ffCpPq7nYJuXvm_DC9vLChAMEBjODLyq3QgE1U1v2Jx5lJAWVsFwb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HA26e_00GHZSeB56cqYePcK5z1Z0vGewfDoezZhjyqEM7ibRCxQzUVYZGhCN6RNXP4w_WAoekYw3nQOTX5jBAAlf45X7izRJefZH8kdsNgd1X5sW_rGN-dnSx7MAhbNlZUOpv5jrwV2zAiLkJwyRvqH9RqTv-fBH65VG68kFwDxe2jO4roSlwqr7PfOnYZJ82O7VFY3QKekUR5tux-6cypWXJS1I-E-4uoQUxh-ulGROpK96j-azZ0HeIEPWiZ0BM9WddJQUhOL1yjkRTIgb80g6oc1o8XPwHxO5oo5wIWJ2onb-Xy589uTdPJRRyJeXUDI36-HOr4rES1GGBPdT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMXjK69jv_6QlGzE3gY8WHQYjzLWXSTBY2M7jO68dWR51MfAXZq0wXGI0ubmUWQSO1LyLIopizZ-XXkGf446gXzsDr22Gh03HT1LHTXxuxb-Oq_gqOpK_HHexGy_SHVCIzqi1g5fsWxQQBUfvftnYRsGiHKAmhzm0yCpgSqb9O5jAS8j4_H0zbtXWpOJqHDakqejm9-HUgA5bBoKF6yC6H8OhxLXcBrfRmEOCONCdjrDcs3aszlf-VV66XDwM4wrt3lCCbSQvbBxleef7uSlWkrGXENMQVcLzilGvIcrlAz1X9h8wHlZ6OSsxpYmvb-q3K9yG7EK6uITqVoE2iomyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=Q24n-pTxQ39qWwUvIHiZWgyQjfgkdt5JW0VqJFtFDkBuFpZ2XsIEMkOXCA-ssEm3G4IkDB5ajK1rOVho_-wSQ3i7hgUXXKbSUUdqO5B6W6DAJctG4BlxcaoUgKLxek5Sl3qu0RqKc2d3cGmC8ybeon8V32atGsPcDSUD3-6ECt99U0kVzvPE8524J8q2rIRwVTYpzFbtg1cmvJm1FHcHHoXpxSRKUvLqjqqLUHvef865FiaNz6OTJn9mooDuncWKO0r5ae5czqfthaCZIk_mURpyfx4x4uffrcz47OkVS65k9BjNtGD_7C36zdsbznKcYCNavkIbt5-jewYnsgpCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=Q24n-pTxQ39qWwUvIHiZWgyQjfgkdt5JW0VqJFtFDkBuFpZ2XsIEMkOXCA-ssEm3G4IkDB5ajK1rOVho_-wSQ3i7hgUXXKbSUUdqO5B6W6DAJctG4BlxcaoUgKLxek5Sl3qu0RqKc2d3cGmC8ybeon8V32atGsPcDSUD3-6ECt99U0kVzvPE8524J8q2rIRwVTYpzFbtg1cmvJm1FHcHHoXpxSRKUvLqjqqLUHvef865FiaNz6OTJn9mooDuncWKO0r5ae5czqfthaCZIk_mURpyfx4x4uffrcz47OkVS65k9BjNtGD_7C36zdsbznKcYCNavkIbt5-jewYnsgpCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZr7BW2VKIck1gbmqMFHVzYSxdf6Xqd1rmCn_nGLcuF6YbQxrk_DxCbQ7y6oEh1Y8XAhxzKcnSwqZG-Jimz55XOKep-Hkb01ZyykIIqB6DFoJgMJyosB7N7tm4fC2TvzNI1h_tKNZH9epj9eq2MtdQzqESQ_f98pfRC0MoZyAZie_-oTrU0fUiW1ocOAJhAIasauxq0w1sR7CMEpkn2BZ6gZSbQEoeAR-6oeuXetvevcznyewyWoNcFGLNV7gH26GxhyfbLNgIyrLKS8Nzlh3atxbN_VI5eQmYQB5Hvx5FVm8uu1i88hidfFN9ZhdHjVM4zzjHvib1SsHhmcUC8uqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=sOv47CbjaAClL4ytZjlJwcfuRtYJOZ9_BK-KgPWkx2Xu1dD9tHkDltvDqhyYZCnPnsL-ae8qEHA3j5KcnBCfTlgS1rIrGHZG9SsJlMeFCb62PcR-1qQPFk_y4hGLBmhiF9i92zit1ZZCx3q0GkweZEDUwCDvaMNbZ9W8Gmu79aGUzcgAsB_-eFP4eBn4HWNsNaYGx9OsuQhCS1DmUe3yCaQbDWXXhMXtlNd8v4J3VJfxOT8m9EDpGrGs1p7vqA29iMnrVhTGcSPT7URYAx2yllvfRg_dxuIgUh1_jylO5DaEvETiS_uQyKsPrzM4Azvwg55wcfgbL40wv7D6MhijPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=sOv47CbjaAClL4ytZjlJwcfuRtYJOZ9_BK-KgPWkx2Xu1dD9tHkDltvDqhyYZCnPnsL-ae8qEHA3j5KcnBCfTlgS1rIrGHZG9SsJlMeFCb62PcR-1qQPFk_y4hGLBmhiF9i92zit1ZZCx3q0GkweZEDUwCDvaMNbZ9W8Gmu79aGUzcgAsB_-eFP4eBn4HWNsNaYGx9OsuQhCS1DmUe3yCaQbDWXXhMXtlNd8v4J3VJfxOT8m9EDpGrGs1p7vqA29iMnrVhTGcSPT7URYAx2yllvfRg_dxuIgUh1_jylO5DaEvETiS_uQyKsPrzM4Azvwg55wcfgbL40wv7D6MhijPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTQCJ9epCBS4U4jSLg8q2C2SQ2TPDfuDK4ibeS4n4WdSgKJ5j57BhEaBRWujmRbF1Z1c99rssjONY6rAwS6ZX-mv7BvjlWI_FgpsrKqlvd627yFZVlb62Y-NHoNnLLR8OaLVwNAgy9R5FFcNmblEuLRRJf55xQeSZPZQxBDZ1fz6b1VuBBgi8lHVOjKXqZpE_0AYaibuMUP4g4a8xXgk0_I6lvYzWXHO1H1eWWamudSQS4r29t7SHpxHyElAoiEfwDSZxyT-l7vdsXozZ15QmmL1YS8TPj_rmRKRCI2KYJ0P-riHaSEF94aZQpDO7LNMj2YTme4N8USsbCi5BAxfhuRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTQCJ9epCBS4U4jSLg8q2C2SQ2TPDfuDK4ibeS4n4WdSgKJ5j57BhEaBRWujmRbF1Z1c99rssjONY6rAwS6ZX-mv7BvjlWI_FgpsrKqlvd627yFZVlb62Y-NHoNnLLR8OaLVwNAgy9R5FFcNmblEuLRRJf55xQeSZPZQxBDZ1fz6b1VuBBgi8lHVOjKXqZpE_0AYaibuMUP4g4a8xXgk0_I6lvYzWXHO1H1eWWamudSQS4r29t7SHpxHyElAoiEfwDSZxyT-l7vdsXozZ15QmmL1YS8TPj_rmRKRCI2KYJ0P-riHaSEF94aZQpDO7LNMj2YTme4N8USsbCi5BAxfhuRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=dJfihuujoju1E4Plk2LPfpbyDhYz9GBFens1JEs1fEEkujzlHyycHijZ_1gITt6gHU8j5Ew4ZPvXKb7FlhqlB0xxUK4uk8-IuJsAUfh-pH11wpwPqE95qPlwn-VB67MdMiu0asoqJus-aNO2HbibO9_l3O9kV5sLofpBm_OQ8acA5ngQtk1-ivTW_tyaCIuxkqEkRXC0fEtmP_yCWZzhE-EejVAr9TiLlngg6ysre6i7HK8aZJ64lfe9yLrpfXbzw03_jgar1Z8AXe-IAevJhnfa6rZ852waNCbatk5JVVwYknKwMYwd-8KqwEYuH5MIv1YQCAuZU5tGHG7c5HR2OYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=dJfihuujoju1E4Plk2LPfpbyDhYz9GBFens1JEs1fEEkujzlHyycHijZ_1gITt6gHU8j5Ew4ZPvXKb7FlhqlB0xxUK4uk8-IuJsAUfh-pH11wpwPqE95qPlwn-VB67MdMiu0asoqJus-aNO2HbibO9_l3O9kV5sLofpBm_OQ8acA5ngQtk1-ivTW_tyaCIuxkqEkRXC0fEtmP_yCWZzhE-EejVAr9TiLlngg6ysre6i7HK8aZJ64lfe9yLrpfXbzw03_jgar1Z8AXe-IAevJhnfa6rZ852waNCbatk5JVVwYknKwMYwd-8KqwEYuH5MIv1YQCAuZU5tGHG7c5HR2OYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=vjBH-v5L7KGzL06FAkUEWe_7wpbyIyeOQfKGAXCRDSZN9GQe7TyLSWraFjmSFj9U_IyDT_03GgjvcNxYQ37DVTZ89Jb9YGBYNu5cDI_8TIEXcnEgmbiNGBWCamkTpChvFVGvrqUM5FQT790R8Res8nkGtXi6bIyDVf0go-r55pfLKdUrAGwa-Pdl8mpI6t8V_vGwqkHApIAXYrz3mCng__QpRdWhdfkOprX0h82ZTo_YrlBytwnun-uLqoNzJAoKRl8ZfSOi-kaC8PKLqoCe9L-xExVZzNBqX8KmkGYajZOa1moQLd4RLIe4AbCPicYEaMPjeJMBz4oCWG1IxU1f8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=vjBH-v5L7KGzL06FAkUEWe_7wpbyIyeOQfKGAXCRDSZN9GQe7TyLSWraFjmSFj9U_IyDT_03GgjvcNxYQ37DVTZ89Jb9YGBYNu5cDI_8TIEXcnEgmbiNGBWCamkTpChvFVGvrqUM5FQT790R8Res8nkGtXi6bIyDVf0go-r55pfLKdUrAGwa-Pdl8mpI6t8V_vGwqkHApIAXYrz3mCng__QpRdWhdfkOprX0h82ZTo_YrlBytwnun-uLqoNzJAoKRl8ZfSOi-kaC8PKLqoCe9L-xExVZzNBqX8KmkGYajZOa1moQLd4RLIe4AbCPicYEaMPjeJMBz4oCWG1IxU1f8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSDeMxQcbFdLP_olH4g9Or9B6N1RQ1F7phUbzEAea8D0CDLcSCdYIEg_rMqO-ayFjECwJSyD11iemkimgP-NT9uJ-Tvl_o_p4_PChr5sDIsf2GEEGszU4kVtxI0TmraCJW8De2dFtmYHeVpeZZKKm7qb5WcPI0s4j9ZI2-6pdo7xolUWUoOXwEzRPXOs9ehoVnv5XPsecGuAo7MN3STC54ZGU9Z4I6oUd-Y-VvVyNmyTAmse8Ua6ACCCNQWhKZsU1NOTYiERZxVyHiriSCB_3diNxbltRiuD7s3JlkN5zcDrCJ_y7HQADYyhep6dbBMVXcVjdzc6w60cbwKpQsOCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=Au3bobJSnBQJ945iUX0r-mGKgNBqtvUsvbTjY5xinn9iJ9cijweer9VGFDskqLOoY3H-Od58HLV-f-cr4z_kFfqNn3xLyJ6C-XKqpNHjdJRQNHO7k_G5LOcb0ok36i7p78DueOzW8OaEWO4S3KjgHA-wkHes0M9Q4Yu_6n3dV9PjZN9x11Gs_eppwJYkF6B6KqUbxwZ1ciwzglNhxvim7BPhy9tx0f4PME39xMokKdMGVcqQKVf1iRu1DwEaSLf0MG5TvhByU6LXYLR-zB_A_u95lEmkPRtu-BXcQjDOd7oJ1ZciRA9H26J_Cr5Ue2GrrasNjqwk1qQ617U9JyKTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=Au3bobJSnBQJ945iUX0r-mGKgNBqtvUsvbTjY5xinn9iJ9cijweer9VGFDskqLOoY3H-Od58HLV-f-cr4z_kFfqNn3xLyJ6C-XKqpNHjdJRQNHO7k_G5LOcb0ok36i7p78DueOzW8OaEWO4S3KjgHA-wkHes0M9Q4Yu_6n3dV9PjZN9x11Gs_eppwJYkF6B6KqUbxwZ1ciwzglNhxvim7BPhy9tx0f4PME39xMokKdMGVcqQKVf1iRu1DwEaSLf0MG5TvhByU6LXYLR-zB_A_u95lEmkPRtu-BXcQjDOd7oJ1ZciRA9H26J_Cr5Ue2GrrasNjqwk1qQ617U9JyKTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=cVpmZ0qJ7A64GfuEZDPtMnZW4Uk3aIXT_btEbILUZ6Ezcdq0qWFxIpv0As0mJuzwVamo-s9NrwjEyu16ldTaIuqn3GyHgQs-ZX7D5NGZh9ceWZZ7IspD1mtIjxTyXETGjrufWFbxt1rl7-mLaIPoZ9U1_jvCsliBsSvhNCNkd5N_-nUBHp96PIUZD5i5hgRGmJSbJYsPZemHAJ5yP4Yp9zAX3MM3o7AuZ9VPPBgYlzn00WqWq15Yzag8WuGf8u3MeiTpjzyCmHZ8S5wYZ53sTX1ndx5bD-OQU4ZPoWv_9gLgRl4JqnAXuEFQRUKDBFG6U80jWBh-E8VSJ8Egf6b8YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=cVpmZ0qJ7A64GfuEZDPtMnZW4Uk3aIXT_btEbILUZ6Ezcdq0qWFxIpv0As0mJuzwVamo-s9NrwjEyu16ldTaIuqn3GyHgQs-ZX7D5NGZh9ceWZZ7IspD1mtIjxTyXETGjrufWFbxt1rl7-mLaIPoZ9U1_jvCsliBsSvhNCNkd5N_-nUBHp96PIUZD5i5hgRGmJSbJYsPZemHAJ5yP4Yp9zAX3MM3o7AuZ9VPPBgYlzn00WqWq15Yzag8WuGf8u3MeiTpjzyCmHZ8S5wYZ53sTX1ndx5bD-OQU4ZPoWv_9gLgRl4JqnAXuEFQRUKDBFG6U80jWBh-E8VSJ8Egf6b8YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن‌
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=NapjnNwUhgX29c6Nezq8oVQ0_gBnsa90RgbS9GxmpUM8qzA1oKnTCU1fSRlJJYuNz11rGEYvV6TNYWruPcqW8Umd95BfMi--T3aCX7O8ILU5TEllYsAqBF1No9RaZSQctSmsEiRR37QMwIQ0acAZxNhULoKmRgR6yS0YLOXyE341q-SkS0hvs53JfqTMRB4CHYQOvF-z8T3xUOB0M5BT8VAZeCAECAojoWvU8GTVGFNb-S-jvguDf54pYm9gZPI4yu5s2MpydH1tPjfNwd4WfQ71G-jDykuZmdQyOERYy81rViY2Cpacy68eLC_x_f664DjkKpoy0cm3vTTH8SoZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=NapjnNwUhgX29c6Nezq8oVQ0_gBnsa90RgbS9GxmpUM8qzA1oKnTCU1fSRlJJYuNz11rGEYvV6TNYWruPcqW8Umd95BfMi--T3aCX7O8ILU5TEllYsAqBF1No9RaZSQctSmsEiRR37QMwIQ0acAZxNhULoKmRgR6yS0YLOXyE341q-SkS0hvs53JfqTMRB4CHYQOvF-z8T3xUOB0M5BT8VAZeCAECAojoWvU8GTVGFNb-S-jvguDf54pYm9gZPI4yu5s2MpydH1tPjfNwd4WfQ71G-jDykuZmdQyOERYy81rViY2Cpacy68eLC_x_f664DjkKpoy0cm3vTTH8SoZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
«موسی غضنفری آبادی» نماینده مجلس؛
فقط به خاطر این کلیپ کوتاه ۱ دقیقه‌ای از «شاکر بوری» بلاگر اینستاگرام شکایت کرد و به ۱۳ ماه زندان محکومش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caYcdU0_WeXdhN9JaFX1mvJpW6mqegD86HH9jC4Ih-ve0FKAO5ll3RfUzHsLG672QS9AcRk0esJUZf7zQqvugOJfznP9D4cgQNri5BjtQWL51L4S2qfZ2J9ltS67OSPhbuav2Z73XNIUXcW9An8fdXErIDfuNNWTMR1p780sviaE02BZESRMrHCFsQSt6vmMr8njxDgbtqKeC99v1uMFXqZWc8prdO4GuZx_wNvSUc9q9WBtJq8GxVi9yGWkd5LfpM2E_tfAPZlaEkIt_8ojK2USSpwk9-LfDfjIzzHTYA1BLRqcs9t6pRz8LXvNdmGbR-01uvknOelkkOTHOBzyAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAiNYdmyDj4p0EB1cCFd_B36Ge3IdZB0aG5zWbKvVIx1dTA_Tf6SfuuFYf1pxKA6_qO4ykShaaXQGRF8_r5TJf4AOlb4lVcycSkG1pomECea2wvmn7Eiz9qvqIDi81LNb1fDuA5jMEuQK8zciPBGVE9bIvweaRV7xTHqeFgcnWB2NBI7pQU0T40Fs9zs_BS9mm0S7G5knno8wnQ1IEivNSbPBrO7hucy9ODmhKsEMRcKa0bqTzFaImv_cnx-DOr3syh7chY6BBhGZOoDi4dkHNF6klHf0RarfG6f1bIewO63JP34fB14Bxbo0zFyKnuSKqz2ADM1monrdcmv33mnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szRTZSTrKDLAw0mMerbNyqPRzc571M862qIXkRZyoPsvt1sXxJYV5NELEVZTNvCtXRWZ2blE31hCmIjsVjBg12EMt3t2Ijtt08nRKLQkC-HW5V1VJ8vhW3UIQN_87SSlZ0JrdLpkBvveHdPLrmCKR0a5-MyfGQD1DBI_kq-wjKmqrGehkGhf3x1awLgAoU8FTldzi6ewFtA2R0cYelZrUO_5sxFLyH7dI0TLPuv0juVKYqqouzZjP0RHGOhkETuJkpR7ubdWHoFpt_LT3y0DXsUFaHM43H75HAC9lzjCthxZ2_heC9f2YQ5r_rEvpYbxgjPr8PXULhcBvtU85MZb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5Lk6n7UH3IiY-l5ItRif8WOhz96T5Z9s9oALjRF0osuNo3z-3OkMN6dYjVPxC2lLXyMVNVSsZ7NkxCUlGeXIi3Ajbh4pVkGWxWozVTqjSQuilerpjyWMMsBxzsb0Xhu55Q1iJW56_8nfEYje2JZRs35_LuFMH8zHnYcXrks0A3sI9A8KNBzKTO1b5vR6AZkovUc-zBNN4iom34qlxCVxKIURkzgGR1CXWKZVSf8enO3syFHPaeBms3KHIHMR4SnGxn_q3b74jzFSLDvP-6jL76EiWeQ_kKPiKvbQDkDNVybaovPjq9R2xaAk2QhYaZ1KuDLaUFTFQSWfN3SWcyUQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0nNbnxcQV32jH-RRnfQTS7DHvmGWgty4hymNcd-GxLJLC3IJoAu2ybPLuUAwwjiBnpuLtMiAUiiV-_04qNYhEmUmRTYISwiirmWKMPD84hIXBwXCQI04_VWIPr7g70y8FmA91SsbAoTpsPIUBPY0--pFUfLHd5TNaeHYwYAogCNqzdKqJQCBE1IBONGnAJjSc8aLfVF4ebZXLTijZFUQSesE59cUoA5-QHVUcCvz7Edc_KM_56cXqmJ2bLn7LMSdRObXp4DQmZ9xTr-NwkPxCGgE1ROTDtKxrk_JB6vWhWcYrteCcjrPzKUx1tYsTqh3-Xr8S5XJKYQimHRtOUicw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=WOPMS1eSYh2Uujz0RzIFJpE4CUFeAinjfp48chd3VtMYGFwpg0yMb1TE5LZf9kgva-VIMIxSwkBrXZEBWvL5Iihb4I2XiLBBsArFbAOcjEGAWTsjumGRd_C-S7AKAcxUsgJA4V8vxUQ4zF7wpSOOdTWeUkSV1SYKKytfWBTNvKyPAHaI1OsmL2i2YzA4c3cwaoZ6M-0ch2VbKwM_L1JHHTdF-LUrC9Y-Clha4wiOQCS7h4RpTxE-TZ9jBjJauZxvSm1WcTBH2aGCnsTFRCUIVWbt4Ejg_r5l6GTesKZkhgFmDjIhY-C6uuKzFrVotkXeObcE-b1FUsclRHd3oR-OGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=WOPMS1eSYh2Uujz0RzIFJpE4CUFeAinjfp48chd3VtMYGFwpg0yMb1TE5LZf9kgva-VIMIxSwkBrXZEBWvL5Iihb4I2XiLBBsArFbAOcjEGAWTsjumGRd_C-S7AKAcxUsgJA4V8vxUQ4zF7wpSOOdTWeUkSV1SYKKytfWBTNvKyPAHaI1OsmL2i2YzA4c3cwaoZ6M-0ch2VbKwM_L1JHHTdF-LUrC9Y-Clha4wiOQCS7h4RpTxE-TZ9jBjJauZxvSm1WcTBH2aGCnsTFRCUIVWbt4Ejg_r5l6GTesKZkhgFmDjIhY-C6uuKzFrVotkXeObcE-b1FUsclRHd3oR-OGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/seHAG3JeusB0ZE0ipqSM9xhc4YcgA477ZDtUKVtfZ_ffdN82VjV-KLByvfI6lOFheg79xYxyxH9WdBxCFlsxo2o2D8ydkY2z3lMyb0wbS_AuXDe2tCRHZ5rBZv49D8Sy6v78Ui4TpxssTDa_MRo8PUItiqo5mqSYiWlQ2o8zFQXCuOcebSf7tN00YPJ72kGzQ-QTGn-9Yb25X88_MTz_sL1Bb5bW1kzxDYvlQrai2ltCB6z_TXMJRevGurVyP7THQmD9na48zxC4W9FIP-39VC8IkPeD8QkUqPYl1Vi1_NYf7kZOiWo_DvTXfjyPzM3HQhjBe2FXz5LDSZCmMbhf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6GrFEu0vL66VlToqaNBSkfMfnFMIP-dQXWe7Hpher-0VBy6clkIumv2OwGOAl7OrHdfTwEvKeYr3XMS2ERuONsoRwdmjxeUwSc0NHoHPgfg7EbUlhTILl3-HAmYF97pgYgnCjHRc3wwZGk2YUppxHbdQTXDWgk2FqJiQ_EIW7aC8Hn0zaElxIZQPj2i7ZBj-THebfd6hU3VYEm8DwjRZ3uyB6NUXUKl54RLoY5qYgLwLDbVHhyhl7nMXYA4jaD1N_QbZjNmXgeqLWeKdSUNtvVd3nCLn9wLs-K6CyOaeFMxPZKaIi4j1VkMXn1GIp5m82YWRVTWTeouh79xLpaPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TE5yPmM40uECXTo3u8hC4csBkTROhf59WSEY6ntE0O-mEiOBK_u0OxlvWeia-2X5s8UXOwtw82ed2Z67zFZebd0-Tviz-0rFC3JdQWLGP4TNPZ2TKshqxkUicgira_VpCTwWywhNo2GCOU-RBo_UOdDUp33hX8TQ8bjoggK35_6_C2yuilbU4ST6lu4QvW-ajmhQv4sXDbB0k5EhZgOQFSoWc5Y0kaZ2173Z6sAuabNc7lqZAtCNIwAJwhtRX-1Q3jdLzfCyC8TXL1r9jgi-Kt3a5iBFgvT-uVkTYCvYODtZ4l8b5_dCyTbzcPkqzY_i95_WZIZ9_bZIUqrfzDkrYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=mncAUwasxpijFZP2k1NL2iK-_RL5EiJuO6NWNrtlgqr3G9cFGX6uIFA2AT5FNnaTQzFu1hF-pMtj3jrXaYvK4jO6b2H5czBjzg5qKxT56QpWyhkUYicQGc5SqoOxe3689FAzXSBTrn3ggXgI00G0HIXHT0yJJ-sKa7ejdG1kWPpONjFEdbztRwtSWvN4CmhDYMkBNtRBvo3v9rwcv3kwtyIDmyW1uXqBJmWT8nEoOR0-TbFzDGGFlykEvmWMeA-p1nK9dAwWounPXGJNM_qG0hpyB-ZgNmNGj4Gpx49Xk9noxu0jmJNadqmE2d2JIzpxA-ecduXffD1LhQgwNItpIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=mncAUwasxpijFZP2k1NL2iK-_RL5EiJuO6NWNrtlgqr3G9cFGX6uIFA2AT5FNnaTQzFu1hF-pMtj3jrXaYvK4jO6b2H5czBjzg5qKxT56QpWyhkUYicQGc5SqoOxe3689FAzXSBTrn3ggXgI00G0HIXHT0yJJ-sKa7ejdG1kWPpONjFEdbztRwtSWvN4CmhDYMkBNtRBvo3v9rwcv3kwtyIDmyW1uXqBJmWT8nEoOR0-TbFzDGGFlykEvmWMeA-p1nK9dAwWounPXGJNM_qG0hpyB-ZgNmNGj4Gpx49Xk9noxu0jmJNadqmE2d2JIzpxA-ecduXffD1LhQgwNItpIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=V22rws7dkbWudluj_QvltTvbTtFQlp3bFoOWlolG_AE843BKBkeoWTWiEEhie4ElhE6owZa1ntC0rwC-1brY-1NZZT-6il0PPVNjfBslUI1E3mA3Q8zcaUFYzqbTi_tE_vheh8by1JFcuzL0HHGnmthSOCumCEouDV0PGOtbPnQPxaRTfnixhWq6Nkr7Y-Vkd6iyG87mtnVruqOKrUwSsrNmB5LAMA-iHaeWcZ3ebUF9f2rXP8dLn9XgXq1jYwDMdWIpajtnXOn33J4CzFhhR8WlK5MYP_RqEl-O8mxtZtk7AnOG_Yl-RP7sESndjhZ2OfuPss2Qam_a-z9XujRaXTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=V22rws7dkbWudluj_QvltTvbTtFQlp3bFoOWlolG_AE843BKBkeoWTWiEEhie4ElhE6owZa1ntC0rwC-1brY-1NZZT-6il0PPVNjfBslUI1E3mA3Q8zcaUFYzqbTi_tE_vheh8by1JFcuzL0HHGnmthSOCumCEouDV0PGOtbPnQPxaRTfnixhWq6Nkr7Y-Vkd6iyG87mtnVruqOKrUwSsrNmB5LAMA-iHaeWcZ3ebUF9f2rXP8dLn9XgXq1jYwDMdWIpajtnXOn33J4CzFhhR8WlK5MYP_RqEl-O8mxtZtk7AnOG_Yl-RP7sESndjhZ2OfuPss2Qam_a-z9XujRaXTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ6FHYFn7bhLUUj43QjrUvzxkCB6igxZFz6-VhMihqSLYs3tfF4FJwTa0UpLnO4hqdTg6TPVhrSbNFbSWO-qG2xrEVG-pyXt7DpKHcb1Fb4DkSBT2nPfy4T7jq1pd1RB2IXV_Y2V_VfPVSxqUv1ZKTrJ9QfXVfovrdupf3z-Ovrawxf8zf5tlaVfZpdLOBOKrG3WldBDUWmd3oRUSh9vqwoiWnbGq87LmPQFdntnGn3hzqsIeYlZCxJLaqH0ANUGIgQU01zwZqJgJu6G6ESqolwyHVf5z_TkIGT16kZRg9YNgkUFTUNCOxb0qDJ7b8T1r3_TlRjJm9KV64sMKGk36zeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ6FHYFn7bhLUUj43QjrUvzxkCB6igxZFz6-VhMihqSLYs3tfF4FJwTa0UpLnO4hqdTg6TPVhrSbNFbSWO-qG2xrEVG-pyXt7DpKHcb1Fb4DkSBT2nPfy4T7jq1pd1RB2IXV_Y2V_VfPVSxqUv1ZKTrJ9QfXVfovrdupf3z-Ovrawxf8zf5tlaVfZpdLOBOKrG3WldBDUWmd3oRUSh9vqwoiWnbGq87LmPQFdntnGn3hzqsIeYlZCxJLaqH0ANUGIgQU01zwZqJgJu6G6ESqolwyHVf5z_TkIGT16kZRg9YNgkUFTUNCOxb0qDJ7b8T1r3_TlRjJm9KV64sMKGk36zeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtkEmCAZjoQzlSvabbaWaz4ioEAh2d15MokRjKAD1AyD78JQ0_FYKBrdOmo0kBns5r-P53XQFVX0aezVCyZDXn3cYTqsQvZHJgzDEtiQNTn-WQ3VojNsw5XCRx5w7sea3beWhtybDml4AERH0H8Nef63Rfzb9-_ypsn4CTijiS90Nacvh2KH7XhU6V5i6pUC_bPOL2-nFubWmxM6i7J1O_f38TuuETpoNv35IADG3XKtzRKQGd8Z5mtLHQajb8KeQ1n0eOfU0z5LhGrp0kR5EGsXfjI5B8aLrVE8OtqGYKiDRIyj2wXQymK5eSZD2xoOuQPQ0mTIxe3VUFrSBnw-0-iU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtkEmCAZjoQzlSvabbaWaz4ioEAh2d15MokRjKAD1AyD78JQ0_FYKBrdOmo0kBns5r-P53XQFVX0aezVCyZDXn3cYTqsQvZHJgzDEtiQNTn-WQ3VojNsw5XCRx5w7sea3beWhtybDml4AERH0H8Nef63Rfzb9-_ypsn4CTijiS90Nacvh2KH7XhU6V5i6pUC_bPOL2-nFubWmxM6i7J1O_f38TuuETpoNv35IADG3XKtzRKQGd8Z5mtLHQajb8KeQ1n0eOfU0z5LhGrp0kR5EGsXfjI5B8aLrVE8OtqGYKiDRIyj2wXQymK5eSZD2xoOuQPQ0mTIxe3VUFrSBnw-0-iU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=SXlRCK9fgY7GrTVYN6Cj4bVJycvgYebuIKvI_spUt-tZIoLKlmEQI8tmJyzRqtCz7XKClS7ZzbKvpmm8QWI3ffiPKN5eQD5SAfZYykuxLQQ-LZBk37h-5TnEcygPOaeHsssfNaVU3UCyJuC7HHURBXBL3kB7VmWJzkOGw4A9QdAz1YftO7lo-8HC7BvfCuKvH3vxrpe61LbbGKrBA3cPibcV5g3tWb8qc_kxFodNmjUQ1BsBWsyBHDoDbX7-Y7CX_Yxr-G4cnuHJipLVfjXngrzGIQeL3RMJ1PEVUfN13HwUTcUyTi0a_byWepGeJcSyB1U5vRRVsKIKQNg06kcPlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=SXlRCK9fgY7GrTVYN6Cj4bVJycvgYebuIKvI_spUt-tZIoLKlmEQI8tmJyzRqtCz7XKClS7ZzbKvpmm8QWI3ffiPKN5eQD5SAfZYykuxLQQ-LZBk37h-5TnEcygPOaeHsssfNaVU3UCyJuC7HHURBXBL3kB7VmWJzkOGw4A9QdAz1YftO7lo-8HC7BvfCuKvH3vxrpe61LbbGKrBA3cPibcV5g3tWb8qc_kxFodNmjUQ1BsBWsyBHDoDbX7-Y7CX_Yxr-G4cnuHJipLVfjXngrzGIQeL3RMJ1PEVUfN13HwUTcUyTi0a_byWepGeJcSyB1U5vRRVsKIKQNg06kcPlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=eK7V2OMUs5TZINYmFyZSryylWgRP-cIWlYbXDBNDN8YdOsRZ6XwMKtKOqrmeo4gXei2fRKAoWqunpqXCCryJsUthKvDJikic58MG5Z34qH-mDFh3v-fbyoGpznN_FIC5fXEinsRs7yURuNSMbCtsL-IpQnvGI2mkTFblV6JxgEub54dPhNik_jWbmjLj5rEs4js3HwpnvVxon7Cr6Qmu3Es_2OjPRLaQZaLakJAJuH1le6ekPydW3WLMlBwhncayktOnuIQaB68aJX90JD8gl0hgnjdfYW1NsRoC0dxDMAbaprW0mOGNckCi9aO3-xr2gWJXryevLkrcAx43fa3UFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=eK7V2OMUs5TZINYmFyZSryylWgRP-cIWlYbXDBNDN8YdOsRZ6XwMKtKOqrmeo4gXei2fRKAoWqunpqXCCryJsUthKvDJikic58MG5Z34qH-mDFh3v-fbyoGpznN_FIC5fXEinsRs7yURuNSMbCtsL-IpQnvGI2mkTFblV6JxgEub54dPhNik_jWbmjLj5rEs4js3HwpnvVxon7Cr6Qmu3Es_2OjPRLaQZaLakJAJuH1le6ekPydW3WLMlBwhncayktOnuIQaB68aJX90JD8gl0hgnjdfYW1NsRoC0dxDMAbaprW0mOGNckCi9aO3-xr2gWJXryevLkrcAx43fa3UFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReNPWNaKpViEXBdxusnVnImSgrW1v-4vqIVSA2c8coJ8yfWd7TiqT6TlJ5wHhF6JbJ2iC0iMmZFB-cBH0r8ZY2Uluz3whJV4gAPivAyUYuBV8Utk93EBUGC5il3udKREJltheRgyudeyz5mnUeZ1v7WZTBvEcl5aGqOdaNsKrK3KC4hWRfvhAsP8ffTtgVzBA3zbl1YoGyKkEUiSNg0BwwVxHFp-KuWUNiydJpjfzeAcy8bwc47qOZ9Jhk6_AgYvxh-kW5OuTyqN5UOsS0hFCzY7WGMtgyc5u2ZUxcQO9_qIRUGugJiC7J750E7ZRvOEUk3pCQEROfHAuUMp2n0tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=VB3zo5nQHIapaVlf1Wt8hqneOMihMrI91dfYd4_qbcEE-qpT57-84CQ__OGGE2Vdj8Kq0K0nnVgU7p1b-3vupT0GKzszcZDcYxVMkI-uo4it3oZ6AZhTqNfr0B-NoLkCb2APHxikrl8HNT_A_138HR8ZD6pd__4FBNGs-wOQkBDRsFGiLpVzq7hl3-EhZlm7fCp59ayv7rmOXIV0UNP5O2QnvRR7I0XTQO90HR1Vu0AdyMeKYgvqlI2xfwwnLPQ6yh5g8hRr2htvzrcRJBMxbaKGQM9m_oV6X4UuQIhCFIAucqTDGgWw2usSdhNG9Ny_QxWCyMzfUjYI1R-F0pYDHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=VB3zo5nQHIapaVlf1Wt8hqneOMihMrI91dfYd4_qbcEE-qpT57-84CQ__OGGE2Vdj8Kq0K0nnVgU7p1b-3vupT0GKzszcZDcYxVMkI-uo4it3oZ6AZhTqNfr0B-NoLkCb2APHxikrl8HNT_A_138HR8ZD6pd__4FBNGs-wOQkBDRsFGiLpVzq7hl3-EhZlm7fCp59ayv7rmOXIV0UNP5O2QnvRR7I0XTQO90HR1Vu0AdyMeKYgvqlI2xfwwnLPQ6yh5g8hRr2htvzrcRJBMxbaKGQM9m_oV6X4UuQIhCFIAucqTDGgWw2usSdhNG9Ny_QxWCyMzfUjYI1R-F0pYDHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aLq959SDVdLyDz3-EoR7Nv9CS2Jn_NSGL96GxNCKTz5F0h66Sw_lGg39UqWkgJHWdf6f0tLaqR18fT9NSqO0Bxmz4UP6cuQeJuJ6BS0QlIfZ3lYHpZNe5UpYSgvfy56aFXGMuxB2uw0xiLo0DPlo9sNNRF0S-U2zsjjwKquJmliyLzH5w605MmdzDVvS3Wfz_hMyOL2j3zxkuVwvEbGaMfZDMKs96Ef-fk0gDbIGYSd00AhOmTTsDz2xTB4Ofm-1FPWoKciWJLwyKgsY1zfEjkloYYkJXKMUM8jsfqAE3cn8sDHXDG8VF8lkdhSpsaDTnv2hJEmhvjswW8vlFXMfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=EGnpUL-J8rS1owSlLTfhVyPCt_rO9mBdncRIxCWPyDLG40aqgWXKuyGdwlLrU4twUyeJXWKNLfSmYklxVKtFpfe69FwyyE-tiOAxCDi_qbwRrT4qKuWm8WzNazQLqcr6jwURavx60t5ogVr_0luh5imPrjGkQCPyVeUTiN5GnXbY1qWLJLa10JuhStvkXNCDkAeA2qmoViLa7MRxGZpuib-gfHQMouJMfcS2SygMwQl3G1UM-YI4_5L-OIBrZO_fQpeqvrukIf3oOV1MSiCY5NsW7U1QUGuUQjNVDUpMBa4GrDx_9uID-VGE56Rmeme7Pr3WpgDiu5rCvCn4EJppqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=EGnpUL-J8rS1owSlLTfhVyPCt_rO9mBdncRIxCWPyDLG40aqgWXKuyGdwlLrU4twUyeJXWKNLfSmYklxVKtFpfe69FwyyE-tiOAxCDi_qbwRrT4qKuWm8WzNazQLqcr6jwURavx60t5ogVr_0luh5imPrjGkQCPyVeUTiN5GnXbY1qWLJLa10JuhStvkXNCDkAeA2qmoViLa7MRxGZpuib-gfHQMouJMfcS2SygMwQl3G1UM-YI4_5L-OIBrZO_fQpeqvrukIf3oOV1MSiCY5NsW7U1QUGuUQjNVDUpMBa4GrDx_9uID-VGE56Rmeme7Pr3WpgDiu5rCvCn4EJppqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=LoUSkw4cUYYQcFlb4WL5IrsGNgOdKV4ArnMEzIPkSFYaIN0g_7tWdvghFkcnwYpCOzKPzNp0gnvPcBXuB5cOtKtxk-m7XruTOg-swpUGFMT_yuksAOymshjPyb1fxZ70fMmL55GsovADYwhI9Sqkf0mZjWDlZuaQCMv6fZCs5g6sl3slwInrB9FhrRCBF2UjGA2cOQ2jNHpV2D8AlyZomCG8pFMMfqVC_niK0RsJBioUaz_XH8Nu9fAloaFTvhifWkAp3E4SsxQfNb1pqD0AL62mESVos9OOvNUcpJy3tB-1ITNnyj08uCyHHmI1gLdN5eBOQ_ETCrYsIySjzbvCFotzy8Bgz15QioMsecQ4V6N8qbM774bI23zLnAWOlM3ZDgs3BXnLxR-Z7liNFk71rPoKHOSvjRHkm5uJy1qHxU24NSh1NPF6jGeLBTgvA1v7u5d8BgAKUuweBQna8kj3vDKZFwXz6PKA3xX5IEYGKg88vYFL1gqXm9zt22RtmeBFfS7WFUplj721PeH4ahVfqXs5HuveDUJWPJz2EU7nn2-olHvE2nbfTX00nLeN6PhoMZF3JV3mjaBsyqX40PiS3eDauncQad1-M7bhbUO_lXgSsBAV_f7CsgCGCBAngqZd4KD0ufNF4pVSEJmWzUhMO8F1z8_qsKtnq4b7R1mL9dE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=LoUSkw4cUYYQcFlb4WL5IrsGNgOdKV4ArnMEzIPkSFYaIN0g_7tWdvghFkcnwYpCOzKPzNp0gnvPcBXuB5cOtKtxk-m7XruTOg-swpUGFMT_yuksAOymshjPyb1fxZ70fMmL55GsovADYwhI9Sqkf0mZjWDlZuaQCMv6fZCs5g6sl3slwInrB9FhrRCBF2UjGA2cOQ2jNHpV2D8AlyZomCG8pFMMfqVC_niK0RsJBioUaz_XH8Nu9fAloaFTvhifWkAp3E4SsxQfNb1pqD0AL62mESVos9OOvNUcpJy3tB-1ITNnyj08uCyHHmI1gLdN5eBOQ_ETCrYsIySjzbvCFotzy8Bgz15QioMsecQ4V6N8qbM774bI23zLnAWOlM3ZDgs3BXnLxR-Z7liNFk71rPoKHOSvjRHkm5uJy1qHxU24NSh1NPF6jGeLBTgvA1v7u5d8BgAKUuweBQna8kj3vDKZFwXz6PKA3xX5IEYGKg88vYFL1gqXm9zt22RtmeBFfS7WFUplj721PeH4ahVfqXs5HuveDUJWPJz2EU7nn2-olHvE2nbfTX00nLeN6PhoMZF3JV3mjaBsyqX40PiS3eDauncQad1-M7bhbUO_lXgSsBAV_f7CsgCGCBAngqZd4KD0ufNF4pVSEJmWzUhMO8F1z8_qsKtnq4b7R1mL9dE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=vm1pBHey0OxFhlPZGGziCiADdXa9j0cLMQnh_qC5g8bgz4Olb6rEi-qPvxt5Vk4utPBIVegRA3LDhWvN-EzWB298P5sh25qas_5ajF2xGNlIkUPNIuIJ-zxBVXzFJyA9c7otnW6Fxj3pbkmYeiku453F-xNYP-fyTkaw-4LpPYqWdKiVfItCfL3FGLv875MzsIBoM9YQgFYS6cXzHkRDw7xc5L-raF4uJK8idB27ozBBpn92nrI844id0I5Gzwjz3KlA41e5M8mOw5UgGCqM6TNv5AJSpSZusjXSfriaabuvQEc44cj3IayrgadWbjIejlHFaML_Z1ODKU5gxBurVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=vm1pBHey0OxFhlPZGGziCiADdXa9j0cLMQnh_qC5g8bgz4Olb6rEi-qPvxt5Vk4utPBIVegRA3LDhWvN-EzWB298P5sh25qas_5ajF2xGNlIkUPNIuIJ-zxBVXzFJyA9c7otnW6Fxj3pbkmYeiku453F-xNYP-fyTkaw-4LpPYqWdKiVfItCfL3FGLv875MzsIBoM9YQgFYS6cXzHkRDw7xc5L-raF4uJK8idB27ozBBpn92nrI844id0I5Gzwjz3KlA41e5M8mOw5UgGCqM6TNv5AJSpSZusjXSfriaabuvQEc44cj3IayrgadWbjIejlHFaML_Z1ODKU5gxBurVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=JbK0n0Xnd2_WvO5lkkTxslDt7wImrXOqeQiBY4AgekP3fv1Y3o1-cZ-ZR2Sz4Ijg7AAVE6uV61KOwKNM_bc1fSOoDcEpeI-Oleu5O0qkPoM8vKywP2M9bo0tJdoqQWB9S8VBXbGjroItpwp1nIuGT6Xc9ZDVXtYYHNrCOl6ZcJUfDykKaY1u0k3GtVoG5SqrdyHOafYXfXUA1IdAzEgsvbbVo1UPvqzT5l8aop-AyPLjoRYcKDfLYVStoyTY71Xhv2BoDe-hGPBEq6LRlfnAe9dmqJHVjGbIl5JcqHGhCgNtSmxPZ2swqe7y60MOkegTSrwe40Kkiln8fG_nTAMpCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=JbK0n0Xnd2_WvO5lkkTxslDt7wImrXOqeQiBY4AgekP3fv1Y3o1-cZ-ZR2Sz4Ijg7AAVE6uV61KOwKNM_bc1fSOoDcEpeI-Oleu5O0qkPoM8vKywP2M9bo0tJdoqQWB9S8VBXbGjroItpwp1nIuGT6Xc9ZDVXtYYHNrCOl6ZcJUfDykKaY1u0k3GtVoG5SqrdyHOafYXfXUA1IdAzEgsvbbVo1UPvqzT5l8aop-AyPLjoRYcKDfLYVStoyTY71Xhv2BoDe-hGPBEq6LRlfnAe9dmqJHVjGbIl5JcqHGhCgNtSmxPZ2swqe7y60MOkegTSrwe40Kkiln8fG_nTAMpCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV2PpRv_xd_4qdaqzj3OIRSfknLdQ6EytVRYkWaQnlqLnI5t7sQ12ja0rwJRnhWIExtys-xAu_SEocntnMZUPeRKRXUx3BJHP7NtYnv1zxwIPR8e6V9VVEZjpDmrBW6wjtJauQjdjX-81pvxdl-qc3-juq9C_8ymAss_U8CfDgNtaEoxqHW1PxwZ3rW3OjJJ1gBaXlKRBV9pH5ImebnqwOcGoxKuqOEgMN2YMFSNXm1_XHz7nrt4SPMUIYQrvHC01mPItqoATbFFJW3Kiaz0d9FKkLLI6DYQGNS5UHMuvjYPONH2HRBLAfk3JKMkARdlosVGXVBtdQcDSwucaMF90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=g7ZOtw1U6ASAZSFppgn9DJYgS0DyAj7MwAbWmKzRiXaeBC72-vCew-j10EHP2aANLQWCa2b3CiBia3ELoLp4vxs9T63J5ENfGDZZEOdnFb0plIEzitJuLVo7wHfcZklBFsgjpkekbOm_PDFbWrkeHETWlTExbQSIBpaL68Dg-1Ollsh2bypn5spXpoPF2Rz0QSBPKe-BnN_R2mbg-DvCqhTEuGBlumrCKMu3PT0xC9JGoFUGcJNgX8GEodLj5TcPXVEvF1lzMX1qP_twQ5PbepRAujQ_4UoJifBcRwOhO4JgjfFgYY_GBSNZ58Lan6O05VMc-KccA41_VNoMgT6mLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=g7ZOtw1U6ASAZSFppgn9DJYgS0DyAj7MwAbWmKzRiXaeBC72-vCew-j10EHP2aANLQWCa2b3CiBia3ELoLp4vxs9T63J5ENfGDZZEOdnFb0plIEzitJuLVo7wHfcZklBFsgjpkekbOm_PDFbWrkeHETWlTExbQSIBpaL68Dg-1Ollsh2bypn5spXpoPF2Rz0QSBPKe-BnN_R2mbg-DvCqhTEuGBlumrCKMu3PT0xC9JGoFUGcJNgX8GEodLj5TcPXVEvF1lzMX1qP_twQ5PbepRAujQ_4UoJifBcRwOhO4JgjfFgYY_GBSNZ58Lan6O05VMc-KccA41_VNoMgT6mLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzRUI7yKCsuRlFdH12T7sK71-_GwJBIquoFitGHgIgzX3ZPx5HdH7g20Txjvfh7snF5XUEih5ktDR3ThzaOmQyXqScwR_FV2JhpI8UpIvbXl2TFj7ERPxMrOFSy50UfCObW895C-3h0Q_j6-lIamqF2iconogCfVzluLwcKUlM8ghMrQVcgPaQg2o1wbTvesvZ7T_7W-pMtD5EaRI5XqDQeb6m6-l4hF5HWzDjSo9hL_T_oP5iYL0J3Kzeckk8ZS8pZ5dDPDfGgCgLIXCZdYs4OkUMk1ot15-d0F1EKyCxX-lu-_XWuR-WMtRogY_Oy-a0pP0UeOfEognOotIvYXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=DybwS6n_skJpiaP0Nz52NAxv6baQvllS6YVKNqEUA0B5MyZo1k75q7kC2eUapUKVSxv-VP2kUBSQCbx-q25OcbPpkySD7FubNU74wfxsnh47dUa06bYwUfYFCFIKHsG0-woNfmByiB6g2cYWmOn5FgoKNH4OlpHtbqxFT_Yi3czE7GKI1WKxKWJKvy_k391rISPq5t0H5fNRqmakH-rTEBWazXDrGLLgmTy580KzFlbZ4zDcPTcNDjPavSSWgmunGMNKPloy0qoDDAT4bdaxN6YOsHrpGQ7V9cPNCaBagk_Z3KCDV4daZLi0S0tkJpLMXCohfInOaU6G_CpzM4twjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=DybwS6n_skJpiaP0Nz52NAxv6baQvllS6YVKNqEUA0B5MyZo1k75q7kC2eUapUKVSxv-VP2kUBSQCbx-q25OcbPpkySD7FubNU74wfxsnh47dUa06bYwUfYFCFIKHsG0-woNfmByiB6g2cYWmOn5FgoKNH4OlpHtbqxFT_Yi3czE7GKI1WKxKWJKvy_k391rISPq5t0H5fNRqmakH-rTEBWazXDrGLLgmTy580KzFlbZ4zDcPTcNDjPavSSWgmunGMNKPloy0qoDDAT4bdaxN6YOsHrpGQ7V9cPNCaBagk_Z3KCDV4daZLi0S0tkJpLMXCohfInOaU6G_CpzM4twjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=JE3CG-cvZpGoEoAs8dknQtN2dlys09UP1BVTwVitIYvec_OoFpyLcNTfyZrH0N4ty-e6Vm279IdVk9NkYeq8hHZ7lD0kuN_nVgaPj2BPTSheHwaSF1w4GhEgZsHJyL7osi7pHP-Oxgi1Cxcoug2JU0u423leFFfytQDJhk0NWBxTyOrT9OniQ9vB2fjMbY_yboGarCJZiomJCuVHO_jrGV0M1jggVbrJrQSJbHPopA1e5zgob_WgxuNHNczBA-0chtJ1fGNUfOcGYn_doxWDOckebznm773h01kKJJ9AkbBjLBTGjs97JkeQW8SjnQrOpYzZNrOHI2rGbgt8wdHdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=JE3CG-cvZpGoEoAs8dknQtN2dlys09UP1BVTwVitIYvec_OoFpyLcNTfyZrH0N4ty-e6Vm279IdVk9NkYeq8hHZ7lD0kuN_nVgaPj2BPTSheHwaSF1w4GhEgZsHJyL7osi7pHP-Oxgi1Cxcoug2JU0u423leFFfytQDJhk0NWBxTyOrT9OniQ9vB2fjMbY_yboGarCJZiomJCuVHO_jrGV0M1jggVbrJrQSJbHPopA1e5zgob_WgxuNHNczBA-0chtJ1fGNUfOcGYn_doxWDOckebznm773h01kKJJ9AkbBjLBTGjs97JkeQW8SjnQrOpYzZNrOHI2rGbgt8wdHdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDVjqWYsI-KMFGyasbKS8CQfWIMVf8Efal50ehJhN1SQHrXieBazWLXvmFFd8Y6BqPfjcLwP_Cy0ByckZe9hRepGBXgUgtVSjAZU7IKqiZAxPCZesQSB8FdQxbfceNMKCF0ViohL0_MXTLDlN7jiHqn4aXRQUJ1YiQsSGsCJdmE4t_f0bdk0h2LehXS_IdM3M8Xd_i179EiZsMfjneIisRiPZAAyLkPPHe3AQRavilGouvOzvX_Uf_PbskG1qLVOD5uNTPQVwaBV5jckHFH-kUKcgj757NyuxoW9BMl0ban2jInlV38FBFAQBOy6pDbHdUd8dSOD4gjyK5VtZuURVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=YQNk2wGcSgQg4IFR-LdFXO5up3SMu_Wo8e-52RaxZIMyNAaeh9oOW8X4TjMyiMMEMC6FQdlKH8y37C8qpzXNhRgnusiMYYF8ekdUDF9SKgOz7YzpZOrZNJusQoqiENePsloKHIlEAfae5BWdbpVecq6hloqssD6XVYvKaNVAcne0vTAp3sjkUs-eVDXGRZZu1zl_A4wcFfeuuXHVcjxLEGGOKhSQVY_ifn4xQjUMsc-1ob_-a14V_ZmjzR3b7bMIKkMwyyL1wruTY7U4vpY3qIN18UA9hCUykfpnHMTmaZIrbUMPbjlhBFFga3zqEvzuiMqA1oAsNgLL1VUP0UBFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=YQNk2wGcSgQg4IFR-LdFXO5up3SMu_Wo8e-52RaxZIMyNAaeh9oOW8X4TjMyiMMEMC6FQdlKH8y37C8qpzXNhRgnusiMYYF8ekdUDF9SKgOz7YzpZOrZNJusQoqiENePsloKHIlEAfae5BWdbpVecq6hloqssD6XVYvKaNVAcne0vTAp3sjkUs-eVDXGRZZu1zl_A4wcFfeuuXHVcjxLEGGOKhSQVY_ifn4xQjUMsc-1ob_-a14V_ZmjzR3b7bMIKkMwyyL1wruTY7U4vpY3qIN18UA9hCUykfpnHMTmaZIrbUMPbjlhBFFga3zqEvzuiMqA1oAsNgLL1VUP0UBFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWFjYRsQ47YiMKoxHI0xg8cGhZm0eTeHQ6baUimVT9Iy4sPr2SRUW2i4JiwBiSMhZCk97k5tz_q-rYGrM9mT2ajfiNw25nJF_4qB8GPnHk0IsleOMS1nZfFdU6PnNikVT6TsKfsgVV1kzFHGw8rDpRq-g7Nj48HggJqYZiXip7cJckxa4T6hk4COsjK3chSdLrzZ5Lm1H6ET1PK9TQsxHOLAWnYY3feHFvYk9-8pu6t72vPPLx1bmk0PJBH-VGDkZYHpW5kLSKdGszZi8V0h0DAG9wn200mezjzpkAY-fFbyJKe2E45tNozKoUaSyDZyFTIPrP3-W4uPUMa4DCyrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=EqhQNJrmi_O_pfpdrzA6szTKg21JlTJUxs_e0sCdMEzFBWWeVEHGFr0SI8mB-HS1zwoLFIdujbH4H1x0clig8d23T1sQRJlNK64pqxhQl88f7TOWrwMBeutuJ7bzJQ8dCAFJiwt5Eu9pI5nmKHmTcOQruzsa9Fik81L0-18rYRuRHXU9bFt6avBT4prNM6A7FQ22LIHRrBuB4HU2LYx9zE6S68ZFAB3jrgrn0Zng-5TIj5UkIbTKSlj-cdYPpbmpzlfSLyMO-UPW1SgXU2LvmioqD6q-xPSdHQer2oy0C3ZkxA4MPGcxncyXY4oYbEKCmroTFy5uI2haMc6NqBt3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=EqhQNJrmi_O_pfpdrzA6szTKg21JlTJUxs_e0sCdMEzFBWWeVEHGFr0SI8mB-HS1zwoLFIdujbH4H1x0clig8d23T1sQRJlNK64pqxhQl88f7TOWrwMBeutuJ7bzJQ8dCAFJiwt5Eu9pI5nmKHmTcOQruzsa9Fik81L0-18rYRuRHXU9bFt6avBT4prNM6A7FQ22LIHRrBuB4HU2LYx9zE6S68ZFAB3jrgrn0Zng-5TIj5UkIbTKSlj-cdYPpbmpzlfSLyMO-UPW1SgXU2LvmioqD6q-xPSdHQer2oy0C3ZkxA4MPGcxncyXY4oYbEKCmroTFy5uI2haMc6NqBt3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glw4xGdNuYoLf8eUeaCnsfmnwNlyVPqB5MDgCSLgSqmh7c8SHZ_8PbWN3QO4TAKJj9x7GowvC0-R5nnSRCdZ9X89E93hG4N1mYGZtxzMGr0c5pOudAibm0D6ZjBLaG_sl--4ZIWn0ZEDzVS5MzzAWX2WdbrvM6H80t7moajIcGqjmCtohtCVi0jfo_s-PKQJjzXoI5QcJlVxGXHczadP3vfQ47XmwuNrYc7jlTyd_l50VR-KeP5dkzRas27f4BIOr9okAtBWHHh3iiIPa_5ax7UTzJRZljc_I7scXuTV0Eyav9o5oEatcq8rxzuhVUrxmMc0lLDItXxAeTXqaogtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWfGfQHwoNBRwcbKRzlqJ7eveZqIg_DyoGFJluxlTri6l3tJ7Yj-vTJzN7KF4UA3lsSd5GzZA1c6qKnGgHu5xwySJmbEN3coGN6BgIQ-JjEW0HWqeqhVGB2eeVvYEUoIiZfFqqrk5Ki9bJ7xDyYYrPZqYjcEKZGkmGAMBwBDE2kGEEpHcniQVlIPVWz0sRt8zb-0dThZ0r53O1SMJWGE3JzOSZpHyF8bhg5YaSVLhkqpqHWndBAcVkmN_QxnDWRrKAohZfIG6QIK0vFzOpymVhnaXV2kCA66Eifnb5jPewKovGruQjVDzOr6KWqbH9ZlfZkrjC8DNMWWowp_G4Ftqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhq8v0P4K3GEVUf6MdoP1gqZfcK0_sDv_2iI8snSIBqWF_0hikbJGxFsXP_xt8uQEgBkU-L7noHZpomfW0mWIlORXxpNI4-GzKq-2bpndbKVt1ZGVU1n4525BH3FONOQD0yvHkypn7vDgIV8gGpAyBIC79SBdtzjh03MEj5LK8YUZwhrZMShOFtlnML7S3EQ3ZpqRVSbPCST9yTp7ITQP91ckQjEildA_2Lq0RSYQikekuoPXoXBVCmHsh0iHit17kDnauJaDzXcX98YEOZT57ZW1WckVUoyhEb-cPqILXS_f7dgv6T6hwTfMU8nDgdzgKRnpq58dqsijsiPOZjs9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=PUcG424auAB4Hr1br6LV8g-jf03oa6NS1fM-L9RY18YsUWV1KwEiAHRLwqVMCw0NqwH0xxF6iRDhdjIATHGDQ-hzxfBtLolpwk_38NcDnDeeEjKLcxZKinm_dZDOgPSmCSMq1BFT1NuMR2s9cWMNgOEK7uHUy_wuGaA1NmcUZedIvWFLelZNS-BjxXpQqCt6kDzSAmxFo5RwmoqoRtI40EnSraYih4JoE5T6pPLXxSmw0Gk3sh0XgJreMBbXm1o-ks3Jm8AKNxMWbC5zkL7aQkilsIF_UBnTuOvbkEg9ehjBpam4MRt_YBnPqCeDCzSxpz5QFVsIGLLaxLFzZBhO2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=PUcG424auAB4Hr1br6LV8g-jf03oa6NS1fM-L9RY18YsUWV1KwEiAHRLwqVMCw0NqwH0xxF6iRDhdjIATHGDQ-hzxfBtLolpwk_38NcDnDeeEjKLcxZKinm_dZDOgPSmCSMq1BFT1NuMR2s9cWMNgOEK7uHUy_wuGaA1NmcUZedIvWFLelZNS-BjxXpQqCt6kDzSAmxFo5RwmoqoRtI40EnSraYih4JoE5T6pPLXxSmw0Gk3sh0XgJreMBbXm1o-ks3Jm8AKNxMWbC5zkL7aQkilsIF_UBnTuOvbkEg9ehjBpam4MRt_YBnPqCeDCzSxpz5QFVsIGLLaxLFzZBhO2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx7Ll-K7_lRzyxd_HnruyY8Tto7fDpeE53PDiyPrD6uqRlI02xMLJ1PxRXuoY_bQ4Dm_wBS_vG8ViwX6bprywNIWB02HkkwMLXhGAFvwqGbnnZVbvjbTacXWQ64qdP6CM7VTP4It4jZVPP59lY5vGnvor75-mWYXe_PkiGhqBW141L7qfIcSrcLw54icmfAU17ktqqfTdsVw6Cuz8ihFlN2_c7WQiwmo-BdpnYkAHth7PKpTsvBiPuIJ8C7y4it3J-llMFE6_1tl18grYL-S8dPDe-eogQR1I6UG1TW0JDVHegkPKuvbDFZWlRbqQB55GZvKC8Vz7omgNtFoavFCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYuDfqWYpj17MU6p2SXe11A9n4mGtUhHv3s_Q7WjoUE_icC8vI5SoCOHNs8_nj2gzF3o1njDMmR9GwQgbHKe6l5I_9ruKfCC17wOnaAY8Ob82_4b-AT9-RK_Uhrzyy5Tmp6Dzk605XjZGFEw-SrkSS6K5PsTJvAHOFRrtHXXBVaPqpoEyylGid6fIX_BzkbPNWU3sIy4vCBHs0PiSaEtNomGNRcGAJU8GfJMALlSddxt_9n9rcErRHiS549CELNK_yoiLSbPtXkp20f2ThL9GzAw7ayQ7WIX7Sh1TreoTe0oVp6DUbvuQVyOeW7BSYW6X2CYXrNwFxEClWk3Fj5rdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9Qv10MlPc9US2F-5pP13INCo8PKDCuVZL3HWl-7Hbra3FnB85253A3dZgf4BvHYQN8OhcUBydK75_6tJMtjl8qzsR2S9VVQKcv96QMwE73hAgr0nNzPI3mFVig5JoF2ueGnEnkOs59GrwCiXPZxX79qRPNr_W8UZWwcXH-UOmUa9tBizOzSObnVhObTxuLFGjJj43-39OOqjWQXAq-mCopqdNMFsQsV4VcwvIcQQIc2r33aThMUYT3W7ah1aN903Ylv9johBv2bJA8eqnSCfdvAmIzoafL31kZXZfNv2_SRe7LgkolhobwCX5pzNasrwuo4bzx5T3mJmWAr3oeIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugrXp1iJTykTzTAg7rgcekEOyP1zN0kyDBhRCAM-R34tYc9ZFP9g5VvsakitWHa1EeYRBcsIkQ91SPdmQMEWHUmjLJpvOTZ_OIZEb-DFqgWe119LZdF8XiKt3x1HoFbmKLeA4DCaJjov6UvhWnDoXkpeMuaPDeLXvM95pkKGwMhOzFd8gESA0CNsIeSbaBv1ekoD22dqSVrEFrioqU3XoauUCZPFrYRdyHJ750Hntk0lq7H9ILvhDfW4ckN_u35LG_xy0eoK4pY1oSrEtjazbOd-uJ0aab-qIaVh6Q-Dt9jxs0sMv9d-Q_NF-yszTVyf93Fbuovam81GaNgvSVvyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=JRW05S9wuKpKlzu6xrne8eR-IBqKvM5TilS9ehDfpj3pQDqkObbu_dMIp640crFwRofduhmlZGH7M6zHSwDUYl6kq1LtCVNxx7bYRFQgwsgdpeKcdOwS-gfClCWHZXFetgrynzCQwsPiTDLM_1GvA2gty6YUqDgBLLEzLqXqTt9QOgCR_i6jYNlq7GZ1ximldisRJLn4dH_wflRSXj8ZZIeN7T8SlXptFuBEsq7WIV928c-W0ta-u_u_f9kQEPFIB4iWqKs7S15p-D0E6kafALsdb3j9laznRZrUCkTRpbc50uPhcz6WQxVaonGFCCZ1vQBoW0dYYDGrj1U7TmRq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=JRW05S9wuKpKlzu6xrne8eR-IBqKvM5TilS9ehDfpj3pQDqkObbu_dMIp640crFwRofduhmlZGH7M6zHSwDUYl6kq1LtCVNxx7bYRFQgwsgdpeKcdOwS-gfClCWHZXFetgrynzCQwsPiTDLM_1GvA2gty6YUqDgBLLEzLqXqTt9QOgCR_i6jYNlq7GZ1ximldisRJLn4dH_wflRSXj8ZZIeN7T8SlXptFuBEsq7WIV928c-W0ta-u_u_f9kQEPFIB4iWqKs7S15p-D0E6kafALsdb3j9laznRZrUCkTRpbc50uPhcz6WQxVaonGFCCZ1vQBoW0dYYDGrj1U7TmRq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=adP0WGOn8NnYl_oD7vjApodiD-l8PIae_GP-tEQRgTMAOx10RRKnfSEkN1rDD97ue1gPVR4kp8mBFTZj2Vi5ticp9VZfzfRHho2OeGmyXEp13sN53RcZ4Ci3-fiCp59RxtgbPA4Rt_2muL-onMBuaG3KELvTJPrwK6ExMDCaCmpoSR8E_wuNlNQQVnO_OaMO5JCvsvqH41-ISOLZtU_e4rT4DUc6lXzpM9Q261H1HEcdYGn-N4GRwyJ7ywOoO4cd_vHrXHMiJahpQRduFQ76n3BQJhUrVyNINCbfiIxWdYq89ZaqIQc1WGJqYDlu6KE1OROjP32KDqTF-wONXC08Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=adP0WGOn8NnYl_oD7vjApodiD-l8PIae_GP-tEQRgTMAOx10RRKnfSEkN1rDD97ue1gPVR4kp8mBFTZj2Vi5ticp9VZfzfRHho2OeGmyXEp13sN53RcZ4Ci3-fiCp59RxtgbPA4Rt_2muL-onMBuaG3KELvTJPrwK6ExMDCaCmpoSR8E_wuNlNQQVnO_OaMO5JCvsvqH41-ISOLZtU_e4rT4DUc6lXzpM9Q261H1HEcdYGn-N4GRwyJ7ywOoO4cd_vHrXHMiJahpQRduFQ76n3BQJhUrVyNINCbfiIxWdYq89ZaqIQc1WGJqYDlu6KE1OROjP32KDqTF-wONXC08Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMyQJfDgY5g0O4oWrcu-6KBXClQaU8GMM0zRki4DKxIBCq2RTpns9kDZlj7U9se2DwX39i3lSiNEaSKQSCBHRzVSm_A89VJ7lPbBDfs-SLn4AGHiigN5ABTCGrYi8no_4qYGWpiH9t3QtirQ_FgTBJK7JZUw_Ybhea_RytRPN9BVhsjGt8Xb7AOaJtD6TG6Ym_uMQCk7DaUCBkDh47aB5zH6tmiKchgkEJiV70DhpvEzlaxnsw4SltUfBv3twWsVqZ3dJbIdbgp0Mt8bxjh7w54R-bXsvTQw-N1odIo9qHAYcmqa1U6BveJEsUiizeXJTYdpydfxrOn-IS98kQiNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
دوازده کشور با صدور بیانیه‌ای مشترک، ممنوعیت‌های ملی تجارت کالا از شهرک‌های غیرقانونی اسرائیل را اعلام کردند؛
🇫🇷
فرانسه
🇬🇧
بریتانیا
🇨🇦
کانادا
🇩🇰
دانمارک
🇪🇸
اسپانیا
🇫🇮
فنلاند
🇮🇪
ایرلند
🇮🇸
ایسلند
🇳🇴
نروژ
🇵🇱
لهستان
🇵🇹
پرتغال
🇸🇪
سوئد
مکرون، نخست وزیر بریتانیا برنهام، و نخست وزیر کانادا، کارنی، توافق کردند که وضعیت با خشونت «بی‌سابقه» شهرک‌نشینان و گسترش شهرک‌سازی رو به وخامت است و به طور خاص پروژه E1 را «غیرقابل قبول» خواندند.
آنها از اقداماتی که قبلاً توسط ایرلند، اسپانیا، هلند، نروژ و بلژیک انجام شده است، تقدیر می‌کنند.
این بیانیه از اسرائیل می‌خواهد که فوراً گسترش شهرک‌سازی را متوقف کند، شهرک‌نشینان خشونت‌طلب را پاسخگو قرار دهد و اتهامات علیه نیروهای اسرائیلی را بررسی کند.
آنها «قاطعانه با هرگونه اقدامی که منجر به الحاق سرزمین‌های فلسطینی یا آوارگی اجباری شود، مخالفند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=sygwURltoBpdAYdhbQRYIYuFS2xC0MUoDAveMMrMoreZ48iC28AEbrrqYReML7yOotaIzUEb8tXWu4C8kh2cY1i1NXxQER0t5ZigpuT1EqblVN9kIgjG2Z1ArUf7uCMe4cxxbwh11XfRZyYV1quazq6kGQKtaxDocu-K4-c2aUrOUxxFA5WfimBWvNj5PFt4-ZhXXX4Hi1iPCmJzE8Yfow0AiLl4Nq0lv18k4HGZ62JG_L8tqvudaQJgCFHd2NhYoWyMvlvZkWEgJINv-BjOMOAuvdwmTwtemgiAht6zBb2fc7ePMImCYLYRWps49tNDQfRMp1ujT6CkXfNpiTJN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=sygwURltoBpdAYdhbQRYIYuFS2xC0MUoDAveMMrMoreZ48iC28AEbrrqYReML7yOotaIzUEb8tXWu4C8kh2cY1i1NXxQER0t5ZigpuT1EqblVN9kIgjG2Z1ArUf7uCMe4cxxbwh11XfRZyYV1quazq6kGQKtaxDocu-K4-c2aUrOUxxFA5WfimBWvNj5PFt4-ZhXXX4Hi1iPCmJzE8Yfow0AiLl4Nq0lv18k4HGZ62JG_L8tqvudaQJgCFHd2NhYoWyMvlvZkWEgJINv-BjOMOAuvdwmTwtemgiAht6zBb2fc7ePMImCYLYRWps49tNDQfRMp1ujT6CkXfNpiTJN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=XaQ4t80of-Len72qzeYR4XDsXGXiT9PoaEidvz95SFc8Qqraj4oUMAJFO3jyHhMGdTO944iCtEj3dzO14AAso6EzILd0thIJyZTf8BDxpeYoTNNaW0DifPjnUcRLdC-pcOJDz1sqXJHrmqOnKAlXGxYbvm32ZGrDRZzkFGLlQLrfCkHqjmGkg_GvcXLevexHOUTvMBaVRM8BX-5XI1cfzKvltkj5kqL7Vzy9Pw8qSEwxe69SjSjnBH_dsPe_PbHt6pDTql2fTcFBOFrO8QbHuld0ZfsP4pvW1Xb5R73SIWrdtZtexgG55hmWtQ0dnO6iH_puzT1mattQgiPOCjpMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=XaQ4t80of-Len72qzeYR4XDsXGXiT9PoaEidvz95SFc8Qqraj4oUMAJFO3jyHhMGdTO944iCtEj3dzO14AAso6EzILd0thIJyZTf8BDxpeYoTNNaW0DifPjnUcRLdC-pcOJDz1sqXJHrmqOnKAlXGxYbvm32ZGrDRZzkFGLlQLrfCkHqjmGkg_GvcXLevexHOUTvMBaVRM8BX-5XI1cfzKvltkj5kqL7Vzy9Pw8qSEwxe69SjSjnBH_dsPe_PbHt6pDTql2fTcFBOFrO8QbHuld0ZfsP4pvW1Xb5R73SIWrdtZtexgG55hmWtQ0dnO6iH_puzT1mattQgiPOCjpMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=MPpt9BCSxYy16vQQei6wNzHExAxGSXJwEVW5oWwMUampaO5rqkV_jFhLc6Cbms2LwWcoKNVia1GIEgHqvIoZXPcYHEKYUpKEE4ZyM31fZkWGbB7z1UCl890YwQepIeIMtpbuZo3nzzl1hH1BQDSgExeMTEmnnSxvenXaJJSWg1oURVZG4Cy-4XxIsX3M5PdTmkSGN_JDlLY3KyX-gb91PuSD_1pJS7w5kNGCySSW7YwBZ9s0xXfPEa2xxxZ8g2GfdC-2GLoBtVm0ZT-3pczjgmOzToFEc0rL-1wCa2EaPnfDlbV-mmlz_kgW6NQSpveeh6tRA3Y8AjcNruRZmERMnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=MPpt9BCSxYy16vQQei6wNzHExAxGSXJwEVW5oWwMUampaO5rqkV_jFhLc6Cbms2LwWcoKNVia1GIEgHqvIoZXPcYHEKYUpKEE4ZyM31fZkWGbB7z1UCl890YwQepIeIMtpbuZo3nzzl1hH1BQDSgExeMTEmnnSxvenXaJJSWg1oURVZG4Cy-4XxIsX3M5PdTmkSGN_JDlLY3KyX-gb91PuSD_1pJS7w5kNGCySSW7YwBZ9s0xXfPEa2xxxZ8g2GfdC-2GLoBtVm0ZT-3pczjgmOzToFEc0rL-1wCa2EaPnfDlbV-mmlz_kgW6NQSpveeh6tRA3Y8AjcNruRZmERMnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDaxkIrgbShGun2awg5uukoCivbuSCC4UKxNjjemfyO21jyJc3vMIr6V0rYOkoHzOrFpDIYcWX9LPQOPZ6w8nP285DKunVMHWErSvsC-hWBQnOUtvMLdmPU7tA1lEt66nrtNi3BgBRgfD7ozP0YTy5nYj40ItCSThuM5PHAkwZj-Djk7fSmzHFt-ivkOsN830b-FBUPg0xHukuGoL5LoeeqhBJc82MF7Ttbcv1tAL0QcIlqKcTy00RUmUl7AwTz2gUykIyFiOn9L485uR1JFGiD4Eywsspa6798QVu5zs0gdlrpprCjuQAXastydvgtOUdqGeS0fldrW1Hz771d2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnBRiC3AeOqrta28-9mq4AwVCiVryy9u9ugejNR_rgU9wxnQGsLM-ahCm3xzLNVtw5YX7JGAhaLMsGvsVRRokb702Y6Y59k5YXBLuHHCGDwPN1ZtmLPLZ48UBMqJYs0Qu7j8y-rnHDeR7kgS_dEpos7yKt2qNG9EliUS9CqAddN_Jbt7dk_1MBvY5A0ff82GeqAUnzVFSsNEaEyuy6V0411-rxuvzFZ4vLIw7kdv5K0sw6lEd9zNRSmKs7bD7VjIy-AJFFuoxPIWdJO4DULdLBzbSHJgpIO13aZnwaCPr32cjQ5YWtAbC2iwQ4x3Giiejr8bWjcaaECszMd0xJ4BYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lu7sSjLJxwG5Dzf8YgbcqDdt8DnrW886PLj8TGiKPSdU8PF27a9htvAd2cUTbB7PzdmcFO-DLA8w39K8qw2NnE5_Z_tr3-O6zWoHYPNOdrpu1klpJx0uMljnhRCu85JZR5SQpog-bhgT0DYe4O32lph92MXVXya8qq7GnR8NAxWJSPnSo90f4_sMq1QMiGtxgSPs_tD2IbYHIHk8t-BWd0exJYw1GNQLi7Ric2jCuLudvMTQzNJVfiJBg8zKXk145VlbkvkCHJLo6c8o8ycflAXAKtEnXLeK1tgx-1Mu0a2zoomwQS47seM1idMIFanU7sik65o9LGgoNtKqov0rwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWWfMYthVhBzEOUwitzdH0SfRVo-cS_gVySIVOTuxvJXKZU5nNz1LYHWwoAP8QIS9h_aVdN_HhKDsZxOm4lFZZ4R6POVaLQebTVOczhRlGGe0iZdnge88V_l2fHxxvXlYJYNDBXCoDC-m4ws3oZZLNrKf5qD8c-koUFv7Aekua678Pg1BjMwNdBGVaiI1kvb0_Bj-PU-ucxvM9Q2HirOwiMbC86sBPrCSYbFQytM1vG5DQUu5-wQ3sGW3mIlhSy9GcHiArsUqhLUoBLxVKd1PyEPWul0Wtq6IjJqLKYYnvJOASqGWeHvpR0Rv5q7mxdeM-C8xkoQeZLTq0MDgFe8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZzjGBhYGg7YIvB2sWsbLbZ3xVBPhxcJBZgwhF9h0Ylu9XuNp5zRWHrje-XzmQGeoDzh8ffeeUAPj-X9pYTaj2YNI6LNugZacskxCkhpPrtKfiFsdfBYuhK_zozv2QruT3rqb5g_elSnN5rBn3ryRIeenoQz8jDBqhXaaNyxyjwQDra5TX5BYpIptzcvKz3TlQSjk9djWHy8olb_9mQZYtLeq9nFiNsty9oKnlm3fYlqZgTpJ3TZxYNw2pw30fZWGZBZsCD6bOou33zwQPMWRaJ_fNok290bP42VOTjLu04iYH_66LgqvmkcAltWhTWd5A8UhCCtlskirtfhg8bskA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqvwyLgZ1GpUDAa-d8PXyN6Q99BUDHOlSQ-t9qqn0xtzQ33dVkB_3xd_AKE0349FJmHI4uLwgDlreXjatb9sJmJBqPHUprM3jYW3jsRz0-p3mui3_OA3jfbEywG0OeVawWHnKk0jb1YJ17fff1QRWVKdVNucW-IWf2b7W2PRm7wsYcQvmA72tYer9O4zLkQnBm47OOpTXjmhc01W2J8spZQaU53sm-Cxh5bYnqHJ5LasOa01EV045ofDhC4OlBTvdZ7OvvRcTZwR4JqtdyLl8-uMt2IE6J7rVeN_7xDfxLxMIFiAHmkLE72Mo1o2b4g5AFsWhckoVKTGu04_AS13kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
〰️
#فوری
؛سنتکام:
نیروهای سنتکام در تاریخ ۸ سپتامبر پنج شناور حمل نفت خام ایران را منهدم کردند؛ این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی طی دو روز گذشته، دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد.
کشتی جنگی آمریکا با موفقیت از حملات تلاش‌شدۀ ایران گریخت و به گشت‌زنی در آب‌های منطقه ادامه داد.
هیچ‌یک از پرسنل آمریکایی آسیب ندیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=CThmWkhQt7l7Q3sXubS0T3TfFAu8nm_flmsEkHscWlL1j1q8533riX-Z2uuTxrky2NZ3PoLFDnmx0444rTxwm9cyD_2hIgz212H2IIhBnR8GiD9SWmNY03cu6YsHVkVHb7rdD-hb6PzVApz8O7cp1BwjiEpBavSnyHSfDmDFdsN3cETXyE4mPjky0pxxbJJEN6eHAdGCQZDxgUGdq-w7glClIdeLkoazSO--lcgBFmUfxBnojRAuRwDJ0GLMoThrVVXXlNJtHqk5nk16_Dhz9RqRuku4xEuwwWh_eSpu7_wnryqU81PDLC9yxU0dt9_K4t6bqEuyU67z-ysvTGHhww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=CThmWkhQt7l7Q3sXubS0T3TfFAu8nm_flmsEkHscWlL1j1q8533riX-Z2uuTxrky2NZ3PoLFDnmx0444rTxwm9cyD_2hIgz212H2IIhBnR8GiD9SWmNY03cu6YsHVkVHb7rdD-hb6PzVApz8O7cp1BwjiEpBavSnyHSfDmDFdsN3cETXyE4mPjky0pxxbJJEN6eHAdGCQZDxgUGdq-w7glClIdeLkoazSO--lcgBFmUfxBnojRAuRwDJ0GLMoThrVVXXlNJtHqk5nk16_Dhz9RqRuku4xEuwwWh_eSpu7_wnryqU81PDLC9yxU0dt9_K4t6bqEuyU67z-ysvTGHhww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=YGYgVyLN4aTuB1wS73C3Bn1aA8G2JoKVVEjtlI8pHjXv-ShvE3AsIjS9HvdtO04aa6BxQIJ62DUup_2UGBQpq50LOroCvBS1eKmtsGzRhZV8bW-ZMqltMIZuiS688JjLRHcHLIUiVayp0_gX6spsuMvHDG4uje4HrQjGCy5FSwa4Ougzek3axoDNwqaNUp3teKrz8bsavY4GYvnY4DLKCYEQREe20iOoinwg6OypXxGRdrSToAw5-UoLzYokbLWqz-q1scqT0rb1eW14O--GDR4qRMtatYsdXYYr0quT4WsYERjI4aKcUonrCHCjz0tGx6dbTiTQAvVP-Yl_eGJ7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=YGYgVyLN4aTuB1wS73C3Bn1aA8G2JoKVVEjtlI8pHjXv-ShvE3AsIjS9HvdtO04aa6BxQIJ62DUup_2UGBQpq50LOroCvBS1eKmtsGzRhZV8bW-ZMqltMIZuiS688JjLRHcHLIUiVayp0_gX6spsuMvHDG4uje4HrQjGCy5FSwa4Ougzek3axoDNwqaNUp3teKrz8bsavY4GYvnY4DLKCYEQREe20iOoinwg6OypXxGRdrSToAw5-UoLzYokbLWqz-q1scqT0rb1eW14O--GDR4qRMtatYsdXYYr0quT4WsYERjI4aKcUonrCHCjz0tGx6dbTiTQAvVP-Yl_eGJ7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=R5vbzz2coJOPt44CRi7D0ThC6E78k0PEoXzpvIBRjB5JdWXot48Ir6Z2PnU895XVJVZiQ19yIlPGfPVdLx4fYBcloC5tarMOI2mBR3lk9XgBLBK16d4TL4OqEu2Hg8P-jMPdPd6NvE8j0EpPo8rsnRiTGdPobAYpHhljeUJ0iJkmRerdxdzojSe3PfXWAiLc4iH2LV3AvP4fEDHKxjoYZU0eVyQk0Hd-6FdyFjR2XZqPhH5a3TQSwqFAOEyTmS_5egzOllPEOZwCm7PHPfTjljYxVsAFrlXIUTUzC2qyV03UiCi7DLXzv3QybgCR3_n4a8GcS-VLrCAefzPXLl0Nww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=R5vbzz2coJOPt44CRi7D0ThC6E78k0PEoXzpvIBRjB5JdWXot48Ir6Z2PnU895XVJVZiQ19yIlPGfPVdLx4fYBcloC5tarMOI2mBR3lk9XgBLBK16d4TL4OqEu2Hg8P-jMPdPd6NvE8j0EpPo8rsnRiTGdPobAYpHhljeUJ0iJkmRerdxdzojSe3PfXWAiLc4iH2LV3AvP4fEDHKxjoYZU0eVyQk0Hd-6FdyFjR2XZqPhH5a3TQSwqFAOEyTmS_5egzOllPEOZwCm7PHPfTjljYxVsAFrlXIUTUzC2qyV03UiCi7DLXzv3QybgCR3_n4a8GcS-VLrCAefzPXLl0Nww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=tNdA2fHG-UFZHrzSbMGKJ2Jl8ehDtvzEgSFilGAUFZt5aaSAyZIcH4uQ9aKCG01W5-lM075Y4bJMrgxAP2AwrGy-As-Cs-mhybNSiV__vtQEqP_yUw1F6KfSsNFkp6r3rdPq3e6nCDV5hyuvcCXyJkOJ7J6RV1gOnRfF2DPCfFJhQUuapfz3W92xeujOcIuY3KGtQxrhDnEu1BZ7zcg4oev5e3DFrLArpuxE03MLP7z49vXlW-HkpaBzdgp9rrnkOKXEO9-Fa0l50539nFQpfd7INnKPYpSZTaPVex2WIz7hurtxhxnGS5PB8oPYYgF-EsWeOn2jlLfYI0-xn4639Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=tNdA2fHG-UFZHrzSbMGKJ2Jl8ehDtvzEgSFilGAUFZt5aaSAyZIcH4uQ9aKCG01W5-lM075Y4bJMrgxAP2AwrGy-As-Cs-mhybNSiV__vtQEqP_yUw1F6KfSsNFkp6r3rdPq3e6nCDV5hyuvcCXyJkOJ7J6RV1gOnRfF2DPCfFJhQUuapfz3W92xeujOcIuY3KGtQxrhDnEu1BZ7zcg4oev5e3DFrLArpuxE03MLP7z49vXlW-HkpaBzdgp9rrnkOKXEO9-Fa0l50539nFQpfd7INnKPYpSZTaPVex2WIz7hurtxhxnGS5PB8oPYYgF-EsWeOn2jlLfYI0-xn4639Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=vUZeV2pybUuQpEkmWFhvngJJUDPVQhQIKTG3NnDoRNobk_6p2NdTkku6D1SQu2T9wpAbtLcNXEZASy3Z-646ZTqioUnaDCi-qIrwvCoKXHqr4jl0_a7UhScItTubTsjfSvUK9YTy6884c0VpCKaaNWaVf6aiQ0jQxnX0zdt0tJ1YPMNqIBGYaosHhy7yJXKtV14ZBYUdzlMz5W2kmUwoJ8O2tinwTsPnh7foHC6TSPXvdl_2IhKNWIwZNQRZf6KfyYOOGHwj5G3NQBTCc4RPLflY27a7XLlhN4_XaashXs0lTf5Hb23W_NV5Sgpz3V8cJlgfcMVyE04m1EP51mSJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=vUZeV2pybUuQpEkmWFhvngJJUDPVQhQIKTG3NnDoRNobk_6p2NdTkku6D1SQu2T9wpAbtLcNXEZASy3Z-646ZTqioUnaDCi-qIrwvCoKXHqr4jl0_a7UhScItTubTsjfSvUK9YTy6884c0VpCKaaNWaVf6aiQ0jQxnX0zdt0tJ1YPMNqIBGYaosHhy7yJXKtV14ZBYUdzlMz5W2kmUwoJ8O2tinwTsPnh7foHC6TSPXvdl_2IhKNWIwZNQRZf6KfyYOOGHwj5G3NQBTCc4RPLflY27a7XLlhN4_XaashXs0lTf5Hb23W_NV5Sgpz3V8cJlgfcMVyE04m1EP51mSJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=ivmW5ASErq5BFBWG9o0JgxiXWx3L60RixyMa_hMldJojP2Q8dLugsLgRKlPXFd-SboqUMPOgcE6Xxhj54kmJHpOeRIPX1pI2uS6nT33RBEjYXuwSmym7UUpDwYjW5Ewu5a8u5oLa61DtM0ptO_Vu3BKgv9Pn0TW65zFctFIciai0n0QZ9T6nlCIapRCHiW05EXABeMnPI639N_mK384zy_dV9yIyyRfQkiQH4dpU8LG65yPiwZ2Ie7ifW1DIwLm6gWLTepMoeyV6Ft5V2gBQrAc4BgK-T1zxJK9N6kGci6_NGMqqnV-A_BgaG0ciTuC5CAA4OqDHMpz3nkXwQ2IIrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=ivmW5ASErq5BFBWG9o0JgxiXWx3L60RixyMa_hMldJojP2Q8dLugsLgRKlPXFd-SboqUMPOgcE6Xxhj54kmJHpOeRIPX1pI2uS6nT33RBEjYXuwSmym7UUpDwYjW5Ewu5a8u5oLa61DtM0ptO_Vu3BKgv9Pn0TW65zFctFIciai0n0QZ9T6nlCIapRCHiW05EXABeMnPI639N_mK384zy_dV9yIyyRfQkiQH4dpU8LG65yPiwZ2Ie7ifW1DIwLm6gWLTepMoeyV6Ft5V2gBQrAc4BgK-T1zxJK9N6kGci6_NGMqqnV-A_BgaG0ciTuC5CAA4OqDHMpz3nkXwQ2IIrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aztJvdQOve-KkFMwjdHUsLXbZon69vNa_ynQQkQQOrhAUXlgk5WtazT69757wt5u1wIU3hex_d717m9755stXYhp9oRsBCQcW3UtTjfzIYhRgWAoReo_On-726EdLJ9Ml-t2JTpq6mnZA602q_pikxaNdgxCm7MKsh18qPYhvPZjTc5zgB6ePwxFgkKu7wb5Ku3SX6GmaIKqUoLAt4a6gus4UF-aFCikOksOVjEY1JIa8-Zk6lOSSex-71dh0bzFXYteFv2YHzou2OS2AZQU9FOyWNox1LuE1Gu10VLOc2FpORixCsEPz_QoY6M6jq0hDHMt8G5KCudakgryCy7P7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=nn9KUdpCI7ZBC2WVvmpTyL3tthlrjQzWyc-KlcR1p4hOCeH6ai3WC1KZ7glsB1w97d7Mk6_rNyG2T1gKrGY_6pWrU2Om5PZs1Ag2SZl8rEh1XdN7peWpDOf0wu73TbCEacCrYWvKichVuw6t1mFstyAUrkZq_gEyMUILO9n8RWugT1JViMRosGCFtTPuO2SkzeNY8RI-uL_ERAfRQADIdecqXMtpze1i6BDz88o5OvgJmJ8x8x1DdgelgGtxIhVAj_sFrtxTfhqOO3ZhL3yH3MlcFpKrxLWdI3yLYJ_QCmmbGpQSqBmxA-kzLXkSTnRaYRBiawKt_mEiBugDJhimRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=nn9KUdpCI7ZBC2WVvmpTyL3tthlrjQzWyc-KlcR1p4hOCeH6ai3WC1KZ7glsB1w97d7Mk6_rNyG2T1gKrGY_6pWrU2Om5PZs1Ag2SZl8rEh1XdN7peWpDOf0wu73TbCEacCrYWvKichVuw6t1mFstyAUrkZq_gEyMUILO9n8RWugT1JViMRosGCFtTPuO2SkzeNY8RI-uL_ERAfRQADIdecqXMtpze1i6BDz88o5OvgJmJ8x8x1DdgelgGtxIhVAj_sFrtxTfhqOO3ZhL3yH3MlcFpKrxLWdI3yLYJ_QCmmbGpQSqBmxA-kzLXkSTnRaYRBiawKt_mEiBugDJhimRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=A6nLIg65kT4CN92HFTu6rIzEDIHg_h-3jikPUfgBvKLRM4_TulwQ5w1xq2bn_s8AegkDE9tRHbNavO27BX0VKQ2env58wjNeGkF8aiXs-bbi2p3kJgRevwOqixNIRd8iZw3ZvTraeSffg8ZmEmXk1crenSyMy68bFQ93vLvHMRfjyE8jV_EVxYD5omWc-eRM4mId-aR25VJaMwObuidJ3JpKuANo6QUSsdNMb0nKBU_x47VhpZA5RXCUXEaKEE7FqVmfKxhQR5t8Hh0P45SjERVLl7JTtXcO63-v7z3hXVCRfghvudA6LGcEaSYgm9egcRl6tdxdG8qmrkWTsgwiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=A6nLIg65kT4CN92HFTu6rIzEDIHg_h-3jikPUfgBvKLRM4_TulwQ5w1xq2bn_s8AegkDE9tRHbNavO27BX0VKQ2env58wjNeGkF8aiXs-bbi2p3kJgRevwOqixNIRd8iZw3ZvTraeSffg8ZmEmXk1crenSyMy68bFQ93vLvHMRfjyE8jV_EVxYD5omWc-eRM4mId-aR25VJaMwObuidJ3JpKuANo6QUSsdNMb0nKBU_x47VhpZA5RXCUXEaKEE7FqVmfKxhQR5t8Hh0P45SjERVLl7JTtXcO63-v7z3hXVCRfghvudA6LGcEaSYgm9egcRl6tdxdG8qmrkWTsgwiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izo8TgKHbYF9bfq72kLAtXjof2EeBUQI6Rot9kKzn2o3Q-0zmsSwLGn19ITDMv8P0QAWLMTwlBey5w-aGH6v-1kMuRBmF_pVI9EHFrta6BAUkrnNy_drZD0rhoaI9GoGm-ceNrfH7VFaNtKLWChYni9mcXtb_3UGkbmpBC4uGy2cu1WFuWAp8_arsGa0xK_OS14SkVt36P1oYWSqEiXshPWqI4Ibv334MVApR7zNs8VjTUds-PbHmMevjUUJMrbHE4xCiHMzSfCYRSzV1prMtsNny6PzZfAzJjGFKFEZ2NJunZjqqKXn3Mdqsc3eyorqiW0B_Qb5552GHcRo5cX7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71313">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارش ارسالی از یزد:
از یزدم موشک زدن همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71313" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71312">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
گزارش از اصفهان:
اصفهان الان زدن موشک نمیدونم شهر رضا بود یا نجف اباد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71312" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71311">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
گزارش ممبرا:
۱۵ خرداد اصفهان شلیک ۲ تا موشک همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71311" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71310">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛صداوسیما:
دقایقی قبل نیروهای آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71310" target="_blank">📅 00:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71309">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ_Kq-NMYN5SpPTnwiIT9uVv1EI4ULp_Y7AHXcvzKWuTk03tIU1P43e6fYSHeVXQ5sBsH-siA4TTjNCcDOmFDvuFfc3zZ_IAYTLMTjYLTsfBdQtAmeUPoaRjbqBK3mXns-rVXdGdKyFrxhdPF3DRvek1G6ijfsAW4rPa0QzzcI3w7oALvaMt5iJ0JmM9xQyyDgNk0rA9C9Q9neWz5kc0jkAda_2EX9fB7dFNcCgTfbve1mOocUGVTqqcKByOq3pjNprX9k1uPUKqYYQzfL3_LgOwvTXTpOg4VKGIWbbQK_z9KzuU6zyuhCtHdY0tGpUBKSgCuw0Fb85YwWrlgkpfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:ایران ظرف سه روز، دومین موج حملات موشکی را علیه کشتی‌های نیروی دریایی آمریکا انجام داد، اما هیچ‌یک از شناورهای آمریکایی هدف قرار نگرفتند.
این حملات موجب نگرانی واشنگتن شده است، زیرا به نظر می‌رسد ایران از موشک‌های پیشرفته‌تری استفاده می‌کند که قادر به هدف قرار دادن کشتی‌های در حال حرکت هستند.
مقامات آمریکایی همچنین در حال بررسی این موضوع هستند که آیا چین یا روسیه ممکن است در شناسایی موقعیت ناوهای جنگی آمریکا به ایران کمک کنند یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71309" target="_blank">📅 00:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71308">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tISXnVKh6zFZ70qDFF8Bc8Yj0tkKb3ruhqI_lhzeq1lbhF_cCUGSRsxk_2pa3ZVk-O1v-BO3IZakTp58_RYNhhLIIDRA5fP9p84QmDdbaw4Qf6rMToETOXf7K9NIZkMoE3wtWeoUnPHW7A-QT8gmw8HieRP-4kSvd1ROFwWzPgGBN07GgYjBuJ1Dq-YS70HDn4ADGpWJK1wSbnvI9Z5Mf4EdRm4MvMhxnFBrh7fYHBzfj_alXTPe82kAHINNdZvDf2guo8rBU3Jpo7EMSwvq6p7tmaXIs_iiPD1_QiUvcrZs-yQjfIzum6SrK7Hn-t0AEGaO7oKklX_Jf5fepjuwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
به تمامی خدمه نفت‌کش‌ها در بنادر و لنگرگاه‌های کویت و بحرین هشدار می‌دهیم که فوراً شناورهای خود را ترک کنند، زیرا این شناورها هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71308" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71307">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1BgBbwyjmsKw35dy3___4YkUj0XdY_hYTKaloqDyAcbLUQx7PcqCwTbqw0eQddeqjZIYaWUVKEnKzWr8FYVf2NWfUszJ_b6s_zjCo3vP7gBTOIR3W0Nlzx5I1-eZqHjjWGyfty4vzY3jDMO52BWIetYVsl2cmMp9ntlACBmhzuKNdjyh2-JPKgh0jImp7P6laIbwozpYImXzzSy6TBZVQHu6d8gMAlgZ9iWGxLNo7ZDURl3lSVkzxes40qGDU17tc7tskShuF4XL6IfADI0XIg3aGzLJzyRr4YQGGNIRR__BUZtHPDgzVgTPw-ZoNs3MdkYkOJNqbLW67Qu0Kw2BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
مصطفی نجف زاده:
آمریکا با هدف قرار دادن نفتکش‌ها در سواحل ایران و مشخصا خارک، علاوه بر اینکه می‌خواهد بازدارندگی معتبر در برابر رویکرد تهاجمی اخیر ایران در حمله به ناوگان دریایی آمریکا ایجاد کند، ممکن است گام تازه‌ای در راهبرد محاصره نیز باشد که براساس آن، قصد دارد حلقه فشار را از مسیرهای انتقال نفت به مبدأ حرکت نفتکش‌ها منتقل کند و صادرات انرژی ایران را از نقطه آغاز با اختلال جدی مواجه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71307" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
