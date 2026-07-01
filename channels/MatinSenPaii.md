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
<img src="https://cdn1.telesco.pe/file/tB_alItS2tLJseLVTddZ08ZKndm4cI22vdVSOV9_LrjX5AhBRwrc1VEBdOglkxO8gJwTzOSMCvH8gkl-wab_dq7BLqA9-V_IrXuqZ9ljoQKTTeYzgScQBM1ogCqa2Wjw-PHscoe5J5gOAqqGIOfL3CFjckE3Q3ybnc0dr66WeUzTAt_csQvmk4XVL0ajJq0z05bLsW-Bhm2KA4gw6i7bPcQahwdI9bYjeqfKGv2c0Tm32YD8SIKSoFCVuXoSZ8vshBE35f9-hWYGpUF5Y-zvg1fVt_I73Jj23vTOmflHhMvFiLnthIG4ay9fthMDkpiNaiqtGmkOwPmcpPNPQfPAyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EeC09xEtvW44xDS4XyWkLqbEzaOgDOZop0J3JUEYWYeDPBQtQfHOpMvpQMQJLqe9j2arjadaJQm5ShsjyoA1kbsW7nMLNmfDzrG1y02g9cQGQwNNArw_VglOjOui3xcSSMmoEzBH3_FMxut3xx1cGywCQiY7X-YvGso2tfjvD2G8h82gxKWN0AJrnj4Y125UwiKIRnxYCLaEPBdC-e0NIA1J0hzrQucVBP0UErZg-jy1WWqCF_0kKAk9Xxmp1uu7Nusx2hKQPYLoMh_zPhndAw208YYttG-2exSMTLwcDpfz007dDN5GxvCD1cYplTvfXihDx9RXyls8pZ4pvyb41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم انقدر UX اش درب و داغون بود. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAqp3u4Ri_sGFCp3TMGZE6-JV_VIGRgMlBNo_JuMFmM7V7XurW-dwzFV1dfEHT5ej2AZ7hdanN5wXQOgJZUBYkQO1mZB3-SzMO2cAYKU927PymmJtefM0AOjcw-UjmTmC8Dgux3B6696ZhWrZE5gH99gq1NkcU9dLHbY_D2EY1sLzhF7aUmQtFRdChqlGBQuAjMYg46KDquYjDYOyeNDbpUzzIJdiYyNH5GliKK-Y0w6bBc8oCy3-O1dG8EmGXtWIr2NAITgOtLGY3FZ_AcA9jNfqhg_2f-MzqD3IoYrw23z1nQMp3bbCErkCrb9YjyjSq9td6bv0gszJrYeBeleSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rmJB3rBfNUfzatu_yEcPz_OnQ10lWfZFps1ZgtfmbSot3rStKns8NBTcRhRi3HeBrdgeLAH0GoJOxgQnLdHLSAClR4X7HVM3WM6M7nqgXj941nt_s8FESinU2MHRoLVN7KIl0Ifav6C_TSBnJSkwEqcFbJqqiwWfgeRW_kXmLjrgmjtBcgJCUyoTbx6nVGVDnT3obj6cOxfVa70mGFb4TsP1lXfPrl6BiLWkn6g-Ee5J4Dh169CgFLPYlsHnvmEykJPBQyPPwRs97CZjv2POYBb8m7qxabEGEUdu4q_Lw5jZR4qy8qfc5-98Ydu2wZFeW6gEA67Qk-Wq4WJOVAKYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y57l6PRbLXLvOGqCLYgGuJQlnIHS66Js_9KvoipXnRq6FG17PFnknf9E7HiPTUMVt1PZ2cPJwelzH9HQKaEaY0zUe62V7VJIGVM9qAHkO4RK3G9zaX1w18h8uXAsbq6T3MLCdxSyXAEUGdxFMz_9WIKVIivtN8ihkmhuFO9rpN2cGdwLRy4nKanqyUroSBDoJccCjKreAz6dVKhsPaXdPCRLJUL91giOYEQjdyUmCuzEWmYPe5wyaN_F2JwygnsIgl_UZTj30qhLq07jBp09xqZ3NWvcgd3KXWc-GiMiJJIuQUKVi-Cmnuh3i6Zl3A0MNYIipPO6R-7QdIFt9IGeyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XURx2-R6nbh2vr-CyPDtHE0Ab2GWMzAFXtx51saQt0SpNT1EQmdIJoUS2FFAP5zu0n-VveKBoWVFwTZNgjFDmIq6UJPvit2DCofRxN0MiswpszjJgfw8s4CvPYDJcwoc6uffr6SPR9Hl8qsqQxUMuQss11VI9TEUM_ugTUCQ4ijFhLpb8BBol-WovQJQOCebEkdMl3DMPV4wXX-ArH1miGgismxM57E_xo_5C9Hi49y9Sm5Buy_cwqK4UUDyI4JldS6Jj78sVE6UGRJ_0aW5wd2_dW0f8c9Z6b1RHA9kYhbY0SpnnmQ_b55x0Mkd7T0yNMHvIEccOTZX6fN6YCD-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRNu4Q2CQKCjNWh6XnrRWlSlniAwX4NSMcblClV6zrnoefv-t40qhqcn-J7k0P7TGXyq5a-TNfmOtycAQAlOs5L1z--UY17aonO07r0QA_7FUvTf9YoIIlpDjMpQ22GR-0ghNOzBOugIsUw_ybAk4XqOaQ3jvrKc5zVs4NXTyj65r38DsiYsatrx9kWvqexdYDIw2eCX0gVcZbbNIffFyI2g9-81Bzm3b6b-pg-waHz5CYZ4WUrWmuM5DlDZSE02FkfuSFHwS0SLFXtTEggS5tx3AUl9cqt8qi3U6grrwt2hxF6q94tYK53yF3YXz-Y8TsJxsPjYy4PysIAz08gp3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=YNvVMkyMIc4vEW0O54QmOGHBJkw12GZYU7HnMSUHJoIVa1lcVSMryfu0h42rE1xR8z7rviu6ysmFP887hW7UWJ70H0HQaa-aqj6hMXxh0BA1RbO6Nd41Xjpc_myy5jnK5_6HlP4WcvCsepHByM1bKNtBYiQW_j01-hIZv_-MX8GAAtkMwC0OCsO9mQrazaJKJCLz0azeEXVUxyrGFIBJk7YrQJKioes-XbWKRGLl5BeEyiElMZHSkhZU6QAuCqfLxsyoRADCHh2Q3Ep5KrHa37twAhs1zyz3s6y6YhlnI2bgOoZ8jejRqNaWyWIGikFSIriaWte87g4NGJYB9tvI9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=YNvVMkyMIc4vEW0O54QmOGHBJkw12GZYU7HnMSUHJoIVa1lcVSMryfu0h42rE1xR8z7rviu6ysmFP887hW7UWJ70H0HQaa-aqj6hMXxh0BA1RbO6Nd41Xjpc_myy5jnK5_6HlP4WcvCsepHByM1bKNtBYiQW_j01-hIZv_-MX8GAAtkMwC0OCsO9mQrazaJKJCLz0azeEXVUxyrGFIBJk7YrQJKioes-XbWKRGLl5BeEyiElMZHSkhZU6QAuCqfLxsyoRADCHh2Q3Ep5KrHa37twAhs1zyz3s6y6YhlnI2bgOoZ8jejRqNaWyWIGikFSIriaWte87g4NGJYB9tvI9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=ujjYy0Gjnsuv7_yWHPf_g3rpF3TFA5yieA6YGeFVVskdWaFCZn9Wq-CI7xA70j8ToGkYLHdevD1BVhF0lpXJYneqDZb3ywRmZ-Y9KJhH7EnI8WlELQcW82eoXJewjactFi7SVte7jT99VMiYDrMoywhTmq8RLZzPO2esfr220Ic5FbLm7Nq40Z77P0Pnzu1BhM1aLifmJ0GrKCuI8qDmZqVqTKQskD8GlneUWTxzaYIAEXKTD55P2_yCkVz5-U-HD3wDek3nlVv2B9sFw88QuVv-Cak4wfzc_2PzfmAy5zK1XU7ICLQljIsd8o5Xl_1_Dj-2KwynyZxOJHIA9TBcuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=ujjYy0Gjnsuv7_yWHPf_g3rpF3TFA5yieA6YGeFVVskdWaFCZn9Wq-CI7xA70j8ToGkYLHdevD1BVhF0lpXJYneqDZb3ywRmZ-Y9KJhH7EnI8WlELQcW82eoXJewjactFi7SVte7jT99VMiYDrMoywhTmq8RLZzPO2esfr220Ic5FbLm7Nq40Z77P0Pnzu1BhM1aLifmJ0GrKCuI8qDmZqVqTKQskD8GlneUWTxzaYIAEXKTD55P2_yCkVz5-U-HD3wDek3nlVv2B9sFw88QuVv-Cak4wfzc_2PzfmAy5zK1XU7ICLQljIsd8o5Xl_1_Dj-2KwynyZxOJHIA9TBcuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQKmjbRwIY9mdY4Pw7G1zxClXYIhrWeeB9FrJZwEuuHQeteQJeIxyP6TIDq53FWm6-BQfM-ksuLX817SAjnPNQSZtN6Ln4inLjHtR-tILVHxpL0cmCUG7_O84LuAc3UlyaNhgncZH3dTiVKAZKqOLcdaMpHT61CtNLhTWjMaOI3jLBgRni7gJcVnjeHQ5jURhHDQXVzMp5I_nQPt4hgObsuZ7MO1zfVPUcJGLUpAEqKSMU2J4fY6ir0SNr4Dgbv7FpbsONxb3X4uMmJbkP-7g9-psE4-F5Z9Y3ptV9qcOI1NeKdF8C7V53jOFhUDpt1VCgQf3OBG4BJA_iQjFz0T0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NDRqwgOaJclXvL-kjmzmspqQFAAhQUvZOW51Al-pIemK0NWVfdpY5sfpmRUQP_vdUxhbTH9SgC7uFSxFM-0w9sBpPj3S_rkxWsizxAownacxG0utfHDdD2YS647GDDhVjUGVAIfAnbqFJluxTevZc4R5hW1p19-qFgehaDmXIGPITRGgfSYR4GVZmE6Xyd_6ejmHDeuHAfv9hufGB-Yv2r8UYCjXHAj6muwkSgN6QvIGM6lGzmTPujLhjkz1_SFO_v6ZbTfcQJy_Sbxt-aRVc941yo1HNo2K1IPtNDGHu3gTdrrikTEtXBiGTAcojubUXpBozwpMJWOXGl4skkELCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oGgWCBmZfPtRUYZhheDxEpD5EtuOxK58Txyr31ekaxuGYeIh1JXnv0L7m0LTa_BbP3kTq0VcBnozk9csy9xnyeuMR92rbt7H4zRB4VFdwV_KENrUq4-n1cyo9IdwNd2uygIJzwxhIld5DvldSjYIjBtgrdBCAHPMLuYggqZO-ghX3m3lYbxKxhEHRxwSO3JrXx3Ab5z0ly3MMID9EQDW4v4JShXAGwm7KI17B5dYkHgLLsq-VDbbNIITGTXlE9zBcMlaoi7kmjv8S39yxVH5TePv0my2dKlaWsVuTOJaG3NDlYtTZtgLiSuU4Gs36UtBEDeYz2XDwmORpHEXSbz6Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!
این ویدیو دقیقاً به شما یاد میده که:
✅
چطور کاراکترهای ثابت و باکیفیت طراحی کنید.
✅
چطور با استفاده از AI سناریو و موزیک مخصوص کودک بسازید.
✅
چطور انیمیشن‌ها رو با صدای کاراکترها لیپ‌سینک (همگام‌سازی لب) کنید.
اگر به دنبال یک بیزینس مدل جدید و پولساز در حوزه هوش مصنوعی هستید، این آموزش گام‌به‌گام رو از دست ندید.
ویدیو با حجم 300 مگابایت اپلود شده , از طریق نسخه دسکتاپ تلگرام میتونید با حجم کمتر دانلود کنید.
〰️
〰️
〰️
〰️
〰️
〰️
در صورتی که مایل بودید میتونید از لینک زیر دونیت کنیدتا قسمت های بعدی و موضوعات بیشتری پوشش داده شود.
🌎
donate.isega.ro
〰️
〰️
〰️
〰️
〰️
〰️
📽
زیرنویس فارسی
🌐
ترجمه این ویدیو با وب‌سایت
isega.ro
انجام شده — حتماً سر بزن!
📌
برای دیدن قسمت‌های بعدی کانال رو دنبال کن:
📺
🌐
@AiSegaro
🚀
هر روز یک قدم نزدیک‌تر به آینده‌ای هوشمند!
📤
بازنشر آزاد با</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_mJbp1ydmkHyexKeIGcrgGkFcV23SRD-KSMf6eeWLCNal-IgAZcmyaVW9RE8I3vsNHdInOMxLWzbkPrINAeZhu-_gs6lpeciCVRj8xyZTbGnOxyVIy77KmrFTaq2l55w7OVnIcLZzQwhRHby8d3qkQ2XTOQ_GaxyahJAd3TH3HT_j1M9FaPyRVEqpLgByU1Vsit51LABeSQvR0VqtZjCSWQHfDmkaeio2z4_6e5PJpUlMc_IudGU0Jig2riGwnKUUi2AnkjcBPl6wi0t2SeEvKr0qmEmhF6SV4bjpxkCGxLmd896yaeMP3vVih_hQ1kgYShRa_Q064f2in1CF8tHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UooEQDtdKCvxW_nGoeBBu-fQokc6kaekJs1QHjvWYMPPeOM0yh6FAp9wWureTHcXrxG_52uTUpz74NncI36Ks3PnunXG5GD47NRHklOllxt4TO762CG_v7UBHIlRk8Hy4ADIjua4Z68qIEftfqm5x-QErECu5qW7rK5SrDzeFCaCEqd6Ds2kiXKNCifTPlwzOMHG7WvrUGQwHtDwt_Ltv6HRAfIlSIiH1_Ht8RA1AMwpBcJZ6gmUjau47OtceVC4YgwXCl2_juTaUllY3la-P3EYFKh8v2O48GS5YF05jF6xGjqld2EG4tzLQxmL9MZewLg0axzrfmBC8_yojN-IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MIZRjzeBqteFIUQw0Z9Io7MOtVg62R5bSw-hQJPlvBosFzVYJFR2VuY9h5dy828Ubi5OtnRPmfRqxiReC8YHN_jBXUW_UL1iWn5R6Inyd9TqlFe2YDBqZBO8rvR9n8lry26iJ85_FiYrkLuivZZgI4PlYDP1Eusv0UXZSPJFgViWZfuUnUDnKbk-KlI7jsf1BHwH8Lr6VgmOGEcosFdmVM_P2Dh_Bi3xqfdLnLtLUJsN6_hY7lVzh1bvi60-j_ryrd9rGMyaRPaoZD66zYXDbJO8QBLszQ1Py_hr0S-q36J78MRXgEz_C3WxZ7df75L_PkenJ46YQ7e8MFB1X_YDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GZNcj9ltDZSu3eVOHl6vYyrtPY4BonNSw2v1X0MwINPxA9ZzBLKanz93y9OXdj093xdjZp6fPBRRlIpsQqud588EL1VF9vpjxisna4k0mhOAerQYvlI0VBOsWPIQRHY5yiTU9AFCbpNR8mEGQWA35iHtuaRc8aXfCuVqOHN47FfSq5ykFFhWJm2a9cJ0OaTGYJsKYAgmV-OoG0Dm5nXmxAedKjrHRThNCrtd1kypwB4P6T-Vk_vcp0uVPkwHBRrgSlurTtH6Cl7nr_TM_gd_vQpHzWBCCNZUY5VmLsnm6r_6Y03vbAVj8a5BfB8amWg3mZHmTm_sKtHGJlrUTQn25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HLFrI08rRN3n4_RgWdjo4PI01E-zsX5qP6Yx8GPy1HXDHK_8U2oQJ2DooYOCBeF_ZHDuEqySz-J1DKnxjf3GJ8tSXh7C4DZBd10go8xaQR3Zc3sfWchMTDukN_6ox5xhDrYQRUqtAeQ3XFFcw7ybq_lUi1EvpOAU7rY69rXhrEu0iLLGldntCVyNKa_ZDi4sArgmSDq7AhfC466FP-OnjjzVccx8KDrbXYQ7KTm6g7PqmcJv5AVxwfmiGb2nzUUP7IQWPLvH5M7UTehsEzg5ToImN5Jzn_pPJoX4FD5gY1Kyze-v92SJQWZY1JekwQtQVhH8VtcLudZSKcTsLdGkEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1i6D4fNILF50hcsNEdwYoXbnUGwQFD1GRaWUefJp1rPpNAqP-zpadtZbl_ATD9h9Ma2cShtlyh8vzzGdKS1Tp7316653YlebfXWDthlyddPcStKeLivlkjxU4sEB8Vd8GanikIZC4l798x_PVrGr8EljqUyRKZuGuVJQeNiWC78m1bl1zI5Pv6AZ7ysO0rnnc4tjMAayUsta91pNeSNujvIeNavb9SCYsO_OXJG66JeerMtgA1imKtnf-xpLSVumONmkR7ZsuF5Mq2x6XAKfRz_79pXQWpzyL2qm-B_-1tHdHAOgHZqrrB-1kG3b81bkfjTs4a3ur8qI6FWL7C6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=S3XQSAU0aiCL1KAsFd44ubSb2IqWUdjTgujI0j6OkzUDhLJWWiD_OeXdaBaCuD7InApseldphawQMfmDlv38iv4ORBEERQGyy_g3C96gvIzmnH8-N_WWUt9RyqtbAXpwNE-9lBdQ902CAA6-p-_PyQy7jCEq9gdWNrfqvYxyh45oao2XDQkRxrPTA32mXILtIAccMZ7lP4b42giuxgFvrQpkIfYEe9tPLtw-WxGuxBMlK43jq5e20CnvSQLR0amqMon3zB7yoaDrUK-waOMUnnnhFxMFii1pUXnCvX3xqAR5-eHmtVGtu9dERgba9SgnwSwkC-tlW5_wVa9u_iq2Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=S3XQSAU0aiCL1KAsFd44ubSb2IqWUdjTgujI0j6OkzUDhLJWWiD_OeXdaBaCuD7InApseldphawQMfmDlv38iv4ORBEERQGyy_g3C96gvIzmnH8-N_WWUt9RyqtbAXpwNE-9lBdQ902CAA6-p-_PyQy7jCEq9gdWNrfqvYxyh45oao2XDQkRxrPTA32mXILtIAccMZ7lP4b42giuxgFvrQpkIfYEe9tPLtw-WxGuxBMlK43jq5e20CnvSQLR0amqMon3zB7yoaDrUK-waOMUnnnhFxMFii1pUXnCvX3xqAR5-eHmtVGtu9dERgba9SgnwSwkC-tlW5_wVa9u_iq2Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UyZD7Kw_3GOLnEWpUf1_GMZzTmzKHyVMKHTIdvF6t9Dh_PgTUedokiy-gdtQTV9IvC6NYH5akPlI4VF4F79cvvUqfI3EzsZqAUMl9oGQ552b8oic4tIWARku0cny2CcC3suRWeXWC0bUUrtDNzbootJjPskHIUGJ2FnwLJd27D-tc0NJc7u8raKUA8x-UUNdrM7Ey71jqt06dEeNztNMXMvYhBnGDWWhzGIWl1zBBGurmO6ydeLv3gk6SMqfxyR7Myhhr-bjcerFgBoOMDSu2R98XpLuizKEBatzMtwG2ggSPoinIiI01Y5HQPzowHZGuUtBOKFHfMFDLzEo9efw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router:
https://9router.com/
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم
2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم
3- کلی API رایگان وصل می‌کنیم بهش
3.5- اگر تیک آبی توییتر داریم، به راحتی از گروک 4 و اگر جمنای پرو داریم، از AntiGravity استفاده می‌کنیم
4- از امکانات 9Router مثل Combo استفاده می‌کنیم و چندین هوش مصنوعی رو توی یه مدل فرضی کنار هم میاریم
5- به ChatBox و افزونه Cline وصلش می‌کنیم که هم بتونیم عادی چت کنیم، هم بتونیم کد بزنیم باهاش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگان و ساده‌ست و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXbxD9y9pgUBeh31jDEgUVKUD35xtfJWhOv-70u4gfcjTYTQ93j3eUuzvp_BtmDG4VjAmk9ABXpTo_qFcU6ejd2u--s0MrR41CvSvgcYf2rLXpEFivZhp-gwHS8HAVw9oA9RxLBrOtDdXHci97__ZLC_qd6EIgvbnRvhzhl82Fa5F25KwS2-lRfkZz_KoWcHIPPUztiETDZuZzMQ3tcyA-9mjY5J_pMaF6qkmfpRcVLU8T2LN1AnxmdgrS5VGwhrFGe9eHHxcgfSstkjmLguIGBTVGudVyF2-1xNodmM4M2u2BBRLg4008Fk55GGyLpZgyDxm10xB7U5ZBs6P0Z1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uTal-9DuH7rwsURoaVY8uhtKLSYmE0tONpQetG2v64eEfcmbo6-_CxUT2r9QGwZNqN4OTP-6pScaVFwLKzeHcqdu8x0gF0VZ1SNQs32Ca1-pHAf5Rt7YNTmxdWyfbILBnghciVvh7jp2t-xgTBDjGL0_sS4HaJt4mSk2iXwD7oxmA_bG5PGGbyxqCLF3eF4V_VlXwMsld1QqGKaod6_8KC7HrY9AZ02Fgs2QxqiZNM9EGHfO20MrDYSkohRZmWjjNdjJ1MPlVK7cBnEL1872VvrmIi5cPmWEZCxH1GpPE99eGT1Y9ntgx7G447rfqOI73xVj-q4zlECWxAgiqpDLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cIHhsz11MHqyJE3V1OqRkTBLiSD1NXf_cK7NEsVCd-PI77-2ZWi3PyU6LQsAUBt7EqNrb6bwH_tn6Tc2AovrV0wTyGpZdjeIdt2738jmnbfIHAsDAoz8mfDE4WP0gTwfng3NpmVhfebC3d_MOTmZVJEs82sF32k_UoPU0taIU7efHjo4cHKyj00jkfbRSTZ9Bve8z1BZ72V7Dqd7rKQt5UUDOjsdospL3Z93eZoX9hkuhDEZ4kQ99ZWkqOPnm7k73_bxaKyY7oIYCZGJpJSo-sggzT-FwcAyeguJQyiDWlhWYWA0eUwxkl3TDW0RZVhL0GZ7gik7BdRL3qJTrulf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dr_vE7tyVgEenoGYriVLflDGpnWGar77DF1eyMNBuVSZ1xp6vHDXlqT3_4fn6phd3WbbWgSrSqslbtCAwZQNUJ56dxF3O-FRSoI8jL19Xo6V_ALQ0AcqaKWD2MNOrVSrcixmZqQCWI7LwzBc90vJSjDmRdbB7Kj923vRQ_t6tY0ROa4U1ZcJrUItBogxSTD96Gi63y_lXP-1B3iuq5TL9I2n4OgcEaegOGLuYSthl7v-5-FL_24CH5FybJVh-zRwwBezGF-rWrmcIuRuyYJEj6FKzgH-vlxYMTtZQRsO0YnIXFMyKe50oztsPeLlNbjxKusgiRZwCvVGVs8aTVIGig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kTi6pM8Vcu1_MgKzfhglx_ZXUG5yOy5GVrcjn_r7m8GBsST_Alqd2g3mnVBfAhu4v86iHCzoq5lKFLX6ruqMtUnAiuIreJgU5cZFqsYB4UDHMnYn5Oa0Krz17HXCo0EAxcjPnzzDp1nkKWDz5tSN72S8CLWxOazUK2Epz_FYdqT_LCfz-YJpEwHXbzj1L01IMxYWFTn30gDGhxslwlQivubKuiJc-qoq-oFqJfk66GUMX269Csud-_VAm3KYoxi2A7WDPdwrygJ1_SoqVZbL8bY2fyELviVYbHntqRT0NpvbWBcRvEyMuE8iED4JCI0y-dXCIUVQu3hypeBaK48-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JfnakDvbAZ_9PDRUBq71qB6dvI1w2CA6NjB6-qWAOqpOT3JP2YT2dwA3r476JsPjop4M2UhpBG5fM7yl6SOT8rqAU9_qtDnExVywn5HH8iWMLzzI6gAHm7iPDrFKrNyvdsn6y5b95C6LLeTXlIjgvvwztf9Mf1xtwiDaRd6qYXBetpj8xrwAjI4CjnOEd6KG4qQRBV1M2plKNgJwnrtSiR0ei0sPkgqa-_UI8-MJEQOske8ybSmfv4xQqY5Nes3I3VNSET1gIT7A3SLWwKttnMiaqFJMlhJyYc2yyG5zIX7MgdKqCtAsudJMMIsLj5sCquMxs_P41WDmwAaACsHX0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kbOZnBuD0eNr_ElK1uUZZ0u_FQjwyB7G87OVxqPvTtftkYUcaq7ALKxfl9NysdciSeKNCYOsXOPWQ7Zo7cHoCoJtq7rdc1xhGUKnFEW07gQyaZU8B4j9bbRaSi5J2FxiBZN30iNoadGzV1pSBWqi45OU5F2KUJk4yB0_B_YiaAMQX5s36Lmo1sllL7ovWeXvFRaZH4s4ui5nS0icyHXAArsHjOwgYkGK1vm3eb6VfJPDHwvRJ1u_CNrS12x2LFzkXez62BqsB9FOfvb1h9a8HpeysZIS2EeCH7c-wCPYk7WApC1GNa1ZXXiwMXLiIoTMOcLsoeDxg7eZRE8fLOm5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XLcIfn5x7UVdadzpXtXSUBat8zgrvAEBTGigYTxQzvS7OkBeeMNRvn_Ln1u3dSmBwlc7z_Va6qbNieJQhIRB8UEAG5w_dZQ7uy1OJaYoF48S9e6-SJyBDXjnHufZRSU4kUT9Vczb5WhZzYunEZtl-X_9QUvLeKJ56VzdQgN5zR8EGCF1Kf1uzH6HKI2YEN2dGn0fUdKqHfKSc_rShNwiCprd6Jn-EzTT_wM4YaM8TKJXC5jlnWUteh8edzdKmzOn5AGweOw0dDojjgjJ1BzfnKm403HW09HoHbeacOGvUfSNARlS0EArdhpkQv3scx5fkhWUaRJM54fryFr9csirRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LV_CgVOa6VjbKdwK5fy5jKYG6qdRe39sA66cHJZzA1mQVutXY9avbRC1IoZYEF3OI04gm4NEBgnRkZ3eFC0XS3szRqDJv-MhBphC4CxSIpBXXcoY1x6Axq8tVbA4F36bMt8MHtzjUel05B0pDBf9NSJZkEHRmPRDn58LwZ5fHCu1n-FVvhmqY8x6Ii1yEabqIxh1o3PfXXjqOZ6iYsJinPV7u5Q6DWDmPRc1jbCBl-yOdqq3NRk_uHKFqAodl7yc-qz-KPbQZmIAcRVUmu_BpcxzX9TL-cLKLD7jR8_AXYLpKBTBd6XxBZXSYOc3jg1BT5DJzsexXle0qKAHetWgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oofuzjRh38Rk1GQpidtZh_G5179uXY8zvlu2tFYyk-Z2_yNvxOEe4JJ81KiRy3LNqZLomUbPRxx_K8cilQnwNzQ5Ua5hZr3WhJuminLtvLDOkGJPcCcM1wrYPDem0A_9fyZ9xY_ELyf0Dt7Qyk0J0XVX99640tD4EVdrHVBHZfkdoCAGLtOviyWfGLJhYnx5or5sQycaArkZzoa1egVgdjiRyYp-qce24g68fXEEOL0WEmUb5a8zrqhdi3LB2vmp5-F5JQ0CPrwyxlrBpRl1W8SmYyXVeBcQ8j8169BgTcAN-FgL64UtAw0KMQk6qjDOxTY8oCebD4m7Dh3wkTKO0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lLtkymoFhgq8zRl8IPn_FWOrnHJEGcax6PQhXOA44qATxV34gC8kTu0lwCJ3JBc9DKavbh3RREaom9qCfwiUahWMsSmGaleIf5ren3IB8SPhE234u8lfoMXRWgQ1drpd3MP_GwDUsze5V9uUM3d9SAh8tEXdUuekUwxB7JDDmTEdkdL9UE8u16CK_zbnDPq3SWI128cALS_chOrB4U7y0pD8zwxCXMGTWzHATB33V9CQvIzqFrXbh8ZM_r5ZBTbqnA9wPI5eW_1IXICSUBhcqpvTzSlBph5rypsDNlTHq2PduBKD2-41uBidePXhPKvlQKG1FSKkUhqWDFxKVljW7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i3h_44i6Yi-tgfPrgz5WGNKGoIZi8Vi8vFxjjOuqnpzrKB-VIAbn9OD4UOcPwQibD473RIiKA--Sd874ooB_a8H3G8hVRKpNGkNfg56gIGlAeIC6JKCh1-ieL38crfiwMKzsfWS-fEWO8_Mm6cGk-tT5K7n_-uszOcz3zxpmpQt1cTvllPfAJq7yLxQiFoTNboqdKZGs3yMgOwKAmAsDPdbavrA5st9fxe-287fTRFrYUIBfA1yKjVhRW40wkVPco_IFO7HW3JfFR3sYvkPyRIeZdeQ__6zX9niEcZzG8BR1DD0F-0DJYyhgm91blRv-RJZHfJUv8Z0EllTRDLFqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QsyfwPh9qn757OhTcuE3CfAekV0zKMN9B9uMdzPREL4Tc6UXrKp1y4RVpMGnN6uV1bXEJd2-J-dY6EkCyxdeCDR7uYF4iXkk4G0Z2oKndPuQPZ39p6nb3bzzzNg8jn89YY_UWjPEZn5XNHNX20noZU4KYCGXEMDIrBM0SJ4imTwAgQpDkRh07hNRbkJrSUECeVTaqs9pjv9G6_yzRMfNfAfpLS42ZCKQGdvt7KiXNirAxxmcyMPhnTI5ofPYeaQeGRR0s9qvHGJK7PYcDLyN3611fx89aVCuwqRYVLpdmmZmGNJm9LFiqA9gzQNebWzrNUQ-whPZIQlmMXGvxj9EeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/utn-KJwp72WMsVk7HgglGaTpztZpnIGFAyf2hTNvg7yQ4cERBIZH7bmnTBiBsspRFNh2jEYo0dXfuENp0eoQa4WIPhpoEVqAVaRgfc5Efh9LjG3bsQi8hUct7_3yzzHgNiMWsoV8n0VZDug4WNGwGHrbIe1zfL0O2vHIVLEwF8H7mnWSpWd26MKbnM7Luz1ViAEr9Q6oEj1Hv7WLHfZIpvwA02mgAedXpBrB9ftwkQ5tUQQJ4Sq94g1gQWV4G7RtcqsXPPRB1V5cL1NW0TTcVIxMQMsNOwcKO6qK2PC7ps0_Fl9RJLgxb1SslNoO_PNLpd-tZSs18ilIwN3ts-Ex6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/imbIHFYYy3gMdvpox0Otxu1rdzM1EIaDyqSc9hmLBvQHd_VEurcZ-9vK3xFS3NVFkYQfPw3JVibzFHM2KnGaxl81y05NrqBaWyZD6HtpLPzrljsmJbmwXZOeIXjYbZ9ee0Q4jbbDfPwqMgxyquh-IXFqzWzsBzrkeiXEWVIRWH8tgWz_joDLaNCRu1iR-qh4fGQpqfWrPa9FNqAjoYyR7PEmXPu0URbTibsfHdgvshskJ4BJjuxplkYPN_dwvKNRjJ2IhhPOAo_mg27WPDtQxNswaloVkGrznRYWIYoFg8odbUHA75qLjK9MhOrTJjlsks6NKHyzJj1PIWF-QmH0tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QpwnAV1wF3bj7OJl5pvo-TOVOQRXvYzv-DOE_JMpvVUKPYcjpwIa7rJf7JoHnkzDhDgAl9K4TqTWTTfNddTWSyi3XwWgoi2PZkp7iI2_MXe6fdaWb3nnejk22Kuy8ICk-IW9zUdZnrMyvzoI7CdMIJTmHsk77Mn4vs2kyruOpT-AVmlM0pDa0nbfZ3ufLHemfAHe3kOKdjXcql62TAVE_pVHvQMHehuwvLDNTq5krOntYOnHwYeKvJdArSaqbKlA3JaL7qSLxIVPv5t3LzCeG88WvPUw1g_JOnuzU7ShV2_PUbKRjqXyX8IwSQ7MMPJ9uuzcc93moBqbE-fkdcfSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QrZAgpOijRna6SG5FO91QINFDECTlq3BD1c-Tnab29qO_KtuO1wT95rW8EtFCoaPtIYARoRrwgLicDa1heLhLMgwRgbLR36XNb3Cn1o6Vu3sTgx-77sFqXbFGJblloBGFcY_UBq4-Wg4s51YH8xjsHop2Ylon6o9HQkhgaDt1Ar8zwktZk1aCmrfLXzI5_NFBD_2fi-kJVz2fP5wmw-g0oerQbsKM_-YmD34L1seF4xtrU_QNmNjzQgCT4Da6H7lV-XwrOC38rCsWCF2KLcY_SyOk1564TDOA6bY1TheZrrjYRVoZZxbUkLyK0Bt13C_5-m2Qghihgpalo-rBLb6wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AHiOPYnthgeoQskf0-KnpEjdRN6DTyYord82TTJkmoTelSMWQwdXwiLx42G5AjLZescbem2ApWugU54nSvDG4UKNXXc2jOdVb2xMVuMNmKFIiPS2rAG1tpxOwXvGzIR8Uus2KtWPxoCoOyJt6O6ewbGWG_Xqv5cU4BnyvJKX0kVykGHfiNojSFfhEavhWvJRlL3zgO_mFqfkOFgldcm_PXX8Y1NE1PwBGnpwp1nM1kjPNRIBXIGyKha6wPaI4DpTLyH-o_uk_W3bAOoi0FB5Og3lCEPbxW-ukOA17OR30ee0HVknKSVWV1u0hnZLgNvO219yj6UX1Mu7i2kqkwEkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پیشرفت ai واقعا گاهی اوقات ترسناک به نظر می‌رسه، اما من به شخصه باور دارم که نه جای متخصصینِ واقعی رو قراره بگیره، نه قراره اتفاق بدی برای زندگیمون بیفته(به جز افزایش قیمت رم
🤣
)
در کل، نباید نسبت بهش گارد گرفت. نباید هم نسبت بهش پذیرای 100 درصد بود که "آره ai خداست هرچی بگه درسته"
مخصوصا توی برنامه‌نویسی خیلی خیلی جنگ و دعوا هست و می‌بینم که کسایی که به خودشون میگن وایب کدر و کسایی که به خودشون نمی‌گن وایب کدر، هر روز توی سر و کله‌ی همدیگه می‌زنن. که خب صحبت طولانی‌ایه؛ اما
نه اونی که می‌گه نباید از ai زیاد استفاده بشه اشتباه می‌کنه
نه اونی که می‌گه کلا همه چیز رو باید سپرد دست ai
چون این دوتا دارن راجب دوتا شرایط و چیز کاملا متفاوت صحبت می‌کنن. و این وسط یه سری سؤتفاهم‌های بزرگی پیش اومده و هر دو دسته پیش همدیگه منفور شدن.
به نظرم با گذشت زمان، خودش درست میشه
بازار، خودشو پیش می‌بره و پیدا می‌کنه
و در نهایت، کار هر دو دسته هم مشخص میشه.
الان همگی توی قطار پیشرفت ai هستیم و صدای همدیگه رو نمی‌شنویم:) بهتره صبر کنیم ببینیم کجا می‌ایسته، یا لااقل سرعتش کمی کمتر می‌شه، اون زمان میشه بحث و استدلال کرد دقیق</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4087" target="_blank">📅 01:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/puJm2zzK-YExMdcm08wahWhN5OiPFlV31lfJLsPey93Ulk30LK33-fqYIsQDqeyH5BfD0JlJLWfGWsnI8OcvTws3YW57nkMxuskjOZpkufCnP6DB2TH8SkO0qhTfF-ZTwdYh-C8IOGy33hSmDlxCRQ8dX1qHTeik9GA5tcLLV-U0VQDXketiFosbwMJF-E_V4detELq7Rm5qwvPCTqOL5fBDh9GLV4OcZ8p1BoB9P7yZWpiz99xg4SlOmFf6dZsFa2NNI7tpVQ5ALdZXUEH8lScHSUyTobCG5uOvzPlj_oo1aXdfN9oNsf0zhXXbQ-ulpZF4GmDEGvELIsMAnRINFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dUzWa_7N5KrH8MRKOkVXme03HKgdA4Erlo4_7bgl5heiRT68Lxdg5sxhD93L3j0omiQ0tVDCG2teovLd-CCQIekBsSXxyT-D1XVzFKbw8DqKvR8FsTc8dlPf8wJPzUruw0_i1nYSHPAtEgB0dJhnIznj8NAcVBXjdBd6jiQuWyqw4UPzmpBhYaIfrGYzpRgft-o3qd9Gld6poeUzi1nV-thZcyroXi75uatWuFRPSjOTNDg4-4jLGlVeWP3ejDpgIJWgd2AmIYdAmvxBYKhe1MN9rNZCcnez3IjfIe6pY9aWn7hU8R_Fakg9R-aL6opEc994hNb9-orb2PyQaGRghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OwtydDDaM5UpaumZGRodU0xMKhaz9wtXOo0VqwQAPJwmKJ-0d5I6SskT8bAEOYBHK3TkuNAXgUMeGUmVIJGcoe8g5ip2iNXn43tuakm20SDxtKB4eYxL30FyxcDXA8iuLUJ_034TYlGG-2b2tRd-AzwUkcHKdcsEvAy7fWPdMkG_SqzlimKm_a3peeLwdsZftbA0Bb_0-Kz1uGaViYGR_yMgbe_e5GQ_lOk9whkzEHBDSq8GQFZjAEVmjCOs_zEgFVPEFZp9OypsN_zx7H7JnO13cYmEc6yCWJzCW5dYvwzzO2muhY9vKQpJGK3tEHViT5nEAzIE_tW9_7spmO_qFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T5-faoxH1kuTqJ2wlWcsUkymluAjVVHD96PdlL8Axu9h0irSjRpUImmowlXKjq9Ck1W29AuPkEbp-vRh5wkWhJKndzM6jminuYDZCQ2hBeq825ipWvwB3YzhhCLV6HFskbgC21bNIGXgPPT9eeQocWCeeL8QvnbsIpPpMYKmoayE_mxIyc0rSfUxdnHNXO9co_6JTqW5HVoXHfZDBIlY9OlsG4E-NZpuBdgAN2LSlTfF_RlkX6jBDxbhcFHO_523kzTe30abG7-3dXWNtIwC9rr93MFpkQM86ufCBUPp3tYssVln81D1O4U0wEIvDTVPE0nvlHMhJqoGYa6a5Hrpfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lcf-KNDtyT0ho6pRyZCJaLMnjYtwU1eUOuN7g66cLnyT_s583cAfOJ6tJVnPQr7ceAMMymwVEMndvR-aRGSdC7sCS-kUzJhbyUgH5Z_7Qnj1Bf21pNjv7V_LNI28hggYER7LpZQiqlxRZFY6Rht02of2kFeeAJtpF9ZBQo2pZnJhGTQ7T6HVhxjozv5PntuBD5Ea_aPXZa4mAC_6_ZnYWFoawp-pa2Zs5QrJ4N3IAqJ8SdSRNMqJbBQXKQiXdrk4TNCZacRC7gTi7xHc3a-uZ0o0h3qInG1fWttnE6pGrPfkZ6vTzj28QES1-nqdoxPU7PVrSTuN-XdI7Y3hMcKBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر توی ردیت، مدل GLM 5.2 رو روی سیستم خودش راه انداخته با ۴ تا RTX 3090 و 192 گیگ رم
😂
وزن Q2 مدل رو هم ران کرده که توضیح میدم چیه. همینطور با اینکه تقریبا از بیس‌ترینش استفاده کرده، گفته که GLM 5.2 داره کار کدنویسی و پلن و هرچی که نیاز دارم رو عالی انجام میده.
تأکید کرده که مدل توی کد زدن، پروسه‌نویسی و حتی کارهای طولانی و autonomous خیلی قوی عمل می‌کنه. و واقعا حس Frontier Model می‌ده.
حالا Q2 یعنی چی؟
حرف Q مخفف Quantization (کوانتایز) هست. یعنی وزن‌های مدل رو از دقت بالا (معمولاً ۱۶ بیت) به دقت خیلی پایین‌تر کاهش دادن تا:
حجم فایل خیلی کوچک‌تر بشه
حافظه (VRAM/RAM) خیلی کمتر مصرف کنه
سریع‌تر اجرا بشه
Q2 یعنی مدل به ۲ بیت کوانتایز شده.
این پایین‌ترین سطح کوانتایز رایج هست (از Q2 تا Q8 و حتی Q1 وجود داره).
همینطور طبق گفته‌ی خودش برقش هم خورشیدیه و هزینه‌ی برق نمیده
🔋
مشخصات سیستمش هم اینه:
۴ تا RTX 3090 (هر کدوم ۲۴ گیگ) که میشه ۹۶ گیگ VRAM
سی‌پی‌یو هم Ryzen 9 9900X
۱۹۲ گیگ رم DDR5 (Overclock شده روی ۵۶۰۰ مگاهرتز)
مادربرد MSI 840B (هرچند بهش گفتن برای این ستاپ ایدئال نیست، ولی خودش جواب داده که فعلا داره جواب می‌ده
😂
)
ایشالا قسمت ما هم بشه
پست اصلی:
https://www.reddit.com/r/ZaiGLM/s/Ew9JHC2XIA
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4PXdFhDWIkfo82MudHhFcgC0inP3lmqfbU0VzTII2pkbfl61fMOaqMrKG6V85ROXwAFBXK5U4qDLhR0uuMZNQorWkIusJt-uYuS4bAhz2Leoi6yEmGgjWOREhzifFvnBiy0dMJYaZkb2CRukS-LIA1OqPmUyn5Uk_vn-AHBUZprwhAvIgo38QwHNS1qtUvvE0_vwhg6jYtxwqIbrrU8thYTlPmnuLzu0Rb9ZrU6kzD-bmyTdtYRpUKxPkreus7w8DNq0h03XRQsxYp51XyB0Ojp7RMQxw-YhHgiwG29dbGugpt9EXqYZC2jD5I2nt2sgFW2RiTPkoYA-2TuZ86seg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/efJ02ojTN8RbAjjBQcNfB1tgj33i6gBfoJGT59Mix9ttR5E14RVct3mS9Mo2hViLCNDATOkAiv501dRs4h4_La1TdyTg9lg_AYVRqmq49cKuMoXUlx4_QzixehoztvzOA-V__AqCMqHxuxAsZm_fqZQ3NAu7UJrPRRvrU4BPP6KtDH7Zrcnh_Z000Xz19IH1cXro4LfAg6qbQzJ4GskBgpr9M2XcCBbcut2qg0lP1Lyv9sO9maYOJScmTA-6jpWHoO0UZIdVrJ37zFJwLPU8Vh9fVVpRoqmyXbampq1cnBN6GsWejL_1bJ_gwaUVTOD-DsgrmeRE94AhsHiXjR_hsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=gcas3zVqfkTFfdFqsNjQXAmDIs3tYNI3XVPrK-JtNWqn0gKukxkv2_X_F2O6vfWF7XPzjY6FpCMSPJ8geFDVgmRpu1OVJNkpauwujQrmOlcIgMDYOeknecpAiZzBuGakIqf1rAiudEOeRsnM_1YTfqrysa39ry1wQpi1A0YGwmU2BN3Qb-L24KcqrL3928kNsmMIseh8amfVEMrCXDyslkelPC_gtdX9XP9KS0aozu6ENkEDMvgFfPDA09b-A7ytXIpv-TiRDLlc42W0eYFCGPAmlF84H3AloRWuVU73aHk31-cHL5oibWmZCQ_nwYEfNGnoMWwecK649RVFPdngVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=gcas3zVqfkTFfdFqsNjQXAmDIs3tYNI3XVPrK-JtNWqn0gKukxkv2_X_F2O6vfWF7XPzjY6FpCMSPJ8geFDVgmRpu1OVJNkpauwujQrmOlcIgMDYOeknecpAiZzBuGakIqf1rAiudEOeRsnM_1YTfqrysa39ry1wQpi1A0YGwmU2BN3Qb-L24KcqrL3928kNsmMIseh8amfVEMrCXDyslkelPC_gtdX9XP9KS0aozu6ENkEDMvgFfPDA09b-A7ytXIpv-TiRDLlc42W0eYFCGPAmlF84H3AloRWuVU73aHk31-cHL5oibWmZCQ_nwYEfNGnoMWwecK649RVFPdngVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ePAoWaYMpxnFwjhv-BYk3-0zStFlX4CB0aADeimwYWAAj51bEaywa6RJoN0wQcE0_qx1BGJRFTb_iDk8F8lD2oGUS84RBsGSdMILgv825cwh1PcGF_raM6Gv9_MnTAqOFnEEbcUmlaL2jb54I5kUCzLjPEI17qVc8PJfs_SXT4ZtyXEOYJFu4V8J9FieuOC1_eDKD2Mo9GZiim--QtgYVfDkSvD-jblDB5qT1SePNSYByoSnOF99M4iIHH5eyfnC015dnFSnPA6su6tkHJxaTaUhY_aisjl34oLIBqW4jrE9qZv97Svsxg3IsOayX1PtIqoS3NIE8EiZJfAL6g6GKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JVWIOIDQsBgyqysnRbB6aTGSDwnvJ7NP5bxbfnQ4UE3h_jX7FAf1WHmKcBT5T5kXoGOqX2kD9t_YEinUKqe9vjUBUAz-DoZqzYax_F0dLUv9jBmNpUzQ0BAp5nK2AmtMO4Qj4AkrkmSqEimOEXaMs8IsbM5-_O5I8-zF88PtQcKsCeTOeUHaYxxnjQLZJaaGGUGJtNZH2DGJGZ1LbHTFk7XNLrHJFcwI4onjLAbKQePqzRhW6yhPqI8UUeaiFvZtvxqv9kZcc8xJrusTtLuQhmt0aTq7Ut3aDxXr1VnoTOzvqwK6XdLLfS32qMUkFALtcuarjEym9W_wmkV50ecE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور
/learn
هست.
به‌جای اینکه بشینید دستی یه
SKILL.md
بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش بقیه‌ش رو انجام بده.
🗃️
وقتی دستور /learn رو می‌زنید، ایجنت با ابزارهای خودش (read_file، search_files، web_extract) منبع رو می‌خونه، یه skill استاندارد می‌سازه و ذخیره می‌کنه — و روی همه‌جا یکسان کار می‌کنه.
چند تا مثال که بهتر متوجه بشید:
۱- /learn the auth flow in ~/projects/backend
کل منطق احراز هویت پروژه‌تون رو یاد می‌گیره؛ دفعه‌ی بعد برای پروژه‌ی بعدی، فقط صداش می‌زنید.
📞
۲- /learn
https://docs.someapi.com
مستندات یه API رو می‌بلعه و تبدیلش می‌کنه به یه مهارتِ آماده. مثلا من خودم سر API تلگرام و اینکه هی آپدیت میده و ai ها رسما نادون میشن سرش، این قضیه خیلی به دردم خورد
💻
۳- /learn my writing style at
https://example.blog.com
استایل نوشتن خودتون رو بهش یاد می‌دید که من روی این می‌خوام یه کم مانور بدم و قشنگ تستش کنم و نتیجه رو بهتون می‌گم:)
📚
🌍
نکته‌های باحالش:
• مهارت‌ها توی ~/.hermes/skills/ ذخیره و persistent می‌شن
• بارگذاری سه‌سطحیه؛ محتوای کامل skill فقط وقتی نیاز باشه لود می‌شه — توکن الکی نمی‌سوزه
• و اما مهم‌ترینش از نظر من: نمی‌خوای کورکورانه بنویسه؟ با write_approval: true توی تنظیماتش، هر skill رو قبل از ذخیره خودت تأیید کن! کنترل کامل=)
🛡
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4071" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4070">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4069">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4069" target="_blank">📅 10:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4068">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!  توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4068" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4067">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i-pS0ttKWC8GbEsdhiODbZXD_G3km7FOL8XitU5fK57GR_YhTFZBbWX08qqgZZI0c4BpmP5bvDYaTpliGdyF37gTUio9a2lwTMsq4zNQT4YdwriaXu_AwRSzUnrs7TsQl2vLUQIGFjcouQ5iu5nbel3MWljCK2U24IE-N7ngpbjJBGwg-4ADd3vUY4Bs1Xd1vLWGXEd0Tl6ymRIi-RHIcrZFcFOXfOjlM8UHPr8OWRE9HEsWy3w3LvpN-Os2USQiq9kyYMbteekkSXDT28puFnarj65IROBDcC4ZiBtmNT7BghXEqROWfLOugpfjZToaCIbJuNqI0cWSRt4U73G8Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر از اسکنر من استفاده می‌کنید و مطمئن هستید که آیپیتون تمیزه، حتما تیک همه‌ی پورت‌ها رو بزنید برای اسکن. چون به چشم دارم میبینم یه سری آیپی تمیزها فقط روی یه سری پورت‌های خاص کار می‌کنن
آموزش اسکنر و اتصال رایگان به اینترنت ازاد با سیستم(ویندوز-مک-لینوکس):
https://youtu.be/JdNeZnclS-s
آموزش با گوشی اندروید:
https://www.youtube.com/watch?v=2otJfXgNWCM&t=70s</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4067" target="_blank">📅 03:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4066">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ai-news-bot-MatinSenPaii.zip</div>
  <div class="tg-doc-extra">50.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1- باید فایل .bat رو ادیت کنید و مسیر پوشه‌ی خودتون رو از فایل پایتون بهش بدید
