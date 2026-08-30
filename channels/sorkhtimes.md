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
<img src="https://cdn4.telesco.pe/file/ZA-Qf694SOL71xhk_OcjYJZDxwvrfzFkf0VGj-Xzxccw8ebj6h4XnmmAtUrq5WMgvDk7gWiJB6GJXWpzfAbxjokvz9NsJoxqKC1e3gy90Sy8kSgO_jrcWbQbC-opz9T9sB1uaWDjqPnhFssURsSjIpbK2Vg3OdNAlKRWC4Z6C--RyiBNH2_EnPfBqXHJlqm158q79YVez8NjHb5eznV6susQqgEP6kANq51mUUMQd2LqPXhasNcXjN4RSvhAEGtrsB6nztcnaG1h6KhuvfpPmwQM0CmB0CA0lF7Nnc47iJPbWLccVkimbQneAFFBarl_0l3uirqx7_t4wcIQ7q9i3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 00:47:45</div>
<hr>

<div class="tg-post" id="msg-139284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk1hebwqU9EG67P9XWV4bvhVJ0WK1mIoX510IiaUZbfqrARRxudbhpedsjcR2_OJ77H7KzwYp49QWniwmM4HLS9sb8VU0a4_-4f3lydSK1OC6_SGu0M6DFIi7wdSG6GTILHdxa30RRm21AkNyBsRbF-ZAb5z_1GD7Kcs1dhAHea_SfESPeirMZIMiNFtpfuyxit9stUYENBc3sYY7yCtMAi75RCRAKGWlDX1rh_2VvT_ddYqq0WfTMe2rKqY9JRZtTb1JvR6RfNGhYiUobY3R5fjPzt9hdoN_WAVrOOndQfDBDrleoEv-gsPHtH9ZNn7nF4N9Pgz5h0yGdGYu4j6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
فوری، با تصمیم تارتار و موافقت علیپور؛ محمدحسین کنعانی زادگان بعنوان پنالتی زن اول پرسپولیس در دربی انتخاب ش
د
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 461 · <a href="https://t.me/SorkhTimes/139284" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dp_8i_cKPGT__cPycwi165Y9Jtl9hmYEEmB9XRIU4y4XwSpx1UAqkVMJKyWJG3qvxpatr0hezPjJQAQAkfPV1NbqAki9H9GnZ4IdaX1f2e5tBa6BMU7dNVHHsWuMTa7xy-4e52TYFYcMzq39w9pyNH5yptmJRcatWkB0pQ-4PXqO6auXVjbehmyO22Evp__VdOCE_74JbR3G-VXGCUPgqw2OsK8qEYakGppDqufyT6Z3qYqOfO27_XIpeM43gumDMt-3PqR5Yjl5aTCx4AS8nA0VJYWxo34cRot6EXvEr0aH9kJRp30O0Ispbf9GZRJeTFUBvF6DJueoTmHpopnTnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 490 · <a href="https://t.me/SorkhTimes/139283" target="_blank">📅 00:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/SorkhTimes/139282" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139281">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🟥
حاتمی: پرسپولیس در این فصل تیم خوبی است
❌
دربی‌ای که در ورزشگاه آزادی با نتیجه یک بر صفر پیروز شدیم در ذهن من مانده است چون اولین دربی من بود. ورزشگاه آزادی باید به این فصل می‌رسید اما این اتفاق رخ نداد. بازی‌های بزرگ باید در ورزشگاه آزادی برگزار شود. امیدوارم دربی خوبی داشته باشیم. پرسپولیس با مهدی تارتار عملکرد خوبی داشته است. همیشه هوادار پرسپولیس خواهم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/SorkhTimes/139281" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139280">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⚽
نورمحمدی: هت‌تریک ایمون زاید در ذهن من مانده است
‼️
دربی سه بر دو و هت‌تریک ایمون زاید در ذهن من مانده است/ هواداران دیگر مشکلی با حضور بازیکنان استقلال در باشگاه پرسپولیس ندارند/ زمان ما تغییر تیم سخت بود/ من پرسپولیسی بودم و استقلال را زیاد دوست نداشتم/ امیدوارم شاهد دربی خوبی باشیم/ پرسپولیس در این فصل یک‌تیم بسیار خوب و کامل دارد/ پرسپولیس در این فصل موفق می‌شود/ جذابیت دربی به ورزشگاه آزادی است/ اینکه دربی در اصفهان برگزار می‌شود عجیب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/SorkhTimes/139280" target="_blank">📅 00:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139279">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ
: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 946 · <a href="https://t.me/SorkhTimes/139279" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139278">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❤️
🤩
کنایه مدیرعامل باشگاه به برخی رسانه‌ها:
‼️
این سفری که به ترکیه داشتم و چند ساعت دیگر برمی‌گردم، از چند روز قبل برنامه‌ریزی شده بود. خداراشکر همان‌طور که ترکیب تیم‌مان لو نمی‌رود، دیگر سفرهایمان هم لو نمی‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/SorkhTimes/139278" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139277">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c73b4d12.mp4?token=IWcJ4zFtqb9-tdG8oF1_MpLQJjJdBfu8uOmnsdAnVx8duwnhtzW26yNRkLLN72u_vxNkYQOuTV5yLErQ_KnofoymZB2hlcs5dhfVYnVZBCdVEPywqPrE29IOjMABGJga_Tnaa05YtISU6JM3Uxob1_n0mAsh5omyo69N7RyR012uf44xnOlF1G8FCX7nNhawwO1opSMpvX1JK66OsKMXulXA_pFg2RxvFCfiDWW7vQAeH1Tfp2nhrk4L8NBpndEOTyEGFKzhD_EKC6fGFWBkANH0eYz5U3vkX8qdlw4GlJPqkyqeEo4lBJunYP1sFKMiSwtqWj_WGPdWQB-Vg5cw7VMH9IaVR7ffgQziV3soLiDE55s6Cuy1wn_R0haSovRxMAC13wnzEpWyvk4VesrGq5Dsc_IElghr4gKuyGt3IaxUNVqHGgwZWLYWfIk-sMKgsDMk1IBY0axq64H0C20rjr_yP6X9wCSjudoBdhE4XpPYZYY5TY788rRKMiEAQK0E6xIp5KPw60l2JTyApMDhJbLY2LuvB6UkK6t4Y9hXKaIqmC39MKy7HGhm74oItG7derlzY48Bi7ineMXJE--DGKdpxgismS32aEjZaENreioojk1PRsa6sSgqcKtJUYShCXGL5o4eSZCPUDUoF5eiQp1Is_sYJlk-iraDow0EUcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c73b4d12.mp4?token=IWcJ4zFtqb9-tdG8oF1_MpLQJjJdBfu8uOmnsdAnVx8duwnhtzW26yNRkLLN72u_vxNkYQOuTV5yLErQ_KnofoymZB2hlcs5dhfVYnVZBCdVEPywqPrE29IOjMABGJga_Tnaa05YtISU6JM3Uxob1_n0mAsh5omyo69N7RyR012uf44xnOlF1G8FCX7nNhawwO1opSMpvX1JK66OsKMXulXA_pFg2RxvFCfiDWW7vQAeH1Tfp2nhrk4L8NBpndEOTyEGFKzhD_EKC6fGFWBkANH0eYz5U3vkX8qdlw4GlJPqkyqeEo4lBJunYP1sFKMiSwtqWj_WGPdWQB-Vg5cw7VMH9IaVR7ffgQziV3soLiDE55s6Cuy1wn_R0haSovRxMAC13wnzEpWyvk4VesrGq5Dsc_IElghr4gKuyGt3IaxUNVqHGgwZWLYWfIk-sMKgsDMk1IBY0axq64H0C20rjr_yP6X9wCSjudoBdhE4XpPYZYY5TY788rRKMiEAQK0E6xIp5KPw60l2JTyApMDhJbLY2LuvB6UkK6t4Y9hXKaIqmC39MKy7HGhm74oItG7derlzY48Bi7ineMXJE--DGKdpxgismS32aEjZaENreioojk1PRsa6sSgqcKtJUYShCXGL5o4eSZCPUDUoF5eiQp1Is_sYJlk-iraDow0EUcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/SorkhTimes/139277" target="_blank">📅 00:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139276">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHcWtPe3Tm6z7P2oytLqLPmsERhLdkFCAymGp16zrFIuMZOMrr2HjnCC9WJiniOSF-ibPYwc_upgA6vUEPDTcPa0ulOXGO4iBuQEc1Vba0Nb1QPmDWa7d5gAs-cXAeVK-_25fl6StCSAnx7L8k-s8_ZR_csu4C9mfdBSPhTzloGUTS4Q6AVBQ3dH79ywl-0M0jhPS1SON793Ubv8Pk6_BH7OVAdC7V4ngUREp4GN-yKKleTP5fEYPsa3j6ScqbhG3f09mdKM2zzgDSBj-osvRK9pJWpkkIYc8CmX_vpSxa7G2qG43SKx3moo25_UPDrlqoFf29HynCJbq9v7pCjkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/139276" target="_blank">📅 00:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139275">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPqyV1OstCYfkegq8Wn4FuB7gSlfuHH5jxitTlucatWM68vL3H_MZFNlkG-ngQ1HUbz-n7FYx-xGRg-GPJYrzGW814SPi0DCAwBeFsJRDiFxBylf5ZkztEVGyfAhRkJd1Ia8qfyT0taOPxG0XEeRnNffXTVbcIkIsdznstjAcvTaqmYGhA9unJl9iRvLVLKQa8wUwO6lRI-dsCmgROnIJiqLPcCxg-oFJYKOWBo5dveduF9E3f4Xl9vf_CVVoX8HyP18mB1XTxlWtgBX1ccxGBbgHzqHG2eSPnDPMsmd80GSHf0NOOhHR4p4sPilVQ5xX_nM_AdUMZYlqtl92ZIHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/139275" target="_blank">📅 00:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139273">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324bfbe3b7.mp4?token=IraIaQz-20Dgzz_dsLrlqth7mivL9sE6wyk1bADvHifaxFAE5B27yCGLi4tsrGvHGWl6FClDtGgA3gR9t_Ci2M0LPwdnKZk0AORcOUMeL9TatEuu1S_4OgtBkFyszUI-Sg0f6n1yBorEJt2oMWmLt5xh0Z2ZqZeSUBWp5oi-vBAXyj_jfloYAY1bW631-t2KEO3DW92svRZrrQe031vBySI1X6rmoNknmi-H9XDl_F0tsb99bBV2zDFB095TgZ3Tt4mqn3lK2tjPli98b5sn5s8BPhpeZNyaodxx0K7psFtGuMSUuuuvQy9X1w0z51U0A-dhvmKlkbsUzw9aouPGJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324bfbe3b7.mp4?token=IraIaQz-20Dgzz_dsLrlqth7mivL9sE6wyk1bADvHifaxFAE5B27yCGLi4tsrGvHGWl6FClDtGgA3gR9t_Ci2M0LPwdnKZk0AORcOUMeL9TatEuu1S_4OgtBkFyszUI-Sg0f6n1yBorEJt2oMWmLt5xh0Z2ZqZeSUBWp5oi-vBAXyj_jfloYAY1bW631-t2KEO3DW92svRZrrQe031vBySI1X6rmoNknmi-H9XDl_F0tsb99bBV2zDFB095TgZ3Tt4mqn3lK2tjPli98b5sn5s8BPhpeZNyaodxx0K7psFtGuMSUuuuvQy9X1w0z51U0A-dhvmKlkbsUzw9aouPGJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمد تقوی، برنامه هت‌تریک در آنالیز فنی بازی پرسپولیس - ملوان گفت:
✔️
✔️
«حسین کنعانی‌زادگان در حال حاضر بهترین مدافع وسط ایران در بازی‌سازی است. از سوی دیگر، پرسپولیس با تعداد بسیار بالایی از بازیکنان در فاز حمله، به دروازه ملوان یورش می‌برد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/139273" target="_blank">📅 23:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139272">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEXYgAsdw2PeYtTbHyvSLv-MZ8bqLhUc9WiknS1djBw6DHbtI7AhsU5FIpnmy-BmFUp-aRWJm6OWe9DE9mpE3Cd7VtJTPoROzfS8uJbcpsa8Qdn2N1NHVYWpin2MDMxHDQjr2DO6iQC5KdNM_rBGbef724ZDCm-qXkM3yGmjrZjjktYWvJ2Ai4m6zDfRoK5qAiDXQ2qk9xyr5oZ4Ls_bpqLpsQNJLlIWsWs1_D98GZZBKpPwVkt8Xh1YE9bsIWbnIC90TyNpV_nTFGk63TsxpqHSLzc_8x6e23bge1LBTu7tnOUBQSg9UggNa97c9o6PuvmLsr2YSWZ5pEybToiiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
وحید هاشمیان: همه اعضای هیأت مدیره پرسپولیس به جز یک نفر موافق سرمربیگری من بودند که به گفته خود آقایان، این عضو هیأت مدیره در صورتجلسه نوشته بود که وحید هاشمیان ۵ بازی بیشتر نمی‌ماند و امضا کرده بود. سردار دورسون هم به من گفت شما تا هفته پنجم بیشتر نیستی!
‼️
👀
وقتی فصل را شروع کردیم، سقف بودجه داشتیم، اما تیم‌های رقیب شروع به هزینه‌های زیاد کردند و بازیکنان اسم و رسم‌دار گرفتند، در حالی که پرسپولیس نقل‌وانتقالاتش را زودتر شروع کرده بود. بازیکنانی که می‌خواستیم را به باشگاه معرفی کردیم که هیأت مدیره و آقای حدادی گفتند شهریار مغانلو گران است، آن یکی پول زیادی می‌خواهد و آن یکی هم گران است! ما هم گفتیم گران است اما وارد فازی شدیم که تیم رقیب ما بازیکنان گران گرفت. این اتفاق فشار زیادی را روی باشگاه و همچنین بانک و مدیریت آن ایجاد کرد که تماشاگران می‌گفتند شما چرا پول نمی‌دهید و بازیکن نمی‌گیرید. آن موقع دیگر دیر شده بود، بازیکن خوبی در مارکت نماند؛ بازیکنان مسن از قاره آفریقا مانده بودند که برخی از آنها هم مشکل زانو داشتند و آوردن آنها فقط بار تبلیغاتی داشت و مالی و فنی نمی‌توانست به ما کمک کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/139272" target="_blank">📅 23:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139271">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚪️
⚪️
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/139271" target="_blank">📅 23:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139270">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚪️
⚪️
فوری / یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/139270" target="_blank">📅 23:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139269">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/139269" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139268">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139268" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139267">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
✔️
طبق گفته رسانه‌ها؛ به احتمال زیاد داور دربی کوپال ناظمی خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/139267" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139266">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/139266" target="_blank">📅 21:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139265">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔄
🔄
یحیی گل محمدی در لیگ عراق :
🔴
3 بازی
❌️
0 برد
❌
3 مساوی
‼️
عملکرد یحیی مورد انتقاد شدید هواداران دهوک و کرد نشین عراق قرار گرفته زیرا که دهوک بیشترین هزینه را در فوتبال عراق انجام داده اما تا کنون بردی به دست نیاورده است
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/139265" target="_blank">📅 21:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139264">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
حدادی: همه باشگاه‌ها باید به تیم ملی امید کمک کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/139264" target="_blank">📅 21:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139263">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
سه پرسپولیسی به اردوی تیم امید اضافه شدند
❌
❌
پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن تیم فوتبال پرسپولیس، به اردوی تیم ملی امید ایران اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139263" target="_blank">📅 21:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3uwyJmPCvdarurk-jx7vb3XTynU9Bc9mflIYwl6_oWIS5NIngQRE67qqP-MArKbe4aabIIFZsgPDoiXTzjTsstZLVZP87rxOptk1HN97nBpxeEYvykX2xW94h7UWLTQA9D15cm3tIb6KsZrHarhtg7GY6WMtweK1pAXLRNLaPamvoZFf9ma38jcv6IP18fPP0q9Il-bFN_jTdlOeRX5EgqOG7SyDi2twh-QsfWCbGBBPgESKy_JypOeMLEySRks-vsE7aVJJgWXDhePTvwclW_CBJ0aALTkndnJGXvgbfmQNlmj6hMCHjIweS9a77CFhDbPcEeqitQmDD93QmEVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
منچستر دوباره در مسیر برد!
شیاطین سرخ مقابل ایپسویچ؛ یک نبرد برای سه امتیاز، اولدترافورد آماده یک شب پرهیجان
[
منچستریونایتد
⚽️
🆚
⚽️
ایپسویچ
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/139262" target="_blank">📅 19:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👾
تیزهوشی و تلاش علیپور برای ثبت این گل کافی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139261" target="_blank">📅 18:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
نگاهی متفاوت به گل‌های اول‌ و دوم در برد دیشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139260" target="_blank">📅 18:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139259">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
🔴
دو گزینه اصلی قضاوت در دربی 107
💢
کوپال ناظمی و موعود بنیادی‌فر، دو گزینه نهایی کمیته داوران برای قضاوت در دربی تهران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139259" target="_blank">📅 18:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139258">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGBHNRwCsIS6Iobd9br8mveqVQTPu-slVHlFOHeProfSEj3P1eEYfTNdjohGuD-Gxe0QC2n2PBzP236-d3tTiMMy_K23YABOUZN-ZUOm0xhqKAu6fsDpIn8dYL8qPDke9rDkhMa-pWfWFpjasWuZqD1JcyIO7nDiCIguOmilUtPS1Vi5ZxSjaxwUDZoe1vwplBRvg99A3XnKY5_KBZka8_mThBVanlv4XG5ZbUlkXXOuILYdmF_m4wmiR9LHpnIj0MQEJUvdUuBdjzioDco4fMCUixaZ16LCB-w1zSWcaSn5fFfKXGo8MLboEAzlASn-SYmIenR1_wHb5Bnek3wMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئال مادرید آماده یک شب متفاوت!
⚽️
مالاگا میاد تا جلوی کهکشانی‌ها وایسه، نبردی برای شروع قدرتمند و یک برد شیرین!
[
رئال‌مادرید
⚽️
🆚
⚽️
مالاگا
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139258" target="_blank">📅 17:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139257">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139257" target="_blank">📅 17:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139256">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
عبدی : من زارع هم میخواستم، پرسپولیس گفت نمیدم. هاشم‌نژاد هم میخواستم که شکمش رو عمل کرد. کوشکی هم جواب تلفنم رو نداد. حسین‌نژاد هم بعید میدونم که تیم خارجی به ما بازیکن بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139256" target="_blank">📅 16:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139255">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
با 5 بازیکن چگونه برویم تمرین کنیم/ می توانیم برویم گرگم به هوا بازی کنیم اما فوتبال نمی شود بازی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139255" target="_blank">📅 16:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
حسین عبدی: 23 بازیکن دعوت کردم فقط سهیل صحرایی، مسعود محبی، پوریا شهرآبادی، پوریا لطیفی فر و دانیال ایری آمده اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139254" target="_blank">📅 16:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
سه پرسپولیسی به اردوی تیم امید اضافه شدند
❌
❌
پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن تیم فوتبال پرسپولیس، به اردوی تیم ملی امید ایران اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139253" target="_blank">📅 16:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
فوری/ با اعلام مهدی تارتار باشگاه تا 22 شهریور بازیکنی به تیم ملی امید نخواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139252" target="_blank">📅 16:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139251" target="_blank">📅 15:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139250" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139249" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
تیکدری دفاع چپ پرسپولیس در دربی/خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139248" target="_blank">📅 13:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139247" target="_blank">📅 13:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">☑️
پرسپولیس برای دربی اردو زد!
🔻
با تصمیم کادرفنی پرسپولیس، اعضای این تیم بلافاصله پس از پیروزی برابر ملوان، راهی اردو در هتل المپیک شدند تا برای دربی ۱۰۷ آماده شوند؛ تارتار بعد از کسب این سه امتیاز به تیمش استراحت نداد و باتوجه به فشردگی رقابت‌های این فصل،…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139246" target="_blank">📅 13:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139245" target="_blank">📅 13:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139244">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrunHVUHnhkNF2NMzNVqVqEXA-FpW0nOCwfTk4NGzGd9uG8mouXdrqzTBCFDxICvTVvPBGCk1n1pud57o73Ikc52XLLdruvPLtaSu5wTw7j_aeFxCMWCfDuQ5H68f8Ly5Aj6r4OqSH_KfNFHbOmfjMFUsH9_31JTQfe4TGil2x0Dh2hrKpSlzRh1RyJBZYPzBQigc6zxjhSycpyq9HxX10af0__9aH2kIrXUi4o1Pjl0kgPsmnp60V7AQwLhdV5RLeetZ43Cxo4R1lXKIC0JRwr63uuRPZNjaPREzISLQEXhTDvdz2sCn9rDvhaz22bCi4u4yXfouf8sfz_pZF1GQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی علیپور با نمره 8.45 بهترین بازیکن بازی پرسپولیس و ملوان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139244" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🗣
🗣
با تلاش کادر پزشکی تراکتور؛ مهدی ترابی به دیدار با پرسپولیس رسید و از روی نیمکت بازی را آغاز خواهد کرد. هاشم‌نژاد غایب است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139243" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mywPe144r2sG5f8IPj1CVmphPt2RGApa8AToPbYb-ASeisApuN4Q016gq3adGAHz6g3tkIDg_XAe03nC3MIlCgSqovBIiu4KNET0a5mi4eescDUfxDAAx2nAvMzCdfONECHCZLhyFnvjEpq3Wmzw3_bKY7GKUQxdBCqqNbq89U00vQtgfjZjbUVqpgfcTnU_HyDGcENQep1H33QcfAkPmlfb_iCkzFU7yS6qw6gHDLafA6_IV75-xo4LShHprLqTfeHYc0ZyXMAIXJlpPvuXLYpiNuATJmzxT1mQKWbGDPPbpSFUya9idNcMaDKPHkO6m6XyVV8v9D9Q2DSnxAS-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در آستانه ۱۰۰ تایی شدن ؛ علی علیپور به رکورد علی پروین در پرسـپولیس رسید و به دومین گلزن تاریخ پرسپولیس تبدیل شد
✔️
✔️
علی علیپور با گل‌زنی در مقابل ملوان، در کنار علی پروین با ۹۵ گل زده به دومین گلزن برتر تاریخ این باشگاه پس از فرشاد پیوس ۱۵۳ گله تبدیل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139242" target="_blank">📅 10:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139241" target="_blank">📅 10:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1Vk-3CAFNv9tqIquyuN03L2zLT9m8UQDVITwnHQ9g9rh8dbWos15f8HSobDgWp2EyNN78eEYgHE0x2L3V9W5VNwKT84LTplm_Fr_n1Yx5YXWmPBdDTGdMTWLROCP2bVsGu2RAQ-vokrNnpmfUOqHuYEJZRrcBvWpKm3YTC0Os8ZgYuna_SsgBovgu1ky-nb3rzKN1VptPB1dBDSB6wr9jtMVvl9JUDU9eHkS6KBSC-Nktd8sHI77rcVVVr6lX55hJg8VuNF9FHycOEeSUN58kP592ohF1VlE5S0ownJcTM0dIDXbbwr50uvZOI18MQzx5dTMdw2k5kbW7sRw_N3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139240" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139239">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
اردوی پرسپولیس برای دربی بعد از بازی با ملوان آغاز شد و بازیکنا به هتل المپیک رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139239" target="_blank">📅 10:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139238">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139238" target="_blank">📅 09:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139237">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139237" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139236">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139236" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139235">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون توی ی بازی جذاب و دیدنی بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139235" target="_blank">📅 08:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139234">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clB09SFqqre6oQ2O7ifCYQxaCnzhU4pkbPpPHg9HVlWIp_-Ng4FGXYVlzt9cHOnI4fUBJjwnzGeWEE5Zy6UEz-UX1WPEaRz6fYny-kQLB8NC733Ut2cmh6zzXOGNqM_JcPZdIU_rbCWKZShCYqeMs1IGdl33aMgkLP8b5cr5WOgW_iA5-QS2cOMRYdquH-qj07kLLL7D7BkQrblODWtAt05UmmUc3aMT0lcKv5om556jyvlM5O3RoRIkwMGT15rt-4ZnAW2sf90dYO9-pcGPQ0QiUZT6IZFjNYuUne_32ZfSVUvCsxqMJupyg8Wu2B-GAAVLZ8a2K2Ro9ogQ6bWoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139234" target="_blank">📅 01:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139233">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139233" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139232">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139232" target="_blank">📅 00:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139231">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
دانیال ایری امشب به عنوان بازیکن ذخیره وارد زمین خواهد شد تا اتفاقات دیدار با تراکتور را فراموش کند.
✍️
ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139231" target="_blank">📅 00:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139230">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139230" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139229">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139229" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139228">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJvAh6JBUX7zIQHM0Dg1SVRAIcwUh-u4kOSXT-NV_S9rUtdZe37QiwVd1pAUAt73Iw2tjJb4JqFqETQYJBJaA8iBPPQr5JWaLCS8C3WKVxTzh3rBjOlgZ6yAPKrXuu_VSrjayasOCsU1e2OGab3So8cCndSJ3FePQAC4vkkQq85Qbme6kS_8AXL0IVlyKH3vH4m3dpIJWd7MkavqrgX_r-yEE31GkseL_t1DzUGlXXeCMOx_EUxBeI3RHB-ruVdGflNtD4Zp4J-3wJ5q9PPCnA9wJzqFSXcbln36znv9KF5Dgm8HHplNrU9M87lC-hGL1zh7RREOzUpvMt_beDgXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139228" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139227">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139227" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139226">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
کریم باقری: پرسپولیس از هر بازیکنی بزرگتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139226" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139225">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
کریم باقری: نگران نباشید. پرسپولیس بهتر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139225" target="_blank">📅 00:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139224">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139224" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139223">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
آمار برگ ریزان بازی
🔴
۱۶ شوت
🔴
۶ شوت در چارچوب
🔴
امید گل ۴
🔴
گل ۳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139223" target="_blank">📅 23:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139222">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
🔴
علیپور با ۲۵۷ بازی، از سید جلال حسینی با ۲۵۶ بازی عبور کرد و به رتبه دوم بیشترین تعداد دیدار رسمی با پیراهن پرسپولیس رسید.
🔴
علیپور در ۲۵۷ بازی خود با پیراهن پرسپولیس، ۹۰ گل زده و ۳۸ پاس گل ارسال کرده است. او با ۹۰ گل و پس از پیوس و پروین، سومین گلزن برتر…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139222" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139221">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139221" target="_blank">📅 23:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139220">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFKOWCVDsKvKI8WJILJvOZkVB_UrzK_6baaLR8ogdpsEndJm4nZES8bIi544kpxIqD_mmLvq5EFd9ClVXoJPVjSNdx49qnvqTY6AP-5LqaHPkTwuPZ1TlU39vzW_Jj3OHhlPJV2UlIjwQPaD7E7U2fmbkM7ejhNVUtmqbGPLP7YbjTT9rq20rpJRfY8f8-6SVd6tmXVg5s8aDpFJlkruKkTkvlJS82zLx0yFf_JUaLU0EfhOjTXIvvbbYkRhHNFjf_m-y6PwY-m6cbn-o0I97PkOVj-YvRvGq_Dfmwl-9JepnvoPuxVo2dKm6VUVYyjhQxs_aIDlSTEkMGxbqXn7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
ستاره این روز های پرسپولیس تارتار
📊
عملکرد بیفوما تو این فصل
🔄
4 بازی 1 گل 1 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139220" target="_blank">📅 22:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139219" target="_blank">📅 22:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139218" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139217" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139216" target="_blank">📅 22:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139215" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRxLw6AgQpxl3Ppb5mZUP2FoPKuOcMcXgqer_mV0_Z_3vUiPRjqJYxxeyO52hH_0ZfLmZxrP9itwl-ylwprN3MnD78Y99781cOFGAr7GbmuTT_9GNi-RT7lHiLSa2bl35pBMKCU6tBObGO1kyFjPVvnEAabpxZVY3ic3SuTMZTi22f8i5lNKAakOgLQZ1g9XeYjApI9GH0xPYPbyUU75lHP7VpAi-seL035z2TeKVhXl9zxQTRRGiuzzeyazqUfRNDTN8y0Tg6ugYhRheQ3tSgaYLDb_QH3Gktnzvjo7r3LnQl6aF4-MlQscRQKxntazWoG6OetaEUGEHn9zg38jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
پیمان حدادی بار دیگر این استوری رو گذاشت/ حسبی الله : خدا برایم کافیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139214" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به دلیل افت فشار در نشست خبری بعد از بازی شرکت نکرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139213" target="_blank">📅 22:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
گفته می‌شود فردا نیز مهدی تارتار برای دفاع چپ پرسپولیس از علیرضا همائی‌فر استفاده نخواهد کرد و مهدی تیکدری در پست غیر تخصصی بازی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139212" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139211" target="_blank">📅 22:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=S-NqrQVNu1CCplu2NR7Z_pw_6tyYKcGIyZlgFCAvn7QyAanFphyGQdoHWdfKF7MDumAcWk5f33cRht68UYrh-SQ5MIy1TiGQHSvbYRrZJZimu7KbTw1GyMvRrcMXQl9h26zhMxerbRmxhKPYw0Z4m-QJkS8ePw1F56-2pWu09eQE1OCXwVBKgEpJaewm3ie2QtpCS4sXiye4hY7bgcfb9WnEUU64gOtnGYxcXJJ07d7DjbTwvTKj-GI3E5VlIgq9W6XwbpnqRac0_6xiEG-so6qwj9bhoVTfEz7jpKi9G9RlnH0vmRJY8Mgvt7KCyTRmsvunoi1490NlgTGR5ywjfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=S-NqrQVNu1CCplu2NR7Z_pw_6tyYKcGIyZlgFCAvn7QyAanFphyGQdoHWdfKF7MDumAcWk5f33cRht68UYrh-SQ5MIy1TiGQHSvbYRrZJZimu7KbTw1GyMvRrcMXQl9h26zhMxerbRmxhKPYw0Z4m-QJkS8ePw1F56-2pWu09eQE1OCXwVBKgEpJaewm3ie2QtpCS4sXiye4hY7bgcfb9WnEUU64gOtnGYxcXJJ07d7DjbTwvTKj-GI3E5VlIgq9W6XwbpnqRac0_6xiEG-so6qwj9bhoVTfEz7jpKi9G9RlnH0vmRJY8Mgvt7KCyTRmsvunoi1490NlgTGR5ywjfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139210" target="_blank">📅 22:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139209">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=sE1OIIgIBM7-gUui6vTT5Cqzgb4jII1raC6AIUILmDCobe5UXNuBNm7M5EVKnbyLQvEdCBKlNYgfd3fLIxFhk1WF4qhKCjiCDmP0lLal32ZogJzV-NRosA2atqTTjzZe01P_U5q7YmN_HUhex2jBe2RrkZ7_IeCf9SHmo83pEaBr8GZO5p0oHJ0T-VNoQmQkMHG6cWFj0TSpG67Pph68Vh0nEQugIP2kzq9H7vhTHoc3wTnF9t35_voZ1vJI7_coWXYEn47ZOjlDFiHi-sN7iLyXI2CDcgzCWZQepnJov2FnETTmcukOBWXiWHSjbqiJbuaRe7lWtnTgsh52bk7k8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=sE1OIIgIBM7-gUui6vTT5Cqzgb4jII1raC6AIUILmDCobe5UXNuBNm7M5EVKnbyLQvEdCBKlNYgfd3fLIxFhk1WF4qhKCjiCDmP0lLal32ZogJzV-NRosA2atqTTjzZe01P_U5q7YmN_HUhex2jBe2RrkZ7_IeCf9SHmo83pEaBr8GZO5p0oHJ0T-VNoQmQkMHG6cWFj0TSpG67Pph68Vh0nEQugIP2kzq9H7vhTHoc3wTnF9t35_voZ1vJI7_coWXYEn47ZOjlDFiHi-sN7iLyXI2CDcgzCWZQepnJov2FnETTmcukOBWXiWHSjbqiJbuaRe7lWtnTgsh52bk7k8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139209" target="_blank">📅 21:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139208">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJtZQGLgmDSX175CKi7i5sQtv7S2barp8q7df0Cpdkh7PxUUvDfEPwUS-qkYzfH4ipejvNnaon29dcXpBJNl2oVWXXvZNhAddWGoWXZGiTulA_Or89ia16Z-MgnxJk8lU2LQXDRwDihEREb9PL89fOjvW3iDAnVwau2sda5no7HxUTlLP4kU6BGOaxcnqu7ZS5n669NIERvT2w20O5tzdE-sO3RFAnsN4zBH1kMcNzvKnOA609j2aV20gfEXzzxsOp_DHztDr-Ob3AJ2iHUvIRBL3Bz5nJKa2-NFwCXRYEX_MRDk5U3DsUm48DQBdIJ281T_QsMd9gd77fG9i1dbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139208" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Y7ypnq7IzAScWsk67KDgBwgNxG9_iVJrPH17WpXsXnHY72VtOLSKj3tUKguYco1H85qdt2z2hjI-C1l3S0LBMdKDFENvYNkZYRC3pRvQcVaEy6l-zWgsaPxQLDts9OqWYXv_o_SqGaaL0x0hlt0FJSvyWAgqpgSwyqEv7aAEqIqMgdARn-TKMbgH-ZLUvvO6tWl_XQ-MPZlj0aju4JswICXOG7STEzq7cDMHszntv5X5EUZfY3z-r5pJVS1z0xD_Solzs64NeVL9EvuyFppJZmJeFrEIzn_uqHyKLMV67hrLw07IZzP6eYipP31lNk1Etgs4Ckdl8QmmvJ80k_O88vE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Y7ypnq7IzAScWsk67KDgBwgNxG9_iVJrPH17WpXsXnHY72VtOLSKj3tUKguYco1H85qdt2z2hjI-C1l3S0LBMdKDFENvYNkZYRC3pRvQcVaEy6l-zWgsaPxQLDts9OqWYXv_o_SqGaaL0x0hlt0FJSvyWAgqpgSwyqEv7aAEqIqMgdARn-TKMbgH-ZLUvvO6tWl_XQ-MPZlj0aju4JswICXOG7STEzq7cDMHszntv5X5EUZfY3z-r5pJVS1z0xD_Solzs64NeVL9EvuyFppJZmJeFrEIzn_uqHyKLMV67hrLw07IZzP6eYipP31lNk1Etgs4Ckdl8QmmvJ80k_O88vE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
دانیال ایری، بازیکن جوان پرسپولیس به سمت هواداران ملوان رفت و به هواداران تیم سابقش ادای احترام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139207" target="_blank">📅 21:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMQn6kMEs_D-xUvFsoBj1FGrCa6k4J2H1bp-44jdhxLjY724l0of4TZYNozCBbPPdP7oW3dVy4j-cXcAUAx-dpr5e1QXr4m5LFEZ3ooMblzggvg5tMl6E9lSCNMORM754rIWeZbwLqjWMHwjqs2rtF57-NrdcntFd3DqqE81BTOKgNMWHdxwptXGqJmDO-cOZ0IkwueWXRw7eRkf5DWt1Sdv681Qq3PHCbej2Hn2ey3d4NBOPyMdY5gzTIr6p60HVSBjjE2cN5SgY_owMGUfcSxCY6eNOBN7jU6E83BNcygvXEfyY0--euVB8rq7X1bPnITpQvJEGzLJ05ijcZDFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139206" target="_blank">📅 21:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139205">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=KZQmRfA7vl0OjY5HxqHaKiT3J65b2NplYF4ledp4jHpLoo5Uo73-gv7Rl_H_kN40G_pMUFWaZ4v_WHPD0ufw4b4tuNCP-HMdTs-ELHLKIFwmRD4tsSGPxY25Mkc7xZVhP-wYPvJbArZzY4uOc3OB6A8l1Cth1hiiKdnNMH_PJz0zlvRbNY-ZUt3p_wIp5-6F5C_Dnlobc3Xl_gdSYyGOBmkK--aL9ZRsdvh04wfo81kic5ST9oecRALblKeAWfuGI6anjLHjlj52FsyJc0u-EUDmwGJLNkqR-47VlRFuaZP6JkhwDqNkYd92j6507rc_QDZbBtzFuzADPQ3npeoA1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=KZQmRfA7vl0OjY5HxqHaKiT3J65b2NplYF4ledp4jHpLoo5Uo73-gv7Rl_H_kN40G_pMUFWaZ4v_WHPD0ufw4b4tuNCP-HMdTs-ELHLKIFwmRD4tsSGPxY25Mkc7xZVhP-wYPvJbArZzY4uOc3OB6A8l1Cth1hiiKdnNMH_PJz0zlvRbNY-ZUt3p_wIp5-6F5C_Dnlobc3Xl_gdSYyGOBmkK--aL9ZRsdvh04wfo81kic5ST9oecRALblKeAWfuGI6anjLHjlj52FsyJc0u-EUDmwGJLNkqR-47VlRFuaZP6JkhwDqNkYd92j6507rc_QDZbBtzFuzADPQ3npeoA1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تشکر اعضای پرسپولیس از هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139205" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139204">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس ۳ - ملوان ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139204" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139203">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
به به چه فوتبالی .چه پرسپولیسی ...سه گل زدیم و شش گل نزدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139203" target="_blank">📅 21:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139202">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
تیم  دقیقه 98 هنوز تو حمله اس و تک به تک نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139202" target="_blank">📅 21:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139201">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
تیم سه گل زده هنوز سرتاسر حمله و تشنه گلزنیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139201" target="_blank">📅 21:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139200">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
اورونوف هم تا اومد تو زمین ی پاس سکسی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139200" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139199">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
بازیکن ملوان اومد تو زمین سلام کرد و بلافاصله اخراج شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139199" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139198">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚽
🤩
سیو تماشایی پیام نیازمند…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139198" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139196">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6343db8016.mp4?token=h9OOUG0l6wY8zJQMObPLdZxlA1kQOJptXwsLRfXRhk0jf68mdFoSriMa5GVq9hGgb4gSiS-PRh0kjrc0lU52Tj7ZiMCe3uVO_-fsBre440rmvhGG7Z7MLBeREpNQ9CEywBFShYD1K1BnEky08G_kls9XSGuHf-v6ieFcKfhE-dzHTmZ3eJ5AQ0rop0CP4EZR80fwOs8KzKlszF1yLy0FJJrY7lC4mr7k09FXjs7vlVTVKgZhHFhloW_6Kd2cYtQqebRvXUq3aaF7Evs3MoA25arr-FlxJRWOkNpcbj93Leb_rIGN9_TKBV2yZgCE8rcPvlAoXRzd8ziayqMXoz_cHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6343db8016.mp4?token=h9OOUG0l6wY8zJQMObPLdZxlA1kQOJptXwsLRfXRhk0jf68mdFoSriMa5GVq9hGgb4gSiS-PRh0kjrc0lU52Tj7ZiMCe3uVO_-fsBre440rmvhGG7Z7MLBeREpNQ9CEywBFShYD1K1BnEky08G_kls9XSGuHf-v6ieFcKfhE-dzHTmZ3eJ5AQ0rop0CP4EZR80fwOs8KzKlszF1yLy0FJJrY7lC4mr7k09FXjs7vlVTVKgZhHFhloW_6Kd2cYtQqebRvXUq3aaF7Evs3MoA25arr-FlxJRWOkNpcbj93Leb_rIGN9_TKBV2yZgCE8rcPvlAoXRzd8ziayqMXoz_cHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
سیو تماشایی
پیام
نیازمند
…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139196" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=l58ZOhu_LWll4vg3jO7NHbKPdzRY6V7y9ijn4sPIrNf05u24W2FvdPAmcsHdDyrzvgBeb_VieVkwEkYuwalm0ybfw8JNA3nTfspH4deGQ4oIsCjMrLhP8HD36XkdlHf0Ol4jLUL7tB9SFvIFpRat7UQ2cPM0Cr2kJFJfeSwxQS_dbY6UZLJmPwgaseveO7kiyy9tGWs9zJ9tATij3dVwIVIM1ky7URxYKmAz8hIqBycg1ZzWMI9rNBL1d2xOSLNJx9VwVTEymQExxHio_6ZeJh8XbPyI8c-c6fyAmqGtzWt5EcMvA7iMZlngVAha0qRsO98vMKG_7hmTnisEDnbceg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=l58ZOhu_LWll4vg3jO7NHbKPdzRY6V7y9ijn4sPIrNf05u24W2FvdPAmcsHdDyrzvgBeb_VieVkwEkYuwalm0ybfw8JNA3nTfspH4deGQ4oIsCjMrLhP8HD36XkdlHf0Ol4jLUL7tB9SFvIFpRat7UQ2cPM0Cr2kJFJfeSwxQS_dbY6UZLJmPwgaseveO7kiyy9tGWs9zJ9tATij3dVwIVIM1ky7URxYKmAz8hIqBycg1ZzWMI9rNBL1d2xOSLNJx9VwVTEymQExxHio_6ZeJh8XbPyI8c-c6fyAmqGtzWt5EcMvA7iMZlngVAha0qRsO98vMKG_7hmTnisEDnbceg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل سوم پرسپولیس توسط علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139194" target="_blank">📅 20:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
نیمه دوم نکشیم عقب پیروزی پرگلی قبل دربی خواهیم داشت‌.......
✔️
✔️
اقای تارتار یاد بگیر اینجور شجاعانه بازی کردن رو تو بازیا بزرگ نشون بدی
✔️
✔️
همینجوری جلو استقلال بازی کنیم بدون ترس پر گل میبریمشون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139193" target="_blank">📅 20:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
بریم برای نیمه دوم ...بریم برای زدن گل های بیشتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139192" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=tOIhJOUT_RDfQUHoMD6aB4iDPdUwsUN6UuQAJYo7ZBQ2batmPFu7heTofFdRdsIj75ILxdOMAHx4-wBFwX8uImwvguLeOgZ3_K-mG8D41V6yLlut9cuVT37mXaW00RbI0ywK-wRxpOYGAuRGY58MxXKk_EYcQfw35yHFMBBOqMXBBr5mIMDYApd4F13MvDntzZECJGy2BfVWc1qJq_XYINaTlgkrfHYWUYyLw6DidsSksCAgUd6aI8cjWijdkrN_SKgZFSvjg5EdOkPrj6SbEHCxVO-XrCV4PD3CQ-oYAe3QRLmtHtukferCFiQRcUn0APeWDEx1nrfg7_9QLKAzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=tOIhJOUT_RDfQUHoMD6aB4iDPdUwsUN6UuQAJYo7ZBQ2batmPFu7heTofFdRdsIj75ILxdOMAHx4-wBFwX8uImwvguLeOgZ3_K-mG8D41V6yLlut9cuVT37mXaW00RbI0ywK-wRxpOYGAuRGY58MxXKk_EYcQfw35yHFMBBOqMXBBr5mIMDYApd4F13MvDntzZECJGy2BfVWc1qJq_XYINaTlgkrfHYWUYyLw6DidsSksCAgUd6aI8cjWijdkrN_SKgZFSvjg5EdOkPrj6SbEHCxVO-XrCV4PD3CQ-oYAe3QRLmtHtukferCFiQRcUn0APeWDEx1nrfg7_9QLKAzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
علی علیپور موقعیت خوب پرسپولیس رو به بیرون زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139191" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139190" target="_blank">📅 20:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adad84121.mp4?token=COKGu4RPICzIF8xPaSWsQjB4bqRgkmn84vley8YwUSg5ZHHXTuD_UZa208_HPFiPoeTSqRC5YkLCBDk2aZtZa2vZ1Q4afUkMI1G74qZGIA7SKmvCecXVA2hyiIw_5spunlA_7wMbk7gOZdjisn1kZQ2zxLYaGgRdcvfT3MS9N6KRmQKRmguuyuxKwwaSyelAlTlB25iSHJG0zUMc6MyCoNCIRHLhqdWAJEwNPC-MOzSVJpzpdQb-b9_iunAYc4ju8TZkrN3rFjLMncVHn2C4htDoeDFBGeqnHah9lOGNh1hmLvN3SJox8f3uOp7uCDkKU_2sw4DNVTvwaKveLzpI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adad84121.mp4?token=COKGu4RPICzIF8xPaSWsQjB4bqRgkmn84vley8YwUSg5ZHHXTuD_UZa208_HPFiPoeTSqRC5YkLCBDk2aZtZa2vZ1Q4afUkMI1G74qZGIA7SKmvCecXVA2hyiIw_5spunlA_7wMbk7gOZdjisn1kZQ2zxLYaGgRdcvfT3MS9N6KRmQKRmguuyuxKwwaSyelAlTlB25iSHJG0zUMc6MyCoNCIRHLhqdWAJEwNPC-MOzSVJpzpdQb-b9_iunAYc4ju8TZkrN3rFjLMncVHn2C4htDoeDFBGeqnHah9lOGNh1hmLvN3SJox8f3uOp7uCDkKU_2sw4DNVTvwaKveLzpI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
در بین دو نیمه اورونوف از سوی طرفداران پرسپولیس به شدت تشویق شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139189" target="_blank">📅 20:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139187">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139187" target="_blank">📅 20:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139186" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/139185" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139184">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=eCAA9APGBcKxb5AqvsnJ_9hHCfRC82BjETTUvlrJ4FJCL61-BZ7FXbSKYTcjOl6XkrgOiqALVjKLpibcUM66YkQinKrSmyKRsS1dhpuo0Q2zxgdIWzFZxvkSAHgMg0OvTEHg3TlvsjhQLyx2KZoH7RuDTAUqNJoTZNn3-0dE9H3P7lioOouhzFyOv_8FM8GaemZcR7oxOWLDMs-XO1dcK_EiPUuQZAkl-qxcVR0aX9UDCWZVH0_mCuU5at1YxOsFabv9Cfjk6I3NMiJoqSE6Oa33lvllCxJL3gY6RdQoDyUUfezv8eN-yAhBg8ktahwlxRbxpsdygRNyJEmHAJxH0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=eCAA9APGBcKxb5AqvsnJ_9hHCfRC82BjETTUvlrJ4FJCL61-BZ7FXbSKYTcjOl6XkrgOiqALVjKLpibcUM66YkQinKrSmyKRsS1dhpuo0Q2zxgdIWzFZxvkSAHgMg0OvTEHg3TlvsjhQLyx2KZoH7RuDTAUqNJoTZNn3-0dE9H3P7lioOouhzFyOv_8FM8GaemZcR7oxOWLDMs-XO1dcK_EiPUuQZAkl-qxcVR0aX9UDCWZVH0_mCuU5at1YxOsFabv9Cfjk6I3NMiJoqSE6Oa33lvllCxJL3gY6RdQoDyUUfezv8eN-yAhBg8ktahwlxRbxpsdygRNyJEmHAJxH0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
مهدی تارتار و کریم باقری از گل انفرادی بیفوما به وجد آمدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/139184" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙖𝙢𝙞𝙧</strong></div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139183" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139182">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSana</strong></div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/139182" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139181">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSahand</strong></div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139181" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
