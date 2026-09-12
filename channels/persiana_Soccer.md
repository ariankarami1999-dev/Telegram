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
<img src="https://cdn4.telesco.pe/file/ptBShGFRi0UIXwwbdd_hUY48Ph30WOmpWBSHiu3f4jxbcQLMH4DlLtYZKbpejm1Sk-5I6ZqbtCQ23reWQwAl3NOdR642i3VnDTfYOVryr5PYP1E130DitS6x7PjZMdlou_ySGJ-2QYAa3AKJxy6OmhUvhBsrUzbufTk70umJ9uDf-zIop-HwsvOu6iFMQEFutmWHcHbHEZu5del1bl2DG8qcsWl5dQr0q0r0wgWK_2DEL0kbXPZaFYd0SaBwod5HC0laoOZxhbsVFD9nORZ-Z2xciPFvnZYUgF2uRtttjyk4ibjBhlep4Fc67pQNdVv2aL5jxDrxpgTshHx4aCMGLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 527K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWWmC_7JEIHb1Q1OWTG5ocfn7_RKOixI8ecIgGqb7wxE3D5xoZbuEqQcrltB605MnTJh_6TFbWUCjtjMW-yQonze0STQvN0Vzm1s_tmNoujzuLFhaFjbuwvkfDyyi4IKAKJ_g4avp5RGceqXSUv_ZCyWxiL84Sh2fIUU8dsZ0kcwMDn7qRgYPB4oD53HGFCf10Toeswo43F1cDgPNvCsA-l8C0ZEWeu6LlVPN8GLKGq-K7Jvj0-wWj8GM0nIk-cU7uqmUnaXOemeYiLbU9AdtX71NxqoD4xhvWThbeSozWcxymLxu20dcUQwhz5tLkg0a5RM7Q6smnB1xpTdD5y7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuT2acNcIzHPgniOyVV6LtFjbPTn5U4Q6aNcfj0sJeKnCK855bdE5JEuQkw2CebGAUxMKXCwkA2KuNLYnL5-fZIzi6u0oR1fRIaal3YVFFkgtv__BfQPZalVOXrARUlGBrevPJ5k8VfDzL5S1s5ObushPNQnya1zCrlhQWGTkbosMPJDhcYlMe67qOT-ln4kR2hNlr4e_JPgOXetvLNrFxWyld3scMa881seVXZQEmypUQasz4y78x32EZnoaoX4SWlJtEM1s8SxtYyHXgdxPG-njmwu-TwK0e7THsfcZvHvvU_6svtA8hXNinmEnhavAbJgPWl7eig6QuJzPajWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tT6havQfxjxr9tkuLTrmq2HtYjCAfSrHyPXYryhbDQqHmK9PENrI0QlEvkOTFgyJlDTXz_fqg0V8TMw0FnBe6Itq82EDrIY1FdKu6m57uW2kvR1lYqLZOEUmnloK591HPSCMyIgRQBeSiRr7XFyCnHhcIbF36TTwFSGRkpLemxPaGbWwnZQX59tJhj0lDoHNIvMU0Xe1E-82N2iuQNl2E9cWSbYvs5dwW_aWhz2AKvNUdJogGxO9tqhB6sZJo0bdLYanOIXRC6vOmMnk8uwXLNK-BEMKycyS0lMy58jxFSq-kxybaTuXX-WbcEoHvAR5uzbOoliy4_eqS41Rw96LKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLfdCT0u4dI8H738pjEK1jp17JpzB5Fb7L_e1PPmWLOxr28haozbwfJI2CIMCPqyn_QJxe6Eq1zOR1dTitu_HdyEIvc9jAOvYjNVfx0J60rvadLEl9HbD3TM8bLHpxuHgkHEik4wutc9yZ6AkSHNfKOm_LYsn9YyLU_BFFOOPbz5wvF69K9nGrlLA5qWy1V7ho6JewprsjllgfDoIMZClCOPxjm7a4caFyD6Hs-k2DPJzfQ9rix99nq8RlPVDHIdXaMz2m3CGiz9QMap5PvljX7qkeMaW6qbzrN4BNlvVe4u_tBP0z8kDPI_dWfr6tWzYiqqDFKoG9O7xQ0DDqNwtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzI6MhehLPJJ2pvuJKhn98-WUM-7zrK_Ogr1hzJP5q1cb_NuXcqZRxrmi1mjGW5JqoOpUXeikq0rcT2GnAvhvX4TACeJZA_8Ja_wOi79K8pRv_bXoW8aoeLj2B9X87u3SSCf0ccF_AQmdC_sohvxyUFN2SWS7lRqLenR71N1XtSmDlhFU9XloaFFsBxgFdPTA_R1tW1M5H9TB2gFYOWYm3vYcTlUTa88J028Vb257mrwsWvbUOZdv6HEM9GOssPXER6UzYuvNPH7TxkOBGjNe4sLxomL2Qlg0c9CULb8SrUrYZkv81uvSGZpGhy52gns8qOowJPh3sdVxTLbatnVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29610">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgIuZJZDsmdTPi_sUJQgpzeULMw4lRdxDyVMlsyGWWqvVvGBbPA6sT4T0I7X1HJWwVdSyuA9a0mgFVBh5P3nMz0cz5llFLfUlFXSD_qAp-syuT3U1523nIO1okwR3e77RSLfuWjAZbu6pZxFnG5njfQqiY5gLv1U6JwQ6kRCOYBbo-FPESqkofmhX6VGpHz-1LS1Vnq9t5DC5m8bF_G8scGYoFCjcFy9KuITTAfPTAk57nD7rufbo1-BzNhOaxNZMJR2Vx9EmCxoGcP-PdB4yUk0JUxIej23v3nK7QzfhYbxeE8cY5Ul29A6IkIAwlZGsz9pshdcp1mvl-aDtvdUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
رایو وایه کانو
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
👇
👇
👇
g21
www.pinbahis.com</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/29610" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29609">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdC85qbWZMQG1pJhLaJKHfimzxGMNG6s5UR3GocSKiACeo0xoC3PLGyyj4VA5xTNP8jcHM33sFyzAL8-8KRpx724FxNOp7nM-9flZGpX9MEwKeMEAGDK0uAnkhTbU6d3AUvm5qKKtI5sZwjv1nW97OB7e5RUgYm-9h8mwxFm8-Ap-t41fqR4f8lQIWg1xtmeXhnTR6TmiT5FqjZFDjXhhsWBFOXiIlVE9iEyQaUXY-2tBOozMhFrx-TjLpcTFddrcXTDZiu89H_IbTUKeV73mTG3J8sKPMvP7xDugCvQuq2xpw6JEWgxhVOPGMJW5WbHWP93JLflD2b2OML1dnedug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نگاهی به آمار خیره کننده مهدی طارمی ستاره 34 ساله الوصل امارات در دوران حضور در پورتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/29609" target="_blank">📅 18:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29608">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFLD-2trte8EFScTgX6vWJaDfI2JBOEILWHIjpSCVZEfIDZ8YkSgBl03AqJqQjfxdY1mFfJ7z6UE9fpirC3L8paG2KpPOasyobA0kDtVbiva3ylcrLIbHV1bj9FT5U8q-qyFTNQkfcctLoXdG67ZT1PB4uaXH2V1FhiLKSeMdmbvqCey0Og4j1CNQJEWxiHoZTtkpF6PrLvLK0bA5iNTRrAH7YIn02mDdFSCow8eQJBD_6BkREpKl8-frXIoQYg2HTwHtBS41WuEmDljweQhNAlNsDpah14ZXoPLfaEyvUevx7IutY_HQI17DMqP6AfZ9dnfe58yKylK-tN3UVqreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29608" target="_blank">📅 18:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29607">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇦🇷
ویدیویی‌فوق‌العاده‌ازکاشته‌های لیونل مسی فوق ستاره سابق بارسلونا و تیم آرزانتین درمستطیل سبز
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/29607" target="_blank">📅 17:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1Gbneqv_VbXrcwh9B4O0ax4MH628kR4JSOwRLyURks8FlcAFPfqIB4lKFd-cL9NElnQsk4e5wQKO7E1dhQTnGGnFg0RcQWIAfFwuSg_h84CTfiaSpy5_lIdOzuHKyYNHktMF_FEQ1XljwW3PmVYzzAq5zLBWIU8hh0UVtj8EFs8xgIHsdMYUf3PwyYU8WHX-9V7bzLxXrA8B-mBKm5JaWCznh5DUOY_CSybXHq3XkwnCD6E26rDxnJTFRN7loe2rilIB6hHqIqmPTNtGPGQkZ-rEHK0utd8g-lDq452Kpa3OW2k9ejEEHHP_-IgE6dqC2QklX-Y1Tm9LmBPcPOptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQ_i44Cseb8uHwThRoWRXsGhBJdzIPcb9YxRNqUxNTybxGKvLVFoiNsCwxpKXzEFW7cTMkfdo6aws4irdLqYMYOWBKynwn_vdUwTAOLpWDbFqU9kLQzaJTpbs3x6y_EglLm3_lRBFYRhrpmPgPA0al8zfhk5gl3DfgJVPrsld1qXmKKiCpnZZvCfZZi_rfENsXailOKxjsif0Iegd6rpNzhKmBIqygPEeiJRGgXA-4ehJLNmtCMAp07ovTZJwp04G3zu0MASZCIjuSU85CHYpk3UloYfgFKZwFCdGNc3vpGMb3zV5ghFKe6sVrEEdtchhDKWAzoRwx5bJFoDKFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js4tgGy7pd_lyN7VIq1c5T7iAfqZVZB3wobrc1Yl7mI_83Ohw4Hov9-R1i_b42JTG1PYT5hois4W2EdFRCD7ZTLHsXZLMzkaPc4Shz2q9FSKjdmKXwKXMDsgU7xIqItiYQyNmw0NM7l5Qi5SlGLnQFMI-8hznqknzSfErYuld6DDBhkDaWK-IMeFTJuCA-vqAwCkiR_UtYcqgQKaSm8alIRiP-JVMkXNi28VwPljpGa5jv6kMq6l9VkR-dd6r0hBNnLF7oWcSSma_zvTPCnHLIDyPetHYUDzpL8ZVY7ZQiVcdaPTjnF8qt1g0ELjihv7UdSfyuA2yVcAcDqPYzvd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD67VcC34oZYj3UvqMeiTr_DW7PRWQeVahl25Z2CMjMoa-weTwAvO_sgcIH8U-e8YYeoFCFr9oHUh5woTVsdLqtOW8RdZtv8l-vlMQLnH5EMRQICtgGRPeHFxFLPHPvXbwZWYgb0p0zxzkq7lVA8AmzZwKat88VFm0ki8zN-6Qo4cc9RwQfytsOcbO6d0bLnko4G92hKbfMBmbUNdY90qVUdMBBEIT4wCjZJn_uF1TddT3hl0fZrmIGMRVXv-xxRuvMxvLftMsQlch9JXCFl617NGwn2fAxaiu2PRaynsYU6xVEqr1Lox6fFV_6A2UdVyAbGzHM_kc14D5e1IOT16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=FDWrkKHd9-ht3VsmHeTFjGfAIUkyhsuGlFFr_EvpT9nmHIIw4xz82HRx-3QnHsQ6NZrOwrWlZ2ZCvBSKktG-4KpwBPtfSn_2xEZiAbQZx8Lu8NQyV0A5hNtk7fFLqlqX0yunh1vOf0LZYCQRxt36G0JB_INccYog_sXSKIUC88P1ezy-O6HC0xJ7Ed8yhW9nKh103BbL80x95TNZ_4NPnlCOOEWL412_Egj49ggJ29domeYx7nEc6H0ULOiDfqRKau9xBQ55nyeISMYckvO3YnXOzwiJcUxl7vF-4w1nZWt50pa1JH4dU-a_e7UMPrwpDjd3ylKHxTjayZqAHQ_ANA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=FDWrkKHd9-ht3VsmHeTFjGfAIUkyhsuGlFFr_EvpT9nmHIIw4xz82HRx-3QnHsQ6NZrOwrWlZ2ZCvBSKktG-4KpwBPtfSn_2xEZiAbQZx8Lu8NQyV0A5hNtk7fFLqlqX0yunh1vOf0LZYCQRxt36G0JB_INccYog_sXSKIUC88P1ezy-O6HC0xJ7Ed8yhW9nKh103BbL80x95TNZ_4NPnlCOOEWL412_Egj49ggJ29domeYx7nEc6H0ULOiDfqRKau9xBQ55nyeISMYckvO3YnXOzwiJcUxl7vF-4w1nZWt50pa1JH4dU-a_e7UMPrwpDjd3ylKHxTjayZqAHQ_ANA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLFnfI9zvMwdyRfrEfjBP3rv4OzJt9wio0tYdmFXzBuoZxwtMHf4pNnGpw7UYuO6X_eGRh3smIbHx6Y1HcFdDuUsFhum6ZztLWJM0iImm4O1ZQlCy92FZR7hT2ynsrs4bHAqvPbfls_9dNyJ67gIZupU3qYiUIS2_pofFqBWIXEQza3c1DubJxjNtBiaKg5pqqeohLGVsAY2ns0isFARcoHb3g69PLFIqBJMqhC_jomHyCxjdmrt1zg8OZznK2eX7V2boR2gbmGSLDkVxtRLoYDcWk1joDj9zmuJNUqPuHKRAZd7sYCf-wyeHnEZ0ACx4XjMlBaeWqVJDzPmopPeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2KAxxQgbk9MWZQTcR5223bi3kInzi_Ngl3LrcPengMZe-Y7KJDXo6tOHsH-mhgbXsJcMNEjewKBDVOchQ1-Tn5UNjGT6-jR8GtcLdzroM2WIGRxswDgfLvQS_r4xRRRxt06h5yQ_NCipoZ0unvXVxn1qU-vM6ew1arX-dFdCPoYm79d4shIBWLTk_yDoBD_H_7qjL_0EBIQS4KO-ltv5VBy6LCaybTLOjSpKYuV-3yk0Z_gEJkACLfZDrl3KgiCvT1ZdlrHSXY_0h54y9kDPJF7iyvME2UKV4y8qJj-9VKD_I7zSsrKNuIvEbtVMvhkPa_t5OXqv5XPPAc2em-WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epWHa-_4Q1w1w5YXSJCrrVqW60B7PVKvo7c3Argnj5ZRjsL_ef6Zsf6W9up1BBdHI0wEoOe9z38Zkd9ZyT08E8NwyBbVZX_VsH6PuVX5A17BEYexMcizellvzLsOsCgs-RSyNWIBguIb9uCzw-nlEeQTwKk5MbwGiYqa5yK0-87s64DDMBhZgKnPwgiGJsViumn2Wjv0j4Zp0vH0R7KNA5NyByO0qsMvv9M0K1d62VUlIqOgl0kET4dxWvF-Y60H9VhQp4i1bMEb3Ea3Lgnx-Sglv2jhB5Aq8t_ilLnC2opewq2NvVhJErzuCMlYzit7qHhbfIDSvL-ce8_bHN76WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=tx_cpQBtTCV4RWYZZ3xKf9vT8Ar5As6FUKN5BGDCLfeIoyjUQ2ZbkU21HuzPTmo0mlfR6I_ZHGWUwOAPnxoLhpwttrcOpj5up7sknYjaFwi174fB6bFTdddji2X7585OrgLbCQcgIUmaAA9X9vECbvpABuUvfkZYuj2lngy2Cl9wJIuV6ceJKlJ9lCH-T39fU4v7wBxgYb5Akfx41lu-_Q2h73n9N2VbvHpNBS_CPMhJl-CDmJWb8F2DlKRy4Xp91TWu3lIumETxYVB0NcIAsnGKx3A7aP20XcvUUKk38qOmFiFYz-m_xNY_xt8mAky4VbGxGjG4tOqPc9OkADDeNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=tx_cpQBtTCV4RWYZZ3xKf9vT8Ar5As6FUKN5BGDCLfeIoyjUQ2ZbkU21HuzPTmo0mlfR6I_ZHGWUwOAPnxoLhpwttrcOpj5up7sknYjaFwi174fB6bFTdddji2X7585OrgLbCQcgIUmaAA9X9vECbvpABuUvfkZYuj2lngy2Cl9wJIuV6ceJKlJ9lCH-T39fU4v7wBxgYb5Akfx41lu-_Q2h73n9N2VbvHpNBS_CPMhJl-CDmJWb8F2DlKRy4Xp91TWu3lIumETxYVB0NcIAsnGKx3A7aP20XcvUUKk38qOmFiFYz-m_xNY_xt8mAky4VbGxGjG4tOqPc9OkADDeNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29596">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T55o4m2VPEQNYrUvLzFFfVMaZTpaK1-8bvgJOpsTLprY5a1GiVYmeUP-eNJW_WnqAEAMVl0pi6V8djBrDY_bZKnuUhgwPAKPs8AE_1r_g1RmhCBW56BaVEkWRewaSTYh8keHu-AEdaSdtz39WAReCJ6WLFHrOvtTJSuESZD1wKOAEtDlqIYrH8a411hwu-zOK6ViGCcbRILOTwLVnTvV2ZItBDqgwTfJO4289jGsJkkYnfO61EglBY3u-6JwsXBYHr1M181twOmlP-Q1IQ_jwjmAWwN-2KTHIXdwotEdMAaWBWiY6RVIs4X6_2uX2TBtSh9EnhKPeEW2Se0bT66XUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاریوس دروازه‌بان سابق باشگاه لیورپول در کنار همسرش دیلتا لئوتا گزارشگر شبکه ایتالیایی DAZN
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29596" target="_blank">📅 14:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wslx7AzbYttC3dSRHXvfdcnJ3MEMxHIzgcMdyA0utFHPS_T4EiG6J_jRrFJTFoOANjjVADS_xiTJYq9aq3RLiZnvGK8ko2eygSY1to6foiFE2ziy-c5gMPxJ4GsVjrr_CjIyDO4t3FehOOgcOpVH2f0sT5evy3uTg-wwkaGMYZr_03K4sJIEsG3mMoLLpXfHgxym8GCaQJepO7_MMr87qhiWVi8szMqcM8mmfopJjMZEht7jZgEznPix0VMsm4YqWchCNGEQBxrqFSaZWqZGR_TE0iAkzzza3Zi8CpvmFzTll80Eq8X4GEhtB8nd3N6B0kGP4FdGEFSCCW3F7jsYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozhCqX3sUhxnPBG20FYBiYuZ1ebUdK6nIsSgseC378L3CyEmTkPyIF8I4Qw3LXO7X3Tfzn6jVig5CUL6KopqFx5_-kyE-CSlA0MPGabCYJJUY44xajgpXAJDXTseptzRZb3-eyc7TiSXG5bY1ezI7bG46YuYEr3uNjoaPeSWh0K1efYrne85YmAW21IOUvYizp6TZ-pE575zlE93601jRRyubL0Io5okIZDKPP1ipdqZWj6BuPtSGUPElJ12hfTDyGgC1CLJRNNd2xUuPZB8kQ3WN4KCnHpRWszyzqh6vNmaoRxELxpXOCDMH0tSY-eibsA1vv24sSJKl21huzPanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro9Ddol6i9_wtX_6TXdieVrYSOeb9TtIJzlCtE-IFc5Zcro2N_yvf9GV_0ti-8qCmOK71uApI1DsWaLl6xQZ5AE7u2t7xN1D1tNkLLbtdZYNUyt9yav0zecDe7L-LOa9ZI5-JrRBCmhJ-pDA8TiPDhZ0lCGQquloeNqUUwh8B-dC1IprmiAFreqL5rTwmUwHfgkjCogc3cdTzuitRdpU5dvQQarlvUscjAl2pOcivgx_3rK-cNCHH9lI0YCC88DAdFMvclSktvgVQTn7sGv4XWIZimn6n3jsRyHabI5c817gXBwb1rKXUZBDd7P_8BaLxcW8dVeLRU4auf2j9cLkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp6OZ-673UuICAPbrKiuyvp0hG_bSkjFTjdhMLI31fiSaIo4A0s96EIEssjzu4gurk6tdupFWqmdzl4qP-g7VeXOoqAdAnrLmlTMriG65Y-pP-gioWzqtOCqegBRg1dSidHmL2QSDo1lreuwHcMTJOt3bcMD2nRYfKWIsOr_6L1Y7kPv-9pfLA4MfRv0D-ylDWNmmvRoZZ-mExYASIv1nx9ThFYUJmck5iIknqVEkmToaXe6Og75QbRDkfwmJ03iQk5e_WjeejgpkU8Z0y99InduU1JGn7zUKJNm_dZ3bQNQ_wJLfPerrBpfvlJJUcvyUOhPwHn8XjhTrvd8VNYYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU4LJ3XxWVKRQs4DMGlWNRyQp6kN3BWG_dWNcMb2mps3_1YBP18x7pD373IQvwW6S7F_FpNq2My1XyEkg9wYin3CiXgYSMqeOLadT7St55zT0n8yF1bgeYJL-SGwdttafK4RmX_qa9MRXGmKWYONroum6dGkW5A4kMEU1ocLV3Rf1i_eeZECce0Cq5Opv_2d6mb7i95VqgizRBogoBINMRJ0GvVRlS2VYCYbnpNTzr32wFUA_hH6eK9Wdvyy2dTxAbiedhzE_GW-5kXxSTjK7-rwbqa5nQajOl4iOH39S6nVemJRoO1sjyB3igBOL-YteXm_XAyyeTnB6g6XLMlmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLWaTYQ_temNHsVC0XaxGGsnLgqeRlf9cKkJtLE1mNZXPya7WuRbEcolxtpaHmB_cNH1tUCcao0KYKUFz03xF0rkDHjCn5qaLd7mIRKx4klZCPKmI13aHofTR0a6Y-gUKu6DvYss1Ymg1lu-fV9MdshVirNY_Hfi4_8A510kMX-GpViUrGUZ45xWTcj4dAsv9uVfCCCE2qLnGnwaJ8dSJFILjnr7-dqomYlgh4MznoC7rTXcGgvvCZenUzNLmqUx788HvmouO7e7GdikGqrIjO0u7sQVk7IMTZgNQ-rI9wWSq1WJupAweFxKApjuAAiJZ9Ksl3LoIRiV1rgsZC-loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
برگاتون بریزه؛ امیر قلعه نویی سرمربی تیم ملی که تاپایان جام‌ملت‌های‌آسیا در تیم ملی موندنی شد درخواست دستمزد ماهیانه 15 میلیارد تومان از فدراسیون‌فوتبال داشته و شرطش برای موندن روی نیمکت تیم ملی در جام ملت‌های آسیا این بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29587" target="_blank">📅 12:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29586">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تقویم
؛26سال از این‌خوشحالی عجیب و غریب محسن رسولی ستاره 19 ساله سایپا گذشت که با یک حرکتش روی آنتن زنده شبکه سه فوتبالش نابود. بعد چقدر بازیش خوب بود این پسر. یه لحظه نتونست خودش رو کنترل کنه شورت ورزشی رو آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29586" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29585">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrQRO_gazYn-vkH540jSTgT6JiolnGh6d1q5XfJBQ4UuytgjskqsjkQwCOjzEY0KO4WA5zyv6E9Go2JgoO6tcPIeahH9yWyc_Y2xFSdYFjnM17h7TmamkbdYf8ij-VMCZkWK93VXMk_Vz_t6ipWLddw71uw8e4vJUcOaDWiXFYhxpAlMF-QPdUrhJF989DKGR6UZmtnjOkJ4ixZXYOELNX5NEUypOAN6T5x3f9bLjBnZ4kKUL-GcaGDgujMKsaSwZhvHZMqaZHGyq3IH8hOFVflk7Ci57VRAn7Y_YCPuYqiTO1ph-bc7QrhFgkq7ws_flvw7Jm6DNJ8sr0SzGayiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛ فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29585" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29584">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkgeN6Tt0kVQbDGm2QjSgLP_63RwC7u26ce0yc72PzQwi5WeJwBcPOQQe91pA_tiJoLN94PlULhnUbJ2jh3x_zR_C-1hispNO_g8O2V32Dv7EcHZwHxFlGfrXQQBxivKLky8T9OxsAVNhH_L4JzTbkOi21X3M18sICKzzjxxa708Fi1eKLvd9FvqJtnXxUFTtTYhQa1NGkDk9y0xcNF9nYg1_D1QSid-ArhmLUF1nKGh3zICmrQVlKXFfjv68V-jpmBHfzeQZY0r6kT3yD8sUxNa8P3S9sblOLQaJI7i45tmgvHd7QMU73R9czvM2jdpvy0wy5YR2rZ9AVjQ6sdnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
باشگاه السد قطر حریف‌هفته‌اول استقلال اعلام کرد برای تمرکز رو لیگ ستارگان قطر و لیگ نخبگان آسیا از رقابت‌های جام حذفی قطر انصراف داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29584" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29583">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsSaVroKEIw1IRiaUpfA_SwEFbYhdygIfoocuT6K37AMa_LdBbJvMxjhDop_utRGvGtA3LBFbwInRzU5xDhc_yAchr_C9ikjDwSVgicYik32hbhTnKVqDka4e7zC9OhwOkCC7jLiFhV8v0KOqooiWoOhWYtpezlkMQdYt2f0sFzHueFJdHJB9WgUK5-PCDEWv2_LJ3lKfIY-pKQ4umZnbpA6CuSihJvc-CBO_NvYF2j6D9G5q2pe5yw8BR7mrhcX_NZ2vHJWVAKJihXgXeV4HKkegsnt_p2xKm8KmJ9EXnQmkabuvkPzxuJsyIgNTHEX8eK26EPjOkbIqA8YJ3g2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
‼️
از تحلیل و آنالیز تا پیشبینی رایگان
از مسابقه و چالش  تا همفکری و گفتگو در مورد رقابت های ورزشی
❤️
🪂
هیجان ولذت پیشبینی در کنار بت بازهای باتجربه و تیم حرفه ای پین بت
❤️
🤝
همین حالا در کانال پین بت عضو شو تا در مسیر موفقیت کنار یک تیم آنالیز حرفه ای به سود و موفقیت برسی
❤️
🤩
آنالیز دقیق رقابت های ورزشی
👟
چالش های نقدی
📝
گروه همفکری
🧤
ارائه فرم های  رایگان روزانه
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29583" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29582">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
فرانکو ماستانتونو ستاره آرژانتینی رئال مادرید که مورینیو به پرز گفته بود اعتقادی به سبک بازیش نداره و قرضی اون رو به‌فیورنتینا دادند امشب برای تیمش درسری‌آ هتریک کرده و نمره خارق العاده 9.8 از سایت فوتموب دریافت کرده است. ماستانتونو در پایان فصل به جمع کهکشانی‌ها…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29582" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29581">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ5ElgYlWErQ-FtbrSuG1Y2ktAzI2F3wLwTBM4wrAZ9SpkTIcKgyAapxCut6I1RDTfk0qzSA_JlQJnpiyxplO9Q-zQ_GtAEp89lmC9DDRYbqwR3RRU41QPFFsTMJO3oMTDhkCkNAUrPSVk059HKLSWOvWf6KzuckmGybYr0xDK9aALyCtmECw7uyjDDyWyNdPAqMUV0d8H6xXHbUQlQpMDE8djbvWYm5a8_rao9T3nDQt0VgJNfhuNL-DC1QWjs8KF6Jx_DVAcPTjOcbfkSZWgH-G8CukQQjOhpIixT8MA11eO02yhCbtvL_NOaInLCy2jgzLsz1GfC7U6L486sHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
47 سال‌پیش درچنین روزی؛
اریک آبیدال ستاره سابق بارسلونا به دنیااومد و با این تیم به دو قهرمانی ارزشمندچمپیونزلیگ رسید. آبیدال سال 2011 هم به بیماری صعب العلاج خود غلبه کرد و بزرگان بارسا در شب قهرمانی این‌تیم در UCL بازوبند رو به‌بازوی این بازیکن بستن و آبیدال جام قهرمانی رو بالای سر برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29581" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29579">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af01699be1.mp4?token=nQ0mDapzBzeXpD4EiN6CBC2-n11NJ8GO49F8XXMAXyXU8ONRDz8EmcNwi0_RUvKcWqho0jeyT2fORD9yO6b1MzqngTjcAjEhhCqn66gLUWlYCcIIGrrXEOSKttXE3SwA2-Gu-aH2s-s8mCs0mSxmgnTB9VqjUD3gadbwErp2wZ6nR_Z4BzI8DJKqjLQx3uKxCBU_kfS7iCqFicSUriN9vXlX-Dmu08e-edqB6EdEvv09MBVQ6zz-P21g8GOXjJbHuvOHVDHbJHK_XSNSDF6es1SvG9ewxlBVgO63PiBkQQxFzio2KY5cpquBKfy7AGQGh_F6IF3A3urXhHsS1zZvn3PdStG8Fxdkt_mkaN8-FVeCUSXHAkxyUvYLQ5s8nTBqS9Ew6_d10MP7Ve2sW2KJnWK91P0fNSjQ9elZSSwjvikFSYghSsbc-j5IpSjad2Xjz0lrA0FMFIZ4K-Jjpb97eIGr6ogjKiwhX4IAdJUM5e8eey7Y6IywuqI6pz7EMl0RHVfXpRs0cWtIKehBn8xJrVfxakuWxC5fboOJJA1G-aXmhQRe9LbaRO-FCx-i92qQpx1jbGI82VTzHU6Feanh7v81u8ldaR8wBur5WX65ybe_V9YrLjSilZxYXsDWHya0Mq2iO1bWKwo5tuZbg9SGqd5pKiFoPShyUGoOg3mCvtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af01699be1.mp4?token=nQ0mDapzBzeXpD4EiN6CBC2-n11NJ8GO49F8XXMAXyXU8ONRDz8EmcNwi0_RUvKcWqho0jeyT2fORD9yO6b1MzqngTjcAjEhhCqn66gLUWlYCcIIGrrXEOSKttXE3SwA2-Gu-aH2s-s8mCs0mSxmgnTB9VqjUD3gadbwErp2wZ6nR_Z4BzI8DJKqjLQx3uKxCBU_kfS7iCqFicSUriN9vXlX-Dmu08e-edqB6EdEvv09MBVQ6zz-P21g8GOXjJbHuvOHVDHbJHK_XSNSDF6es1SvG9ewxlBVgO63PiBkQQxFzio2KY5cpquBKfy7AGQGh_F6IF3A3urXhHsS1zZvn3PdStG8Fxdkt_mkaN8-FVeCUSXHAkxyUvYLQ5s8nTBqS9Ew6_d10MP7Ve2sW2KJnWK91P0fNSjQ9elZSSwjvikFSYghSsbc-j5IpSjad2Xjz0lrA0FMFIZ4K-Jjpb97eIGr6ogjKiwhX4IAdJUM5e8eey7Y6IywuqI6pz7EMl0RHVfXpRs0cWtIKehBn8xJrVfxakuWxC5fboOJJA1G-aXmhQRe9LbaRO-FCx-i92qQpx1jbGI82VTzHU6Feanh7v81u8ldaR8wBur5WX65ybe_V9YrLjSilZxYXsDWHya0Mq2iO1bWKwo5tuZbg9SGqd5pKiFoPShyUGoOg3mCvtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما روز به روز داره خفن تر میشه! شبکه دو یه کارشناس اورده داره از خاطره قدیم میگه میگه کارتون میذاشتن زیر کونشون فیلم رو میدیدن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29579" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29578">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRzSBBelcyInq5OiG7OxLv9nwaA8XNWaIPxjGEpFcCpOVChQcJNjP9vUU9-bfUHS0UhSo7xLr-45jpU0Wsj8GjkiyZ19-qMe25TJCbkxiT_doqpJ7JzkfBruRMljDMwkCDY0YAQhgcD63dpuH1NJYMWYyYAU9n_CYgySN2sPlr8VXeplkuGFicSooKldAM-T7H3xTEi48ZDJEp5KzI721e27VgKiGBPf77xFXfxtCblKGpNCTGNgRJjINjcdKbYx6HuqMEulwCgvIbpK4yBQ_JRWDa0rodRyb4l0NDz6emPT_nsD-MLwToSsxazW_xbQlJKMr78Txf48XdnoUlKcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29578" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29577">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJl-Yx-w2lPAd4Qgl05V_2JzeMgwBcQ8TE2rXT2v1-s5lecKuLWWi8G7ROOBNo4VoDqA8vow-1rhX6BMeqUlLuWJY4noqNO-lqJG904u0GEvSoHWL15k2N0o2wCs2KHaNOZB1rdvBTbTCfb3TUoQ6cBhSqaNUKeRJdzJhXgDIK2UtLhq2KfT8ozejbSZqdghUL_nfbrLlBJw7XNUp33Qnx680dGsh9JoCvQhoPVeE9kiI3FPWkqxrx5zmefADrAk6v6nkehw8oHiMgnG_UdKw7JPJHUOrPejNIzRvxhWVgJ5GYgfFA_sBU4nJtjIdm8oBQq6857LK2KoOM7iVUA1AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با این تیم غیر قانونی بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29577" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29576">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29576" target="_blank">📅 09:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29575">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=pgVjYov30yeZ-xAbcTEy-rsF2OE2KauoKuODJhlQgzkQidx6s2di-VfBnJiNfjn_lihsinlbpHLZcecjZ8dS9eYGsNjetx_5KyqtVu-9Ws11-44gDxonHGIXBhDY90LiGAVZ5dPYhlLjt8u1uKxnh5SxM03ZL81AIgDdP9Q_koKYVmSZ2fO1Oemvba75VTOJlcTmH0iOrWd87D0ZfjndL1f3KyFNvyPacMzeLXpn8xeaNMrM6-TcOI80uBNNzo8lsxCC-HfGPkzV0Fa9kI97xqRSAHdTaLqxBXrxk010sQa_DXmi_iNuW-zCAR9wygvqsJYtcsmeQxc8vbYxZLT2bWvO7Ns8e301VlMuhRLtW-1msp1znn-noZ88vosOjDKzf2TsU-iN_U9A0IxHee2GUq-ElFGAuX_YUsuk2f6QOkdt1kPnrHemmx_fIU_d-9KxFUbKSPhYpZ8uGzazavuIvE0c11ZDP5l-X9MMraEnf5peTqACzpmMsyHSWrBBQ2rLxJU4P1ViQDjW9DC30OoRinYLn0IzFNbE6hiw_afShKA1osGWikvYVccU1NpoUf1l46fA1B2B7_e4lEEuH2sNJv-6U5geby1SBK2NgtarMFjanfYDajm7jvdosAdQYthSlA3xWTI09uElW1qBu8vqdzpBbYjI1xitsKBz5B5lVEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=pgVjYov30yeZ-xAbcTEy-rsF2OE2KauoKuODJhlQgzkQidx6s2di-VfBnJiNfjn_lihsinlbpHLZcecjZ8dS9eYGsNjetx_5KyqtVu-9Ws11-44gDxonHGIXBhDY90LiGAVZ5dPYhlLjt8u1uKxnh5SxM03ZL81AIgDdP9Q_koKYVmSZ2fO1Oemvba75VTOJlcTmH0iOrWd87D0ZfjndL1f3KyFNvyPacMzeLXpn8xeaNMrM6-TcOI80uBNNzo8lsxCC-HfGPkzV0Fa9kI97xqRSAHdTaLqxBXrxk010sQa_DXmi_iNuW-zCAR9wygvqsJYtcsmeQxc8vbYxZLT2bWvO7Ns8e301VlMuhRLtW-1msp1znn-noZ88vosOjDKzf2TsU-iN_U9A0IxHee2GUq-ElFGAuX_YUsuk2f6QOkdt1kPnrHemmx_fIU_d-9KxFUbKSPhYpZ8uGzazavuIvE0c11ZDP5l-X9MMraEnf5peTqACzpmMsyHSWrBBQ2rLxJU4P1ViQDjW9DC30OoRinYLn0IzFNbE6hiw_afShKA1osGWikvYVccU1NpoUf1l46fA1B2B7_e4lEEuH2sNJv-6U5geby1SBK2NgtarMFjanfYDajm7jvdosAdQYthSlA3xWTI09uElW1qBu8vqdzpBbYjI1xitsKBz5B5lVEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌خاطره‌انگیز و دیدنی از عملکرد گرت بیل در تقابل با بارسا در فینال کوپا دل‌ری فصل 2014
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29575" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29574">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
گئورگی گولسیانی مدافع میانی سابق پرسپولیس و سپاهان درسن 35 سالگی از دنیای فوتبال خدافظی کرد. او بزودی در لیگ برتر مربیگری میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/29574" target="_blank">📅 01:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29573">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1VOiknQEA0iflHCQruMkJjU7kwtvusuYSZwmMDCrGs3t8DwQ9rgoAUFHzwZ7P-AIG-XrkNrYO5KglMWPQpNGxdJMaiQKd8fyehy19IlFvCruyP23I4wcd9Wy18NdtP4PSlKABhgN5lUUGPKQg_-avtJ72lKn4PCBiimZ-2wDFiQorldF7GOBGRcQDEemh8tYJa9u7SLYja0rt141VtPUBx1O0Y6Ar3twKGilItFo84b_dLnlLPGU9rAqxB44W3RSTkaUbpEcSZznjZwEUZ9-QD-8gbL6zVEVTz2sOfXDJ_Y1kzf1pqCKRlY0DtA_KQXzoK_f2xTEIONAZ607OmLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/29573" target="_blank">📅 01:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29571">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5wwWzT_-ZnIOzluCdAMHWHHjt2GveAnyP8Gmlhl9KtuqvvLggYk2VjDzwGWO0j0B199AcD7zqXINie1XR7Plj7e8lpAy8OAfrBwqFFrR86XvPu56Aq2WUURt01PpV-PFQ61TDdH-hEokKuXSdIMjthPEL_iLfv2t84gEpwVSaFxdwUHE6UKMXGYeyt8MAocc2THq9D8tnF1zE5hpQfsIIqgEaxDn2ozhIlIZYabl_z4NFoh8fnE2WVY_0bNOxklzeFgMDGoKb0HWw0mGHGgfEsgCcKgkZ2IacAa7rPVw92ynf8N1f3E4Z9FiBJJpdrNSoMWYP7Jx4lcnr6W4v-ZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین گلزنان ایرانی در تمامی مسابقات در سال 2026؛ سعید عزت‌اللهی با دوازده گل زده در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29571" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29570">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJlLXXDdgsYXq3WLDOBDqJmmRMjblQjcLF8tgIsm-W3bw7cshcNLI8xHc_aA323VLWN7j1dzAnE49GBmBTV-4cCJk53RxWiiOCXSkclv2TKxaVjp0c1ZijRZ5Xhg1Ks93-bBncRKwZ6v95afAIiwzbQ5dnzdmszGIZqHbwW3h3X7pdyIRAVncFCL0648vBQmgij0PABwyWDV8hZeSCCAMT0YVUqimmJentIUYExu639TPNOXKSoCkupE1sBUB8uIIhkgd3dj1vWn1sEUPrNgvZcOCgVhOTC1JwfLS9R25lgSgAPHW_EPptqGzCPYnk8PifeM1Q088gyIU80kyJDW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری زاده و نکونام سرمربیان استقلال و تراکتور به شدت علاقمند به جذب شهاب زاهدی در نیم فصل هستند و حتی صحبت‌هایی باخودِ این بازیکن داشته اند و به احتمال زیاد زاهدی در نیم فصل به لیگ برتر بازخواهد گشت و راهی یکی از…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/29570" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29568">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5UdUGFHq1NlZ5I8iiFZufH3CngdNoy4usS1pRs8Vj9WCb3xOqGUe5h-OgLyM_KAsu9e6Gci9qJMHXXCqyFgei3ygpWk6R8xDkDnmkn1cyvNAJSUaCBOAgC_Y3F7zJbMnaX3rU4FE6CW0-Avdw-EX2Jkp7aiei-0QawfEusGLxsQYJNztyKH0FiWnQqGxWMAL-EmGcj2f0pgfD2izXOhddA35sP28_fEhRgFCKcfm-yMg3hNoL2JYUbRhanAYCt7JFI0HjA53S23J7jYc9bPeByyIx4sh4lN9tK8wr1SGMAyqCSGINuEyxcWbmdFjHCQByAZo3V_pD9QuvS8SRbv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ فرانکو ماستانتونو وینگر آرژانتینی ۱۸ ساله رئال مادرید، با قراردادی قرضی بدون بند خرید دائمی به تیم فوتبال فیورنتینا ایتالیا پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/persiana_Soccer/29568" target="_blank">📅 00:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29567">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFauMRYdqDDLKZ5ahs6zfxg11sni3OjyNRd5nrGOPHhl9YiVsFOTQXMafANUTLEYf-X2kkYbNDISKskGkXZLixMScsytN3FX6zjPquQfsKvYLND_rs0Ggap0MeNchbqGz_EBynaGrCTjzxmK2qRLMT6kjbSgZPcfgG8cyacNfKP1bSgOBJE7WMqZ3iN_Xm25U1dI8bX60sho1R4AtxGvhwojCbMdF_3qZb3hh6mnTYyTXOgP67-caI2D5ZP2kngmlRb2Ti2PKbyAEPOsw1vqq9k6TBGbEQu559KpJf32ccp-e1yEiiW-8kSR1hAFkw6YtkykL3iYwiJH3W7XtGP4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/persiana_Soccer/29567" target="_blank">📅 00:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29566">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=vIf-4jUKP5L77flBDCN1g-cfDWnbmJQKMvu2JpgDYnX5BCUOHhvA1zHxtgEftbm-_ilSMzyiKGlrguG_U1x6BvdN_H9BDOWaR8gsXZukFw_3p0gjyL40L7jpvB3eJBHgABWrh0cFtJYgycJjsy2T4NjcPq44PciRZN1Oe7CMVJs5sX_3whqzqLpyjo-8aEIuzluPASu7ED86I4L2IZI0kUC6RedNHjs2jWb-93wrTxeuhdRupOVPefB4MZ4T64UmOt-1fpvZh-wB9UcJXkSRCasnwV74pnM1p9-3NOB3zguBAWFC6N48IAfNsflCO_LICU4N4JqcRHJJutXpIetsSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=vIf-4jUKP5L77flBDCN1g-cfDWnbmJQKMvu2JpgDYnX5BCUOHhvA1zHxtgEftbm-_ilSMzyiKGlrguG_U1x6BvdN_H9BDOWaR8gsXZukFw_3p0gjyL40L7jpvB3eJBHgABWrh0cFtJYgycJjsy2T4NjcPq44PciRZN1Oe7CMVJs5sX_3whqzqLpyjo-8aEIuzluPASu7ED86I4L2IZI0kUC6RedNHjs2jWb-93wrTxeuhdRupOVPefB4MZ4T64UmOt-1fpvZh-wB9UcJXkSRCasnwV74pnM1p9-3NOB3zguBAWFC6N48IAfNsflCO_LICU4N4JqcRHJJutXpIetsSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌مهران‌مدیری‌به‌گرفتن وام‌های‌کلان در قسمت دوم جدید سریال جدیدش بنام «مرد سه‌هزارچهره»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/persiana_Soccer/29566" target="_blank">📅 00:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29565">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiNT8Cr1K9GVlWsfOhOLrs2vXSGcgb8FNjYPZEjbQD8AQveFuQiFNMDyxDLNP653p0780iB7hFuxOLAjZtmL1SNdxmppEnX1UhDyW5dWFRDNVpUGmymjfBgezyiN93N8Z7xQsn1e3ozscYMILeNHcCOQdPjJ-XfJ5B8kQ0Obpwzh_dt5sRGsQOizplG7CwpCWWIo4MFvPLMs-3rIKDHsMPeSnigiO7xePFVLnmT2Z4KgCM8qWYSsytdyu--tRvSDJXtNHZ4y1K12VRkXv5mKkABOCYpJDvnBIsI853zCYqupURVbmNmofeWvpEUvdaASmQHeXjjL4ZB9TuKnecU8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/29565" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29564">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTKAGfJGw9WV4JOeiXnsfiweyeTvWgeO8AZ0FMURiABDrqigw_utstaEPqN2UjefvqZXS_Pf1rwGGyugQZR70VPjXE7YpiI7nLTsA-c1RUKUolitO4vyss9eDaAyLf6zxPM-9l4j1SraMhXWCgIMiVPruN0iMXek6iy6NetoXlsYycO0mkOqQebJcsXBoGvSjuWt3VZPSzyymZ94GmcmqAVoQdbEpWC4dODQbEo5htrz2oQSGq8fYyj0vx3eY4ZqIQvGw6VL_ZmNTFswMApDi6LOAhdPvm7gX-GIpIE17WDBXgaVJXfzCYYTwUWBKalsl0nP0RfG5Pn8kniVADGcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شکست شاگردان مورایس برابرالوحده‌وبرد اتحادکلبا با پاس‌گل سامان قدوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/29564" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29563">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_QWutbpepxJyLbnOUchn24IbFeQlAIZlcjOYTS2eXTziS1b0km0CM68xOcr4eBzqPUUP3-Om7od_O07JmkQUQe_QZlEtNtmEZZVgyh1Ocj_vNDe-iVd38zTR8Xu2ZXH-i3VL7TvH0gS_72ZrxAeQDvUqrHjFSYmIJ9SKbCEj1EJ4g7ygFqn5RwIFUtp4EdEFutpJe0XnmMtgQ0nsbWw5ebeZjOrLaM5hixqGmtZmxe330w30DuHAekKrRVJUPFttriD0qqlyCRckbOZdnWidUZ88MB8n_TsrNS7rP01mLoQW8-_q5uI-cMNRJJ82FYZDP3zYE3ABTLqG8NVChIQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29563" target="_blank">📅 23:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29562">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr01sIpz4-WpdGr14Xklz25R-h8Ztv29kHBotvDEIduywbtPYHPqS7K-oWwOkDlGLr3YvPzmxqWRYVAAlXPHpIhsgkP52MYNlwhbYF4Dsmz-gcsdebnA_LBRukNY_VU3iDr0D_kM2A66aEEvgxYL0G55Kzp2bT6LCi4o3d1pSeak4g51g182Prk3mjGtnQ_ys8MFi4A2Y3Hg8xBLkA2iC0BRQRNLcENCvMAU19i3h4E_dXSVxDdQ8Gx38uVKKU2Pqzfhx8FEw-4ckO11Wtwx-3in2nenirmja9XaaoaL7bIsts5Pujt5Z2Kzv7xgVazgcTFvKtFYVjlzc2ruX5y1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رقم دقیق قراردادی که نظری جویباری و محمود رضا بابایی با فابیو کاریله امضا کردند 1.2 میلیون دلار بود که بعدش یکطرفه فسخ کردند. حالا 40 روز فرصت دارند که با این سرمربی برزیلی برای پرداخت یه مبلغی توافق‌کنند درغیراینصورت کاریله به‌فیفا شکایت میکنه...…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29562" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29561">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhFsVU6m5PbK6fAR-1TpYtLDA0O6faZKyxya6M36rPJjxlO_p1D0ZzCNQCMRoWMZyMOEm9njrAPITdhDPXvDSSBN-EEY-w7egHw44c2uBpFcBOvgfZO03xEoP6aDGq_uvEDBXauQ2Pl1MZaPqxmMEfDmt5gOj72TDTO00TumivWU9XtLilqEnYrzPo7K1qNCk0u7KYJYQNbzDrarfIRFixVnAN6-lLAWAjB0qN_6X3qxl7s-eowVhRFpukN89En87xu3MZX2aBEr5UhB6pZFo-w6srfLlS9lOFEhra8lUEYXbvIwuDtwXPetXD5vKfCIxqcr2NWSiGp3tyOl6F5Bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29561" target="_blank">📅 23:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29560">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNslKD5psAmSz1BV-5X-zx3x3G8QtIg3wQ1BEZWYL-QguMFAVjLw0j4JTYmG8Mpd_5j4AZym70cbFhucpgFvUuzLYGzDy-dFVBe-0MbKC87LrmYkcy2pybehVXwIjCoPrBZ71_DBu7HBDWODLVhhu06vswJ5XPuwE--NzCLmykU-x5auMT3slqruLOnkiSINW4tnAQDPKgqsZrvCz_F5fMxP7cnYsm1WE1N6GJhdRBCD8I-CFYjGD9FcESrJtTCwflmu0BdHdPxsLkmkVa3GGohm1cNaLVnGm2FGPVjE1GZksYCow6XnJPglgxSN0kZM_oeJN6F4GJ91mAWEWm5oIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29560" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29559">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZtLxwkyA8L1Q7eWpzaFRCV1fqsOyakyZZg6F3eqHBgiGFn7P2FRJstjevhuHJ55m8UzjIkJ2SVq_sgWk4yeDbGUou5B0nOqWmlqC_a7DE3E3o698coEz7lS5-iHJMBpXjj92aaj9VhJ_nQTj9o2se5xjQgxUhycS8JW4PUJL9JyTHoVMCtnAT-U7FEFnAB442P0Ila1NO28KnL4AMAWyNejYpNFPZogGNei3LSOh2aqP_Cu7HInhl_jmLkg-n3At3Ac3St1rX0c6RZRrYaEKtZSQ5TJbJInZx_zoYJL3sbKfSQvhIg88lZEoJ4ako3NuW90ruyyR2Ze20J6nGLWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/29559" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29558">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=G3L1BN1kSd17g0Vas2aQjrQQ7TS8w6GfJKUOnpH-uQcARPri8YtIXO1OSJvuR1cM6bvytidH4qibrjtEao8BJ8cyW2egqTu2T5_2ZWqq01lYgNC50l04wZ5Q_tgdmu6eqiGgtSMXdjsm0RzBXb0HqvFO8vQ3MFE4PUdKcAFN_TVmOh76Kby_T3faZOWcKp3kWGd1FC3eRdXSBMAHmxH8lxwIYe51EZXhazVuLMaEx8_WiidE25gJvET0A4c1DYCC26kcCsfUn4LE7jfOM8pKs_xbKXNezLdvGw89iWKQ00gx0wrpvk3kRXpmUQ91M0tGN3TLzY1NESZK14HnLag6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=G3L1BN1kSd17g0Vas2aQjrQQ7TS8w6GfJKUOnpH-uQcARPri8YtIXO1OSJvuR1cM6bvytidH4qibrjtEao8BJ8cyW2egqTu2T5_2ZWqq01lYgNC50l04wZ5Q_tgdmu6eqiGgtSMXdjsm0RzBXb0HqvFO8vQ3MFE4PUdKcAFN_TVmOh76Kby_T3faZOWcKp3kWGd1FC3eRdXSBMAHmxH8lxwIYe51EZXhazVuLMaEx8_WiidE25gJvET0A4c1DYCC26kcCsfUn4LE7jfOM8pKs_xbKXNezLdvGw89iWKQ00gx0wrpvk3kRXpmUQ91M0tGN3TLzY1NESZK14HnLag6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های‌انگیزشی‌رونالدو دررختکن النصر دربازی این هفته این تیم؛ نمایش یک کاپیتان واقعی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29558" target="_blank">📅 22:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMBP5IS5B-53duFQFYTCZfVhwvU1l4-nbaQd8VhrkwxxxBCR-zFcgzAnmVTceF-I2iOpv641LCHR17c4OmIT_1ZkVn-xMQtnfbvhm9ydrXtHRoW90JC-AdTrodrMBcCj-Qtxa3fTESnUZa9O7XDx7kWKde-y4qdRmCWi6gWIjquRCOl8oUXjswUfbfoWiQ-B-BLOosw8slwG-Fh2m-du6hsguv-6b2VvNk7BfzPNyLyZdz-g9Ykiepg6WuZQR5A2zUbgCDVdwK79kv6vnWHnDWETIGVmVAydQKq1QYexB2YJcB7_YVQQtf_D7U3po3mQj2uqB5TqfDN3cGyhAaHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvGWp-r7KLUblG2CI2U9dDF6c_zH34-7JPmBojFLUKM_mTfSS4V3ZCisH3Aqb-NYBLopi0X01i3Q288QqAECr1vXWsT76UGaGKkiLSN1ZltigHaDB7IA4OLqXHvUO9lYYFdrpxyuWZAQcxOLqIx8-fPMjweMpS3EqC5DBSFTb6qeXf_0H4Wtvz2Z-8Te2r9duacSdsAW58H-h6yf0bnMCiAD9IwtX0jsZKlhJqf7r35IAPjuIJVHx2aBXT7yXODlSFHd8uBttZkyrtQe_qsD0AQSUuYSGtFIoLbQXIF7lHrM9KjpP_QxgPnqSF3k9C0y6HKpsfWaIg3lRcj8TNAezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29555">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpW9omjGKI-mFKZZM4EBkf8SbiFIseP6h1Bg5pcpu_CHQ352FaSy4CaxMuE0SYTzkwqo8AkObmteTIUcF5_RfMrl9-Yqe_ss8iNPIEQtU4qokVotLwrYc7iNH7PqkxwPMnU4JyNi7ZgQg0J-McOO-C0AvY1w4mQbus8uc7MikIUxVVa8l-Lc6bpZ_5orGBGnlIJTup1y4_Tsxn04VJZEF7HiEAUmC80u_91zm30XgLb7NZGihFT1jdkeJGrzEQk9Ca391FEtLfBx-weeqnQgzmeIHVJ_C6IVHs-0ua8beLq4VkilyLpfgmD45hwVnSvOLUft4A8vRAI_McrV-D3azw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/29555" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29554">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت‌مجدد مورینیو از وینی با یک ضرب المثل جالب: "تو فقط به درخت‌هایی سنگ پرت می‌کنی که میوه دارن. به درختی که هیچی بهت نمیده که سنگ نمیزنی. به درختی سنگ میزنی که پر از میوه‌ست."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29554" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29553">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=gvfcZcQ5WBjO-E3c6pxaocQo8Zmy2otPrvK-AhB1VBXFx6S9FzJKjv9gx_6rM15pP4jYUZKWCmfOQOukt8shBYgBZDMu7w1m1HUayOL8di1hjGguTJJn8n9eBUR3yD3plXTFnL9W9LpAjBFbV6DhPBs0QzptAU8tAlqAxs2r6Nps0RZO1qNGojUXi8aizK8UnWUVr4dBQmdGq5jnaNTYxKmwa4uUm9fq7SdgRmyM281b1I4DjaHfEHTYbM6QeZ3r4fIlAf510u9xYBnJ6dFoo9TZ5UPSpmiRhE4AyQDZ-xpv0v-R2Wqt9pB_OkSMcB5evwW73ZovHYA4NtKj4ew65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=gvfcZcQ5WBjO-E3c6pxaocQo8Zmy2otPrvK-AhB1VBXFx6S9FzJKjv9gx_6rM15pP4jYUZKWCmfOQOukt8shBYgBZDMu7w1m1HUayOL8di1hjGguTJJn8n9eBUR3yD3plXTFnL9W9LpAjBFbV6DhPBs0QzptAU8tAlqAxs2r6Nps0RZO1qNGojUXi8aizK8UnWUVr4dBQmdGq5jnaNTYxKmwa4uUm9fq7SdgRmyM281b1I4DjaHfEHTYbM6QeZ3r4fIlAf510u9xYBnJ6dFoo9TZ5UPSpmiRhE4AyQDZ-xpv0v-R2Wqt9pB_OkSMcB5evwW73ZovHYA4NtKj4ew65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29553" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIjpxRAYBu25WW--g7ffKgazCgDzrwG7qe-859D_OCHTqKET3AG4nsIH5C5cojzEc83ux4_ZstuYGsRPVyUumnRoRNB_qukWqULoyATxdpcvneX2mi9t8khc-yS5b4IS8L_11LIOBlirtx_Ew083vW3tjCfWxbHKQGegmGoamEoh7jQ_kShO-C3Pb51J0khvhklVUXB4LJngFTMrVRXPsI81B3nPqFdDHrYEUzdH6J0ssiLcWpOU_2m7BCOP55E4xVM98bB0_olnEzB_5l7blaVAoh0QRmNeitIj1dXdjIoDLS_--zE_sSP-8ceIbnhdRa_GIQL5x_XzECHKapYJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روشنک‌مسئول‌مسابقات‌لیگ‌برتر:
بعد از فیفادی و بازگشت تیم امید به ایران بین هفته هشتم و نهم بازی‌های معوقه هفته هفتم را برگزار خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29551" target="_blank">📅 20:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
کارشناسی داوری دیدار استقلال و پیکان و دیدار تراکتور و استقلال خوزستان با مارک کلاتنبرگ: بنظرم باید برای پیکان پنالتی اعلام میشد. هر دو گل تراکتور به درستی افساید گرفته شد و گل‌آبی‌ها هم سالم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29550" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d20sSdHKiGnTYJHEeHiWDsqalH0hPeCld6SRV2Agzf1m28od4d_nOIPosJ9mTOz1KDI6_fINPL-4ivdWZajS4upovEWbCRJEMAJED60WN0fcZqbgd767le53f-_TeNzwfxKus4vqJrYfEARg0AnYC4JMdh7jM9_Htt-YzYWy7Z57e2BbbCpnpkbLwVbZgDJ9v7LN8vSNesO1MbJ7SDAmq9WX7vp2VjPr8aTafWLuXT-B_NKq9_98Hz7xOWPjHU7Ub0aJdZe1mjbAM_lxjfXO7bybEYYl9J3FEDlsOm0ob2522K4SQbqta1ZXLbezjRnITAqblIcLNB2LCT003z43xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نشریه‌فوربس‌گفته کریس رونالدو هر پستی که تو اینستاگرام میزاره3.3میلیون‌یورو که با پول خودمون میشه حدود  910 میلیارد تومان پول میگیره. در بین تمام کابران و سلبریتی‌ها اون بیشترین درآمد رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29549" target="_blank">📅 20:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhdwytJ-owYOwvaPxdQKQnXdaCtlwBcZcuD__YE9qlpfjhrCrfTWqrKpQMVdxdGJ9lnyn4VYhV-JretlORU2hG0r0_J1zW0hX6FIfLQSn8ITx1lqauGt2WnfRqRjHUnhAw9F3donsC79HkM9Q1tNVnaYtGAS6RBg0Wegqwen7H2THF-oGc4aJrbxdY85qL1pSn3iV0FaDBqMyV1N-K5sK7GPwfk6enLDKXVhFgMtyMWYI4SlQW755ecxlpJmDxSLAbz7NUGvQSDMj1XCeBw0bKGeVHhFWUc5zSV9o0y97J3bS4rWwjTAel3ONDBaQYbADWOyFt0AnKn8E-gbD1rISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
#فوری؛ فابیو کاریله سرمربی برزیلی به فیفا نامه زده و اعلام کرده من پیش نویس قراردادی باشگاه استقلال رو امضا کرده‌ام و درخواست غرامت میلیون دلاری کرده! گویا پرونده استراماچونی دو به وسیله جویباری و محمود بابایی راه افتاده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29548" target="_blank">📅 20:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOSoIrRwHMzPyyc19xaTkCW0YJiMTFrF_H3kq4XVuJ7giuGJbuZYAtW8F3YqTAjbgpq-UC0xJWLTrm8lKiKpjX3wTuXdOtFmmQJq_hGWq_sakeUiyWAgrgmX2-oIdfzzMvBFe1O0A63z-pE1YP8fU1erbnLPgvw_Rf9G7_rrG0m6Mesg5gfWZx2g0wiyeBmiYg-zjO1m8sBGqAf375o9VVxjtnSGgWsBij1IdOSR1Rpa3ZACnpxvuMbW1sSyEvNCHcdIAT5Y8LGGjOY6kTp6XM1Kw-n4Fp_6H-49_n1nX8wm_aJGFEcZM-w25Fxq772-boL1DxSmEuJbBoozFxkdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق‌ستاره 29 ساله بارسلونا با به ثمر رساندن شش گل و یک پاس گل در چهار مسابقه بعنوان بهترین‌ بازیکن‌ماه رقابتای لالیگا اننخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29547" target="_blank">📅 19:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhcQ7Fzm4YMHUWPGuJKSKhBxdCd90dP5H00uSzZcgFyKZJT46AGD7Hpm6MlXWW1G8VbhxqHldCPuhjv3APZzn9E16jtYhifQiZZv9Wc8FBrCgUNWZw898lmqo9GxBho8M7aSFRTdBPWNayVgPUmqujZ8W7wKYb3ctG3EfaSiQSyfq5QjMP34R-7T8NmgR-kyGKhF3wGleEuRvQjU3Mq4sMJg9KgSV1CW0rHSyFQck9O027DZaXaVhQ5mkwVCWOZXUEVPn2FqCUjyjyaJtzZfy8COkq1bHkRw-Fr3JbLr8JKuRTlY_Ydxb1TKAn5RyNkHf521E8VCzwltqlq3zl0ZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
‼️
علی نظری جویباری مدیرعامل باشگاه استقلال: هیچ خطری باشگاه استقلال رو در پرونده کاریله تهدید نمیکنه، قراردادی که برای فابیو کاریله فرستادیم امضا نداشت و فقط سربرگ باشگاه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29546" target="_blank">📅 19:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THT5g7dw2WKDAklSoClkwRW0DivmwGQ7kyJjOyXEB4ue2olbZQhG2pzRhrIg2MlfAoc0-LkX1SS1lZVKWVlQMGTS4p0Z7QcZdN-ivDaAHwipgjT9FCk9x-3rvyWNoW7htXGcD0FLRaQTIo6AMzN-xkc0-1DPjicadfWPP2KJvjob4kw1J_uJVQ_FsX5KdeiyBzXUjF2PcQYnMuckMwEtWC0qtfHGFE-k1Etw41X3MNPhwcbI1MZbyh3tgQjd_6469k9vk8NvXm3eRpeuwMpf_Yk4Z-5L-BFws844_ASpdMZ-Fk2vnZzcJSsP58Ju4WW4J3ozrq94867Zeg1-O5WLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
گئورگی گولسیانی مدافع گرجستانی سپاهان بزودی قرار دادش رو با طلایی‌پوشان فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29545" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpHxahwyAKlhOqgS6yOdap0a_5anNrVPYf3zk_bOcTdhTk3-BXf7nODiqyE18SByE96z9BFvYx2o5SBrusKw2Q2eA4aZka1XscTQh8SetMB57_Y_iVDpeo7pc2CGVhJ8l9T3PdGQUQ-0LuMIdNXeui1ZVTFpIrpZ0hEM8G2omr_Fq1CZkT7n63lO00KEQvW7EsKUk8qDg6aei7nJuoaDQhYUOtUVIlV-ZDaEVL_pyyK3fJa7TZRwD1YTxLWTzxRLjx5GhFniXCjkBaAVXyCyZmRrJCJKVGZmuvAu2goORXz2P6fVf0eO-ME912qaMDLHPXmNdwSNEywxpgR2A3EZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN:سسک‌فابرگاس و میکل آرتتا دو گزینه‌نهایی‌فلورنتینو پرز برای‌فصل آینده رئال مادرید درصورت عدم قهرمانی در این فصل با مورینیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29544" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-dowyf3iaBZK6wjSSG3uRwqI1Lz3Z0NgRWvYGwRunHJIw-5n4CCpGRCPl4rrRiZlSh58GMdtc6hs9eRjzWv9UiZ_WZk-4H2aSlGloqvPHirXnE8bNdJpm7CAnqW3yOT6G7rAWnte3-weWBx89HpJEUDjkDrgP1BmvM-42_D08P873LY5-3j014pP10JvHNzxjw-pszrhKYPYiL6b3b8XskSi4nxrqvWD0XVP82CyF3IEK34J90XE4D5uQQ5-fkqaRIt0IRRWU6c6oj9N8gUR3RcReQ1mRi-EYfFSfgQf7cnBuNF_Ms65dTYtr9HmCBDz-LHHOk8JE3SZm6rAngGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfyLU7LfPG7uLQSp8uZYZLerLiMhU95MIr9Jfg62PuO1XtZBml9mU6O_a1R58j1BnPCI5ZRbz4-jMXayx_hVNV2x4cftrofrLoIQ_t8hGQgp1JBDa8PVX9aio8mpcBgXD20CeleH5VTJLZ4Q42y6-T632BRNXhy_8EKYe6_LW4OhbZZvamBGF6rQc_gD8NbJVwdDshc3DJgly3sdSp0ZGo2h-JRTzT7uqq5UM_L5g1FkB9gaOAQII0TH4-tmRtF-o2nFyuF_bcAur1gaKXc4Mb7_HgNnMYzU2fm9o8AhWnNdUyjqOvwkintJYNTe5SVIMb9XP5nloWD85nnbNsHa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzUXCXgDCANo6Oyr-KWEV4vZXERoY19NhuMGSOYNW5jrxzMtagvchsb1-ELk4-AfGRKBvxWfO1pkeZ-o_f8TRvtN8KLMK_xUqZKeY7pOFgWCVbDVHQLKZgO1mUnoQF8IsYJihWzRAots7h-BON8XJ5avjNstSuguacpwVJf5cQ0Ev5d7rYhKm5xc_iWXth-0PObq6aga83mQtz-2lIAwLT81Djw2NfuumEymTdwEInDfbuIos86Rbi_UTu7SGBtnH9CTydVvMd5dS50Dev1p6pvg2rRd_a2ZVQj7NfSRpiNb6Efwkqav3gxboNm71rMuDvekaBwtT4hWga9NsXdG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=eYB6D1D6gojftjukK5H3v-7BB5QIfvENOZjvPS7jvvRtSJfLqqOyA-q8ioV1VHfWBoWnb64TsMLKRrunufP17rgKR-3-Cy-ERZ6fyvodpy7jfsUQPOgcdB8BI1923rPlST7-sCmZ2h216NP3lWTFURKlgZU9c1dnR4rSBIt8nj9r9gPksRXQFi4oQ0nc1eblJ_Sa9w87R3Si0aXMS_7veng390WnQM-_hdQPdHciBAIm-HK73ruOJxARtdvmpZ-DzqQnCcmEVXSUIGt1RkXaI_cWa_cAUlsV3fHQONS5sIscJo6qNK_2V1XCGFWWWazHcySk7Ygl0lqi12jWG7qf1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=eYB6D1D6gojftjukK5H3v-7BB5QIfvENOZjvPS7jvvRtSJfLqqOyA-q8ioV1VHfWBoWnb64TsMLKRrunufP17rgKR-3-Cy-ERZ6fyvodpy7jfsUQPOgcdB8BI1923rPlST7-sCmZ2h216NP3lWTFURKlgZU9c1dnR4rSBIt8nj9r9gPksRXQFi4oQ0nc1eblJ_Sa9w87R3Si0aXMS_7veng390WnQM-_hdQPdHciBAIm-HK73ruOJxARtdvmpZ-DzqQnCcmEVXSUIGt1RkXaI_cWa_cAUlsV3fHQONS5sIscJo6qNK_2V1XCGFWWWazHcySk7Ygl0lqi12jWG7qf1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAkOiDGWwF3wIWuTCgvtJhPjlT1MjMrpCrFbj3qPR9jvoL9UOfpEPb19Rc4Lt0WLHrQtaX0JWe9VA55dX2_6eKLizezSiK_VsXvOwTC3iYFxjF1dNUAF6bjK9a1ymp30zpGDscL7UZXn9sXneO9DdRHkhm4mJuszQieAvAxsqK27g8gd2zcMXvG-xZaV7u4ectv69A1cBV5Br95HtFurfEiKQjjU58PMCCBlh61n2WdpujIihvYn5Gm22g-cffyrDfv6oVrq7Oix04_PPmt2r72oo3J9--DXf_j2oOJVv5H86UeRIwqVSlBl9myLYmdhwgPawqP-ChYP6widJYxJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=BfFH8LXPckOt1Dx3TUk9d8mbqTb4Oc7Tonzy3j7aaI9ATIoteV85rdvhRDVb00legVcHbqxgW1M_DBGZ4RcJz3k0DJ5cGZpdb2de17Pz-fpDJE4iT8pxdA7ZiyYKDlyqCXTQo-JPzBHhTSJ2acz7MyWL3M8-D3BtwMuloBTllPlq9_oeUTu6CAJYu4K906_3cfrPp3rQX3fic6WCueariJ5YZwWhO0RG1vSSv5glF4zui7zPFt3EZBlNnL8Gv7zWQ17vU6RYIo637VHyncghreZGggAj51JcpNBAn1gnYNU5v0kOCaT2qQA6RIs-KetF3Ocx94INRB9-d7ROeD9nxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=BfFH8LXPckOt1Dx3TUk9d8mbqTb4Oc7Tonzy3j7aaI9ATIoteV85rdvhRDVb00legVcHbqxgW1M_DBGZ4RcJz3k0DJ5cGZpdb2de17Pz-fpDJE4iT8pxdA7ZiyYKDlyqCXTQo-JPzBHhTSJ2acz7MyWL3M8-D3BtwMuloBTllPlq9_oeUTu6CAJYu4K906_3cfrPp3rQX3fic6WCueariJ5YZwWhO0RG1vSSv5glF4zui7zPFt3EZBlNnL8Gv7zWQ17vU6RYIo637VHyncghreZGggAj51JcpNBAn1gnYNU5v0kOCaT2qQA6RIs-KetF3Ocx94INRB9-d7ROeD9nxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29536">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDX6A9kT1ZTYsNlFH4sLWUYDI04tUnrHq6-2Fy7uOyb3n-S2q4y7csSWqt8s735Sa1N00iJzmLPQyYWXwydDwbESvMIT6puTzRZPsSx9giwuBWByOMbFJeRozByO6vVnUAyA3w-0rvfIhUopU8UQx61KsdI2lY1dH0pfG3VITI80X0VyvSt8Yc-Dr5nFGMXF2iC-CEBE2-sGM31e84Uiin8jyBjd_8ofBECxmMxSXwPZsrjgS9-8mfh5Qy-FKfdukeyLadQvEHP4lS2AxpkaYqd3arL4fq-mvUxt8f9IsXYBjGzu3vhEF-th7FgGk0QzLCe-4goZDug6U9ILb1zlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29536" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29535">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_LmlrKaboNDnEvld0ZYOU39YYzUsxuzCWMXSCcKYeCqV9V5MRgGdTs4tou8RveKFMRuY72QXaj96lLX9ZHC7vUt7x03E9qT-V9qyXPZQHhNAxoAk7UCbALoWme7ycq3Bh3qvM-Ytn5W3AhHWpATwEBVx3KNW-2o0AOpLMCJ2F4FCPeTmiC-QBSk2uIhHAKKyBiXPNT8REMd4dgSJ5fSpG6RE1ycV3B0at53j-C8HtIGEan-n4ZzhYIZ_kuIpLRei2tDlII5k8CuOFH8j4aRR-1jYnYkFY_ickUCbzFJHQBdln8K2JiQDix18XfR-5pJmiWD0mwOpxSznysC7C4BkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کار انسان دوستانه یاسر آسانی با خرید یک خونه برای یکی از هواداران استقلال از زبان وریا غفوری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29535" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29534">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIYqD1mZ1yONl8_Rn36l5Ip2G0dMtCawiGV68VF-RLpxuqrxTl-gSxKey3j_FRnDJbK10ntU7F2d1GpiOBZxLNf36SrElREhWeOMgg1zWmN6HSv_nVFElnfXOXvxpZj1ZhZvXhIybxKz5azStPrsHgtOr-fc6DEWCaXcZ3OtdYxgfxyamVH-lh3HvAubnSLM5KZfRKUbfhxlWQmMlb1f69jAUpjwXMvIW5XuRww9eMsvQ7QzSlUSyzjEkEAr2Pvhm5oOPbPo0o7-t10nhMFHYBeCSHOqJrHUcsyaV4h7Lnt6DG66yd_RDFbJDVQ3JesduK5GoHy4n7ptu-0FXByweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به گفته کارشناسان؛ علت اینکه فوتبال محبوب ترین ورزش‌جهانه‌اینه که شبیه‌ترین ورزش به زندگیه و دیشب یکی‌ دیگه از این اتفاقات افتاد. دیکتاتورها وقتی سقوط‌میکنن که خیال میکنن دراوج قدرتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29534" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRDmY5EAu0KF__O3RK-s2JUnN1-UyS1PfA-llehIRdxsC6DcFiR28xUNI0nyuxq70JajOtMXwZXrjlnSdLvRIZAP8Ek_RjadhAUQtHJ1h2pDLzQwN5TA69vMbLeyTJ1xKL9QyqMRJj38IzixM_MAhFf_jHUwjl-4ap1dQLxsVS7_fziF7d0juJXlN_6LRAejqZL_dJryk1jAKEy7uN1w-r-X45QhC6so2F0_U0bZlgwOGXuR2YVVwWFUMiSLpqlCu-Xc0yu2-8eLLsd9TfCRK3stTRmuqquHT83o-lu5jtIQYjcS8ESFEhgFcv7q2XN6EX3LA2oxW3mkdiDICjYU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#تکمیلی؛ سران باشگاه بارسلونا به این نتیجه رسیده‌اند که میکل‌آرتتا سرمربی‌آرسنال مناسبت ترین گزینه جانشینی هانسی فلیک در سال‌های آینده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29533" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5Ny3I1k8Cxkm2K0uiFJdNLnE-dUlPJtRnjpvfPK2nh6doyB0pak4kTRs_vOsmdqfvl09WXZfKJNninodYwNQ4BMXmk79LNwnExQt9TYRSf8zwxFmSQbh5u7hnURLhF5d8ULQ6GTrwaGhnjqaTvr4BlJSDtJXlk0Sad4p6xphRcPdb-NhmZx9TWRMojnte0-E1Qz8COZ6VVBxpYw4e_59TIXVyKttrKZquPK_3gC7hxvzkqFyOsX7hKVZrp292crV0Q6AvMP02ZAtRrDAONdAYcM-A4K8Ck_EtzY1OeRj_sdxinFn2rpghfVxyxmFAm7By2ZkqDkqEgS46_sGlxOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29532" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29530">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2YCUQFTwR5IbIE3Tte881Ki5WWLjVmGEK_MuN-S3-G_kcQXKiyzk1nwyAXbwRCL3-NRWo1n8Ge8XThg9-BNfWEUksc2uZQb-xjbbu_5MU5GTuCDxN_nzHWCTmCsobB1VJkm89gRhl5ThppAeKmg-yUxwj8o25J2Q5ZDbD6lhci1bLY4AKAiS5PcxJHJVSelRxm2-Lzv_wnX7DJt2Ty10GBOkqKDZjuIhJxX5ZxSjfcOFVc5rPXUK-DDnqr4B6di1aW5NPkHDghmWpPy2NGrJIpLT2tBAIQ0HqxhdzTihhj4NWzbYBOA_S7BQ4iEc5RTmA1xLQlekf_NQyURGOK9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29530" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29529">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSE3MJySP9x2v0DLzJkjqcwt7Ah6qku6kzWgqhe-Id6ClyAhT84t517iRXYcyua5ObNxCuzElzUPr2NQe4kJPG-vZaCGQ9dG-BlSw7olLxIB2C1MkEaPpDRWL2fAf7cw4CZRNWN4-Me3Dfbw6OlMfNbHJ4FicHeGWeGpuBxrWPEH6LMjv2-ODIE6KvqeMHuRohE1lAPTmG02WHHMdPhPsmRHK-lv3V_dHBlei51x8D1-cRkK3Ajj2arIvE960xFGIAOZNb0pMvl_Nq80Y_bo9EVuAfY_Rrm618FJaaHBmX02zTEjBr9tVZnNJwi9SVoSR3Rsrwt7taU4-xSq_KAePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29529" target="_blank">📅 15:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29528">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyQr6JOvbyX-QkDEc4M2nt12KGoLPZspWvzkBzq4Pld5S6u2c0ocsxIED-B39Zx_OPiKhDlg3Ti3OPaSoyyu5PpzhdEUL-ofl2xxk2XjJpvKHY43ixiy_EYqrMANVKGHO6fZz6G-0ouXBB5as61AwOuDcGf0QziS-QkvkTu91KFSSIdQBoAMTNeuILE1fDnmp4VHHJTt8iH-n4Aww-j7OsWTO26585IqHSzAdVq189ue-SAvwxBOw6viJ5jjU2lZIMXBBC8yy8GsNF0GMEmKRiJA0mfVGlLiraIMJQHckx7OgFosaxYsf8SMm9QPkw9yInTvHJJiIzCnp9IxY6tB8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29528" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29527">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKZ-lOrrNhT5lLickwocTwBeVFsPRiGXVqg687M0CkxcEzeTIlBnkB2OiFKO3fUJF8-4wQgwIOt9Qz2i0r7DO9VS5dE6vC0Sp8iF2f_miAXhlm2eiLc5RgUXiqqzmN53Et2it1VHn7PLcwbtU26U8ZeK4rY24G6xOgpK-fRn3UTK9sc7q1n3Yhtki8y2-145FfXZqotESVqaUx8433shNrvO7RnGGi2dDYMa7WrEpDZV39t0I4J72znBHK-iQFS7TutvlAdDfkvlN-saX7xD7ic6mgph0WNaPVjjXTdYkSSTPggHlUhNhY22Zm4K4WYjMzWSpIYq658kVjFIc7Zv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29527" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejw3aokFYJv84F2HtZS57d_-ba6qPUYSNQY2gTBYKVwNsMMXKURbdxbb3f_4eS3ldnnHx2IipTogJD18MfJot9yfqj4Ibuy9k_C5yH4Qu2-I91-kGJWCWCP4O7kW5avAq9im1GnR6xdaJ9_1ficP3eKS-PoUXmHJByjV9cdok72iy0I5U9eJdkggtm8Ns73wE7lO3sSHSgmawhCwu5iQ3u5MdXEo-L1iNpuwhVyB0qNz9nGqk-PD4f8fEgLwqhEGBVKixaNr1Wnn4jY0VJa-JIeIoT9qI1p3IXiYhRVYb5BYVUPf__pVCol7qR64Kr7ZeW0y4My4t0iQeu7kCEfPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات؛ یاسر آسانی ستاره آلبانیایی استقلال مشکلی برای دیدار با السد نخواهد داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29525" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUkVGAXe5gQQtYF49hk7nSwbF84hxS7xaNwfDWv4CDMrkKOZnkVJAXke6bTdLDPVx45BJ9CrDhsARSGdudbO_NMstpzgOYUxySv5AJnVHhgGthS43T6ShJTceRLfgKywbAeZG9vgtLiVobYGc6j5cCKGLY_Vu2r7y5NCXvNUhXQo5TsdRhpUBPAcGxN7hPIqf_CG4SpayfKmX-MWzJKf9Wp6kggl9mMGqyAvUjfVgIa9Q86dVuPjWPcIjw6tc4kaG36OPFO-UXDnMU8X93xJvn3_9fOE7n82SXx0WexxVQahEZdNo7OfKVfmTKoeFv4OGpv1vI7j5QI2azFt5osQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئیس‌باشگاه‌فنرباغچه:بااستعفای‌اسماعیل کارتال مخالفت‌کردیم و اجازه‌جدایی به او نمیدیم. حین بازی دیشب یکی‌ازهواداران یه‌بطری میزنه توسر کارتال که باعث ناراحتی او میشه و بعدبازی‌میگه استعفا میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29524" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTkrrFdmc9Z1_TyCnezoTkOc-O4fQJdN6GIUUo3yNf7rh4HgGXIsoBP5Z8SlLLgtjVcrFk26The0G0E4xNE3TvWyPouCb2-yGi-Zoz4Nq1TohCjyN0RAF3PrG9tr6-1rEcpmMIV-QP4Qw62WMQXsY_7PHvSOYmi5YMwTUZVUEB1oPpzU8SQdWgBgMsR_kPXDJh0wXki1TiCmG-3ZmnaMsFrLffxJ5PzAVTWjzwUm1JdJezyzNWcKgqIF-91-gv0DkaeQW-5SnChPDnhT3Get0_tPUoVACd0x4OkSkzZ2uU5b00FfMAQZ6siMH27xdnQb_IbNPSJ7PjzkUb2fbY_cNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر رسمی باشگاه اتلتیکو ناسیونال کلمبیا برای خامس رودریگزخریدجدید این‌باشگاه. قرارداد خامس یکساله و به ارزش 1.4 میلیون دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29523" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6Ks7fXmAxZTgbH4KR3RXghnVIUrEajHtt5zWpM6MQvmZqrbMKc9_uue5HnEMz2Uvsu27IRMA7864WYCiJI2DHTdNk6HEgreNqR-LutWu5tGV13vNcI7I7AKutJiI574D4GV-q6SiU_wUtbGqQb2Otz5vOA7ciHrWMHh5DVLRa2qDIwvyqmbG3AC_3mMrIgOTyg0YPdVj21o44ajDhlMASefmjjz08TigwnIMReikKIEoqYco_ue0eVOtcLCXVoI9D7Mljbq2xGBBYRsr71xurryXYO5pscSSUxizIcVsIOxiMrAio01HWe1ml7NWB9-_hxiat_feBcnvD-JV3yeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29522" target="_blank">📅 13:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29520">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGzMzvzE7raLb9zwxcSrvA-qogSbieTDHpXfqLSoeJspQH-rzT_EuMUAAlRhpPFONmCYhyoOjy5Mv-ZIqhaztlZ5SsXmZf62Zpl0MH0spk8FAdQ5VcxHaCWFDKAbvUThIqpMbxUloiCqX-ymovTxBUCfr14fzxNTz00T72GfKUyDX6R817m6elSx-ZEwatbWK7p8OZ2k6Tv1uenfgDpm3V2bwQZNyvw3kO61hj_z-fd8jNAx_uil8gnISZHqnT4VNylLmS-jhc9-WJfVFAxjsD_Suqh2boRmxa3T1usuZj8SIUNOf5TI3E7bmFtCbv5eBMTKFFW5Ks_1gsHUtSVrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9CVjcPI3Zxja8abmRQTDOhOTNAilZoaH8m6BDZWt9kM86t5-YL3HRS7rGFvYwVJ0V5EBFKDxxpZJQWLAzIa0vgEbKoM5DTscQLVUv_NhEfpHwmA1Ate8smyA_jpwJjsKDUC7btrzkmA-mc8iNXa6AYazjn56OqC_pjcSwaQs0ZlDULRaS6VZ9rHpErd1OHC5nWyNRLltBMeLmZ6n1UTnqRKgiB9kSIC-zxhgaPf199WEgF8x2fBZNqn8_NlMMsKy_4peRejb690MmEyUY0ehYtx2FiSBNTP7PmGPop9SW9hPU-cdu-KQ9przjgNpVwibIgIdILpKgDoxmlmm-aGrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇺
دوخبرنگار شبکه TRT SPOR که پیش بینی کرده‌اند امسال بارسا قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29520" target="_blank">📅 13:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29519">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfDqqF-ahtUQF0ygdznP8xFLrwlX9Z49trA0Dnj8Ve2qrXCvpkIEH4nBXuR7Ob7oRrutYAO89I3Fs9sQk27yzxdrcBLYYenH2ZIvis6ldH0CddkHwB3Ms34L1QHiBpFajz7stj6K6rT28vbjjveTSipRV7CTVS-pojSi9v_w5ADzRCVlGYzC3MMFWUMEDKl0mjCJTqlKfma1BC0vu1D9R9R1FKJewDWMiUrhaVI8wiRMDof2hQpp9y1GyF8H64vBo22vGVaAiTz72zLp3pXXQXT02bLvxds_8KCOFAOikNrR0gH2UN3iFaAIw1-ByqjET86pjAu8Dt-1_SEUXCrupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
🇨🇴
خامس رودریگز کلمبیایی باعقد قراردادی یک ساله رسما به اتلتیکوناسیونال کلمبیا پیوست. دستمزد یک‌فصل خامس رودریگز 1.4 میلیون دلار امضا شده. خامس دیروز درآستانه‌حضور درسری B ایتالیا بود که دستمزد باشگاه کلمبیایی بیشتربود و پاسخ مثبت داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29519" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29518">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTFycQbyYN2x2Jd5t6NVilL0ng2NDZ8nlEahGSepxWVdOL6yJ8h6mg4x0biFBnlfl1bHIhADBTY98MzTlN_YZ_XD82YRufI2IEXpRr4XNdOvmG3yEGch3ixWiSZeclJaZLVa8SW0NKsAoZiLDKqRYjJ4IDfrxL-CwRViL5RuiP5sCtlgsLkO-GwRvSRQFVEr8QMNqYexOKt2CvTi_NmjbxfZexHRWVCvsqYPDegnGj_ReVqK1iXzVWgTkXMc4jLaO6vOtY7up_sbILSjq2jwUJUuWhg3M4J6Iaf93hKe6pehdIkzfucTyNQ455p7zUVgwU8dmb8RsV9wWI3f4wpE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب استقلال و پیکان از نگاه نشریه متریکا؛ یاسر آسانی بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29518" target="_blank">📅 12:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
نجات دروازه‌ برگ ریزون آنتوان گریزمان در بازی این هفته تیم اورلاندو سیتی در لیگ MLS آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29517" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm3KXcMSPOWQEanKs9fn3ObfcVBs77Gdy7uTftP4d5_JNqfhwdR7_w2iVsPcUiBExSb6H0KdSyY3FujXfYX6Wo3RshLO-MCLwFFkHqGvNHj7uv1xphQ43vhe9QOK8ALP1yQYKDPmsqCY_pwWRG6ku_9RVUyVGn-CSKuTX0-wYzsA130G6QpDv6Xner-eh2m22-K35GJ-AJNm2EcVejSymc28Obp8G9MLgvxSefUtKZP9fNQh7lsRyrNa6cn77HSXQujR1ge3Ws9hreYz9dQDiuJwxZC5ja-19GNhe4GNIsZJgZEbpiEjWdCCC4MQdfywvR4et3QvtmzinxMtRp2glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29516" target="_blank">📅 12:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXeYrxuwuFUqaIGD-Sh_1VoE5LyUlqzJpox3zv40QxsGyYtnYyMyQc8-SiD_OlT-oN7qwpT2lyjEHbyFi4WSSEhKGRU0kPvyJ0zo9YBXVdiw92QsjMKdmBLMsRfdJf4tC7GtG4pkZvsRI8PNmFI7aZS59Tqn8qLUaSdWWY0Y5cJ8sR5uI8w36CVdg_PMcbxGsUoYKi36UY1c11ob7K1pQMOplsKZ0v4WJvs3ao8LLXAzkmEyN8N7ibMo9rFtoi2QrSBgVDmMDS_KH032kidbAII_RRxGadlA_BU3Lg-f4Bz1ZxsPcoAwNKT_T4t8nbhLbRKia1Nx2Q1GXab8DFydZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29515" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29514">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29514" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29513">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbgbX-Jkxq6WOFG8mmb2LYOy0Q15My8B0bHTkAc2GjsjLqUdG_E5e_GvqrZqoU5VhWxs725oBJFamRIowLueE318S5-7KbzLT0IaISdxrDuP0pqPsQJ6iwfvC2bBWZ9wMcugeQqXy7D5F6UZfEaQwy0e_18Q3Twl7HDG4yzBfEnlImua7KsSIPS8zvUNUwgQg4H1oLP3TyRcF_rsVf8cygYoN1XQH9_R9hbAmRY9Xlf4Ovm5Hx4CNH8K740fjvts3okS8AVrBnTVbT11MHOIAq2Wbnfqho4KqbzMxZ505AdwTN6QMHBIaYhDPhLbPLhEoiP_2miEH1T16FByEbw8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره منچسترسیتی:
یه صحنه تو بازی ما با پورتو هست که روساریو داره باسن منو می‌گیره. دیدن عکسش قراره واقعا جالب باشه.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29513" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29512">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz-vHzeWaHIjB15VPqOaMtUEhuGBt1kovdtewMKoDcOEXQ9u69cMDortkma82xnbyDKF5N8Rdt8EFjxQZfAYjAxU9XBFPHEBPEotWvXMxBKwwOd_bOEZRq1M78s7XZZqOhYX2njPnPS4UJnLQzsLG8CC8tz99qbts7JaVnfZFMiISU3HGTX9eXMwTam8JtKkj8R3C8Gin9ZB6WxdwOCSLjzIF_kNscJ2EiwSlKdZMJLAAj_0QRihTSqNQxMgmsVhl3ZyZwbsLqllzfqyb8eEFoapsGpNGBIK1HZlR-k5V72CZUBcdgbEtjSzQF8Q3XMOewnxMe-wT7nC5OkrKu9NWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دی‌پائول به لواندوفسکی در حاشیه دیدار بامداد امروز میامی و شیکاگو: تو دیگه کی هستی احمق؟! من‌دوتا کوپاآمریکا و یک جام‌جهانی بردم. تو چی؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29512" target="_blank">📅 10:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29511">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWQ-mJ6-jlD-PT1QBPrjiXVqhToBgVRtI3wdt_tlrStzVmrOBkYWcv_fnWbzeYGndLY5edkZZlzr8vhHdbIhMHjHn-moganm8vgu3z1KDepYD-Pq8GstfGq4_V2S_P_J-s_WY1vk-4cVTCPxCohD3HV4rHkqG67tX13ygl075Rnw6kJJBuFTgFCxq6YXrewwAQxn6fupJexBMoMmtQNtKRgbEOCr5fr86r1jA2KsP6Y0Vzd4-fNyCAdfKJ-vngpt32HJb4XeliLC4NeSYHiBvPXsLH-YGFibIXZZdA7GTHGbZawAMUQhcby0-jZi_CYsETPS204_SvO2W7s383Y7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس:
اگر کریستیانو رونالدو سال 2018 رئال مادرید رو ترک‌نمیکرد ما پنج بار متوالی قهرمان لیگ‌قهرمانان‌میشدیم؛ لیونل مسی قابل احترامه ولی بنظرم رونالدو بهترین بازیکن تاریخ فوتبال دنیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29511" target="_blank">📅 10:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29509">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=nbqCrixqvsKWRtazxr3TaqSuTN-ngES3P0yOXY3nexPO3F4R3QUdY0JuCOFbGl8P3zpWMRJ9Qajtd8vIOATdGlP-IetRK53XkN52TCBV8W5IJJsw-mdmaGlRakBymCH1A5N3p36wJ3XK0FYHMdr2ILvh1tFo4HpXtGnwpt8PpHjl7SRgzkZ8_aCvtIjTKOLbgPLvKQMYchz53Y7733FYNtBNb4GChYqLVlQwgHcZx37utaBE6pLuIxgigszkReqS3jR7yFrdNxHd9R8Lf5DqyEjl_rChHVQQ8w2bGlk4H_4lJ5BHlIooLEuanQSNNg25NRrFnnrtaEEDXa9DH6xRgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=nbqCrixqvsKWRtazxr3TaqSuTN-ngES3P0yOXY3nexPO3F4R3QUdY0JuCOFbGl8P3zpWMRJ9Qajtd8vIOATdGlP-IetRK53XkN52TCBV8W5IJJsw-mdmaGlRakBymCH1A5N3p36wJ3XK0FYHMdr2ILvh1tFo4HpXtGnwpt8PpHjl7SRgzkZ8_aCvtIjTKOLbgPLvKQMYchz53Y7733FYNtBNb4GChYqLVlQwgHcZx37utaBE6pLuIxgigszkReqS3jR7yFrdNxHd9R8Lf5DqyEjl_rChHVQQ8w2bGlk4H_4lJ5BHlIooLEuanQSNNg25NRrFnnrtaEEDXa9DH6xRgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب سسک ‌فابرگاس سرمربی جوان و موفق کومو درباره بارسلونا مدل هانسی فلیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29509" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29508">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=Ick5O5s4yblBexAqRWLpEq5nGa3-kojRk6zKLZQk-V07kUV5lCYqI919GED5dw45u1xOV_CuAQBou6fQhWYEnsByy0aWqdxpy3A1hHEPy7zx_bld2joHX9ZEewqUf3h3hXDQF1wdDlwtuhnGl1VbnSm7GDKBeYsSr7377EGzGkK5EcWw5EWC_TEcVM_pnMWv5x1Bb_1dvEn1oOHSa6ImOGe1PGGk24r_hbYGvL_O-jLDV-My9UzeVxpVjK0JnnHdBV5rwQZdazyEjdK1NiJPcfU1e5-QlJtDbdlpy75XCwyGJHz4THY6plUwVz-ZUppzSK9_XhBGb0VxlX502YqSYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=Ick5O5s4yblBexAqRWLpEq5nGa3-kojRk6zKLZQk-V07kUV5lCYqI919GED5dw45u1xOV_CuAQBou6fQhWYEnsByy0aWqdxpy3A1hHEPy7zx_bld2joHX9ZEewqUf3h3hXDQF1wdDlwtuhnGl1VbnSm7GDKBeYsSr7377EGzGkK5EcWw5EWC_TEcVM_pnMWv5x1Bb_1dvEn1oOHSa6ImOGe1PGGk24r_hbYGvL_O-jLDV-My9UzeVxpVjK0JnnHdBV5rwQZdazyEjdK1NiJPcfU1e5-QlJtDbdlpy75XCwyGJHz4THY6plUwVz-ZUppzSK9_XhBGb0VxlX502YqSYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از واکنش دوسرمربی بزرگ دنیا پس از پایان رقابت‌های‌جام‌جهانی 2026؛ یکی نایب قهرمان جام شد و دیگری‌از آسون‌ترین‌گروه‌ممکن‌صعود نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29508" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29506">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=EznClc8bOLSJpgx--JEGtVKITFzaSQ1mVkXIIOhV6HJMH_shP4sGKkgGOrd_MZb5TAkOzu9HqR0vSMYC332eILFse67vLgKzftVzbbr3Fgnp9tqe1NDOY9E_GEK_wVhM5-Xj5u5fw5UlpMOdqoEwj2km7GWQYodKqC-VuSEJRh0ieqjcw0nOfWoCGinm_tE6oiyJmZmhZPHMtWlAiKi-sbB6lUBR0LsaF3RO5JjS4_t5WO-P1HDU9N_anD-zrT57fuGkFylIxgfO0oss0JXjjhOH6ickKKu9ePGJeoyGLuOiQIRXelAbmKZFYGcVWYWeI5Nptg8W6lqa6kHTnYoElg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=EznClc8bOLSJpgx--JEGtVKITFzaSQ1mVkXIIOhV6HJMH_shP4sGKkgGOrd_MZb5TAkOzu9HqR0vSMYC332eILFse67vLgKzftVzbbr3Fgnp9tqe1NDOY9E_GEK_wVhM5-Xj5u5fw5UlpMOdqoEwj2km7GWQYodKqC-VuSEJRh0ieqjcw0nOfWoCGinm_tE6oiyJmZmhZPHMtWlAiKi-sbB6lUBR0LsaF3RO5JjS4_t5WO-P1HDU9N_anD-zrT57fuGkFylIxgfO0oss0JXjjhOH6ickKKu9ePGJeoyGLuOiQIRXelAbmKZFYGcVWYWeI5Nptg8W6lqa6kHTnYoElg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرفان‌کرمی گزارشگر دیدار تراکتور
🆚
استقلال خوزستان: گل عارف رستمی به بیرو بسیار شبیه گل ده سال پیش کاوه رضایی به این دروازه بان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29506" target="_blank">📅 10:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29505">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59654769b7.mp4?token=EPmxdtRwpKKU8frmd3yOXgmvDB5lEqrKm_mozNo2ruwiyDBcNM_PjIpQ5hHJpSTBpq_ftQBSd1mUAphXSl42jDfAzWqcqZMxX_Q-fjAuXRIgGYupKn0_aegFsi96Toy_OwSpDz_Tq5paWgxrnFa7vr6li3G1VYsyl-4PqJCQyGMwbUf8XUWkx0k1zDt4rjVHeP372w4sQF7pGKDcRFLG6r4IHxGlcIOfRVlPpPt7xzDP1sfPVzZGNGtM4l4tVb8OyLxQqZUGhuNtPJ5CXwcCKjztByoHBFwF_DXqQBB-OwKFpTUX5d_1vWn1TwSrU0SdFIMrRKPs-XXyR9Z40LKEiUVhYnpHTS2Jk7DAqAWBMJrKlT2zAabDBT0by-u9lMwUrOW1StwksI0aPMc9IFW_gmp9GUZdP50KRZeoS1aFPwLGkaHzCJOQ1ZcRdTM4Wbnh-5uRnU9g2R9RmT3lfgclcgePDA_7Me3JUlxTxBA561E7tGY5gaN4jcEU3K-W_U01mBFKdzl5gJjBf5WOHDsvmGl1kwP8ZYtLgGzZrbNvLr1OeV3XReWO-VHNKE-mjpGbgnAuKxf_XDjOfbyArvNdTICrAQ3DDdkT6ef1wKwF-bOgJ0Ry0xBvNq9WlPqlp-5dn98SH8F3sbwdLSjtKzu_rLwAfaKQeILzqMt2iv9xKaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59654769b7.mp4?token=EPmxdtRwpKKU8frmd3yOXgmvDB5lEqrKm_mozNo2ruwiyDBcNM_PjIpQ5hHJpSTBpq_ftQBSd1mUAphXSl42jDfAzWqcqZMxX_Q-fjAuXRIgGYupKn0_aegFsi96Toy_OwSpDz_Tq5paWgxrnFa7vr6li3G1VYsyl-4PqJCQyGMwbUf8XUWkx0k1zDt4rjVHeP372w4sQF7pGKDcRFLG6r4IHxGlcIOfRVlPpPt7xzDP1sfPVzZGNGtM4l4tVb8OyLxQqZUGhuNtPJ5CXwcCKjztByoHBFwF_DXqQBB-OwKFpTUX5d_1vWn1TwSrU0SdFIMrRKPs-XXyR9Z40LKEiUVhYnpHTS2Jk7DAqAWBMJrKlT2zAabDBT0by-u9lMwUrOW1StwksI0aPMc9IFW_gmp9GUZdP50KRZeoS1aFPwLGkaHzCJOQ1ZcRdTM4Wbnh-5uRnU9g2R9RmT3lfgclcgePDA_7Me3JUlxTxBA561E7tGY5gaN4jcEU3K-W_U01mBFKdzl5gJjBf5WOHDsvmGl1kwP8ZYtLgGzZrbNvLr1OeV3XReWO-VHNKE-mjpGbgnAuKxf_XDjOfbyArvNdTICrAQ3DDdkT6ef1wKwF-bOgJ0Ry0xBvNq9WlPqlp-5dn98SH8F3sbwdLSjtKzu_rLwAfaKQeILzqMt2iv9xKaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29505" target="_blank">📅 09:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29504">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=OLMjZg_K9leYWr33ggWxFzoCLs7ZEo3-8OMr_39Pu0S3B1rvmx1pTeNBcJJ02uw7VaVzqROkEK7Enh2kZZeRBgCungNxlQazxlOG_FhOjLRWSfl9GxKKAm9Jzh9Yp2Vx0c3tVAkTChYDaCUwIHjYBoF5cdZbI0Si2ZXYhBW3lhzEkjO99xP6h73sQDwMNhv9xjZue0Wy7KK8ho6MBqgPh1xvx0TjG-6_FY_l4Uva87w-mbviMj9Vy_ai5mPwoSLAev3DTdxj_6QYbygdEMoCNDGIGzpNuonGMSZjvKedhIbjMnQ-xMWR7zSZkjexMqxXwZj-T3WrZYoNK3SsnszjEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=OLMjZg_K9leYWr33ggWxFzoCLs7ZEo3-8OMr_39Pu0S3B1rvmx1pTeNBcJJ02uw7VaVzqROkEK7Enh2kZZeRBgCungNxlQazxlOG_FhOjLRWSfl9GxKKAm9Jzh9Yp2Vx0c3tVAkTChYDaCUwIHjYBoF5cdZbI0Si2ZXYhBW3lhzEkjO99xP6h73sQDwMNhv9xjZue0Wy7KK8ho6MBqgPh1xvx0TjG-6_FY_l4Uva87w-mbviMj9Vy_ai5mPwoSLAev3DTdxj_6QYbygdEMoCNDGIGzpNuonGMSZjvKedhIbjMnQ-xMWR7zSZkjexMqxXwZj-T3WrZYoNK3SsnszjEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29504" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
