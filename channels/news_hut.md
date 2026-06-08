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
<img src="https://cdn4.telesco.pe/file/jwa-aGPNbzZ3bHB-Hhx__1Av4pwuR4mBTOGMKUVXnD3aZd0dNnj4uY4FQDnzBeYn7aplP0jhUpfHIrWY85IuIl0ph8s7h9Ka9KrOulKjt_qgl4nGo9rzNwmCUOQmRMxTFdCrFMbX8tvI0kv2--qiMuKeriVBoHynElbGYS1KOsZbXOuvny7cWIHeeqLNRDoFboiuy5JjKVmcDE1RqOuuN2dp3Fz9VA8di6p3xAGBBJEPvLnzY1ZVlYrJjAIPUyIW8Q_4Mo8jiOUgI93DyfL9TmXxepE6i-HjhxWhy6l1JBoYVT4X-Adifqa5nLHPtfMk09u3oJYSs-TlqcFdopoVPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-65452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoltcB2dRwVE0_h56r2I2vudF2mFPSxNUm1pnf00z5syucIxtDMsQoj9p0h7Z190ofC4I4LTV5GITIvfDQp7g5gq0pzsrsd4CmNB4zV2BVNzqKesxtXqhgNLIzNIIo6yiD0fq1C67jno5oylWwGoIkKxilY4RH0dW52GBt-SoWepOxY1iuzQHI3NE-ifRuKMN0zgv4rMbabM4Pcnqzqzk1QaXexdPxYllh842NAD39WOas_xq_xM-oAKNbin_llIgNBCWP67WiwF7T3QfRLWUbedZckgqe9iMvKAx5VCD4SPp_QqG_Jf1dDE_GFONBuceu0bZUS3IQFcqX_l9xiSEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN22t3xj6yzPBzLB93OhDnAb29rwZmhJMHSB609aXahQ67hG4de6hjQ5SsDI_2PKz3hnD_FU_po2yTUWek7RaWmhJaZjMuGGh3fTTPkDaygcucWxVNr9cJX7Dx034yqZzRRWDyOOd5D0dZ56rdYTnHpzrluOz61T9FOwKONhhPHNHzN2YHEM_HN5BaiR3F85_nsmj_4hxM5PJ5AJTgd6LbJRAQuskBaLnN_ZP17PcKuz2SdpLg11Do1DUCqz3qGG1hhcN5iu8ZhN_VwNJ10J2zgcVWwOsf9g940baFmLvv7F3FdPGZ4jXpJ83uiGmS2FVS23bbLOPV1hSr_jh-k2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjAzZ-qn0i08yO5pcXCKk8XPg8r5Hvi_pv0KyncpfSVo1Cw2lOTfwteJZr765samUOlp28LbJOT33v9HoEngquS8UayJS1fD6rSBhzra-6S7mEf4BhJr-Q6Jta0XM4KcplEEi6T0S4hZ3k383U5Mu8RGsM-0w-VZFwWzud4gnpjzsdAXQQ77-91v1Lse85TBUasJqD0Y8tB2ZqucoGl9oQgkNms34Y5hfaLCqVNpZc8gIChC0axfXc09LwQpGbfR0sy9Hs0m1HLM5WFQasCFUUCPQm82ILREBzeZxEe11dA_GaOA7uQLd-LkiS4meGnqxUtlpbAb4Hf13SChB5wGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0wAoZrZx-rsCyftKRq66dscVN67uix2mmx2xJLcnxkXbybxi2lA0bNfu_eOTafl6cW_fRAATR-nrRhqJqgD1jM8-hMHMkYrQdeC7OhfPj_8QZaNjEqObVnBTEsLk64yxQpkkaw66QuZNgrjC-xEuFFdExD6Vykz6Q9Hf1LpyvORsiZ4nQ2yFBTxQFBBKnm741FGk7qhHe41aGqn3XmBSSM7g3NFlSN4RTWxtB145_0KdmWxouemYacVQZQ9xCB6_nokIq9gfUdZDmOZkD63yFculVqonKSxd0kjF5iqivWfaJxPc5ENpLRZtm2Gzr3uWRaPu9skEGm-rVXD9MKw8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/news_hut/65452" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65451">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگاعشون
⚡
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/news_hut/65451" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65450">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf7gLoue2fl_hMpIhShAdDhetERg00nT_ylh5E21oeurHPvqK-Kq8_8m6v_Uxo3muWR8Y3yJ8Sevy2mq6P9nSeVEUQrUJFZnXP6bklz0UBCWJrml8Z-0NZEO57ydU4WHSyPyt5VWUq6tBZLAyS6Bx7810K9sFr47hN6QFpfxoaq3Zs_K5j3rIvfadyk97K9lEQfsK_u-AIpJ_Fkpt4Ec73CzDXnICDMnIiocxZ5l5Nb4uqaJvxsgiZfokXnobyI-iAB4_gkGy9hT96d9wnmtwMaNDMEWjjJ9SkK93vIn2Lyehb1v6_aOUiKK277DrSfmnqMZEFjG9uIOXEIHaHqS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبانی
🆘
کامل در لینک زیر باز شده است، برای دریافت آن کلیک کنید و عضو شوید
👇
👇
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک را لغو می کنم
❌
❌
❌
سریع بپیوندید
🖱
سریع بپیوندید
🎧
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/news_hut/65450" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65449">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD8cYoM2OEQ7nlgB0WI-GkTQ65gO-N_aVHncI7c98Bker6RQSOk1hDIHLDzhGPlvOXA4vDqAUTwYFB3qKWtonkPb8Qt83RCNOZsROXMnmjJjjnPvJwsNPkXUc8vQl0z_R5oMmNyFoC73V1zasOyxsHcN3ypo1w3P9OE1C5VGaKllp_em2tVsrLNXPHgM_RUpNl-iz6d75QVeTNANjb_7ZzbVxK4t76s2W0syXmqTLkyrStnJoqch5Aa2hieS9fqzDn3FOhYAVju1GPYbXCf0dTuzBEt6c1jVNBkBzn8_Yb-TJr7i3CHt2Uwcot3Zjxi94G6xyYu8L67_9lHmqM8bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره با قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/65449" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65448">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/65448" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65447">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cty0FMP1N6CqCSDjz4dz6Do3tduzTItGQNUypcj7QzwhkTjBLVlmcjtFKlNPE0v_daIrrQ5YEv4jGBYBPzjbevyRdpBklSO3hBTiOXtfxm3t7231glP33mTjhnKE_y8WQ-kc9wMclzRfCTKQykAgy09y8jlZH_ZuCoruZJK3XgfXifjL3f5_fcWbV33ywZ5XS3R19Vs8B9WZqQPE1JvgFFm3FN3tZc0oe-POIuHVjjGg_tC8vmRsemzdLP3xdKASevuwWWg7I46-4gdTLmgBKeTzEtsWNSj2i8WQZra3V-XVT-CVWpwjezi0hokR8VriOY6IkTzWfXjxV_j3OvTkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
دیلی میل| یک فوتبالیست بین‌المللی متهم شده که در یک هتل پنج‌ستاره در ترکیه تلاش کرده یک دختر ۱۴ ساله بریتانیایی را برای «بغل کردن» به پشت یک پرچین ببرد. پدر این دختر در گفت‌وگو با دیلی‌میل گفت که دخترش پس از این اتفاق دچار وحشت شده و در حالی که اشک می‌ریخته با خانواده تماس گرفته است. این حادثه زمانی رخ داد که او همراه خواهر ۱۰ ساله‌اش کنار استخر بود و والدینش حضور نداشتند. دختر ۱۴ ساله که از دیدن یک چهره مشهور هیجان‌زده شده بود، از بازیکن درخواست عکس کرد. پس از گرفتن عکس، بازیکن تلفن او را گرفت، اطلاعات اینستاگرام خود را وارد کرد و از طریق حساب دختر برای خودش پیام فرستاد تا ارتباط برقرار شود. به گفته دختر، پس از آنکه او سن خود را اعلام کرد، فوتبالیست او را هات خطاب کرد و درخواست بغل کردن داد. وقتی دختر مخالفت کرد، بازیکن اصرار کرد و از او خواست به پشت یک پرچین برود؛ جایی که به گفته او هیچ‌کس نمی‌توانست آن‌ها را ببیند. دختر که ترسیده بود، به او گفت پدرش در راه است. به گفته خانواده، بازیکن پس از شنیدن این موضوع به سمت دیگر استخر رفت و خود را پنهان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65447" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
اخبار جنگو تو چنل دوممون پوشش میدیم عضو باشید
😉
✌🏼
@Futball
@Futball
@Futball
@Futball</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65446" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqhmfxynPMIWZ4a8DdPnvsqbEN05LNLI3iLBOgvQBnOTCvUIyMu5PmXr37l4U3w6pM0omKXJz85S8VdhxILxVZ4mb9XgHhH3x7sGw_2DhtrZ3Jws9ucIzaxLJ7KOIrN9Iq2boLJEM_am0PesFpTGuH1tUaZdE_jjs79JkqoOYf-P0CgPkUv6m6__JDAFbzaZq-a1G56AMxHsHZcNLGdZzCuITrJ7EO6anU5EHg9C5ICkgrlijNZQJOOjs4k4qEopeDGdv4iNu3LaiNmDYrY-_GQAvljBTBIzDzAv2zml4Zla8-Y0T0bmqcaY936H6XbJr57x23vN4gNNgw3f9fu4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65445" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
مارکو روبیو:فقط کشورهای احمق وقتی به آنها شلیک می‌شود پاسخ نمی‌دهند
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65444" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇱
منابع اسرائیلی: حملات دیشب و امروز کاملا با اختیار و بدون دخالت نظر آمریکا بوده اما سنتکام در رهگیری موشک‌های ایرانی کمک داده
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65443" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=lBVHEDHcMKotLLANHAUsuBKqjV75zInL1d2cfzFksy05_T03D8lp1wugs7aDe6wZNwAbq9ie67MI4-eRSZd3SMeK8ndcY9c6UjmYr7-9gSz-iS6q0yyq1Z8tJaVQwNQgEJINnPRyDXlNmgcapgnP6l4F8KYwIoWxn564ZLQAgDg0PjAX7apIn_c8OKbIXklLYBDIWZK_vVG989j5dJ12OIAR1GZjiOtLEdsKK29lPkkKMjlu1c1ylsTPDZbgRFdcOa3ZqkNdOBJbfTrK7wMl0oh83E0qJ5OvhfFCf2Fhn4rtI4Hf-tZ2IH4OKXqTa0UDVvEG6bt3Jatf-tJ3htQgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=lBVHEDHcMKotLLANHAUsuBKqjV75zInL1d2cfzFksy05_T03D8lp1wugs7aDe6wZNwAbq9ie67MI4-eRSZd3SMeK8ndcY9c6UjmYr7-9gSz-iS6q0yyq1Z8tJaVQwNQgEJINnPRyDXlNmgcapgnP6l4F8KYwIoWxn564ZLQAgDg0PjAX7apIn_c8OKbIXklLYBDIWZK_vVG989j5dJ12OIAR1GZjiOtLEdsKK29lPkkKMjlu1c1ylsTPDZbgRFdcOa3ZqkNdOBJbfTrK7wMl0oh83E0qJ5OvhfFCf2Fhn4rtI4Hf-tZ2IH4OKXqTa0UDVvEG6bt3Jatf-tJ3htQgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
‼️
‼️
بدون شرح:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65442" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDw0lGEVOD-vWu4OeDs1tX7WEmCuPtaCRu3u20o3vNCyGYMm-cln_yIefPLxkClHgPWNq5G2J-z1TaAINEjAwzLg3oLcpjjD98UaHAfcY3pceTsxYeRG1I3rAkUY47pQU3gTVm4Gsnp4HvatyHlssamY5ZcQ9poCr-Vlxs8uj5wE12MNgLPTyYx33X0tTpoF6h1_hsCKq7qG2Oi29OQvpuKsa2f5_y41XAPHC1JDhi3DjOI9aiL9rUUkyk5iLa52MC8aROk-aJL-ORKn5sQUcPpqx24WRLwXs09756uNl-h9qaG-tETVDypWuWt4vzsU73BGDbnfec0nZFLZemAwPmVI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDw0lGEVOD-vWu4OeDs1tX7WEmCuPtaCRu3u20o3vNCyGYMm-cln_yIefPLxkClHgPWNq5G2J-z1TaAINEjAwzLg3oLcpjjD98UaHAfcY3pceTsxYeRG1I3rAkUY47pQU3gTVm4Gsnp4HvatyHlssamY5ZcQ9poCr-Vlxs8uj5wE12MNgLPTyYx33X0tTpoF6h1_hsCKq7qG2Oi29OQvpuKsa2f5_y41XAPHC1JDhi3DjOI9aiL9rUUkyk5iLa52MC8aROk-aJL-ORKn5sQUcPpqx24WRLwXs09756uNl-h9qaG-tETVDypWuWt4vzsU73BGDbnfec0nZFLZemAwPmVI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
حمله شدید پزشکیان به رسانه دیکتاتوری جبلی
: صداوسیما هر روز شعار می‌دهد اما باید واقعیت را هم بگوید
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65441" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65440">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65440" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmhkZW7JUc1y6LFWal6SvHPBUK_QqzL8IOfpoEnYsLaNqqpvx7zYfAZinMmbaSVWqUyxtGun69WO5w09Lo_SBNuj_mhxkRzvwZp1QNa93Uvv8SW852V4qPV_AgSkR9De5ylNK84tNggG66y1KlqwS0RhCx1EkMlzBl7ZVGsVeD5gBK6rHon3DMK8yiIeBfNTbYV18kuXYvhC9f8tyhHszHStVVZWcYdA_w_KIY2_unt_0ZtlDxUZREOgiajcr8i1c5KtDRxTKRXWHvixLjaSq06hoFTbaPxfuaZlRYo3dPlZm87cxEwl-DIVKvalDjIDyX88RVGIa0hmr6xoDGx5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65439" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65438">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری‌فارس: سپاه دیشب در حملات خودش از آخرین نسل موشک‌های خیبرشکن استفاده کرده و تونسته تلفات خیلی خوبی از دشمن بگیره!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65438" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65437">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIunnKkkHdLPNbLCyu_BVyFR8GpfiQXIVvI6dxFrVlhsUXjKgww6XTJ8yXJbq98uRc4K0gTDaFSRoubLtTfuhWPr5KreodO7r9uFM07jx5zXxu1-vYKLSvbffrb4Yt-jpZCQYWt9JQQQ8ZEacqSGDh0QIsdSXUsOMvW-OkXkf9Hep9fSazjKalWyZxtCoAgaKBtLdbLQKt61JV_DEtiK3IjU_p0EAqsl_nbCTwljDPeKQ_am-DI1tSl39PRCh5-CUJTYtky3ksjvH2lixF0GyJ_hI2vM25xTQCf0TWDL43JZMNgB0rdVkqSKiSSHyRRKoJ2XUGftFjmCCccmu1pcKQVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8792984a2f.mov?token=tl7T0cq1VHB3nb81XKFClP0-jR4be1hoSCrftPuX-rBHOzDiTq0dhphA3ivFuqsz2jWLGOCgnDVAvpXqaBy9m5K8E9HtuCHzU2qKdiP-5iq4oxSu-bPljPCQT5fhF5AkDgqOITG7V6BULWKFEHMMOPE88zc_m49LmB3gzi95lmvbO2iR7ZO5gXPWzGjcYkf4ApJk4FvFUJbW01ajHNdssiyb7O9rJmTUyX7EIfKReH0fo0qzfl-_v7b5-Cpl4dxZbze9r13B0gW5bKTh33aPI_gxYsPIOYvH5d3OLxN9N-FXj2nusHrk4CHviFHOv8x6Hgo4DBGc35cDZeZ8hnyIunnKkkHdLPNbLCyu_BVyFR8GpfiQXIVvI6dxFrVlhsUXjKgww6XTJ8yXJbq98uRc4K0gTDaFSRoubLtTfuhWPr5KreodO7r9uFM07jx5zXxu1-vYKLSvbffrb4Yt-jpZCQYWt9JQQQ8ZEacqSGDh0QIsdSXUsOMvW-OkXkf9Hep9fSazjKalWyZxtCoAgaKBtLdbLQKt61JV_DEtiK3IjU_p0EAqsl_nbCTwljDPeKQ_am-DI1tSl39PRCh5-CUJTYtky3ksjvH2lixF0GyJ_hI2vM25xTQCf0TWDL43JZMNgB0rdVkqSKiSSHyRRKoJ2XUGftFjmCCccmu1pcKQVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فیلم دوربین مداربسته از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به حوزه ریاست فدراسیون ووشو و شکستن دوربین مداربسته و درب اتاق رئیس برای ورود به اتاق ریاست
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65437" target="_blank">📅 12:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65436">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=FfXwfpeykLoe1J0hrQ2zpB2fbAelGKKWUmcWwaufouWMdNwjEiUEzGbLE7dCDc8Iyo7xEMrp_tP2U1gXLirHn60HvUwTw1L-tMVDmlCaQCacGdMGBo2uoGPrIB_TKPbo0BYZtkB-UKHGNGOjlhErfrlJ2tpC8mpih9SVMbsH5dgStF5n2jrVBrGXhBiv2MfNJN9HQvy8s1J2D9f-1Gc26lvcIYA-0NTvOeLa6cZaZNRyxGJ2wb-HoE86EyupQ2uyeaoPd5550qcngQCs9AwefvE2oHB5Cz19hvIwt2GDiUztp_4izPU0-WfDTOVuQY54BiJxdyHm-pODyHOdSgmwLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=FfXwfpeykLoe1J0hrQ2zpB2fbAelGKKWUmcWwaufouWMdNwjEiUEzGbLE7dCDc8Iyo7xEMrp_tP2U1gXLirHn60HvUwTw1L-tMVDmlCaQCacGdMGBo2uoGPrIB_TKPbo0BYZtkB-UKHGNGOjlhErfrlJ2tpC8mpih9SVMbsH5dgStF5n2jrVBrGXhBiv2MfNJN9HQvy8s1J2D9f-1Gc26lvcIYA-0NTvOeLa6cZaZNRyxGJ2wb-HoE86EyupQ2uyeaoPd5550qcngQCs9AwefvE2oHB5Cz19hvIwt2GDiUztp_4izPU0-WfDTOVuQY54BiJxdyHm-pODyHOdSgmwLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتشر شده منتسب به آسمان یزد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65436" target="_blank">📅 12:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65435">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-At89nvIebyUt6P2YsI76aZV5qsd4AhzZ6CwoIyLsliKYxArahI4KmSWz7ehWHCYuUKtOfl6i7N6rabB74KLN5HkjWK4mqgzkYcMINjz67bWxMB72MAwMoKVvTwwMYQx5YdHxJ2RJDhaS0uxBVPPsMa7aEohy3dOTALmFmTjcbBFmpNbBOGhX6glloQlLO5K8hziNM0OAfKT8DX5MGD2cBK4ugR2ZNClaB2jnPx0ULUiHte_ZJ66SZEcy6nL_GncfqLs9jKfOEAWrvgIwZrjEDwiZX5TXtHVzXKsLsAGwQxasSxcaio3Y6tOGy3L061_1160aUl-mJNxxlFqvRs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مشاهده ستون‌های دود از شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65435" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65434">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
گزارش رسانه های اسرائیلی از هدف قرار گرفتن فرودگاه شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65434" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65433">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ اسرائیل: حمله به‌ نقاط مختلف ایران را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65433" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65432">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
صدای انفجار در اصفهان و همدان
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65432" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65431">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
گزارش ها از حمله به دانشگاه هوا فضای عاشورا
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65431" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65430">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
غرب تهران و کرج گزارش انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65430" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65429">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
صدای انفجار های شدید در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65429" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65428">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=cD6TkLreM_wy_CQGes_lpDXAfFHeX6Jt-fvUMsBQ5yW0lxFBhcOoZh5rr46lC40y5I5vcTsCZ827mCKND00ft-sUJWqrNKYhOzTX_XEh7LboTSwtdGZ_fdzlp11MNp9apc-5G_qOhe5rrSOqIHPU-mVCjL9qR3CNgR6iMkKUrzpQtKZrmEfCrX6NNjLkYCBmpGdaWqESlVjkRxJCWQrkHNLMvIZ0eBy48CSEJzuYot0b5FDoFLsgwA9e5L0MeSf_tAZ5EXuvfPkTCKCTMaljBeKSh6QItlQ-MdUqH5x4y6qxGYBWYY3orV8wC2ta0rUIXD9TgBkfbIV3MrjbiK2CJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=cD6TkLreM_wy_CQGes_lpDXAfFHeX6Jt-fvUMsBQ5yW0lxFBhcOoZh5rr46lC40y5I5vcTsCZ827mCKND00ft-sUJWqrNKYhOzTX_XEh7LboTSwtdGZ_fdzlp11MNp9apc-5G_qOhe5rrSOqIHPU-mVCjL9qR3CNgR6iMkKUrzpQtKZrmEfCrX6NNjLkYCBmpGdaWqESlVjkRxJCWQrkHNLMvIZ0eBy48CSEJzuYot0b5FDoFLsgwA9e5L0MeSf_tAZ5EXuvfPkTCKCTMaljBeKSh6QItlQ-MdUqH5x4y6qxGYBWYY3orV8wC2ta0rUIXD9TgBkfbIV3MrjbiK2CJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
در ادامه اوضاع بگایی آسیا، تو فیلیپین زلزله 8.2 ریشتری اومده و تلفات نسبتا زیادی تا الان داده!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65428" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65427">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=TNBOQLvNg5Mo9ZhSM-p5tR7PswPpuJyfQY-D4DYZlZ1Yh7w6MU3hSJW_Mg9OvoPqaLM-hIaX9ETW-SDYkI0YyqARIZwqU-AJXgmf8kkh5lwm7UltSHNueuncalZ0VOD_f0d0PCE-ZxchfyoVbJLTTGcXxRNe3tfM_n6hNYVB0t0GYutUap6lRN35oAhHEZ5taFUHHa8nlnzeFOCj4yYOdRI8w0J1y99XKBOKl7jQlg0YIb6K9yn6ZGNqnbXDAkpy-qTyPeIy-yNFHRl5A7dZ27MKX9so07cmEJQaWpnm_fTFT6pW0Jfq6fXeOKWNKgqZRCm3sCrevrCyPA30R4WL-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=TNBOQLvNg5Mo9ZhSM-p5tR7PswPpuJyfQY-D4DYZlZ1Yh7w6MU3hSJW_Mg9OvoPqaLM-hIaX9ETW-SDYkI0YyqARIZwqU-AJXgmf8kkh5lwm7UltSHNueuncalZ0VOD_f0d0PCE-ZxchfyoVbJLTTGcXxRNe3tfM_n6hNYVB0t0GYutUap6lRN35oAhHEZ5taFUHHa8nlnzeFOCj4yYOdRI8w0J1y99XKBOKl7jQlg0YIb6K9yn6ZGNqnbXDAkpy-qTyPeIy-yNFHRl5A7dZ27MKX9so07cmEJQaWpnm_fTFT6pW0Jfq6fXeOKWNKgqZRCm3sCrevrCyPA30R4WL-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
لحظه اعلام خبر حمله موشکی به اسرائیل و واکنش هواداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65427" target="_blank">📅 10:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65426">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
فرودگاه‌های غرب ایران کامل تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65426" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65425">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRDBgSf07GMYfBxxb17hhnP2E8gGpHpex9uC3eqDfMp9DBbmf-OEiGs0Jt9TzsSEvMJRKru9cFY2_bMZMxa3kNwwZiP5GP3ctw6QvhHVNp3XAX3wwpIItIDGI5it2O2_0kkVPT1OB5Jb4K-7l096Ol5ezEWOzih_zLTT1-98iR3XYFgM0HHJEabx48oY7Mk3PpwULXDX4_92tXKfNt0rOnU_k2Lk-0m_nZcd9b-8lMmy5GELH5pcZeXsNI9iPIvajwl8N2-davOU99jCHRyAgHO1xkYkf6CG2PX7pQ2AdHc1OuvjdBx5Qxdx1F3BpEJ-pwNnH_pS20EQerWZtivM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت ایلان ماسک درمورد ایران: « تنگه هرمز به نام اهورا مزدا از زرتشتیان نام گذاری شده »
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65425" target="_blank">📅 10:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65424">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaSTTQyrW5rHOBsdzQ82RaLgLhuRhVgcqV5GPtdBz27CWY0k7TQR2xQD1bUqR8pdru8m7oMLG5pZW3SXdQJokTDaCtVRXHzxy9cGWgnjGCND_1P18TCqSqVUQX7SHdhXavDssOZ22y_BAcQ4Y9F019HmAXMZ5OcQSZYzEV27udMPRw4lzFgu7AgtMGdDeTzNZtgeUb2EUQUdaqq3gecwPyQuuqiwxYNsmLDxnTGW3CDwUMccJsDAVtGjTDzQxW5nldfyJ_tbfcoQ0ueEtMnnTpuku_yegSKxVdzMfBq-nyVZTGk9ZqO9KUMXLmzBc2ZFKjvyCaM2aXE5P2zSbZWlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
حمله موشکی سپاه به مرکز انرژی اسرائیل در حیفا و ناصره
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65424" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65423">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=Z7qq56yE6roCZ-wBHB72QTD3boxo03CLhJ_o-36LpDjV32oTQ03N8YHEyAyIZxyXI9oLSdmDb56DdrW7L-K4yJu3q6iCN6vFtMYglXcFg0_Xun5BUxv-Mqn7Zn6lP-ng8cj3FEPEIWZrZ8lyKltJFYFCnshRsvbgwRI8lcYwxmn92CFmp34yXLbKYzhaidnIZFai69_2Vegen6b7g1RsM7yeNtLUq3HEhkmDuxlwr0SEYBbiJq9beGiXICQEtIWSpQ0OG7WkIJzbgA2MfX8xET_Tm92dFfCP-0ddgudBQNAP0MQez5V0xzkaicWT5gbjAkkS3AmmdmSPCpHP33ri7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=Z7qq56yE6roCZ-wBHB72QTD3boxo03CLhJ_o-36LpDjV32oTQ03N8YHEyAyIZxyXI9oLSdmDb56DdrW7L-K4yJu3q6iCN6vFtMYglXcFg0_Xun5BUxv-Mqn7Zn6lP-ng8cj3FEPEIWZrZ8lyKltJFYFCnshRsvbgwRI8lcYwxmn92CFmp34yXLbKYzhaidnIZFai69_2Vegen6b7g1RsM7yeNtLUq3HEhkmDuxlwr0SEYBbiJq9beGiXICQEtIWSpQ0OG7WkIJzbgA2MfX8xET_Tm92dFfCP-0ddgudBQNAP0MQez5V0xzkaicWT5gbjAkkS3AmmdmSPCpHP33ri7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تصاویری از پرتاب موشک از ایران لحظاتی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65423" target="_blank">📅 10:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65422">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام انصارالله یمن تنگه باب‌المندب بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65422" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65421">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
یک پایگاه آمریکایی در عربستان سعودی هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65421" target="_blank">📅 10:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65420">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=RNV3-ueNM3_k6RsUGx4ZjpRoTyPyH0thqUXvQugb5ypGXhiJ7mLenp6pf8U88XoZAMtx66zycwEoTeeBDccJEGEV8FqSp5j6k8ZsQ8tNPMkADVq2LOv2C6GZZ325mojKtzJiy87-oVH-FcKMJssWg0VMmjprK3QtR92CNxsnGRBXtGiET_XQ3K9vt1fMYOdFr4I1dUhJkRVsy8z6TkxxsSFJxLSjmHGKVGZqvnwFwSjr0BwOY3VfuU754D4zwsaxA_UVavjne5QX3oQ_51_gI8yN9CzjRC9RUdj9HPrKE3n-FyiBdM4wla8vDyFCm8gB6dvSh2v65R4s9g02LKsOSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=RNV3-ueNM3_k6RsUGx4ZjpRoTyPyH0thqUXvQugb5ypGXhiJ7mLenp6pf8U88XoZAMtx66zycwEoTeeBDccJEGEV8FqSp5j6k8ZsQ8tNPMkADVq2LOv2C6GZZ325mojKtzJiy87-oVH-FcKMJssWg0VMmjprK3QtR92CNxsnGRBXtGiET_XQ3K9vt1fMYOdFr4I1dUhJkRVsy8z6TkxxsSFJxLSjmHGKVGZqvnwFwSjr0BwOY3VfuU754D4zwsaxA_UVavjne5QX3oQ_51_gI8yN9CzjRC9RUdj9HPrKE3n-FyiBdM4wla8vDyFCm8gB6dvSh2v65R4s9g02LKsOSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
با تایید اسرائیل، پتروشیمی ماهشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/65420" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65419">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب موشک از ارومیه ، لرستان و اصفهان به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/news_hut/65419" target="_blank">📅 07:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65418">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد  @News_Hut</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/news_hut/65418" target="_blank">📅 06:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65417">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووری
؛ انصارالله یمن از آغاز حملات به اسرائیل خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/news_hut/65417" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65415">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/news_hut/65415" target="_blank">📅 05:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
با توجه به شرایط خاص مذاکراتی و همچنین آغاز جام‌جهانی، حملات ادامه دار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/news_hut/65414" target="_blank">📅 05:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=VbJ1bZwSqhwp_JpBG9MK-EJ6EtI3E0BCLkkTv90sLbpGxiO53RzZnEmrA1VsglFXo8-MBCUT6gF40izWlV_G0O9sSgYWmBrAxIehqcnC1GDTx4VGRnV6hw4lnXG90GNR38dfBKX39N3wCgxDLEaNZlkvsoWcNl8zh1cmdN3cER7MfE85bhIYOQJihA_CRLJOgsCDELMoRMQ1pLmrAE_iUnypMs118NyLl-Tb_9K5AiBTlLMIP0UPTrOguwFea66I_rAeCaclJe4nWiLY8Q3lusOHbdjFd2oyC0FMCDEDeIFeQqJMZKUygZPACey2tFBbhd5GqSuwJ-V9YrOzK6-eaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b906cb3be.mp4?token=VbJ1bZwSqhwp_JpBG9MK-EJ6EtI3E0BCLkkTv90sLbpGxiO53RzZnEmrA1VsglFXo8-MBCUT6gF40izWlV_G0O9sSgYWmBrAxIehqcnC1GDTx4VGRnV6hw4lnXG90GNR38dfBKX39N3wCgxDLEaNZlkvsoWcNl8zh1cmdN3cER7MfE85bhIYOQJihA_CRLJOgsCDELMoRMQ1pLmrAE_iUnypMs118NyLl-Tb_9K5AiBTlLMIP0UPTrOguwFea66I_rAeCaclJe4nWiLY8Q3lusOHbdjFd2oyC0FMCDEDeIFeQqJMZKUygZPACey2tFBbhd5GqSuwJ-V9YrOzK6-eaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
💪
گزارش انفجار در ملارد
@News_Hut</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/news_hut/65413" target="_blank">📅 05:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حملات به تهران  @News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65412" target="_blank">📅 05:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65411">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpcSkz6Wgggo2okKM0phU3jme1OtLRsOrRRkvKfj9eBuJ8GjsOkgsfH3AG7oc3ALU4h9T633VeeE2U08o_aK8iznfB6QWmmLY19rc1HkQY3dRdvb1DkZsKX70A6N15c9FyId6RRdzdUqNcIl-n4IIy9YtM0nQHBFxn59yeZ7dVjFs_tXa6RL-M33nUSZK66FdrZCqv6dAF1xBXfpy635IEj0dQCRoEY4k_7k2EqSWbkSy0c1DEFw4HBb_234HGBSggSViJx2NIUA1LPtQFWu8k_dwVdBuEY9r1-hjfw4LEojoi1nfWEWpwBrQuBeVqCwACkIT2loEgYuqCTEPvNBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65411" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65410">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFz-w5ujCxHy622bbj66r01dUKv15A8MYAQI54lrhYh6GVGjssOZWZxDvzdUXHG6JMmSRVksQY3rPuluZzRE22sXpHSL6j10yH2TnZnwk3y6uqXE8aQfxDVpcXJaCplObCFOhqGsCsDusmi1EXkUROFD2UkG3lfEyH5UJCLq5EeqCoMEBHE0eLH12zJ_-7Wk5tEFeMosMnFeDTiS4kxIOMM0TD9JTmUsLFh35yH2QzCaak5sBx2i-wmnOLzzN2Vm8TKNiXxNTNNGQJTcnSDsgfCV9DrnbDjsD8lKasX9n3ajzklEQ0ISLji1X8Hr1juageTjkj649CCqPLPQSqjG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات به کرمانشاه  @News_hut</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/65410" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65409">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13951b2150.mp4?token=ZePgWIu_oGHnlpVWg2XsalrN1l0t5mjl2mbnCYkDGrmZuJxxRD2tAK9_IapQDRRRx_1bfJ7s3MIXG7InZkCbcRr2zDyDTkCrsbX-9lFAxUac22IEKbzE3e3d4xR4IpIgI6Tq9bY2FnF1HUuvap2l-fJWJKvuPLljbEkq1n8CRuukvT2I-DefbclaJBc8RRzc3gnFkJVIAoF0zIczZjux6ncXfU5m8M-Qdivn4qZqSKHUouGm4KWLSF0f6_InrzEy3Vwkxg84xCcycXhZNUOZiozWEdZkO0qQbsEUXJ3oOk4hoc2BI8bQKzFZ9Dy3U7HB9gztHgYMUIuXtSnaRiPASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13951b2150.mp4?token=ZePgWIu_oGHnlpVWg2XsalrN1l0t5mjl2mbnCYkDGrmZuJxxRD2tAK9_IapQDRRRx_1bfJ7s3MIXG7InZkCbcRr2zDyDTkCrsbX-9lFAxUac22IEKbzE3e3d4xR4IpIgI6Tq9bY2FnF1HUuvap2l-fJWJKvuPLljbEkq1n8CRuukvT2I-DefbclaJBc8RRzc3gnFkJVIAoF0zIczZjux6ncXfU5m8M-Qdivn4qZqSKHUouGm4KWLSF0f6_InrzEy3Vwkxg84xCcycXhZNUOZiozWEdZkO0qQbsEUXJ3oOk4hoc2BI8bQKzFZ9Dy3U7HB9gztHgYMUIuXtSnaRiPASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
انفجارهای متوالی در شهر اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65409" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65408">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K08xjcOo_5lYb_Gm5t5W0vbaIc5DDRaEPYtOogp2dlEaByaybDHtfiMNu32CHeMmrlbH0Pw5QbPFQCvM8Xo9ZV2Sb4gsl4phKBIYtG1BTeMEAWPs3MxGqnkBZR2SXke9yjKLFXNtTr360VO5b_tUUv9mwkh4gFxpLLoIMpkfQv4NzXiFkJmxFIoWJAd4PZ7PVH3IcCPhnU3VhMBrqj9OajTWNzarvSyfESxTLz6AUswT-_3pTz47BPfuXoRe-RxAc0MvAqmLJh9XnTq-jlreNLc2kZsEX0Qx-LFYtHg0Oy3RoxV0vHjZmXHnoCdRy0IbMyYQoyJvxl2P_SIcZ0_-Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65408" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vZKk-c4VpA7uME8mmNArsTFJdG7xNjfi9Cxg2ad3qtByvDsdSGB1ZR15ERSyEGLBOXZzhDMekruUHWlM27urxAP3Zf0Z1GdN2DOrIvmhreFlH_b-QmO_Wvcsv5JHtSRcOGnOqXMCh0dxu7SELyUbu7VdAVnvJJL7t31M4vqM4SuozLQJTArq4x_pOoCRAj7RcHbFuGSf3_x5PSjeaVm5NEYLl9a2eyNN-Q12xxQ7X8VV65CdMyS0Jp5MQo6Sn0zu8EPvAD1SWPTNN1YhMbDNHVTgY9SRxNTEG5AVbO0lEeE4TZ5pemVJfrN_6VH2Osx7zpgT94mHBvfwICghvdytFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇱
نیروی هوایی اسرائیل اندکی پیش به اهداف نظامی متعلق به رژیم  ایران در غرب و مرکز ایران حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65407" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65406">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65406" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65405">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRBCHHaT5UzBAYxTeCEvxjN8BvlUvRcN9ymiXHTkhTg1r-ndefHs2xXF3jqVw4DDhhMABMPIS5_uZVhuYRf93QI8kMGHhmdIOQIbawJUe3eU7r-J1zOka1nU4BzlyxGwGjLnRVINdCpBwhcMhi8WEqzRyaPJS--zdwwQun0tCgPzUXEmoa_f9JgQy-CrVMr6fECWQ0iLl73L3V5rb5zgIZ1paHLxMXS53CAL4ONkxsIEDDVN-Jc4tfATov_cWKQg6bwAGk7CMLhMxysL5xdDb-dAxcQqxSvGUqmUtlPNPQu7I5rNRTZjSSNwvP_IQhtyxCJ0g-rx4mcmfJSLgP9wOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65405" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65404">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9iwOi5Wlj5vGycpZ_zazPBGsu6mj_-eDUlUr_wkn6JqbtUivdOoF_ji0UBfNxN66YUCeWI61sVz3Q7hugeq_5KhhbOrGMXSSxl1pHPr9rhEP1uU0wBQMsXWumySSzzGTd03UWe79Eg0opJPsiskFJq_7gnEO_O8osQ8oKL-vS61wlRpS-8tsYtcguDQwXmg72XO5Jxj3FGd_XzcQ4qfnon5j5E_i9Vvt2MwqhhOwsSq69pAqzS-AsqcuuWv0fyNSDVwRSaEQ2LJ1COTrpWka2oXnEVxQMkicQmnGjEJ8wx7m52GuiO5tYz4F-PVBx-n5Lj6QBr5zNzwHtlbe-PPzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65404" target="_blank">📅 02:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65401">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: نتانیاهو چاره‌ای جز پذیرش توافق با ایران نخواهد داشت.
@News_hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65401" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65400">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombetcart - کانال بتکارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtGJHfB2Jc_pIFaaNPKJ2rrjzu-beeXrNiIfk6D-iGmAQInXpfoDU07Mjlz-cfa3SjtJpMxkCvFfUgIr2l0saA0H4u8xbhfthSCeQ-2dsPAiVSZ5mj-ncZ9nGBTntKow8a6rSSCEyaxVe-9QqHsVZ6h4C2n27Jpb2oA2sBWUh_6pGRrcdNVsUVTccIJvkhT5Kr2K33GKrNHkbnCHKBhksbE_Eofacn4QJkigwsi9K4lQJxLUfQ1-iNHvhhqvVvesHTedTYQQy7lcAPWky_sDORZ3LsXiTT58rRs2YUzH7sNOje70E4yy795Y04QGKkIWuR0dXlDzLmLoCVsX9_7y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه فرصت تاریخی!
💥
بزرگ‌ترین کمپین تاریخ بت‌کارت شروع شد!
🏆
برای اولین بار در همه‌ی جام‌های جهانی؛ جشنواره‌ای که تکرار نمی‌شه!
0️⃣
0️⃣
0️⃣
,
0️⃣
0️⃣
0️⃣
,
0️⃣
0️⃣
0️⃣
,
0️⃣
6️⃣
تومن
❗️
☄️
جایزه‌ی واقعی برای ۱۲٬۵۰۰ نفر
👉
http://bit.ly/4ep75qf
⏳
تازه لازم نیست منتظر بمونی جام جهانی تموم بشه...
🎁
بت‌کارت هر هفته جایزه‌ها رو مستقیم به حساب برنده‌ها واریز می‌کنه؛
✅
سریع
✅
مستقیم
✅
بی‌دردسر
⚠️
ولی یادت باشه...
این جشنواره‌ی بی‌نظیر فقط مخصوص بت‌کارتی‌هاست!
🚀
اگه هنوز بت‌کارتی نشدی، الان وقتشه...
⏰
فرصتو از دست نده!
👍
وارد شو و شانس خودت رو برای برنده شدن میلیاردی امتحان کن
👉
http://bit.ly/4ep75qf</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65400" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65399">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان  @News_hut</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/news_hut/65399" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65398">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
آغاز حملات اسرائیل به لبنان
@News_hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65398" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65397">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل: رژیم ایران اشتباه بزرگی مرتکب شده، ما آماده‌ایم
@News_Hut</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/news_hut/65397" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65396">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ترامپ: نیازی به پاسخ نیست، صلح نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/news_hut/65396" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.   @News_hut</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/news_hut/65395" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇺🇸
🎙
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم
.
@News_hut</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/news_hut/65394" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65393">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: ترامپ بهم گفت الان زنگ می‌زنم نتانیاهو و می‌گم به ایران حمله نکنه
@News_hut</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/news_hut/65393" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65392">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات اسرائیل به بیرون هماهنگ نشده بود؛ اصلا از این موضوع خوشحال نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/news_hut/65392" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65391">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد  @News_Hut</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/news_hut/65391" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید: احتمالا اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/news_hut/65390" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
📰
فاکس‌نیوز به نقل از ترامپ: چیزی که به ایران پیشنهاد می‌دهم؛ موشک‌ها را شلیک کردید دیگه کافیه به میز مذاکره برگردید و معامله کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/news_hut/65389" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/news_hut/65388" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند  @News_hut</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/news_hut/65387" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ارتش اسرائیل: تموم شد بیاین بیرون
😐
@News_Hut</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/news_hut/65386" target="_blank">📅 23:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل: تمامی موشک ها رهگیری شدند
@News_hut</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/news_hut/65385" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
وزیر امنیت اسرائیل: امشب تهران باید بسوزد!
@News_Hut</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/news_hut/65384" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=fn2-OfX9KQRjzzqfgUrtfCfhCxTJbGHbQKmsblzuDnY0Obrfb-AjYCH9saqKvhRPq8c2xiQGpYgtgmwstuJj2qICA1Xc5ys7FsLLLLu7miRIcXWpJ1w_qpzOH5ITCI56GcRgYz7j2AreapMDtmxnkftcaAAkrwj3QuicAdRRZn7SVZI9wT8mpyx3mGfy3ZZs2aeyj2TVgWMobwJk4SSWfgBHbXtNVRi22ie1H5pKIqoF2PmWM7phMwfCr4sW1JJjUq5baKTd5Z3vUrVv1tgcXOQaam_Z0GwvRIZncPS5wIlUz28vAxCrTHqbvbfJQxRS9Z82-qGD2_POXvOtq4qhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d76423eea.mp4?token=fn2-OfX9KQRjzzqfgUrtfCfhCxTJbGHbQKmsblzuDnY0Obrfb-AjYCH9saqKvhRPq8c2xiQGpYgtgmwstuJj2qICA1Xc5ys7FsLLLLu7miRIcXWpJ1w_qpzOH5ITCI56GcRgYz7j2AreapMDtmxnkftcaAAkrwj3QuicAdRRZn7SVZI9wT8mpyx3mGfy3ZZs2aeyj2TVgWMobwJk4SSWfgBHbXtNVRi22ie1H5pKIqoF2PmWM7phMwfCr4sW1JJjUq5baKTd5Z3vUrVv1tgcXOQaam_Z0GwvRIZncPS5wIlUz28vAxCrTHqbvbfJQxRS9Z82-qGD2_POXvOtq4qhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید از اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/news_hut/65383" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO-GtV-PHBLvZ5zmuF6Y9JvwLWrmknm7OalSqs74hVSar1CptK_Cg0kgv7mJQE5dzs7P89iZ0ILXFkYkgbYHb8IV503tk0HJH9DSD0yUOnBzMMLukFJsW-Vfc0NimpG8uBLyv9TFVTnB-diH5nHXKvSyfTOpYdV8kK1kau54wKWIvKQMxonUZjKMTpgcBXtc7l7moAswcHpaDM1omlfP_QjKuvU4ecmHOyujNVNUYOxbozy5ZFjr0xEwtlhQTW2O3gqcIClK3Cbi-FnGj-Zyg0EsZjpqRkjmfm3TK7VKS3TL-Y_l9Q2-dlXX3RiomI3U_JH8dJrBtOJd9XqtQD2p9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی سپاه به اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/news_hut/65382" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است  @News_Hut</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/news_hut/65381" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
گزارش غیررسمی پرتاب موشک از کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/news_hut/65380" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
📰
#فووووری
؛ خبر اختصاصی ایران‌اینترنشنال: سپاه پاسداران آماده‌ی حمله به اسرائیل است
@News_Hut</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/news_hut/65379" target="_blank">📅 22:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Npd9DnU_5X-ftXeDXAarZUcC0W_I3Llj3fEkoX841HrKHkwlKd21HYpxNq7mvbO1gGiHdolE6ZGUtASB5zasH_wEhRVxb2OH2JZR1cHROfSu9LEJlc5PMLxbIGM_WkO1OA0Iywz7aqzfg8MZF28PTSRgjR-HCtF6O633CfbtC0eCzg2XqzUDaSCCracP1YrTTHHV0BnExpvZ4n-KTDdJE5ZewaG2EihN7cPqGtiWg_fFeL6cV8f8VDl_vUIM6r9qQ-hCKI_M1x4tWMzEZYc7Xjfy5OnLpwtIIrRuU4uQ1v-R54IuFCsNnwCWVNmkFpUghzJboQZ6XKTPDuzM2eZfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرواز تهران به استانبول به دلیل حملات احتمالی ٫ مجبور به بازگشت اضطراری
به تهران شد
@News_Hut</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/news_hut/65378" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65377" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65377" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUzY2bJGY0P7MDYEz_9aKccXDmUt_8l-B7m6J9SDxekJkC6HL73BWt8LMYHq-zjX-bv4aAmsYVRlQNXD634n5T_De3vd8mosyQL_PzNstIZraegujc3adIL893fyNPPzGR8wCnRSuu4U537azWneZN0oLqvms6XPurWYgdKDmv2-idx9phgMYfzUNRIX1rn1pjSbf61dNL5RNHZWYaMyF8AmHgpOmC9jkuPmV-FKUapGYQB7aj3uzfBt-qC6UslqYJX8oVTsf4_1dbjT5uIvBRyt7eTmI7oV1cD5CGeXsR_ra3gA1AbGceiCr5i2S2Z3xoK9dRl3JxThwl3JdVANQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65376" target="_blank">📅 22:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RJ-zqKlUq61H7IFMxqetfyvVTJxz17LTxnrL0C8qx2wcMAq2NE8QaCa-2o4yhQcTORVRwQxCBv7cgs8j_ep6qb8TPIYB2S-DhU6ZpIlGm4F0jxdEeOtiVhNiTwPcRXs0JCVe1MxTe4zDgQGu0MPQXEWnl19UxrZB-vsNnXX0cgn6lNtc4m9qwwRDsRKQjse2_FsR7kx2mXDqLl0A8iADy0GzxLTBz9WVZbnMDZvRUb-GP43h6n2SlS6Wd0HLmhU68XvOzvlugfrs1ogqnxxzItgIscgcrc7r4y_w1WQYsZyv4apFHfr0gUZK02TLAphfpiZwzKvYJ6Eb3edVivzssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
د اتلتیک: نزدیک محل اقامت تیم انگلیس درگیری مسلحانه ای رخ داده و 9 نفر زخمی شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/news_hut/65375" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشمامممممم؛ اریکسن وسط بازی دانمارک دوباره قلبش گرفت و سکته کرده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/news_hut/65374" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzYtprytOW6N5hkHNmt2TpwwarJfFpk1vIFu6rL2hsyjwxzVaZUF-E46Jvn_Uz9rDL2GUULuOz0oWockBGpgAj06i0ew_q2aRqsgH2_CcuVuNJ5DlXF2mngU_H6JAWUdnH5kpNt8KcW3_RqWR9vQVXjeZo7988JXmQzMhZGcDQ64SGU99JJVA59ucoR5OeIgiC_0BLZoGtUEeaH5piTMKQW2KH3t6rm0ibb_METeXj3KtyTURDH9R6Ulu8Ze5EIww3kWIyisnJjEO9F4PvZmwadfD0cVKYJ6BP0AruBKw68X8_QTdnoIz1WDCWoYxByW9E9umo67-mLjtY0PXy46Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۱۰۰ روز از آغاز جنگ توسط واشنگتن و اسرائیل گذشته و به نظر می‌رسه تلاش‌های ایران و آمریکا برای دستیابی به یک توافق موقت جهت پایان دادن به درگیری‌ها با پیشرفت ناچیزی همراه بوده است.
همزمان، وقوع حملات جدید، فشار مضاعفی را بر آتش‌بس شکننده فعلی وارد کرده و دستیابی به صلح را دور از دسترس نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/news_hut/65373" target="_blank">📅 18:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
‏ترامپ گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
‏ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/news_hut/65372" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65371" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65371" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkYi9m2cOmRZSYcxuEVAnBh3K6yaZAC0y8S58MdGEQQAzBRzx24-JdIZdDp035GwDAj9Gcc5YQyEteHNFgMVDSTqB472aGRdLb6pLO8fDsa7j0ezdHhCYxnpJI8s8pCrnjBEfnYtciOGGOHlnc0GCfCx3o8hG2GxaJl-2Mo1LugSjgQW6_0wViCATAyw2oelDUtSphQ5ouYpecxLURCA_-hbohazQ9OKhzxISdGsUGRgsudqVSvW4JXg9qbigtuQkIcD9FoSVVgYPu8EFH5z_ASvvR3iC6pbDBfyRqWOqwFLxPSwjvbbeZUzSaFrA8eMNOh3GESSdAuDxuYpYnLAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤼
روی مبارزات با 1xBet شرط ببندید و شرط بندی رایگان تا سقف 100USD دریافت کنید!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65370" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: احتمالا بدونیم مجتبی خامنه‌ای کجاست؛ اون از پدرش عاقل تره!
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65369" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیما: منتظر واکنش قرارگاه خاتم باشید  @News_hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65368" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم   @News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65367" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
محسن رضایی یک‌هفته قبل: اگه اسرائیل به ضاحیه بیروت حمله می‌کرد، آماده بودیم شمال اسرائیل رو تبدیل به جهنم کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65366" target="_blank">📅 16:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65365" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/atRNiN_b51c1cAs100I6dtezeLolOLv6TBFFG_XN53MGuO2IgfcALZKK1rBTtjtrxnYIB9ajScCP0jmDIM4Ssr4oMoxC8a5x-CxFy9uZTTIGwrnLCANtHQJWk2DtaUhYC4Pt-0p6h2dXSR6HZPZniMq5RLiehNC7c5rUTugbgkdABwbau86wf9X03wQomiXdRIIzpDdv8MDnY_Bdj8TLm_HykvaMSCdJ6rvuzlkH19mKJMukhjXnC9eOK5l8XtyjiTw5IsjkPKN7nxVzElpysXYM4cvOyTcMOWxrOsXi2FoFsKuA6x3iFHz1PLvCc9ouqlhs_kkKMJWFZFo1SVnSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65364" target="_blank">📅 16:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ اسرائیل رسماً به ضاحیه بیروت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65363" target="_blank">📅 16:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65362">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5u9BoR8zklDsqxIYtJouEwsxR5hUu2_NoCGG9RjUzlwmACm1KFFEc3zMJdfcsf1YOh11LnCcx9o716EP7fYoDjzk2Gk85ikppKjufv7xQj8TXfj-ZVD9ufFp6MMehh7ZDnK6mAa6cDHaJdzBUQHzOpD-GZWB8rlGNkjVMJlFJ717G3i-4TZhjb9XkqsMcWIwfHXo5j_L1V577afHzbWN4JDhggsg10FdUWvv5iZKyl1Do74dtk_i6USQzGjZGa_LGPszRlxc271JRrVB8GrR63yk-LbXXhyDOm-qSPghWzfMdyPMHhb8BEZAmuO_FYyhvvq2i8g-I4VmIidMHMAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل امیر تتلو:
توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65362" target="_blank">📅 13:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=rQPMNGKOQ_Szk2IQViDhywiKU-kndiDSSiERyRK9frwhGM_EU37-genOIvfpK1Vfsa8o9z4fO34iSIbqx65UNSbveZq1JNI-fmV20egMmS_8tW3muQhPPLfo82Ad6MpjXTiKf7PrXaMh56GOEiwEHQzHt_daDe3fDX7XSG8vwuSW0Gm81KGydC6h-nx8iu2Bj7OUhxTSldakLTQmzm4PiizecY1_wJzdcTEv9BX2rawZwqeD98SB0mVrUWLRCWMljSG6lMsWc8Vl-bzGUcjOkmLurUefQ-iLEQenLIQJCwg08wOjIKkVicO5UwtTaogv3_outs2JP7HpUloJULe4YF20i6EGu_U2rycQuPcx7_qrZBtZVAOsDiSaBIrHkyCzniOuwTJWbx-sf7qC-2y3NoriQmBooeTcg57BHZpJQIPYdVcvpC7MpHwxWLbdMNlQnYbaCH5deGzc0Z9wr11IrffJ_tIfyey8cLHrj9_JxSQtLJhtgpzl98uHc-oP-V9v2xrsxXwkUseZXpMnkGs7vjuihqWZdATh5lMRHa68znOG012sd9gK0bewKNwCm9eIIxToq_durnuEOBza7XLjxw_GzUE8JMQqu-QEkDmS-C2lMm0lehn0WXmGrmzywN1md30h36HyvNv6Dfo5Vevx8zurP-iex4Zh2Zs2Llpp0s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cb33d933.mp4?token=rQPMNGKOQ_Szk2IQViDhywiKU-kndiDSSiERyRK9frwhGM_EU37-genOIvfpK1Vfsa8o9z4fO34iSIbqx65UNSbveZq1JNI-fmV20egMmS_8tW3muQhPPLfo82Ad6MpjXTiKf7PrXaMh56GOEiwEHQzHt_daDe3fDX7XSG8vwuSW0Gm81KGydC6h-nx8iu2Bj7OUhxTSldakLTQmzm4PiizecY1_wJzdcTEv9BX2rawZwqeD98SB0mVrUWLRCWMljSG6lMsWc8Vl-bzGUcjOkmLurUefQ-iLEQenLIQJCwg08wOjIKkVicO5UwtTaogv3_outs2JP7HpUloJULe4YF20i6EGu_U2rycQuPcx7_qrZBtZVAOsDiSaBIrHkyCzniOuwTJWbx-sf7qC-2y3NoriQmBooeTcg57BHZpJQIPYdVcvpC7MpHwxWLbdMNlQnYbaCH5deGzc0Z9wr11IrffJ_tIfyey8cLHrj9_JxSQtLJhtgpzl98uHc-oP-V9v2xrsxXwkUseZXpMnkGs7vjuihqWZdATh5lMRHa68znOG012sd9gK0bewKNwCm9eIIxToq_durnuEOBza7XLjxw_GzUE8JMQqu-QEkDmS-C2lMm0lehn0WXmGrmzywN1md30h36HyvNv6Dfo5Vevx8zurP-iex4Zh2Zs2Llpp0s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با زنده شدن دوباره دریاچه ارومیه هزاران فلامینگو مهاجر بعد از سال‌ها دوباره به دریاچه برگشتن
😍
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65361" target="_blank">📅 11:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4vqYGo7Ua6ZI_KRCHQzanqZgb7Gpxj0YsyVixz_NmrauW7n9fbek0steJH211oPSEj3QS_9PDTE8d9v4L2OtDRZcRub8rsHwAeQlqKGAGtwdOPMJKSLvOWBlpNiaIJPaUuoXw_uSabOswLpHAbQXLLEqE4RW1aEllo1HN-ir4DXAAwxdZRdagxn0dnF9rndTGbGdrNS9INN_cqHovakJOPSxwxLixeGzNJM43iqCkePRrtYjZ6iCibgGs3bhbKcP3duZHCKIDeeUg-k9_fLkENPKMsbxLGjkCPXitwqSTbzb4_fgQsq8lXFqRnli8UXB9vM03Fivy1oa8GHsdXDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خوبه خدارشکر بعد از این دوتا پویان مختاری هم برگرده جمع نخبگان جمع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65360" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65359">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl3Y_in6l6rNR7YnqIA-me_V6_HZxsUVzNc367O0uHRwLKqP8FbJVcfuhLX-WXNoMh6_ok2niib08aieFjpFiPDHzGHbnJrtxvJw_g8Fm-ee0r0Li05Cs7etwPiIyrubQu4zGNKPPjb5R1Bwc-76a69bmsPjLs5Msk-stuOBk5VZgHuz4pEu2Z9iNfnZaDXlcCveD3LP25Ne7cKE6a06cBbkPe4Fx8bz3xH_zPprhD_EzMRrsDh_LrCggwGum2sWyvsaVv10eiKjXGCA2xu5wam7IZRhiAXPaWW5H6TM8SPKfko2drnQQqntZmu-hrhOGAInek_lD-9uTzYjRG_Myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65359" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65358">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884f21c214.mp4?token=JEBcPhBfe5HDnw7JWx5-o-qOgUAAlaMyp18OiJXI_cVH_kzPKgvKB3kn3t8_zf9l5wzBEl0VAUQGdZpoTIKOoRQXxK34_MEDzFceSpswlzw0QBlAyl5v244bCutfprjGeynZtpK5RKYSxNlZZjXGDvToJswkWvEGxqlMjHuzN5rmnptpL2LrYlVsHcBPsB0JXvbyo30Z8WpArf_UA7CWgx5xiCp7vTaYqDwwXNTAU1823sXkg-K_SgrG3V8ngF9JwQH-vZQylpAqVjfRi2SLnwBNNLOxBZyNfxN0qryY6SUq5brJX-bmUqQj9Z5HwKldUExzJUb6jn9y2pfUpqXpjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884f21c214.mp4?token=JEBcPhBfe5HDnw7JWx5-o-qOgUAAlaMyp18OiJXI_cVH_kzPKgvKB3kn3t8_zf9l5wzBEl0VAUQGdZpoTIKOoRQXxK34_MEDzFceSpswlzw0QBlAyl5v244bCutfprjGeynZtpK5RKYSxNlZZjXGDvToJswkWvEGxqlMjHuzN5rmnptpL2LrYlVsHcBPsB0JXvbyo30Z8WpArf_UA7CWgx5xiCp7vTaYqDwwXNTAU1823sXkg-K_SgrG3V8ngF9JwQH-vZQylpAqVjfRi2SLnwBNNLOxBZyNfxN0qryY6SUq5brJX-bmUqQj9Z5HwKldUExzJUb6jn9y2pfUpqXpjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از طرفدارای حکومت تو تجمعات: ما تقریبا یک ماهه تو خونه دیگه غذا درست نمیکنیم و طوری شده فقط میایم اینجا میخوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65358" target="_blank">📅 10:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65357">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌐
آفر ویژه سرویس های VIP
✔️
🙂
Standard PLAN :
🔸
10 GB
➡️
90 T$
🔸
20 GB
➡️
160 T$
🔸
30 GB
➡️
240 T$
🔸
40 GB
➡️
310 T$
🔸
50 GB
➡️
390 T$
حجم های بالاتر از 70GB  گیگی 6,500 هزار تومن
💵
نامحدود PLAN :
🔸
ایرانسل و رایتل
➡️
450 T
🔸
همه اوپراتورها
➡️
730 T
⭐️
تضمین کیفیت تا آخرین روز
🖥
⭐️
تضمین اتصال پایدار
💯
⭐️
تضمین قیمت منصفانه
💵
⭐️
پشتیبانی سریع و واقعی ۲۴ ساعته
🔜
⭐️
مخصوص نت بین المللی
🔒
🔖
قیمت همکاری همین آفره
💎
🔴
@MAMADXVM
CH :
@proo_V2rayng
CH اعتماد :
@prooo_V2rayng</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65357" target="_blank">📅 00:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65356" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65355">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sg6GS8fMTgj7Y33dU-w9CpmKDMNkGlWxp1N2rkA6vmJeKOYPRF-JDU2y1Lrncp60s9fHZDytZV-vIUCyPwxv_qwUaPrlGhR7xpj80NZQ62FOBNt3u8VzQGuYotjlNpIeEhgSkKgcpQ6f218R5fflv8dtOXqMmblgrAvtZNLb7qWU1iSmvuJ2OXAapIjZakCLO2zX5jIIaSiy906UnlSZ3qRlVGA4KJyDjzVaoC_hMWw1H4E2Nyui8CxMS0Bd4a5vQ7Irzyn-UHRXN_-qBLQir8Cs-85C8rX1IyExfvY2pZt9mtIyLYG01v77aFPp1onzEhq2f4Znli4JPggJoBtNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65355" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=qYHtbdfdpXx9gFLGYwl6ewcSr2UaBBy9lkltWaB67WrmInW0-E-UuZ4xQS93W3ZBmthT4tHbn93RySydYZuXuMmWdgo33mCO8V4z0fvvDdLUgx9INOHSEjpOuVgwrZdnX9jVdOGFoWKOEJMuF8HZt7D4dyaGMxl254Gihf2HhOCQmUqRPjd5QW4M8qGAwvHWj_1HOIso8M-pBYzdFaUTyuphNaMtF7L3-vCjDo9ri484a3RUhHuDvnDXXYzCwY0jS55bivQiTuPZtQgZnGm39nRZVWFubpjIczhh1keC_f1ZnVMUbJzmL0DYiysQMhYuML3SmzmYNODwgw0eS2X0dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=qYHtbdfdpXx9gFLGYwl6ewcSr2UaBBy9lkltWaB67WrmInW0-E-UuZ4xQS93W3ZBmthT4tHbn93RySydYZuXuMmWdgo33mCO8V4z0fvvDdLUgx9INOHSEjpOuVgwrZdnX9jVdOGFoWKOEJMuF8HZt7D4dyaGMxl254Gihf2HhOCQmUqRPjd5QW4M8qGAwvHWj_1HOIso8M-pBYzdFaUTyuphNaMtF7L3-vCjDo9ri484a3RUhHuDvnDXXYzCwY0jS55bivQiTuPZtQgZnGm39nRZVWFubpjIczhh1keC_f1ZnVMUbJzmL0DYiysQMhYuML3SmzmYNODwgw0eS2X0dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت، تنگه هرمز برای ما از بمب اتم مهم‌تر است
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65353" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
صدای انفجار در جزیره خارگ
تسنیم: خنثی سازی مهمات عمل نکرده دوران جنگه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65352" target="_blank">📅 21:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWsqEMB6frW7qULQ4pJLVPnqgAnOfuSR-_i6cDh0u3eZ8vpcDq6zThxvKiaEoB-bVoXoUdObyNlRHDBlTNGzPyAhxgQumqH0UKw_pl5DKOPpOzYHfsmKHoFlNaSEXAOH8ZLta-3SRDWtOZRBrf50mt03bJk5r1uJ15J1hcgM5BtvvcXzXzMkWxG_rWlSfr5Gr2A_9t-SgIug2_IcOH98ilr9MRcbbDRXZkF-47uCIFNQw8Lu_W2070-8Upl2iC77NwAgPlIYmsUfDR0lOecxzAqU5sq9pkZS-uxe-G5QBuHH7oMOIbl5HRHdO8j6HN0nxzDnQ7GhyoIpcTlTnpHekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملا به بلوغ رسید!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65351" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457010896e.mp4?token=DlAITIummu2P4pOn_HdLZ3VRZ3QGKrQS3FfcDoF4HFI91qLrUniqp_8gdeWwWwCX3Qx2xoxHgShIOZs_D6Rg2EXypzLwUGI7aw-FnsEtAtoH8wE0gFe_301OmCF87wevVrla2UL-3BVifbXtaEl6C2fgB_z9V8vaVRPw293abrUq1FnGfj6N63ANot_BzqIb9xBI9z7lLf-URy7MJUHxnXIHffnOhze9y_HSCJrYOMjxeibJ8gLnJzsUbmUzKHf99W2yoffBbAdpUxbGaJXwUj8eOTaqF_R6Jhg7RPXP8bq5sdBtoejHIK0GRqTlCD9yGDkvtvnLZeqmXSa9hxDsaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457010896e.mp4?token=DlAITIummu2P4pOn_HdLZ3VRZ3QGKrQS3FfcDoF4HFI91qLrUniqp_8gdeWwWwCX3Qx2xoxHgShIOZs_D6Rg2EXypzLwUGI7aw-FnsEtAtoH8wE0gFe_301OmCF87wevVrla2UL-3BVifbXtaEl6C2fgB_z9V8vaVRPw293abrUq1FnGfj6N63ANot_BzqIb9xBI9z7lLf-URy7MJUHxnXIHffnOhze9y_HSCJrYOMjxeibJ8gLnJzsUbmUzKHf99W2yoffBbAdpUxbGaJXwUj8eOTaqF_R6Jhg7RPXP8bq5sdBtoejHIK0GRqTlCD9yGDkvtvnLZeqmXSa9hxDsaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با وجود مثلا وجود اتش‌بس ارتش اسرائیل اعلام کرد که در طول آخر هفته به حدود ۱۵۰ موقعیت زیرساختی حزب‌الله تو جنوب لبنان حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65350" target="_blank">📅 21:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65349" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