2- من با venv و همه چیز گذاشتم که دردسر نصب یا ... نکشید
3- توی config.json هم باید api جمنای و توکن BotFather و آیدی عددی خودتون رو قرار بدید. توی این ویدئو اینها رو یاد دادم که چه شکلی بگیرید:
https://www.youtube.com/watch?v=7qYPK3dGoK4</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4066" target="_blank">📅 02:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v1RyKQ9OPsHufdeE2Fd_Qau3JGxzYcTVDZrOyQ4VmBQ-6hGG_-mcDBADBLEz-uhcBgxWfkJR1n4hM-lrOQr3x1ZQsmKPfdWJ9gKVoCpDqInlR-j8sOZLj-Sdplr0KjJB4rXBXYfL1ahHEi-VQnVHoNT5a0c600vFGEzt87uANMKAhNwCULU45LRoQbjACoBvSLccsSbSSP2-a4JQjYi7DRCbyfQ1_XTi3svsjHQWRedWdMTmI8TX8S2k4pqFFA0BYi_bOGeznAlM2W2kC9PI9hGA1nmvAsQZbXfuUhepHIFU5ZgR49cHjeVenSSqtE7x4VruHHf3Fww3k5VEcF-qFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VjsoSCEZ2idGlzEu_e4RTiL-_3CMLKFOCPdddf4EH9patrdiMQuK09X2RyzSgLxAiEPDlYUIc2nx4EIQ_JRwKQUxjTh3ih9ddQZoXXim8yZ6fUjUSeP21iuQfH8sje98PHjzZHsvzv0VgjXq3hRrlD3I_Og0O0r1Ky_T5TDhYlOC6N4madq9Wk9u2PpTKkoeqjIFmti7oLyUhRPQJhzmmSZsqBS8Jtrr60Ux0VibOHdyQNLQe-8qbtjvnyYOd2FwYIGjRJPEDLXUk_nVyMDK3d6CsdDNkDo5QZFiSaWjJ9DAylPq-8OWtxYZFC9-ACHgJYD3Hl3kdxPDCFJwZm3hwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZME2VI5h7DPRz64Fp6nW3omgmCOn_2DsgZYGImWI9m5E2w6l5ZmOAfKJvjPNpn9b-bddzIxGv9E4qmye_Ras6enHfj-Pum4ojYRCBUWV_Mii4oAlbmod0vXlFAfp_sTJuhQvRajihyk7h5gWH79iEy8bI2LeMqyinhIS3zwgi6ixUl8RxVApl7_QULVQwPxlECJIoPYVlgpGxVAzlRJd_JMk1MCPhLXpJjHTiS6fzDblL2AsTlje1E_DJF1WIhiDyj73rO0HaMecOXfhR_qVhxrdXSIkVC9P6jCsl99nQlA6YfFumeYAZvVx1qMGVa_84yJ07CelFMfvEJl2xLoX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nsoPZebLNF01y4ifI5AFUAC7AQ8qJzuD5V_BNcXiYc0M6OPW5wNAPojDXEwbphzSot8EDoenLo5t1TWoZbEtMUVCj5Wm9M2qyruiR7GjpMxdzgWXNpcL1y6my9URNOf1BJwp9VhVOGapf6-U-SnYnfTGM74tJiXv8AYLI-62YFcBP_Qe3QPISOThFcIGfNHLJrkTqT5qdUNVGKMybz0a9EmheEOXxhfaCQjgNLdQHqkGWlAKI08Q6zB_rGPsVVGALRRdRylRBa-4oorO7b07INstziOspsn7m0dMspASh-JIarMniDJdxzwaqrWwZSIafgOc_0zoHy0Qu3RkTsxtvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!
توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini 3.5 flash lite ترجمه‌ی روون می‌کنه به فارسی، و توی ربات تلگرامم می‌فرسته پیوی من. که خب کار ساده‌ایه و بهتون ایده میدم چه شکلی می‌تونید پیچیده‌ترش هم بکنید!
الان، شروع می‌کنم فرآیندی که این اسکریپت خیلی ساده رو ساختم، بهتون توضیح می‌دم.
1- اولین کار، گرفتن API ها بود. از Nara Router تونستم 7 میلیون توکن رایگان روزانه بگیرم که اینجا گفتم چه شکلی:
https://t.me/MatinSenPaii/4061
و همینطور از
https://aistudio.google.com
هم یه api رایگان جمنای گرفتم. که مدلهای دیگه‌اش به درد نمیخورن از لحاظ لیمیت، ولی مدل Gemini 3.1 flash lite واقعا توی لیمیت‌ها خداست. 500 تا ریکوئست روزانه و 250 کا توکن که اصلا پر نمیشه. برای ترجمه عالیه. اما برای خود Hermes مناسب نیستش چون که TPM بالایی مصرف می‌کنه و Exceed میشه.
2- توی Hermes، از قسمت مدل‌ها،  Nara رو اضافه کردم. خودش اتوماتیک تشخیص داد و گفت کدوم مدلش رو می‌خوای؟ گفتم mimo pro 2.5(که در حال حاضر رایگانه توی Nara اما خب واقعا توکن مصرفیش هم بد نبود برای تسک من).
3- وارد چت Hermes شدم، و چیزی که می‌خواستم رو بهش گفتم. گفتم که می‌خوام یه ربات تلگرام بنویسی که هر بار رانش می‌کنم، آخرین اخبار ai رو با api جمنای بگیره، و حتما از مدل gemini-3.1-flash-lite استفاده کنه و عینا همین.(اگر نگید دقیقا یهو میره مدل 2.0 رو میذاره بدبخت میشید) و برام بفرسته.
5- سری اول ربات رو ساخت، و بعدش بهش گفتم یه سری قابلیت اضافه کنه. مثلا زمانش رو بگه که چقدر وقت پیش بوده یا فرمت بندی رو درست کنه. همینطور گفتم که برام یه اسکریپت ویندوزی بنویسه که هر بار کلیک کردم روش، این رو ران کنه( این شکلی راحتترم خودم)
6- همونطور که توی تصویر می‌بینید، خیلی تمیز برداشت خبر GPT 5.6 که واقعا هم سه ساعت پیش اومده بود رو پوشش داد، همینطور خبر های دیگه که یکی از نیازهای روزمره‌ی من رو برطرف کرد تا حدی. که یه دید کلی نسبت به اخبار ai روز داشته باشم. سورس کدش رو هم براتون پست می‌کنم که اگر دوست داشتید، تست کنید. هرچند چیز خاصی نیست؛ خودتون می‌تونید بهترش رو بنویسید
7- چطوری می‌تونید بیشتر درگیرش بشید؟
بیاید با همین "بات جمع‌آوری اخبار مربوط به ai" مثال بزنم.
شما می‌تونید این رو روی یه سرور لینوکسی ران کنید که 24/7 ران باشه و هر خبر جدیدی اومد، درجا بفرسته واستون. یا حتی ببریدش روی worker کلودفلر. و هر یه ساعت یه بار چک کنه، اگر خبر جدیدی اومده باشه واستون بفرسته
همینطور می‌تونید یه سیستم پست‌ساز نیمه خودکار بسازید برای تلگرام و بدید که پست بسازه برای چنلتون(و این وسط توسط خودتون یا یه agent هوش مصنوعی دیگه review بشه!)
خلاصه که راه برای درگیر شدن باهاش زیاده. کمی تایم بذارید، و کار با این ابزارهای جدید رو یاد بگیرید. من هم خودم اول یادگیری هستم طبیعتا:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4062" target="_blank">📅 02:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4061">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qjT0D093WFt1xWvJ7XJRFyhXdm8_IW0LQB74xMLblcfqpc0FvPzC_AQlhyrcgI3Ihram_d2ciSKl_lbEPC4pbJK6wLWkeEs7BhCFiDQ8vf6t-2t9yh4rszVLgqp78C7RZZOzPfEM7ku_gi8IzahQP08CQlitb_7gkkRNTzBIU0spC9sat9bw09mVz97uchWoJYrZqc-GoqG047lMI9ZUQzViOWPjkw8pUfFClY37WjBTS0pNqrVVoVeY6BXXUj44lfWdOuwl9TNuOAIl_zFVq8YiXF5V20bfJ37ugQxW-a5O7kaUK06XJx7YH6wENfhKA1UdfsxfWTh_YSE_Voevdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه!
یه ربات خیلی کوچولو هم دارم می‌نویسم.
دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes
خوبی این سایته هم اینه که روزی 7 میلیون توکن رایگان از Mistral و MiMo Pro 2.5 میده و هر روز دوباره شارژ میشه. نوع API هم open-ai compatible هست. اینها رو بعدا توضیح میدم برای دوستانی که متوجه نمی‌شن پس نگران نباشید
از این لینک هم می‌تونید ثبت نام کنید داخلش:
https://router.bynara.id/register?ref=PJ6RZMDB
رفرالش هم چیز خاصی نداره فکر کنم، صرفا اگر بعدا خواستید شارژ کنید، وقتی با رفرال وارد شده باشید، توکن رایگان اضافه می‌گیرید</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4061" target="_blank">📅 01:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4060">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مدل پرچم‌دار GPT-5.6 Sol برای برنامه‌نویسی، امنیت سایبری و اجرای ایجنت‌های هوش مصنوعی بهینه شده و از قابلیت‌های جدیدی مانند «استدلال عمیق» و استفاده از چند ایجنت تخصصی برای حل مسائل پیچیده بهره می‌برد.</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4060" target="_blank">📅 00:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4059">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به قول یکی از بچه‌ها یه چرت می‌زنیم بیدار میشیم می‌بینیم ده تا هوش مصنوعی api رایگان دادن
😂
چون خیلی حجم مطالب زیاد شد این دو روز
به زودی دسته‌بندی می‌کنم و می‌ذارم
همینطور بهترین‌هاش رو(که زود گذر نیستن) ویدئو می‌کنم و یاد میدم</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4059" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4058">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اگر مثل TTS اش بهش چندین تا لحن و دوبلور اضافه کنه هم عالی میشه. که اتوماتیک تشخیص بده و صدای دوبلور زن و مرد رو تفکیک کنه. که در ادامه به نظرم این کار رو انجام خواهد داد چون همین الانش هم برای بخش پادکست، اضافه‌اش کرده</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4058" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4057">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود! همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا. دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4057" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4056">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=cSOWqN-RSv8qKDTmMcghxOhLhFjqriLC9Ibb_zl_M2ZU2hj401bSrAhqVi2nl1qKHHPn6EHRbGsm1Ozt6PnUsjLyyhhosaApYLkJO5ee-zGAV2sJzbKhAbOwAOEE4_qBk_AlZEkx6h0SjV7Zmi-oMGYY8YMNUBmJ08IWTVD2CGILkSx_X3xjQdkO2FjdzO0hbEycomYOq5DoeWRKwNSMI0BaoydJDyUA6DvPGMWbypFajvV7Vu7mT4b3Y-uGPZJRm3pMoNIUNDRGTHRXTO7mVQ5B8RBcDXwzrrn-eSWXWPwInZLzNuO425D6CzWilC5RwW6lMHZyOUTJMsG2AZSETkrAFnhxn0DW95uUuF37igIxn-uYOn8forV8R1IdaOLd_FJcPznLs4VN_n8NEp-Uqb1_J6ihrSfeDALIzRy508S_dJsou1EW9G7ptgF_XBpaMlZk-vZW3nX5vkFqGVzSh4wWalyQ757K25PPXGdDdLRmqdA1e9mzSwPvLTze-k6pxgploIJf1GDVIYMc2r58PdGT09P-CR17362fDYno9CAVCwE2Yf2X5uuO4vhqUM59Ul6P-iYFzh6OiIhP3Gtye17gn87dCk8Y4RkNIWBBsgIso9bzB0jsDdR7jKfEf0pMKML_tz9ngt10e2h4IRBmdosIY3-oZgAfbkeQ4lcyufA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=cSOWqN-RSv8qKDTmMcghxOhLhFjqriLC9Ibb_zl_M2ZU2hj401bSrAhqVi2nl1qKHHPn6EHRbGsm1Ozt6PnUsjLyyhhosaApYLkJO5ee-zGAV2sJzbKhAbOwAOEE4_qBk_AlZEkx6h0SjV7Zmi-oMGYY8YMNUBmJ08IWTVD2CGILkSx_X3xjQdkO2FjdzO0hbEycomYOq5DoeWRKwNSMI0BaoydJDyUA6DvPGMWbypFajvV7Vu7mT4b3Y-uGPZJRm3pMoNIUNDRGTHRXTO7mVQ5B8RBcDXwzrrn-eSWXWPwInZLzNuO425D6CzWilC5RwW6lMHZyOUTJMsG2AZSETkrAFnhxn0DW95uUuF37igIxn-uYOn8forV8R1IdaOLd_FJcPznLs4VN_n8NEp-Uqb1_J6ihrSfeDALIzRy508S_dJsou1EW9G7ptgF_XBpaMlZk-vZW3nX5vkFqGVzSh4wWalyQ757K25PPXGdDdLRmqdA1e9mzSwPvLTze-k6pxgploIJf1GDVIYMc2r58PdGT09P-CR17362fDYno9CAVCwE2Yf2X5uuO4vhqUM59Ul6P-iYFzh6OiIhP3Gtye17gn87dCk8Y4RkNIWBBsgIso9bzB0jsDdR7jKfEf0pMKML_tz9ngt10e2h4IRBmdosIY3-oZgAfbkeQ4lcyufA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود!
همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا.
دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه و خیلی جذاب بود حقیقتا. مخصوصا وقتی که بخواید با یه نفر که به زبان شما حرف نمی‌زنه، میت داشته باشید
از اینجا می‌تونید استفاده کنید:
https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/4056" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4055">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚡
اگر برنامه‌نویس نیستید، API Key را بگیرید و بدون نیاز به ثبت‌نام وارد سایت زیر شوید:
https://B2n.ir/newapi
آدرس سرویس و کلید را وارد کنید و از مدل‌ها استفاده کنید.</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4055" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کنار iran internet monitor باید یه کانال بالا بیاریم iran bank monitor که وضعیت بانکا رو رصد کنه
بانک ملی درست شده بود باز قطع شد</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4050" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/noGRaR0I_R_ZM2lJhsldhQ9J3JlsdIZtm1nap4Spxk8RtBBHr3SObfXXUCDX13AzoRhGqr39f_jcD6weQpmueTQxJvPdCBtISh5wZZjAtsqGHpOZKfqHYCYR08-k-zdY1sbdOeYXAsqqvHvkBmwzACloSK5vzXxbWGtV-cLPwixyCVYiKpzByFoAYQrvV_U_g3-9vZhZjcOgmRn2QygDawVRad0SFtSsZi-dDBciLX2s7icX1yBtIEyvArxRCmyTrh8yzlW8l0fT4FIcyBtU0Fwta6gLCBu7PwJHRv0R7_2p8CSc-rfLdb7u1dHp0O8Gy38SqWrWSPhRu3amFru6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/4049" target="_blank">📅 14:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EyeFBnbL2H0dmp7K1kCgtapZS-A0LIT2tVtszbVwz5lWoHpGt6zeLm50iUja9Wkh1TxV4_yJdD3hds-_jKV1n96UQqVgx3drToRK-t3brLUzcZ6loxDLn7AdvOHPZVbORspxfMAwStM4FDOmDePF_ZzZPMq8woaw3vRq9xz5SmvG9fAbbbQSi038S966pomw1ezwh-GmyNPSUPd0I0XhI0CH4Efwuan8jA-T_LE6PH8pFY-yvUZgwHvjGuVpOmJRQ8pr6SF19BvvLObBc_tFRMueKrhke1D06aCEL3ECgOy-2PerrzOLuYLKfafZVRkj10Um3-0PRquphtxj5oveHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزنید این حرف رو بچه‌ها. شما چیزی به من مدیون نیستید
❤️
همه‌اش لطفتونه
و ممنونم ازتون</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4048" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dastamo Begir</div>
  <div class="tg-doc-extra">MEZZO</div>
