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
<img src="https://cdn4.telesco.pe/file/U3tXZOi1J_sW_ACPha3F830QfLfnxHjX9PquzIYjr3-jMZOvXdxB1qThZhMPe9NYdQewQiyPmu1rVwTtXDZteMMhuSdZSQLSDC2VXRBnTCwblPyCFEhAQ_V-md89IO7xKIjVa5YclXIj0SWbKtIhFxdT8U4Y6GacZ3eE-nthoAL1GJmD_diIQEJwXP4mTwiI_Y2Z80bGvEaCM3MAt2f78q43jwgQkVbCfLZDMVfdrzDClU0iXThRVD2vR0-0dz9W32zpCWh31Aw5lbV_f52UpjaHlsElomEmh5lAoTwnZhZmbuGdzS5j8m9Att4OlSlMzmubWjXmoZT-9lQQrxw0Cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 921K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 10:37:55</div>
<hr>

<div class="tg-post" id="msg-133170">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
گاردین: اروپا در حال بررسی پیشنهاد‌هایی است که ممکن است امکان وضع عوارض بر تردد در تنگه هرمز را در صورتی که اجباری نباشد و مورد حمایت آژانس سازمان ملل متحد قرار گیرد، فراهم آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/133170" target="_blank">📅 10:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133169">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی: حکم مراجع بصیر به اراده‌ای برای طوفان انتقام تبدیل شده و هیچ گنبد آهنینی مانع آن نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/alonews/133169" target="_blank">📅 10:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133168">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزارت دفاع روسیه : ۱۷۸ پهپادِ اوکراینی رو دیشب رهگیری و منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/133168" target="_blank">📅 10:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133167">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
آخر هفته برگزاری آزمون‌کارشناسی ارشد
🔴
آزمون کارشناسی ارشد ۱۴۰۵ صبح و عصر پنجشنبه ۲۵ تیر و صبح جمعه ۲۶ تیر برگزار می‌شود و کارت شرکت در آزمون از روز دوشنبه ۲۲ تیرماه در درگاه سازمان سنجش قرار می‌گیرد.
🔴
داوطلبان باید با دریافت پرینت کارت و همراه داشتن اصل کارت ملی یا شناسنامه عکس‌دار، در حوزه امتحانی درج‌شده روی کارت حاضر شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/133167" target="_blank">📅 10:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133166">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXHYZwR3ef3m7yP70gJO4yxAw4HqOt5yhS3J2TSq9d8QjshhjpxFV3m3ZU0iinJOpAPyfdQhMtHZcvp7g7HW6iHfV3J7octkPJAJYlIJUTHHj7C-fkRxtG5fzJs1z-uUvzO-dmaD-j9JxGiLLIXxoQW4Splh6OqHpEKSyGzzDcyqgjQg9umTh8mvT2p2JBI9JKO_rLaKYTWP577EU4tZDwjHdG1BNnIHa1NnQO6BGA-_mzqk08DBA0m-D-JAOGE1Hp6PAGxNCPXCmBLSyhtSlzgyOIj1cyLPXJ-331vEQrbaWtgOww-4jQq4uwBaLCvaUGbVmhhoUp-BnX2f-EMpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی وارد مسقط، پایتخت عمان شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/133166" target="_blank">📅 10:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133165">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8bcc4a11.mp4?token=vYa6pQYrgy4DDJi6tYHL6Yve0O3FhBppy5Aj7m9t2tdVi9vgStxq9vSlUsxGSI_b5Gatnrhww0WYE4J3-w21OWQYjoaOO1_9fDkCrI3Q68X_9LurIElvCbx7fZy5Z-9eQ6Ti2fJUpS_F9jDMxj_B58UZl7edY9NsUC-bZlHePT7khPo8Jnlek3LKxWlaWtiHuJ0mqI3wjxFjruIZZER4bo5rr2HAMgZvmcD7x5G_f-7M2uxry6je_BfYLHSrWvr5BTRTN1nF2R_cYSnJ9nZFjMgJ34ehWRCtyvuZE59ALWUFSBf1jC1BewyJjEubGph5mEuUmZ_LI5Aq1_Twk2pnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8bcc4a11.mp4?token=vYa6pQYrgy4DDJi6tYHL6Yve0O3FhBppy5Aj7m9t2tdVi9vgStxq9vSlUsxGSI_b5Gatnrhww0WYE4J3-w21OWQYjoaOO1_9fDkCrI3Q68X_9LurIElvCbx7fZy5Z-9eQ6Ti2fJUpS_F9jDMxj_B58UZl7edY9NsUC-bZlHePT7khPo8Jnlek3LKxWlaWtiHuJ0mqI3wjxFjruIZZER4bo5rr2HAMgZvmcD7x5G_f-7M2uxry6je_BfYLHSrWvr5BTRTN1nF2R_cYSnJ9nZFjMgJ34ehWRCtyvuZE59ALWUFSBf1jC1BewyJjEubGph5mEuUmZ_LI5Aq1_Twk2pnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری دانشجو ویدیویی از محل انفجار در پاکدشت منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/133165" target="_blank">📅 10:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133164">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MqsKy8E74J0cJ-2JLhQxlKgBhk0D-M1iLlxXm_2Ub01H6AqR60Y8ngoQd3zn1EPKAwqmvdxoO597LyOY5gHnphLHRSQSCdn-IqRTEJ59cYqoh9Oc0DIIfj3bk7vLE5lWEzLFpg5E3PGLgOpCloEfjpi60YbJCKt_dKBQ2AhhadApOTC6ZnGxxRt-6N6Nl0Zp0ERQoYdoSKjGl0lvH-TPiky86ZcVZVoDJ1QzvSv0gZmOvBLPuV1WOmUv4VDsaMw9IT_nhRJL4KiuS4xvsS4thJQDRMyGJxLzd9qjgk53w9YB-6-l0M9u4EeVRr29AlKjydhBakNP2cIZ6ekoRKU5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دودی که از پس از امحای بمب کارنکرده ایجاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/133164" target="_blank">📅 10:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133163">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcde87d59.mp4?token=ezG38a4UujzKq36FxYjaWKrOYPyTj-wqWb1NllrIp6MH6VYpVZuFCICLkkozA-UoSSENp_29KupM5QeP7SDfMuGdnfIxWgqcxyLZLfazfl0c63earcrT2mfAeB-wPItX9JZOdeoidTzXya_xH7-y3z8IVdZ3lIH44177KNLIU_pKYocgUWCJP2l9ERrPeI3YSzZfxV9fHF0xG8DMUF0ZuOJc3HJqWHYkDjw56d6NoZfRoFl43v1U3Iq-g9J_tb3FG3-xz4dc0FK6AtK5vdGSJszUu8wMdYgzdJb_ZaLu48UM4dQgeEHPJvOIX6IQ1ODmeAjOJOZfmEbuzOTw5MDI3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcde87d59.mp4?token=ezG38a4UujzKq36FxYjaWKrOYPyTj-wqWb1NllrIp6MH6VYpVZuFCICLkkozA-UoSSENp_29KupM5QeP7SDfMuGdnfIxWgqcxyLZLfazfl0c63earcrT2mfAeB-wPItX9JZOdeoidTzXya_xH7-y3z8IVdZ3lIH44177KNLIU_pKYocgUWCJP2l9ERrPeI3YSzZfxV9fHF0xG8DMUF0ZuOJc3HJqWHYkDjw56d6NoZfRoFl43v1U3Iq-g9J_tb3FG3-xz4dc0FK6AtK5vdGSJszUu8wMdYgzdJb_ZaLu48UM4dQgeEHPJvOIX6IQ1ODmeAjOJOZfmEbuzOTw5MDI3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
10 کشته در سقوط مرگبار هواپیمای مسافربری در باهاما
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/133163" target="_blank">📅 10:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133162">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه‌های تلویزیونی اسرائیل:
برآوردهای اسرائیل نشان می‌دهد که ایالات متحده و ایران در حال بازگشت به مسیر دیپلماتیک هستند.
🔴
به دنبال درخواست ایالات متحده، به ارتش اسرائیل دستور داده شده است که تمام عملیات «حساس» خود در جنوب لبنان را متوقف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/133162" target="_blank">📅 10:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133161">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فرماندار پاکدشت : صدای انفجار مربوط به عملیات کنترل شده مواد منفجره‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/133161" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Acj_klh_nt7s8aH12qoqsfa4Lb_1I6gq7pjkE0aCqXmXC9RbmByNBAmmKhm4NUlBugtThaPzs7bs7WaBTw9aQjgNF0ccDXH4JZZBFHLUuUDmBALDqswYg8NZcvtuHE8VCSL34ffdB4GMKe8GAKXtsxCUUJovO53tLxBNgcMVMkascoXKXqzmNA8xAL9OmtUoOQiSn0emFKCFfprFZU22jWHchAxmNgvcXZFOrJrvtdaIVnA23HbOXFITrUyn-QPxZiayoQfOBwzDbttfqMcbGuqjJezoPZJlYVzlMDLdHE2Dt8TVmOrxZNuCKOn9AERmhntdre5Mp02WkYXB9nuBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nm-jOfN8rutZCgO-fstyOmSTwLBncRaUMLi9JZkIy-rBMID1lD7x7LPbsRI3WmrRojynfF_4LIGCY6ILO1gLPB4qOLR9hq9FNG-VhD_TwY4rcpqPdMeIM0IJWwIi7cNobNTB3q2lJiyykzQ1nY1MElXcExwDFxyFGSA6GO4G3AkyR_dfKS4MaNQ6auli6JCb_V9bnyVyEp2sU-GhxdH2Uut4xYswkfNtv6vIxONEWPz0ZsofHt65VPxoZA9WJ2apP0sRIiSz9xGeZYHq5n8huf85dgRBL4Um1WMLw9X9sOtQJIPm-0wL35VclVxzpXI15NDLWU9UWh5sEqyt4iGYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fT-aenZm8n_NEfnxXjO-nRb8aVigfknx_zr7jrL6sUukWI1zZhVg3KGXpr7mF7m2PpJ4xtkjaGg99JV31QbpCCGElKCVheo8mAQUkcI-8FyMcUl4Kaw4i_A2OatgMCh-BZHFwnS8cGO2hF1xbzeRkXNhblYv84SJhw0ijotZzfqZNfFwpJYQ3Jxk4GmBkl79zX08FveiZb_dfmhIlMv9sXtb0_uknOb9U8jOTMSGpBJVsrYp8__qhDU1rG_Zvonxg_--I18Bjv3MMagTa0_TLXE4XMceKSkX4N9JdJb7OMFleRrasGnpYOAdvefFt3PgQBTVw7MFeiBotQov6ZxBqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=N6pDH4EIIYghi_yZQ_5r2dCoiU5OL9UhpyrQntgXWwz18D7un3sJ0cKZAG5CplYa7dg-YlT014qrU80352PaXUH4Z6eeDUarS_VoXTycC1t6G3cW47Frdprg9VLZGtYJUb4_jDxXwKxURPlS_J7KWeYY51E5ks3xf-9IXkeEARMxN_zn1ro7byvpA7YTwKPNRTnOKsxtpge8j1oJWKhr7zEsbxlYjLFXZYXAd9oaVYg-lyHbJPeCHN8I2LjoS6DAilQ9reYOeLh5ocfHEI97Rve5DOT7ibLjnH4MaENlgwepshl1f78XoTVUq-Rnp5aBinCviD4Pj33umrpD1e1S-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=N6pDH4EIIYghi_yZQ_5r2dCoiU5OL9UhpyrQntgXWwz18D7un3sJ0cKZAG5CplYa7dg-YlT014qrU80352PaXUH4Z6eeDUarS_VoXTycC1t6G3cW47Frdprg9VLZGtYJUb4_jDxXwKxURPlS_J7KWeYY51E5ks3xf-9IXkeEARMxN_zn1ro7byvpA7YTwKPNRTnOKsxtpge8j1oJWKhr7zEsbxlYjLFXZYXAd9oaVYg-lyHbJPeCHN8I2LjoS6DAilQ9reYOeLh5ocfHEI97Rve5DOT7ibLjnH4MaENlgwepshl1f78XoTVUq-Rnp5aBinCviD4Pj33umrpD1e1S-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار حوالی پارچین، پاکدشت و قیامدشت در جنوب شرق تهران و دیده شدن دود
شنبه ۲۰ تیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/133157" target="_blank">📅 09:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj9ImzUYUHLd-L9CQRQfOjN6BoDSyOT-ArfL-FJ3TTqvjNk3YyVFgYJAhRmmotEiLXLU82tgbGyy3vd3mNlEqfEu4-fl8EHtO7JidEEwws9rEpswW6NI6_5tsyc4xlTlQTHDWakmbSIKsdxCrqGmq96YQHdvIdT1rTGSIDWB-PR-bVLFmQfmb-caEK9m7RmFsA_3RGQQEFL4d2c02FjU3LP69whXmTRRR9wEqZa8OpN57sf89xFEGp7AsiTehOfa6Iziciw1P0M0r0qosk7Uw-3SJH7fQufECsvwxjKm-UM6SxAgEcCN8RSyL8Z84ILJQyVJWA-EEcIA51bB6M-hcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس هفته جدید را با افت آغاز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133156" target="_blank">📅 09:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع اسرائیلی: ترامپ ممکن است حداکثر محاصره دریایی ایران را بازگرداند و به دنبال ازسرگیری جنگ تمام‌عیار نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133155" target="_blank">📅 09:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
صداسیما: ایران به دلیل پایبند نبودن آمریکا به تفاهم اسلام‌آباد، آماده ادامه مذاکرات نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/133154" target="_blank">📅 09:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCC95OWRApzjFdaFqebCPR_LtdgJRCckzKz1EtQsB6AR1KNuycx2j62vmXaBQ_IHb-EntmT-QWzYLv6g-X03zA6w1W_KoDDuMta2AQx8GFLwx5odwhPFHrsHuMJWMN2NRFrEd1MgH2I0IyDkNlQj88Ua5FsRJF_FaZbiIDs7qeqAGIzvR7ueoRVH3jnHtErqbGg1-icl6TbsHn8Htpd5TUJBbsh7xnslP7o3d3TBJe3PzGHheTwtyqJRLT0ZmRg4B0OGDAUzxdmLwT_u-0Qi9n_m-RVPoexz5Ou4UgVWioqTNzjZndxzFx0uzKTvh6E5RwHolazTQUUAgz7Bk53YGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس : ترامپ روز جمعه، با ولهید عربستان، بن سلمان صحبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/133153" target="_blank">📅 09:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رویترز:  کاهش فروش نفت ایران به دلیل تغییر رویکرد شرکت‌های چینی که به سمت خرید از بازارهای دیگر در منطقه گرایش پیدا کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/133152" target="_blank">📅 09:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133151">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a515cd66d2.mp4?token=M58Y6fovKxV3n1dcyoy0gwRxPtLnwuX9TUILfnVzDFwvRHqTYY5b3G-28Ob0DB9YaGi12x-0TVLTzMjXOeb5Kdt9J9-c0BwK2G2bWzBrjSc70uUWM8AfDlr8Js6s293FDoysnAQ8m4OOgQQeHA-OxevpX3Ak-PYzR4aerUUaXV-qf1KRDhBACeolT4qzEc6tzuRAiHwWBM_Pc2WODcou2DYqr1oNDXs8Ffd5dQ8vYTHccnLfp0pG5r8Q_P13lAjBoRUuXDz6iQZKj8spsE5mZYk2dg7P1GOoB_YF-Hb_Dwemk-709ODXML5tOzzIWpcQFcfFffBeM4h2pxKGzjpBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a515cd66d2.mp4?token=M58Y6fovKxV3n1dcyoy0gwRxPtLnwuX9TUILfnVzDFwvRHqTYY5b3G-28Ob0DB9YaGi12x-0TVLTzMjXOeb5Kdt9J9-c0BwK2G2bWzBrjSc70uUWM8AfDlr8Js6s293FDoysnAQ8m4OOgQQeHA-OxevpX3Ak-PYzR4aerUUaXV-qf1KRDhBACeolT4qzEc6tzuRAiHwWBM_Pc2WODcou2DYqr1oNDXs8Ffd5dQ8vYTHccnLfp0pG5r8Q_P13lAjBoRUuXDz6iQZKj8spsE5mZYk2dg7P1GOoB_YF-Hb_Dwemk-709ODXML5tOzzIWpcQFcfFffBeM4h2pxKGzjpBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
35 کشته و مفقود در آتش‌سوزی جنگل‌های اسپانیا
🔴
در پی آتش‌سوزی گسترده جنگل‌ها در جنوب اسپانیا تاکنون دست‌کم ۱۲ نفر کشته و ۲۳ نفر مفقود شدند.
🔴
شعله‌های آتش بیش از چهار هزار هکتار از جنگل‌ها را نابود کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/133151" target="_blank">📅 09:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133150">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شرکت هواپیمایی سعودی «فلایناس» اعلام کرد که از اول اوت ۲۰۲۶ پروازهای مستقیم و منظم خود را بین ریاض و حلب سوریه آغاز می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/133150" target="_blank">📅 09:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133149">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0aaW5crnEmGlXdVVyT7Hv64bEZ37Mbis7e9yOTEFFpoAyj8J2Fru-bdafW1wO2xkLdh0DzjY5KizRLzRTg_CLkYvZdVJfVVxmsiCezXtbdPn_knuAC9SePRJU0ry0g5WCWPSzGSRRklC0_Uy6YD4fMvslm_tjX6txqyBp3jkuWJCBnOn8lleYW7ptW-rQB87LFWAhRfCfneGbeATIsUHV5Jd2PbXKbEOD_GAht6TNJIHrr_1gvAtlC32TCLRZ5CG0etCrebjeY-_9VDwZEaZ0z8ofpyvI5LdTmEOoL_X30Jd9h9pgPPKjKlzg9-F1zUo1LKeLcxRUbB9XuCSr659w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ۱۰۰۰ موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا - که در این مورد، خودِ من هستم - عمل کند، شلیک خواهند شد
🔴
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133149" target="_blank">📅 08:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133148">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بقائی: نیروهای مسلح با چشمانی بیدار تحرکات دشمن را زیر نظر دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/133148" target="_blank">📅 08:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کیهان: «پل ملک فهد» عربستان را با موشک بزنید
🔴
وقتی پل «آق قلا» هدف قرار می‌گیرد، باید بدون هشدار قبلی پل «پل ملک فهد» را هدف قرار داد. اگر به پالایشگاه‌های ما حمله می‌شود، باید به پالایشگاه‌های آنها حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/133147" target="_blank">📅 08:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی:
دولت ترامپ معتقد است که احتمال دستیابی به توافق هسته‌ای با ایران رو به کاهش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/133146" target="_blank">📅 08:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133145">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سی‌ان‌ان: یک مقام آمریکایی اعلام کرد تا زمانی که ایران اجازه عبور آزادانه نفتکش‌ها از تنگه هرمز رو نده، واشینگتن وارد مذاکرات مربوط به تسلیحات هسته‌ای نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/133145" target="_blank">📅 02:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dU1dhkIgpIERfMFJIAVy5zoVNWjEYwyG1dnr4ayuucTPOuo_LcEMHJnDOHV3PcTdRADxbz7JexI6aCb6mF3d39AbZ5Qfd3vgFItb-Vpipg4Talwddnj-heRwDNbOeBx7Atcwi2DYdhQt2jF1B_K6nvqEDzXI-WalJ7yK6B0sGM_P2rZs4_xrX907_xsLcGPb2zaAcH6XeIq2JeBsWHhcDsfT4lVzYAeVPBXtroi3_ZyAW1CMqr8HUKUs8lMykibjCZ-G5RxXqEPMdUAY-gfZ7RZPpwnzRRwwXiqSxNb2QiG4RjI5TMlBnr5MpcEaf1bOKrQAXVh08jCXVwbrMM-cPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l6ROVyL19MtEa60_oLmE9Du525GXLwL7ymeeUD7MSG_X6aHGU3WbenoaJyKnMc0U3pQ7ZuGgYlDtu6NfWZq54jZfh3Zon7km3tzSuwGCe3KgLW49bVAtkGOqrOZAQKSN5Ud_oyXy7vZujth4Vhsm26VHu-0X8p8LkepEQo9-r9odODz72fqnRfSpBM0K_STrMS836MkO93OnII7PFaeCjL1RwirmDv9n049Mo1TU_ZRo1zEj_HXNVVFV69e1mL6EJPLgHd2IVH0mJSWr4GM0FIBblFdOGDxAGP6WYB2ISSsAij1O7tw_UoAbZMqGiWhrmQ8Nx3o6CsLXWM6D8HTpPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دوستان به شدت دقت کنید این کانال و امثال این فرد کلاهبرداری محض هستند و کوچیک ترین سرمایه ایی وارد نکنید که سرتون کلاه می‌رود
🔴
هر کانالی بهتون گفت برید فلان ارز(لیست نشده تو صرافی‌های معتبر) رو بخرید قطعا کلاهبرداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/133143" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-v0sv8iQ3-Ps5ZvNlHtfv7g77HfykaiCBOCK46FScNICq5MF5F7dyjpfGXlQRQ5lzQvnVYPaebOiDLVV8vq5z1KnB1zDva7Gl_IkIbmw_QHXhxaOwWcUrAXrN2OFfquMmo89lDamCyP5zsMouStuSAVz--mM1SeitTHdqq2uf8DYK8qAJNSUypQxJZ-_omZrULgbc64WtOVOhLEkl-ao2ZWhjeV1ToZkBJFaYErJbg6hI14PzXGhoOgqD-WJeMecGqUUGRYNq0Hewp0eLOxZJmoJPV8cAf18YuzwC2gyHU30ZwhpSX-8KzykeXXW7-64nbKn2N9YAwx66FWIKLA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الناز شاکردوست به دلیل استوری اعتراضی در دی ماه به دادگاه احظار شد!
🔴
جرم: امنیتی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/133142" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس:
به گفته مقام‌های آمریکایی، آمریکا به ایران تا شنبه فرصت داده که رسماً حمله به کشتی‌ها و اتفاقات تنگه هرمز رو محکوم کنه و اعلام کنه که تنگه هرمز برای عبور کشتی‌ها باز و امنه؛ و اگه ایران این درخواست رو قبول نکنه، عواقب سختی درانتظارشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/133141" target="_blank">📅 01:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsDWieD_sMG-5h5_inS9pOV8yNvf5EaGge0F2kvcfjZ0qzC0NU6UhrbC6rOP_fHr3ATJFBi0UpYMIMuoGqU-tx2SSEyUG_IvVo-1ELkiSKrLVrCjqLA0YgYgGvk6mRScA_7BLKvvbhxJsuFMNHfUYbDJC2T9_nD73vBYnugcayoLamBFlVjna6g2PHYgQAMp_X3hIuWiINFfed1x7ez6rKsRmdlp6_Qs1aZVITF9_mZFJWUvV0MXyybp0pN4rTCrQ6S0VsY-vNrdcxGqcOx6j8omYWgff_Kt3kvv8F4hLYUtIqssoC75SHLcbP1BManSmchZtI1S_43vUvoJp7kzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
اگه میشد خودم خرخره ترامپ رو میجوییدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/133140" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">تیم ملی ایران هنوز شانس صعود داره
‼️
اگه سر تیم‌های بلژیک، مراکش ،سوئد ، ژاپن، آمریکا، کانادا، پرتغال، پاراگوئه، آلمان، برزیل، مکزیک، مصر، کلمبیا، آفریقای جنوبی، اتریش، کرواسی، بوسنی، سنگال، ساحل عاج، اکوادور، کنگو، الحزایر، استرالیا و غنا، بلایی بیاد یا هواپیماشون سقوط کنه
تیم ملی ایران صعود خواهد کرد
شانس: 0,0000000000000000001%
@AloSport</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/133139" target="_blank">📅 01:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/13ba9b7985.mp4?token=LXm6yooOqJFzimUdwfN2B3d2zZllv9c66QWf-OlzWbxUXtH1G9ioMx2cxMkOW7b14gTPtZmMTAvqSs7ELv8l8jeUyOxkgN_UFOd8wqfF7wFFU_LMHhaYN3M1gC0xiseDBvGBBS8KzhN-GDaRNsBRHUK7yhgwvHFl6-1lnwQ_vwGrEgLr_waZj-NEgKUIo6ygXtMVlOWOdWMWlTRVq-s8rEuIuklZO-zWeM6pDEpst5UvOPmiE5Z7jPVDdGPmNyFy4FTcwdpT2TiqPuvdbDgIHLgI5YX3ltwYe4bix7BAp4x7iKP6k9YPEZlEKUtvZNR6xvo4dEA_X55UPWwhTxC2yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/13ba9b7985.mp4?token=LXm6yooOqJFzimUdwfN2B3d2zZllv9c66QWf-OlzWbxUXtH1G9ioMx2cxMkOW7b14gTPtZmMTAvqSs7ELv8l8jeUyOxkgN_UFOd8wqfF7wFFU_LMHhaYN3M1gC0xiseDBvGBBS8KzhN-GDaRNsBRHUK7yhgwvHFl6-1lnwQ_vwGrEgLr_waZj-NEgKUIo6ygXtMVlOWOdWMWlTRVq-s8rEuIuklZO-zWeM6pDEpst5UvOPmiE5Z7jPVDdGPmNyFy4FTcwdpT2TiqPuvdbDgIHLgI5YX3ltwYe4bix7BAp4x7iKP6k9YPEZlEKUtvZNR6xvo4dEA_X55UPWwhTxC2yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه دختر دهه هشتادی: من خودم جز جوونای معترض ۱۸ و ۱۹ دی بودم.
اما بعد از شهادت رهبر فهمیدم ایشون چه شخصیت بزرگی بودن، خاک تو سرم که دیر فهمیدم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/133138" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
آکسیوس:
دولت ترامپ خواستار آن شده است که ایران طی بیانیه‌ای عمومی که قرار است روز شنبه منتشر شود، اعلام کند که تنگه هرمز برای تردد کشتی‌های بین‌المللی باز است و متعهد شود که حملات به کشتی‌های تجاری را متوقف کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/133137" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e875fd4fb2.mp4?token=gcgtoS14XPZMKk1WBzJ6PWQL1K_uP2iXlippep0fubfQS38pn-v3mn6pBDqfZYl_KIziaU5p5Xxrecw5U7eIYIz8z06nizfEtlhjoEOJHARtKpuYZ5CP0MGmLfE60FZcn2Fvpzum3QrRTgcLnqj9UmX6xgQ_jnT3fUmUybcC9WjhPyHbp8IKZJrFyZ7ePibBL1IlruWUWPpAvbD2E8Gwx97q7Ep8dxwToRxQFqPh88IkgPcpErXWsOckfr46V2hQob2AU2UXSFCdgUbbKD12ODsBjF0xspY5IP-ezZT72DoiAUCd-kPgROEI_Sr13N01T9_VyjgDfh5B2hann86Acg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e875fd4fb2.mp4?token=gcgtoS14XPZMKk1WBzJ6PWQL1K_uP2iXlippep0fubfQS38pn-v3mn6pBDqfZYl_KIziaU5p5Xxrecw5U7eIYIz8z06nizfEtlhjoEOJHARtKpuYZ5CP0MGmLfE60FZcn2Fvpzum3QrRTgcLnqj9UmX6xgQ_jnT3fUmUybcC9WjhPyHbp8IKZJrFyZ7ePibBL1IlruWUWPpAvbD2E8Gwx97q7Ep8dxwToRxQFqPh88IkgPcpErXWsOckfr46V2hQob2AU2UXSFCdgUbbKD12ODsBjF0xspY5IP-ezZT72DoiAUCd-kPgROEI_Sr13N01T9_VyjgDfh5B2hann86Acg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی وزیر اسبق امور خارجه:
اسلام‌آباد یک پلن فریب بود، اگر تیم مذاکره‌کننده هنوز به این باور نرسیده، جلسه بگذارد تا برایشان توضیح بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/133136" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGpNa8KLJPja5d2WzgOu2y71x6GhGY-yaX7f72IvjLBvE1YdzjFmXB1eoVlkMYGuI3zXtXuwGGhq5oOz_undn3sSMFAIf63Rkygwv34gG24K9yjgfwhkx6q3Mzmg7DKG8SEq2ALNsBbcUYF5yGkFiLOa45wzFf8m8gVBvp0jVNEIcWVm4WU3YyfJHLEx9ocbxw8eDt0Xo67oOQFJcLL_iM7SKMA6EIl7CcHg7TDs9YCYXSlCkm-cmFhBH3eDAH8QobsPf31t_9UPEVtwfl0x-GSgZ2oUh5RTtxJnbXKUUIyNU0dQsX9yiKzNqVWxBvWK7PnaxvFClNhrGFxwshCrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره
اپستین
!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/133135" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
معاون اطلاع رسانه آموزش و پرورش:
شنبه جلسه‌ای در رابطه با تصمیم نهایی مربوط به امتحانات و تعویق یا عدم تعویق برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/133134" target="_blank">📅 00:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133133">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbP2K_dgIUvRPAq1X-ekG4JaahxrzAy6dhU9AP4ASOh5LEbP7cFzY9yYi23voYabmRIfPDphLPiSK92GrGfaSCp6Yf6yqSlpaiE099MdzeE2m-75z06NBO0Lv-i1hqhaVInMITXuojdz008IBLUQ6-y1s1mf5xl_z6nNna2rgdy4UXranap24YsOqn43qVPalpbmEZKHrPqF4VaNUA872FOqWeIDHRlsBZ1IvyqjLZ5LGC-EpVafjVLUM6YOY0xqw9-xjOIMMhWGoVnTv15q_MGGDAkcwGtRwFT1fiWLpMPpRf8MdX1K0GtsluQH7YcVEd9T0gS6JM82XmawqI_yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان:
یه جون دارم اونم برای آقا مجتبی میدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/133133" target="_blank">📅 00:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133132">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری / العربیه به نقل از یک منبع مطلع:
تیم‌های فنی آمریکایی و ایرانی در تاریخ ۱۲ جولای (۲۱ تیر ماه) در پاکستان با یکدیگر دیدار خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/133132" target="_blank">📅 23:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133131">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده: ما هیچ درخواستی برای مذاکره با آمریکا نداشتیم؛ اما درخواست یکی از میانجی‌گران منطقه‌ای برای سفر به ایران را رد نکردیم
🔴
این دیدار در مشهد انجام شد و دیدگاه‌هایمان را به طرف قطری اعلام کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/133131" target="_blank">📅 23:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133130">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرنگار الجزیره: احتمال برگزاری دیداری بین ایران و آمریکا وجود دارد که مکان آن ممکن است ژنو، اسلام‌آباد یا دوحه باشد
🔴
برگزاری این دیدار منوط به موفقیت میانجی‌ها و توافق بر سر فعال‌سازی باقی‌ماندهٔ مفاد تفاهم‌نامه است؛ پروندهٔ تنگهٔ هرمز نیز ممکن است به این دیدار موکول شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/133130" target="_blank">📅 23:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133129">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHzE1bX0Z3j4AJvJ1pj13RpxFCVzgK8EQF0TEoTVQA14BCMOjtEThBeZBf2SLLKcIRRS1iFuaRrhLUwwg2y6_9tHtGnOUfd_gtJCiBtLnyDc7rHvQSi1L6gtBOqOIA87OMRWe6bLOViDJQGMZnNQyEkrAqcYyx_9mZSkp-B28-IVeicMHedjeg_xFrca30mwsSoNU1qMy5tt2DLAwRzn2DH-z0uxBWSj37CXTKJ2vwbVZPjTfxN2_AfcS-iEo9gT1WVbPDtF6kyJljAMEcL7XoGaKXXK7687ZyMcBsLImNAVpnb2LHaVxRNqxqjWsklWzs2ZiAY_wveuqavXEJVEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی در تجمعات شبانه: هرکس مانع قتل و قصاص بشود؛ خودش گزینه قصاص می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/133129" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133128">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b106bf152e.mp4?token=ReMMUKdPERNIyr8U79W4_BP8wGO-TqU4v8zxjEdIovNyYp80gBJ7em4fn0rtnYHIKGJIlBnivrTZRfKsvntv6zQIsL6j6w-LzqwweB5jTRZlBF7USMSJEgSOShLHuOWYwgCfmzHNJZyRTOnEcCpJDHfeWERe-quiRY175Tc0IVqd_RB_yJWo0HSGYiMwfAHWgMrIATt4pEuAiFAor1duWOgdJycrZlcspsahV-J_CvpKwMd_pjXb7efl1FPvBCpoUk0Co9gyBFMRZsUuYsGBKZkko3y0PdI2IOwaC_71hJtzp_mk1qYlX7dXbcU_iz__oOBgPnkaaCsqWDrK-pR_OIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b106bf152e.mp4?token=ReMMUKdPERNIyr8U79W4_BP8wGO-TqU4v8zxjEdIovNyYp80gBJ7em4fn0rtnYHIKGJIlBnivrTZRfKsvntv6zQIsL6j6w-LzqwweB5jTRZlBF7USMSJEgSOShLHuOWYwgCfmzHNJZyRTOnEcCpJDHfeWERe-quiRY175Tc0IVqd_RB_yJWo0HSGYiMwfAHWgMrIATt4pEuAiFAor1duWOgdJycrZlcspsahV-J_CvpKwMd_pjXb7efl1FPvBCpoUk0Co9gyBFMRZsUuYsGBKZkko3y0PdI2IOwaC_71hJtzp_mk1qYlX7dXbcU_iz__oOBgPnkaaCsqWDrK-pR_OIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون کرمانشاه آتش سوزی کمربندی نزدیک به میدان شهدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/133128" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133127">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مدیریت بحران آذربایجان شرقی: آتش‌سوزی نیروگاه حرارتی تبریز ناشی از نقص فنی در نقطه اتصال به شبکه برق بوده و شایعات درباره حمله به این نیروگاه صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/133127" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133126">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ایروانی: اگر آمریکا به نقض تعهداتش ادامه دهد، ایران دیگر ملزم به اجرای تعهداتش نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/133126" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133125">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ناسا به دنبال ۴ داوطلب برای گذراندن یک سال در یک مأموریت شبیه‌سازی‌شده به ماه/مریخ است.
🔴
شرکت‌کنندگان در زیستگاه‌های منزوی زندگی خواهند کرد، غذا کشت می‌کنند، سلامت خود را پایش می‌کنند، پیاده‌روی‌های فضایی شبیه‌سازی‌شده انجام می‌دهند و خود را با روز مریخی که ۴۰ دقیقه طولانی‌تر است، وفق می‌دهند.
🔴
هدف، مطالعه اثرات فیزیکی و روانی مأموریت‌های فضایی با مدت طولانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/133125" target="_blank">📅 22:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه فردا با یک هیئت دیپلماتیک به عمان سفر خواهد کرد تا در مورد روابط دوجانبه و تحولات منطقه‌ای گفتگوهایی برگزار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/133124" target="_blank">📅 22:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLEMGvVGpcWh76zu4YaIAJNLG5AzEnahb_SybVYD13EPRMtSnSVS0WY-r_wFD7tgHQbRU5W9WdrZYaUpmBaGJMlnTXj8WiZK7kJRx15pwzl9sf2y3Rm5w2OfPH3yW5AjpS1_PrPBuN0enhYrBpjX7-br7kb5vVOpmSl6TIVOlrqUP2umMMoEAdBYUjmlOb3IHKwInbCVrHWou6V-fK9HUchgo6bCLtZbc22pE8eQGlrJ09xVZEpAm7LOgrkeCkWiPOG1CPYvTv1jENprpzVwSwA67-ypsso6J0aeU3zTTvmGrYouAYZ-0f4qYGXnyCVb4IfFMv2tuJHJ-NefBrF9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین یه حمله بزرگ با حداقل 270 پهپاد به سمت زیرساخت های غرب روسیه انجام داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/133123" target="_blank">📅 22:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزارت بازرگانی آمریکا روز جمعه کنترل‌های واردات کالا به امارات را کاهش داد و صادرات اقلام نظامی، برخی ماهواره‌های تجاری و تراشه‌های هوش مصنوعی را تسهیل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/133122" target="_blank">📅 22:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
العربیه:
وزیر کشور پاکستان احتمالاً به زودی از تهران بازدید خواهد کرد
🔴
العربیه از قول منابع خود از احتمال برگزاری یک تماس تلفنی چهارجانبه بین آمریکا، ایران، قطر و پاکستان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/133121" target="_blank">📅 22:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا تحریم های جدیدی را علیه ایران اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/133120" target="_blank">📅 22:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ef9e8b4c7.mp4?token=UIUf8z3f8n9Uz6zfa6N8oc1PeKqt29ncA230FUYRciIh1yc67Brh3KY4B0G8NC913nrGrsPkl1h2r0kQ5iKq_BayrrLrY99yI14X3nqx3H_6zPVkWmajBW6232HHFcpnCSP1jE0TAT2jimlo-YYoGDPS_ubpAbG2vtLZs8kGybeMg8E4LOVIsAhTmeXN_TKFQgVzpVDfabx4TqhOljfvPSnLJeZNAxyJGUpXOqdFJWtedUfQMjWUcKmW5TvcKi2EBkqsnw1iDiHLMdhEuYZd6UQxSfIXRE2SC7zOWv1sg-gXxem9K4-3RXwYwLXts1HbhXk-eK3rCwu4GXZ4doqgkGEhyFgug8f5_1tk_sMnBi3erQJLDDLiqKhR9MkbkTKfN0F2FvxcDW085RZPlv53FpewfpLrp513FmbsZjQJkgYUrt0NjP-fs7GJAc6rXFpgWt3maPn2Xbg3OlCvys_D1SCLRwueyZf7sQdp0mul-afqOp3KXjZeNf62zwZ0m8aMpAdsDC0hRiW5QSb72xtEY2eKVTCYoCfIPstiYDXFHitAR0_KGWcF2fZhpdmE7d3PpuzPzDyWCkSSTlCXAm9jU3Cn_YnY_1O_y1h02H5hJEB1n-oVNhtoV6KVZcTwkYz6gBm1_T_JMx7mtxNbfPTaLfib_s2y6ZTHJx2aElgnNeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ef9e8b4c7.mp4?token=UIUf8z3f8n9Uz6zfa6N8oc1PeKqt29ncA230FUYRciIh1yc67Brh3KY4B0G8NC913nrGrsPkl1h2r0kQ5iKq_BayrrLrY99yI14X3nqx3H_6zPVkWmajBW6232HHFcpnCSP1jE0TAT2jimlo-YYoGDPS_ubpAbG2vtLZs8kGybeMg8E4LOVIsAhTmeXN_TKFQgVzpVDfabx4TqhOljfvPSnLJeZNAxyJGUpXOqdFJWtedUfQMjWUcKmW5TvcKi2EBkqsnw1iDiHLMdhEuYZd6UQxSfIXRE2SC7zOWv1sg-gXxem9K4-3RXwYwLXts1HbhXk-eK3rCwu4GXZ4doqgkGEhyFgug8f5_1tk_sMnBi3erQJLDDLiqKhR9MkbkTKfN0F2FvxcDW085RZPlv53FpewfpLrp513FmbsZjQJkgYUrt0NjP-fs7GJAc6rXFpgWt3maPn2Xbg3OlCvys_D1SCLRwueyZf7sQdp0mul-afqOp3KXjZeNf62zwZ0m8aMpAdsDC0hRiW5QSb72xtEY2eKVTCYoCfIPstiYDXFHitAR0_KGWcF2fZhpdmE7d3PpuzPzDyWCkSSTlCXAm9jU3Cn_YnY_1O_y1h02H5hJEB1n-oVNhtoV6KVZcTwkYz6gBm1_T_JMx7mtxNbfPTaLfib_s2y6ZTHJx2aElgnNeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فحاشی های هانتر بایدن پسر بایدن به دونالد ترامپ: چطور ترامپ از این کارها جان سالم به در می‌برد؟
🔴
چرا هیچ‌کدام از همکاران سابق شما به او نگفتند: «برو در ماتحت رو بزار، آقای رئیس‌جمهور»؟
🔴
عذر میخواهم... پدرم واقعاً می‌گوید: «توهین نکنی ها، هانتی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/133119" target="_blank">📅 22:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا تحریم های جدیدی را علیه ایران اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/133118" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا یه هیئت فرستاده بیروت
🔴
تا به حفظ آتش‌بس بین اسرائیل و حزب‌الله کمک کنه و نذاره این آتش‌بس به هم بخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/133117" target="_blank">📅 21:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سناتور ارشد جمهوری‌خواه لیندزی گراهام: ما با کاخ سفید بر سر نسخه‌ای از لایحه تحریم‌های روسیه که آن‌ها از آن حمایت خواهند کرد، به توافق رسیده‌ایم. این بدان معناست که این لایحه به قانون تبدیل خواهد شد.
🔴
من همراه با سناتور بلومنتال به نزد رهبران جمهوری‌خواه و دموکرات خواهم رفت تا ببینیم آیا می‌توانیم زمانی را برای پیشبرد این بسته تحریم‌های روسیه پیدا کنیم که ابزارهایی را به رئیس‌جمهور ترامپ بدهد تا به پایان دادن به این جنگ کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/133116" target="_blank">📅 21:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، اعلام کرد که طرح‌هایی را برای ساخت سه شهرک اسرائیلی در شمال نوار غزه آماده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/133115" target="_blank">📅 21:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
صندوق بین المللی پول IMF پیش بینی کرد رشد اقتصادی ایران امسال منفی ۵.۴ درصد خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/133114" target="_blank">📅 21:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به ۱۳ شناور در نزدیکی کریمه، از جمله ۱۰ تانکر، یک کشتی باری، یک کشتی مسافربری و یک یدک‌کش، حمله کردند.
🔴
در ۱۲۰ ساعت گذشته، به ۴۸ شناور حمله شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/133113" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL0Froa6X-JiD5QVtT5Ex_Zai60TlN-uLOwESIUyXMm-hUQCHqRMt2jO20am4d6a73IQENpGdzoKxVqq75Q4DjOMFkHHLY8bbWDARdUa8LiKrAqjbdYosSitRc7SyvnYb-mXc38EM0VJHuIlPLhu8_WaM6cjXRPQRXKhEkVE4tzKOrJYwp3WHZqddndjcwzOqsv7G5RWuT9aaATScH9WwRVqDme-2gZ2EygWjUx62kmI461iJaN-Ru_-U5QkkHkavcb1piCAVDqlhpEvwkJ-mq1_8bON_WRQaaaK8D3UwG-6MEmFWvAE7b-gugIEKGTPTY8AHH14YqQr6BEpJPtR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار CBS: مقام‌های ایرانی روز شنبه برای گفت‌وگو درباره تنگه هرمز و اختلاف بر سر مسیرهای کشتیرانی که از آب‌های سرزمینی ایران عبور می‌کنند، به عمان سفر خواهند کرد.
🔴
میانجی‌های قطری به‌تازگی مشهدِ ایران را ترک کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/133112" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شهباز شریف در تماس با پزشکیان: ایران و همه طرف‌ها خویشتن‌داری کنند.
🔴
بر ضرورت پایبندی به مفاد تفاهم تاکید می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/133111" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
منابع خبری اسرائیلی از سقوط یک هواپیمای سبک در فرودگاه این ورد واقع در منطقه شارون خبر دادند.
🔴
بر اساس اعلام این منابع، در جریان این حادثه دو نفر مجروح شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/133110" target="_blank">📅 21:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d149dc62f3.mp4?token=H2ExFIBl8F7B2weNIVm7VMQmNKWLIBQKYInzBU7qvoE6UR0ec8l4Sv3AnldHiouYtbPkCjk2OlwGEk-tUCJjChXNXDibrALl8QLyryAN6cX5QhAz9l0bDQt605eAxAa1JACfmhZ7k_c8Xb4wjlZ3JZqaLHwh7rbqz4OdmxHm82B3jAfhG5NtTtsq31d48Yu21JlXHbBCvmUyiSj3NjdFs9hC3v2HQRUct2jM8_qbJlowqu5HLfFKeLmcFLeXvcG28Hf5Hf8kZJ_w3gGWWRiaOAIlv0giF3fqWmyR9PdqGWL9sI6izHu8Sh8NpbxndJAoHDMhhotjVV-y41-mcGK6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d149dc62f3.mp4?token=H2ExFIBl8F7B2weNIVm7VMQmNKWLIBQKYInzBU7qvoE6UR0ec8l4Sv3AnldHiouYtbPkCjk2OlwGEk-tUCJjChXNXDibrALl8QLyryAN6cX5QhAz9l0bDQt605eAxAa1JACfmhZ7k_c8Xb4wjlZ3JZqaLHwh7rbqz4OdmxHm82B3jAfhG5NtTtsq31d48Yu21JlXHbBCvmUyiSj3NjdFs9hC3v2HQRUct2jM8_qbJlowqu5HLfFKeLmcFLeXvcG28Hf5Hf8kZJ_w3gGWWRiaOAIlv0giF3fqWmyR9PdqGWL9sI6izHu8Sh8NpbxndJAoHDMhhotjVV-y41-mcGK6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داده های ماهواره‌ای امروز دو اصابت آشکار در باند فرود در فرودگاه بوشهر در ایران را پس از حملات اخیر ایالات متحده نشان می‌دهد.آثار سوختگی نیز در اطراف باند قابل مشاهده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133109" target="_blank">📅 21:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تسنیم :  انفجار در قائمشهر را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/133108" target="_blank">📅 20:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کان: ایالات متحده از اسرائیل خواسته است که از انجام هرگونه اقدام غیرمعمول در جنوب لبنان خودداری کند. بر این اساس، رده سیاسی به نیروهای دفاعی اسرائیل (IDF) دستور داده است که تمام عملیات حساس در جنوب لبنان را متوقف کنند. این دستورالعمل به IDF تا اطلاع ثانوی و تا زمانی که مشخص نشود تشدید فعلی تنش بین ایالات متحده و ایران و مذاکرات بین اسرائیل و لبنان به کجا منتهی می‌شود، معتبر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/133107" target="_blank">📅 20:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiSWS1InBAvwfbSb7cYdb9GedIfXBuQQz4H0sGRIS4_ac5eDPIJCKVfVXyl7pPh14UJrk4Gsc7q7ZhEJAXnhqb6o67CqocpufXIzVM5xkEa49GXthsPc3aR7Hsscvhh3358L6I71Ej3Mn6KhWyw9N-78labPZ7FFh50zEdzBbZwI3IJhCgwIxzD-wGeEMJdRDjL3DXxrAK55ps24N86EG2WakUQfzM4dnkIoZwm7fcVJGU5IV8aZWjAfBshWjGDD3nhKMeFdoRLVGUnE45O-TVNcvGHH7mfnYzX10NDqT8k34gKnBI0YIfPTug4EAVqHoolZXnRqOkC-crttDHnA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شورای اجرایی «سازمان بین‌المللی دریانوردی» (IMO) در نشست روز جمعه ۱۹ تیر، با صدور تصمیمی، تلاش‌های ایران برای تحمیل حاکمیت بر تنگه هرمز و ایجاد نهادی جهت کنترل تردد در این آبراهه را به‌شدت محکوم کرد. این شورا از تمامی کشورهای عضو خواست تا حاکمیت جمهوری اسلامی ایران بر این تنگه و صلاحیت قضایی آن بر مناطق دریایی کشورهای ثالث را به رسمیت نشناسند.
🔴
این تصمیم در حالی اتخاذ شد که تنش‌های نظامی اخیر میان جمهوری اسلامی ایران و آمریکا و حملات متقابل دو طرف، نگرانی‌ها را درباره امنیت منابع جهانی انرژی و ایمنی کشتیرانی افزایش داده است. پیش‌تر، نهادی تحت عنوان «سازمان تنگه خلیج فارس» در ایران اعلام کرده بود که تردد کشتی‌ها منوط به دریافت مجوز از این نهاد است؛ اقدامی که از سوی شورای سازمان بین‌المللی دریانوردی «مداخله در ناوبری بین‌المللی» خوانده شد.
🔴
در مقابل، هیئت نمایندگی ایران در سازمان بین‌المللی دریانوردی، ضمن رد این اتهامات، آن‌ها را «سیاسی و فاقد مبنای قانونی» خواند و تاکید کرد که ایران به دلیل عضویت نداشتن در کنوانسیون حقوق دریایی سازمان ملل (UNCLOS)، خود را ملزم به رژیم حقوقی مبتنی بر این معاهده نمی‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/133106" target="_blank">📅 20:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
قالیباف : تنها با کسانی می‌توان با آمریکا مذاکره کرد که برای جنگ آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/133105" target="_blank">📅 20:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قالیباف : این درگیری با تسلیم شدن ایران تموم نمی‌شه
🔴
اگه آمریکا به تفاهم‌نامه عمل نکنه، ایران برای دفاع کامل آماده‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/133104" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رویترز: کاهش فروش نفت ایران به دلیل تغییر رویکرد شرکت‌های چینی که به سمت خرید از بازارهای دیگر در منطقه گرایش پیدا کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/133103" target="_blank">📅 20:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: ترامپ مدیریت پرونده ایران را در دست دارد و اسرائیل در این معادله نقشی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/133102" target="_blank">📅 20:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e41Xk20WT-zVxmLf_i-tILz-mVLRN2IbZG91-skDhXxk1SC_-8MgetdACWqNZ9BcyRCMvb6eBI-Vl6coYj1sm27zp2nKtyhPeXNBd59aUz2iVfHroKgy711GyuuzsTwpE5jl4evSEWNPzs9le2Hw2glajcinxzvhmqgFHqv2sqovkNvh2KaKhR6Gq5RYZkbjK4opxlkqXKwnXWo3ylJHbMlxnmAl8pFuPoEft-lo2Sp-ADC6LH8Teeh_P6DPiD0WdU4cdizqz85MlK1cx4-BCGz-gkqpzHslYv1Pq5mTwNsbXdohbzgF5qEMXJLmE6CJOXqUwzNGI6xtQqghnpf4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی : ترامپ بوزینه‌ای است که نام انسان را سرقت کرده و مانند یزید، به زباله‌دان تاریخ خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/133101" target="_blank">📅 20:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزارت بهداشت لبنان : بر اساس آخرین آمار، از آغاز حمله اسرائیل در دوم مارس، ۴۳۲۱ کشته و ۱۲۲۰۰ مجروح شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/133100" target="_blank">📅 20:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
جوزف عون ، رئیس جمهور لبنان: مذاکرات مستقیم با اسرائیل ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/133099" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=clpxHV5l5a5ZnVvWmK5704QFABP1Juwm0KjJHtVZsqWTvYazeaRHiJ62Nw69gXihcSoEqzJ6WpN-46H0Zsnrl_mglt0Y94ybenoD7EEJzVoxWcO0NHwu83SMklZoNG1TXmeht0tGWmihRGPA_szXj0tjpRmSbl_btSXMngzpk6Uldv3Q6YWBkumRm8wQLJRnL8j0xQ4Yp4k7_JKfzw3aD9Ondk1DFZqF65yfLM_frapf6SWN9ieyWvrfXdtYr6WPj77K4YMiWfTPBuV8M-ZRCEXFVIUtFZt3Etxw4zFV9Ja_dSQgqDx0dxgi7Beu4KB7Ses-4KgKmOS4r6HEr3w1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=clpxHV5l5a5ZnVvWmK5704QFABP1Juwm0KjJHtVZsqWTvYazeaRHiJ62Nw69gXihcSoEqzJ6WpN-46H0Zsnrl_mglt0Y94ybenoD7EEJzVoxWcO0NHwu83SMklZoNG1TXmeht0tGWmihRGPA_szXj0tjpRmSbl_btSXMngzpk6Uldv3Q6YWBkumRm8wQLJRnL8j0xQ4Yp4k7_JKfzw3aD9Ondk1DFZqF65yfLM_frapf6SWN9ieyWvrfXdtYr6WPj77K4YMiWfTPBuV8M-ZRCEXFVIUtFZt3Etxw4zFV9Ja_dSQgqDx0dxgi7Beu4KB7Ses-4KgKmOS4r6HEr3w1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در شرکت اکسین پالایش پلدختر
🔴
فرماندار پلدختر از وقوع آتش‌سوزی در شرکت اکسین پالایش سراب حمام خبر داد و گفت نیروهای آتش‌نشانی و امدادی در حال مهار حریق هستند.
🔴
به گفته وی، آتش‌سوزی از انبار مواد دفعی آغاز شده و تاکنون هیچ تلفات یا مصدومیت جانی نداشته است. علت حادثه در دست بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/133098" target="_blank">📅 20:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: در دیپلماسی با ایران همچنان باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/133097" target="_blank">📅 20:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
الحدث: ‏تماس تلفنی نخست‌وزیر پاکستان با پزشکیان و بررسی تحولات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/133096" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نماینده روسیه در سازمان‌های بین‌المللی واقع در وین : روسیه خواستار تفاهم کامل ایران و آمریکا و حل‌وفصل جدی مسائل موجود است.
🔴
ایران و آمریکا باید راهی برای برون‌رفت از وضعیت کنونی پیدا کنند، در غیر این صورت وضعیت در منطقه خلیج فارس بسیار پرتنش، ناپایدار و خطرناک خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/133095" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فارس: درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/133094" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133093">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
شورای شهر تهران: رایگان بودن مترو و بی‌آرتی در تهران تمام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133093" target="_blank">📅 19:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133092">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
چین و روسیه قطعنامه شورای امنیت درباره برنامه‌ هسته‌ای ایران را مسدود کردند
🔴
روسیه و چین پیش‌نویس قطعنامه‌ای را که با هدف بحث درباره تحولات برنامه هسته‌ای ایران و اقدامات مرتبط با آن تهیه شده بود، مسدود کردند.
🔴
مسکو و پکن تأکید کردند هرگونه اقدامی در شورای امنیت باید با هدف حمایت از روند دیپلماتیک و تشویق گفت‌وگو باشد.
🔴
هر دو کشور معتقدند که رسیدگی به موضوع هسته‌ای ایران باید از طریق مذاکرات و آژانس بین‌المللی انرژی اتمی انجام شود، ضمن اینکه امکان احیای توافق هسته‌ای نیز حفظ شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/133092" target="_blank">📅 19:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmKjY1lcUajedjMIkCcsHIu0d4a2WyTaL1aJnJh0wHo3YYoi3HpQCH8zZIXJ4eLIbd0qJ-LkSJoJUGtnpKjTAC8g7noiXukswg1U6IDINK89FbQWFOi4Hq3VVdpmVGO5pmG_Xf8VX04Io9IUBoaWGmlbo2PfgclLTGbZJtD3El7V0erSN3-trBto9Qpz3qSpvYGkePfyEyfLf4kkfgkHHSjyOljKx-FVHQ_PenzoHBkD0rN6UkjAClbqnN4InUHWIVEGs7j037gHJ6kHJFYkk-HNaTAlQcvIOgzTIYE0NWnI14wtt_MVC-weiVh25r9PQp0m7qgn7j_lWSJs6FpKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، نزدیک به تیم مذاکره : ترامپ و آکسیوس رو نادیده بگیرید
🔴
تا وقتی دولت ترامپ به تعهداتش عمل نکنه، هیچ مذاکره‌ای انجام نمی‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/133091" target="_blank">📅 19:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133090">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اف‌بی‌آی جزئیات جدیدی درباره یک طرح تروریستی علیه رویداد یو‌اف‌سی در کاخ سفید فاش کرد:
🔴
«ما متوجه شدیم که این گروه به‌طور ادعایی قصد داشت حمله‌ای با تلفات انبوه را با استفاده از پهپادهای مسلح به مواد منفجره و سلاح‌های آتشین برای شلیک به مردمی که در میان جمعیت فرار می‌کردند، انجام دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/133090" target="_blank">📅 19:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TagBr4quqZMqyZzcKesop8_2yQK32CXqFXUAVT4oJYOCW8a9Wm6AEkbnEluu7KmBPbhVswx-0qOhsRuaUcObS191ELGvGN48oK0BNH5-80N00a9i--JS2yJ4XwOS7dxEiFwnOwppYL15OA3QHV4MQdIugMomI7ZXB353U61bYxoJmACsWQVJ_e0nbeZvbG-LajnLfeutqA4D2aaMl-8xp8YQUTA0CvpFuSYce4d0lUn0SqSyM5cBHyVrldSlOh4u06QrtAYhsc0sgeLy0Ax0NRz85dzwhgcEfXAoWbvkPGMAg63GqxiLZmrlNHwQcbBzOfrL81KyrLHgL5uQjcofEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: دور جدید مذاکرات ایران و آمریکا، هفته آینده توی سوئیس برگزار میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/133089" target="_blank">📅 19:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نماینده پاکستان در شورای امنیت: ما به دنبال دستیابی به توافقی جامع بین آمریکا و ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/133088" target="_blank">📅 18:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سی‌بی‌اس: ونس، ویتکاف و کوشنر در تماس با مقامات قطری در چارچوب تلاش‌ها برای تقویت دیپلماسی با ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/133087" target="_blank">📅 18:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: من دستور دادم که در صورت موفقیت در ترور من، ایران را در سطح بی‌سابقه‌ای بمباران کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/133086" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133085">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6y87womfBzzf39wpBSc5Z7exnrD0ABlduxzbgp7UZe-8ayW-7R5z2T6Il-gehogl6JhZv5fSkTd9ny4msvHI5JPkZXXEiEmE0DTiyqj2wFBzcwCsdfSeulHCZ5uFhIJDyhCAxdEspbZJTwhJBeJjEOlUVAvMoFDcXt_GINpVf4EJEbE0KGJDQW5-IwN_Q0PccA1J4xHuMcfzdCEXSPlxnL_G1-gqTq2pIFHV8JrbhM8LVFZyo5RKphPj6DBPh5UNgA2rrlUuH0QuNE7KKy2uV21TUl2iMcSFwjzlGhwyhxj0rq2I3m8rs_TtyB24WWO6sxlfyHcql0bmJMVTTUnVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری منتسب به کنارک
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/133085" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133084">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / ترامپ به نیویورک پست: در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/133084" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133083">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گزارش‌ها از انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133083" target="_blank">📅 18:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133082">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/391b205ef7.mp4?token=IGxdHawr41V9mNpVu2mn8eH3qI5xdo6Wx7k7NOH0Oue7yvYczrhiI3sIFpXbbnG0aSVG5qb6Qe-mlbAvh8IqEaeIbb96SMm1rRw-XuzjXelgEEtbBRpMprDg4_Cd8kMG2vA-eg8gOgd9IpkvxC6KuWVZy0BV2F9e4XAUuh7kroBHm1L51bPqVO_0VohpdvA8cUUeSBKRrpBj45ZIOTRPe-VBNsdPlcmCGZxdFPMYOWiQZYQHd9LzyW3Ub8bUhT1QT7xNDMluFl9bPpzim4qdW6LcyBOsdgEEr0nfzIxQz57g5dfjoDjUZWFjxWsx3kRJ4FctQ8ursiA-VeMGQWTbWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/391b205ef7.mp4?token=IGxdHawr41V9mNpVu2mn8eH3qI5xdo6Wx7k7NOH0Oue7yvYczrhiI3sIFpXbbnG0aSVG5qb6Qe-mlbAvh8IqEaeIbb96SMm1rRw-XuzjXelgEEtbBRpMprDg4_Cd8kMG2vA-eg8gOgd9IpkvxC6KuWVZy0BV2F9e4XAUuh7kroBHm1L51bPqVO_0VohpdvA8cUUeSBKRrpBj45ZIOTRPe-VBNsdPlcmCGZxdFPMYOWiQZYQHd9LzyW3Ub8bUhT1QT7xNDMluFl9bPpzim4qdW6LcyBOsdgEEr0nfzIxQz57g5dfjoDjUZWFjxWsx3kRJ4FctQ8ursiA-VeMGQWTbWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از بین ۱۲ فروند جنگنده رادارگریز F-22A Raptor نیروی هوایی ایالات متحده که در پایگاه هوایی اوودا در جنوب اسرائیل حضور داشتند، ۱۰ فروند در حال انتقال به ایالات متحده هستند. تصاویر نشان می‌دهند که هواپیماهای F-22A در پایگاه هوایی RAF فیرفیلد در بریتانیا فرود آمده‌اند، که احتمالاً یک توقف موقت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133082" target="_blank">📅 18:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133081">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / ۳ انفجار سنگین در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133081" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / ترامپ به نیویورک پست: در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/133080" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133079">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
براساس آخرین آمار پایگاه بین‌المللی هواشناسی «Ogimet» که وضعیت دمای ایستگاه‌های هواشناسی جهان را رصد می‌کند، بندر دَیّر در شبانه‌روز گذشته در صدر فهرست داغ‌ترین نقاط زمین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/133079" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133078">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c4e411a5.mp4?token=RHUvz8BLqF4OXcK7xnZujhzSVeUryim2RQsGTP5BEpysOLT62Iifvh91_ylM45Fcd3gl29RyyQRxueCeOG-wt8tJvCJpIcrxzAnP9qOu05G6J-RmJwFR4Tu3Ws7lgGcsh9oNlDqbwvoqxXh5-cQ-Ov7NJAEYDKvQ_nz5G_XBIObSYT_YJm_3ADHofBiHZm0LV1ZhbkaAuWYyuYulS_YgQ1X5kGgRVf3ay7w5VqZIdwQbxVkCXq3CmRw7sp1dDbDpNSq70mlwQFhVge0UI3O02NBw2g5trEI60nxjSbiv_WygukZbaVyG_00ZgzC-uG8nQd8rI3sPEtmd4MYmlkS9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c4e411a5.mp4?token=RHUvz8BLqF4OXcK7xnZujhzSVeUryim2RQsGTP5BEpysOLT62Iifvh91_ylM45Fcd3gl29RyyQRxueCeOG-wt8tJvCJpIcrxzAnP9qOu05G6J-RmJwFR4Tu3Ws7lgGcsh9oNlDqbwvoqxXh5-cQ-Ov7NJAEYDKvQ_nz5G_XBIObSYT_YJm_3ADHofBiHZm0LV1ZhbkaAuWYyuYulS_YgQ1X5kGgRVf3ay7w5VqZIdwQbxVkCXq3CmRw7sp1dDbDpNSq70mlwQFhVge0UI3O02NBw2g5trEI60nxjSbiv_WygukZbaVyG_00ZgzC-uG8nQd8rI3sPEtmd4MYmlkS9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده چین در شورای امنیت: قطعنامه ۲۲۳۱ منقضی شده و بررسی پرونده هسته‌ای ایران پایان یافته است
🔴
قطعنامه ۲۲۳۱ در ۱۸ اکتبر ۲۰۲۵ منقضی شده و رسیدگی شورای امنیت به پرونده هسته‌ای ایران پایان یافته است.
🔴
اصرار برخی کشورها برای برگزاری نشست درباره موضوعی که از دستور کار شورای امنیت خارج شده، فضای مذاکرات را تضعیف می‌کند.
🔴
سیاسی‌کاری در شورای امنیت، اختلافات درون شورا را تشدید کرده و روند دستیابی به راه‌حل سیاسی را با مانع روبه‌رو می‌کند.
🔴
چین از کشورهای ذی‌ربط خواست با حسن نیت، مفاد قطعنامه ۲۲۳۱ را اجرا و از اعتبار شورای امنیت و دیپلماسی چندجانبه صیانت کنند.
🔴
نماینده چین با حمایت از موضع روسیه تأکید کرد که شورای امنیت دیگر مأموریتی برای بررسی موضوع هسته‌ای ایران ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/133078" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نماینده فرانسه در سازمان ملل: ایران باید به طور کامل غنی‌سازی را کنار بگذارد و به آژانس اجازه بازدید از تاسیسات هسته‌ای را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/133077" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نماینده فرانسه در سازمان ملل: ایران باید به طور کامل غنی‌سازی را کنار بگذارد و به آژانس اجازه بازدید از تاسیسات هسته‌ای را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/133076" target="_blank">📅 18:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133075">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری/ترامپ:  با ادامه مذاکرات با ایران موافقم اما آمریکا به ایران اعلام کرد بدون تردید آتش‌بس پایان یافته!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133075" target="_blank">📅 18:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCrFk6bVuT81Nxsjhg5-rF6FFjJ03drbkwsIVBrv_GGsTaBWEEcmH2fsTGcZdSZ9KgbmKZ5QWt5wGvZ5ZPeGUZCvx3guO1VnFgdyt7iUOXzhC6DXBNa3rA0RmOI5UFvIXoWmOPwHUTayvNbmJVGTbQD7n9e_J2bLxbdEHDcatdPrCk7qmuPdq4dRO5UViCvKoBOxx-0-h2-vc_1j0cj_9nzVAdqtNQcUGz83dBT6yw8FAIfJ1VLNQc61fMd2VEJ8YaafO3NLXoty_2KdnI9tS9kk3XT5bn3-FY2jJOhvGViMP1SjFWYSU9ckr3rr3hCcJsM3y3bglpn7uMMWRR3H8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای به تاریخ امروز از ناوهواپیمابر ابراهام لینکلن در حوالی دریای عمان و ۵۰۰ کیلومتری تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/133074" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUKYnxZlJlH5fDu02SdjxvvOdoKJZUL3B7dxs3KQ_NgITgVh4DuB0JFbc80AuoOzPtZ-vz6qjSNIzTA-Brctd1wOrZDvwjhzXOucZLIe96u-hqlGgsEra0nsyQDCcpnIwLrjJSjoB1Yumxp-f4k95lMUvhSwGQcxRr-b4qaIjPhsdmUXEFeClhTLp_oA40PgSTvSSFAqBhAEyIKtqHmHkGjm-Q-b7wQ5Er-1tEQ-xDD4XLRtImGTMTbhzooBPIQ5MItEgq0V45q00JXqp17G2ROxdEqKUD8vmwk2HYh4ybCWTjRaLv6K_VoiI9yrlkBR3im5qBN2xL2z8L8GHg7jAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور مجتبی خامنه‌ای در مراسم
‼️
🔴
امشب، موقع برگزاری نماز میت برای علی خامنه‌ای تو مشهد، یه فرد با صورت پوشیده و ماسک، سمت راست تصویر و بین جمعیت دیده شد
🔴
اطراف این شخص هم چندین محافظ ایستاده بودن و همین موضوع باعث شد توجه خیلی از کاربران فضای مجازی بهش جلب…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/133073" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGrezwEHeU4IkOj_O66epWdLmVouWnsg4t8Y-6MGwMd3mCPcfe2_p9z5SSlDISK7N6YDJNWltkulzJV8oXOIk2wqMCdljtD4TMEqeY-lNYJhsH690WntoAIDpYTl_bu7KeQAEAUzL-ARcxNOHYSJkkObOb_JO-kqbfwIfn7-nyZSc1NXNmExNenhBI29NkvKPnPwus6h2MRaBpZKkWJyDRTBJeAqwFoF1hxhQh_YTDPqrXV632uKqfyjGXSznxO9rfuYE33nSdt9xcfwL0lB6ihYsmhg9oBrmvlquQiGl0-aq_P4BAkOg1uEQSh1Z0W0_A6jOuQGW0M0tsK4wp1k7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از پالایشگاه ساراتوف روسیه که واحد اصلی تولید بنزین آن تقریبا نابود شده است
🔴
این پالایشگاه تا اطلاع ثانوی فعالیت خود را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/133072" target="_blank">📅 18:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
روس‌اتم: ۶ نفر از کارکنان ما بازگشت به نیروگاه بوشهر را آغاز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/133071" target="_blank">📅 17:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J46Bo7uXjB9G6mPTVcHHwXwOKv1MCSPIgRKYbRpHiiHOZBDYQhKLSI0IBXLlaYDEz29AnVl0dhSbrnvdBkn86Ns2twM0PPTOTY4-rQN4tCUhOk1nwP3NgqfN9J4qGHs0pv4fkGzt5XpGMnsDgWsMy91r4One1b2kD5b4dCwRDKciRYkSkTNzK80dNagvv-4NT9v2CYEsNv5cX65P1IUf06ShSj0KgxLCPrvYpKr0FHmuCFaAX7UYn9aluwourCziygCicOCoAhwD6A9TUeqjwxLGnMhMRRUJIO_1DTLrS1IBx6CE79OrnSgDM9oAm1pEEDGVcxSfcpzRdW7h4Crjsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد هواپیماهای نیروی هوایی ایالات متحده که امروز در پایگاه هوایی شاهزاده سلطان در عربستان سعودی مستقر هستند، به کمترین میزان خود از زمان آغاز این استقرار در اوایل ماه فوریه رسیده است.
🔴
آخرین هواپیمای نظارتی E-3 در اوایل این هفته از آنجا خارج شد. در حال حاضر، یک فروند E-11 و ۹ فروند تانکر در آنجا باقی مانده‌اند.
🔴
به نظر می‌رسد که ارتش ایالات متحده بار دیگر فشار خود را بر ایران افزایش داده است، و به همین دلیل، بسیاری از تجهیزات حیاتی مورد نیاز برای انجام عملیات‌های بزرگ، از این منطقه خارج شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/133070" target="_blank">📅 17:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
طبق تصاویر ماهواره‌ای یک ناو هواپیمابر آمریکایی به همراه حداقل 3 ناو جنگی در اقدامی عجیب به فاصله کمتر از 300 کیلومتر از سواحل ایران رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/133069" target="_blank">📅 17:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رویترز به نقل از سه منبع نزدیک به کرملین : حملات اخیر پهپادی اوکراین به پالایشگاه‌ها و بنادر روسیه، عزم پوتین را برای ادامه جنگ بیشتر کرده
🔴
پوتین در زمینه تصرف باقیمانده منطقه دونباس اوکراین پایش را محکم کرده و مشاورانی را که پیشنهاد آتش‌بس در امتداد خطوط مقدم فعلی را داده بودند، توبیخ کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/133068" target="_blank">📅 17:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tax60Yux_prJIX9qiBoJ8uvgM9Gqy768U8GjNKSVYvV__DGruq6ynj4bAlHt40uapS9Hbanb4iNdxxc2ZmODWW94BxCwUeQxHCSfoFk48SbTKQjjAvbqC0xZcvfzA-NCqYx5NXtqn8hJ9sksq1uLejQ3klPcu2dnlF-YWsRGzSEV8jvVU8xnblHP7UfvRdK__OPsfpq5u1evN0dOpeQxgMYT8eIThkK3dGy0LB-QGSbl1D_FLTqdnq-7hALEiHzsWAjr3uFWFXC4HeAoNY4NkgFYQEOGV-wVDcA6XECoXhhNQgdu5NLSfbgh7LfTXCz9VDvzgUkjaSV6951db7TYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق تصاویر ماهواره ای منتشر شده؛ ایران مسیر های منتهی به سایت هسته ای فردو با تپه های خاک مسدود کرده تا مانع حرکت سریع با خودرو به سمت این تاسیسات شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/133067" target="_blank">📅 17:41 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