</div>
<a href="https://t.me/MatinSenPaii/4047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4047" target="_blank">📅 14:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این نت دیتاسنترا کی می‌خواد مثل آدم وصل بشه من نمی‌دونم.
فکر کنم جدی جدی کابلا رو بریدن الان نمی‌دونن کدومش مال کدومه</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4046" target="_blank">📅 13:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">موشک ملی‌شکن
🔥
@HexConfigs.npvt</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4045" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kvanHii6oZAysuOm1N5vPN7E2jk46COBGMZu1qcQ0WYavZZ-SxQTAWwMeoK6ljJG_pl39UZUdkbGfM-1zvjJ0hiGLeME8V2Wz0MUsKYIUfRUA32vzTx_FzXkjrpwUB32h8Vff73T9h7UEYXrSv-DLhZlJ5-nFOe2mm4UlPhyhO8MB__Kiw_Iv5SYou1f97d58uIPRcXrxu_gwst1GvViNzQTbHUGj30ftZlKlZXxo71r8nw1sjn3qWmGitwKmAoWAnHi5rR3YtLR0aCqh1bS8n9YdEBbnTkPALzL-LAH3Nh50tu3eGo34R2xb9Uv_vRZUQC1L9Y7FdFbrggPV3gxWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4044" target="_blank">📅 13:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB
۱۰۰ دلار میده
باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4043" target="_blank">📅 13:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چندتا نکته:
1- کاربرا توی ردیت گزارش دادن که برای استفاده از مدلهای anthropic زیاد به باگ می‌خورن و علت می‌تونه استفاده سایت از apiهای دزدی باشه. بهترین نتیجه رو با GLM میده
2- اگر از GLM استفاده می‌کنید هم، یا به ایجنت فول اکسس ندید(که .env) و اینهاتون رو نخونه، یا توی پروژه‌های حساس ازش استفاده نکنید</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4042" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8SUDz1KYw9v1oFqc5EOZbrcD4CbuKV1AzD22zcA0jCnQMZj4FVwzXbR9XwUXUZtnTsU-wCwW7I8np-lvvx-KbulUr_lBRmuRoLlE4bBWq60zq8OKnuveyyz6m9sDKzibtow6uWGNnD_SwpRJJ_f1WOdurd3QK-uqKpU9OsmYBXqc3-1P3zByYfdyyki6spXSJYE0CHeDpoqv5Hc13CpKKRC2jKVhEfAnOp4Qy7rpihnBbP2LudAETdJe6trtVOP4Ud-JK-F5MSEZTuHYWHy1RdfdR-2zu9w-9MQI2qHICyhkF0Jkh4vBZtZyFg_z9pkg-bOMpuOubQlR4HIHELKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایپی 188.114.97.6 دیگه سفید مطلق نیست و با ایپی های دیگه کلودفلر فرقی نداره. /// البته رو بیشتر نت ها به غیر ایرانسل کانکشن خاکستری نداریم و به راحتی میشه به کانفیگ های پشت کلودفلر وصل شد. برای ایرانسل (و بعضی نتهای دیگر در برخی مناطق) هم با استفاده از فرگمنت…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4041" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bihKIIcnyryikYc9uBUjSB4qroRs5YuvEondUs5RJTP7dA_Gs5OVpCjvmj3KIN3mIZKQJAItDgcmPXOWOHpjlz1NHjOnXdzs4FHj_T9HiPO1PigQJ4eg6OrakxQjUgeS4puWgi9_9wQ7l-qjf-G4a-TSC2Fa6c25updez4U8_gM3sz-rzHUsG17CY_C5_JCHHWgJX8uW32p8DzpZRkE153IAPQDdmKI8Bqfl9009bWxtX9BaOIv6I-rTq2zULz1aMkOKJpsaN5JL_3OGzilsrsfuinHcBgIxyklA1k2vAtSEokKqcArITPEZ4e9xq8wTMxGpaNluVNelKoMZNlfA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4040" target="_blank">📅 07:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CAKGGkbmtiysI56ZqmPcXrK2d3oKWsqkqgfPPdZoAxEuPCOxS3Y8-UlLssxInKiB1o9h4PWVpo5s2DGUIgfmaewPtW4DQU57s5PjsLzODfDTBFk5ZougIYsYX3a-ZoQvtvDSNxeTfJyK0r6ICsP7hRBp0GbnkILi3bGNfa19IVYsVrul06TU43oW9hOZwsZXXLuyHPZY3ZMuRr5oBzltb0i1Dck4LOpOuHHrkObkSgF2W2k7l6QOz-yq6F-SJ-Dd8dufb76uuU633ctHmCXrHDQ2hqdTcUlHAbzvLb8ZGJ24_Lz9hXoBAJlMRjqoPk89fY588b0ecWSkGOd-ZSXQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.  عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4039" target="_blank">📅 01:30 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
