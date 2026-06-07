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
<img src="https://cdn4.telesco.pe/file/QpcFfaDThY3BvG0_KwCOuHz9pZtTikXOiYxM-puMw20t6md_vRPfnobrcl-M5z1_MYzllKTKz6sAkzkn9PQ6ORlIaXBxscpZEubJDqiSp_6Q-28PEAzeOoCGpdsL_a4T_uApOu-DOmzXqBOwGck8QtPQ2TSqJHPTKlZ7VaOyskyXZC0KWagLESW5BfOWWC6u1fdoxH9w30jeCFE74CTnuJwPkPmuw6IN4eLCYRwe2EfQOz1sePf-MA000DiQLeJvhg5AwySM0QU1Whoa55pJBKdhemf_u3fkKOBwsi2AinWlw6Kq9zUWOfXW6MbuZgF5UXOAbg3fEomt1ljXgnLaPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 02:35:05</div>
<hr>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O687kfXCDyKIY1EZANFUFsQVcUroLcam_YWhXyjRv3BggUuxWev62JT0nDmrBSJc8k81pIwXDj18_7wTbC4stvJC2brJoACCYUY5OXJynjZvwIev8od5bMSpbi9J-yHv-NBTk5Y7w0B-wfUyWiw3aiMYfoKlvA_QmvYEgaN8sAZowTnvgYp7XcOj_Rgg87IAug23TCFC1954lREAEKz6FEviJkn9olOcKqGsZ_2J0pa5OBH_5aozyiJxqlrVwQpR3BPQGrNcYKruMQyXL9wDB6uPS9I4SnR8rbW5PnxNKKVXzv1gZt1rIsvZejWalbHXr2cY8X8S9B-1ZNmP09ff4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpkjHFFL2jwlOQug4T9GrARuwGVZf0ZcOFm57RktN0rHNg3SBJgXliDZ7lnOy71FfjfG2d82phun5R40Rn7For-ULw-D-b9BHauUNc6f-01XbxrahLS4Ulzjlbvg9wWGv-AdjRQpasKtukdsooGG4-9KCahGQGKlnl5_YEUEjr5-LDeMfgZFJRNzsXjsHKjMbiqrVTvizrNSwBaib5H5g4YzP6UpDucXqwq9quq95nCGjlS62IFvSrW7Efaq-lyOzdqidvKb0NdufY2TvhP16hWxBvoNXkTHArk6UPKPQLX8vbw5_MTxUnUNRdxwaXMZTLDTg0PFPLGO3l8CS9-mNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IufHf_47SbFPP7H5dDY-ltfnKAnqbn4ECAg7ss0UgN1N5SWfpTABsXaQl6NFHpmGNBrKBmhfiaOFQEdRXO2WJ1sa-IOylJ5iKJSWAePCY6IlNmtLRrscnlNVHp5aBccX2dFBL-ihzvZcWnXx81xfBJhTpl5qvpFXIkHJPBzK9ZPtu_aXgATLwnXzyy-O_N4Dq-NniTUJdAIohZWKUPxFbYVW334yR12IVup_lXpNTwkst7mSj04TArzFF9kfLtIGnBfs3fBwdtdIPqtkqjrUhuQc5VGeIryTVGnRGvN_6Hwh3LgCpRc_pi-C9D0TqJ8ENRNNs-RES9mX9xAbvOJTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiiMXvXkRe8VgTrYXjP_Z42DFCxQ9CGqpbL6d0C2GPh9ULhU-QIfKU4FcH8Mo8Sqff_7iBwJFkwmYFt7RytM35jhfjPS-cbv0EU4-8sDrTr9zOejBXbOZvaT19M2xmK9Sdn70S0WyVEB8jQhXjWNqaZ-kNv-DzhTRH_I0qBpZ8kT1kCnbRRqrpMu_qPY8vYvbUk3eZcUitr0kzpyFPOccnaLvHB8foi0jTSgnYQB5133lyKNPIm1LITXf4QqVIjcCjNmHkRosHSayeh6RPLA9Rz-OgXNjDZoI0XZ5dmuR4K8jAIxo43j_QqhvXO4n6RlUd2e0udOfKWtmOCfJvExqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO9DeXtLs82O7LWa6-l5n013lGuChQ5hn2FcCDh6p-KdeMFxod4Wz1YJfkDSJSi8JbJszJG7vYqI5xSpec61Ab0JWp5b1_GbRbJnUcNSWT7NphpUdjrP6IzD57M_hXVpGgXc2T2XUPb4qcQZkg2S3CqpM1ei3Aovd4xwPdmjPa3cOJRgLcofMUHOCuhi2jF1DnBYZ54u2iqu1hq6DWrfX-N8fTmH08GWmAdH0-GgX-NXyEiUMppy9Ey1WIV1ooo7GZCnWWOe1TE-n0UcqmIV4nGZ3__HMrefNGuyF-Lw9wz1-4VH7ZCchIUJatUEByTdNyccHakPcXFPgx29HfSU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8D6xoVzq6om_kzaBAPJOjFiSt6SsLtMo7qEujscJ3E6-ZtICWfKjZ4aSKCGm7XbWBId7elHZwqaYv-DvNsN3XlBbac_IZKL0AOmr-R5NNrab3PEQk0s_nIxuF0TRb54fILxeMeoqAe2EbxUXvLglOJOiygdwvh1ssBLkP0ffzKk5odXzPaDuUj43TtJZOhltLZRoHCqqRu7J4WXNh0RV7lhtD_N3_nYlC8t-0gM_EKBlQaBj71sBNEYFq0_DjxQW3Fc5-f0ubWPzil_d-k2jkapEyixVixI_mysPwM1YN18K6sNORfkKX5G5IlPpYWYZXcTnM5V7V43EZGDGG3EqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiRnqu1cVmBqqz91wq2H0uZCZ7-hyb6mrY_2f7tWufd7bXR3p-MEReAOcEblA8TsQkEe3AHRdaN6un-miWyahoRswXvNHj__Rkm7UIijGHj9kXmQkCxfsZA74ify_hnXMtdg9BSfUK_jYDE4PH1vbLkzCAmv8W8ZpULZ28eSKOlWMM3jV4HdioMmto61QZ0iA5-aJpLChEd0mKhzqqVqRu-67UGlbCW5bNQswCvhewyqUR-KSPB4mAKkXqiG3IITOlu1FsmVHM1jr7uzviaeatpS8useQIw3kiouv6Yyw0R0Wi6ACf4ALY8Dx4wLyNAyGb4jvtyfMy1_EqFcBtOLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=MfWm5GgC-BJBZHsovqW5CU8-vYZ0l438QYMwcnHBbddf4-YpRagC7mr0wQHI86afd5kVMZ5uq2OjmHU1IkssRr6S-sWJ_VodLNcnV9aW-Yqo_3AkmHpxeH_VUgtnmyn5wEjymiD1LUiljkvB5Iic8GQD3gag213iaPwKxIooLl_zAJfyvRM6zDqz6YxMBLNnFP4jQJkLE6XAG3upQhykTeiZxWTAUQ_kZXKuqEpZNgASjCJNL7HNRSK_8pE2Ux50nWPJd_Bzf9s5sirKlV-iW-NxCa2JavuqmyX3OOtV3uA_6X6nWgSFJNs-1nnmBVBtRwyR61rar8ro34V-1F_bPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=MfWm5GgC-BJBZHsovqW5CU8-vYZ0l438QYMwcnHBbddf4-YpRagC7mr0wQHI86afd5kVMZ5uq2OjmHU1IkssRr6S-sWJ_VodLNcnV9aW-Yqo_3AkmHpxeH_VUgtnmyn5wEjymiD1LUiljkvB5Iic8GQD3gag213iaPwKxIooLl_zAJfyvRM6zDqz6YxMBLNnFP4jQJkLE6XAG3upQhykTeiZxWTAUQ_kZXKuqEpZNgASjCJNL7HNRSK_8pE2Ux50nWPJd_Bzf9s5sirKlV-iW-NxCa2JavuqmyX3OOtV3uA_6X6nWgSFJNs-1nnmBVBtRwyR61rar8ro34V-1F_bPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=E2omNYCWWNVvdvzx930ZXfESi18XeCrDJgnTCPKDMsP4Z9MWUaiMjAElP1bruxkttRDNqcxrPj9bzgh89IJiXDZE7EQlwdh9dB3sY_lZw_kFZVeE8H4QeAEbjeYNunEmbnLsehsZWgOuKadXD3cbNfh3TXG44wA6eTXibJ-SI-uJm2xHUXSZOzsxPUEq2lnpH4CxAJw0vUIhQNhCOHOnJ6c8YYznlIbiEN1hMxmO2RUk0BBlXR9mmn3tOzai5DWGn7V4GDfDTbR8bngSR7BLPvTUSmGaOmzGoVgEZh-PfcAdoRVmWuC6T6AqqFO9BzuqNdFFMoXkTqw8cAIkn_ot-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=E2omNYCWWNVvdvzx930ZXfESi18XeCrDJgnTCPKDMsP4Z9MWUaiMjAElP1bruxkttRDNqcxrPj9bzgh89IJiXDZE7EQlwdh9dB3sY_lZw_kFZVeE8H4QeAEbjeYNunEmbnLsehsZWgOuKadXD3cbNfh3TXG44wA6eTXibJ-SI-uJm2xHUXSZOzsxPUEq2lnpH4CxAJw0vUIhQNhCOHOnJ6c8YYznlIbiEN1hMxmO2RUk0BBlXR9mmn3tOzai5DWGn7V4GDfDTbR8bngSR7BLPvTUSmGaOmzGoVgEZh-PfcAdoRVmWuC6T6AqqFO9BzuqNdFFMoXkTqw8cAIkn_ot-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3k8KY8kGJvAP2AAndTAuIcDP096hiOqHTX4vN__zSrCUG0XWofcZCTx22ov7tmWhSiTc-vF74teZiqGYAFjm1a6DQH801ylGKPGAdqcqOaW6wViYyrTtuOfzifaUmsM0RwwoyV8VKlihrrsyyJpm9f2BD31PYqOQpRtWvIrhxh_Lde-QQMSYONGi7tQt-G9FBVZmySHCZcKOLvhHTdUNu3_NZRaLZeH7F7h5Vn6ufiMYQb7fokh-SNt3LlIBCawziVsp_q95a1wCExGQp_ayPotx57smXhxGaLlpPzT5FPSdrZvIbWTaNpDp-SkTt7fdVRt1PMBIh0ZmVKn11t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwsBSRMMsea8Rh-Jk6A36yJIVd2Vh3LgTWw11UH8i3TDitHOnAV7q4iH_7z9w0o2FB1l23z5s9UJCcy1DnMe_JwKFIBhS0IAlMEL2HnSPJSSEIDTTpD41poQ3z9xA4rR7FqE7zH03J3vxG6FsOTiJ_myZtzB5f2tdMZKCX5fLB2z6_84jpBkG7RrMfHoQW55-ajzkvQQdVX4kIkSlpkHTEY41Zy0yN9AFJbRo_WSGsim13CLiwBJhh8DrtrGjellCD6HETb9tuIdrzSPDD-YBRrN_OUV_huG0ScsuRwh2aMU1kOBD4qovMYzuEVwyEqkcXYtAwi1LWvSCxuJ28ilKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjJdmhaYFieVJi7IE_OCwTZTkMO9SSs04S5eeuX5jRtnXNkWbTASMG8Ge4yXy-5ZquB8_L1t2JLWMewcokb-FxjDnOb6hQ-f63J854tSRM_9y1DeNo6r-nqZA5PGR3rXmCAE58w-ufoCdBSoJfhmd7DjfOjdKwjMLtBk3sq_-0UMjYKlem9ffFx4Fnme7qA1J7zUr4K-ABO4NgXgsS0sIGu-2fbcWiPoOMvBf_uwTJ9vRnGIU2skiyL6i6n0iioGhbpnAHp6M7LYvEgNrLZUTXCNuP8V0qi5JZSUul9u55LpYugUDFaO4_5hcSMgQkv81RLxh5pvn7RATfiLM5r18w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1x-BVeAVrVqy4mSpPmJ5dygrDSKN7QtYYLvPlgH0AeSW8jfmFWdNnTibGG39_9Uhnt-Edx_NmFKL2l18GcF9cn4967kSFIOC1rt8DWlqDojxeNDJT-OICUSbaI1Ew0B_gWdjRDGvQQB-F1NqjSjNl7CitvEHCK3QlO5M-ci3WYJRCcN1uhGUfFL9M21mA5KMW4bjbYchhjkXouFdRyKHVBKxM1tipzonLNyEXAlJYqjEA-0_nESdOZt1Ff5Y8tacxBgceyP4nfAdCfQWcSdeBtuel5UrM_e3eo102cH8xp8ZnKDKYH--YrAN_YOjEDiG4RgynQXw1r-maacsxCk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5lFeayWe5GBYDK2yyubEqVC8iTZjk7SU3D-z7840b87h53awnp3h78BOewUmJ12xYSXhIkcK2pHEBCas_rp6Y0PIb2Uk2CvQWxa8mzvDfrON11SAmT_22ZKAf6l40Zt2zWuDZTtPWpcphDk_Ne1a3QJViSUuJrot6atjsyjbf6_RhwlhxNfQMCO1V3TBiaZxxN4e2BBzkiuQN8ECavAAwMuAPCc3HwgEf7M4kgP21u3aIfBnWNB7YwfAn1G77bV-hZV33bvJWcPVaTUYpTPvbyZxecSJIfLpVIjbT5ERmdz5aXIIpoZzsxXxCYQROkQ1qoOU3GHl5D64W7htjqYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnk83ReowcOvjS4tDl5FXmhN7bHgkggHIsn-it_jEgwrSBNMhOBYNwMlFKT3UNInxOitkQVonMubKS8WAMHTA8-Yc7Pna7rUOwTQDFE8eZBISrwv-2bDCF_Vn-qZwYYMuat5IWxBZs3eTjl83OYZ4vt-Vv4UldzuDEGd3SPrNY74XvkJibV7aZrFMvv1sZS7OtLe_PnRAedNxXPgz9goXwA_9K25UmKtLK8C5HoCbAqdnS54JCZMbod-edQ6C9e9Uq-RGkTnmhBE85vwN-v_pyvC3xF1cmuGD8TLP1mz0npBwZC-SUIVYMYwjtUT1HJOPFIpSZGOSNpeGJ0NqE1tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccSMDKLKa0pwm7wjroosWfHzy1ARFJ0NNDFEKB-0femTMr5vw0FiTboCxOky-iiEf7tpO-R8FXdwzfrQXfUa29lcbTAJ0A9uuQfBljUNsmFrfYFTb_z7CW4hBU5RVawEVh9ya4IuopZ8k6dGNDGaDWZcIhHgNNcW5ptJhxQLa_6iqmmE3VfBkVQAdHXo5nPZ0jWk7721BEiCVz7AD1OeS5o1qU-lmUKginrq1zOSwC2F-9iNTKNQ2m_XYwk-UN9moBAq3ZE_MVwu1UI-OyVLs4SmQYXQHeVgnPX6MEXFK_oKwmD8f0SeemsgVeBiIjM7UwvEHLjuW1GdWyiY-YdAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2-CH53y7F_vB2Ipzbb-_kx-yUx90nTzaAgkj_mPOg7jpzZuVr5JNg6oI7fYN6NX797OgnnFVK51IRE2uLLXzljI5DPojkO2SGrpuQTp_Md6fXhzm-ODV519YHFmM0ygZ3qV6ZG_yXjh1CZ0w0kFk79O_XwdXBdNvrys-8vmgclYHkvLQEH8PWTlDiHxpuEoxyFbrcZmgV05zkv6RLcSXkQFkXMB4zEd93XCZdqprGSy4FXpYZdt5-VStEJLxG9KBQYPt3ahG1Hr-nmJG10TiyUX53mXct2GYmnTO2iTcGokTPAyE78nfhbgQfXr5Ff0MjuOifpzMmn3Y0mxJuF1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4QEcS3xjni5SEku-2iaq67tOSDaTgNo-Ih2OM8i-rVly9gCm05hn_Vr6aYB9BE2htzUZgkwYwNSg4B_m6ZSZzeDzeCiMoP-pNt55EJSqG1L4MIbw7YeTqhXkw6iSI1pQpthOm8fM2yVoWZR_R6_AuvSAbaoDfGBseT8g1taGppzjPntwFgIL4pSh7XVj-sNkKoFPEgcyO_tp6qg2f39m_RBCe4zBoGck2yINP9Q7oq4rWSHuTE3loI4q4wtcdwEfVSSrdalq2iU6N-cwihbt9zz7Yx9lQ3iGaOHzu3htNbCz6Ne3QNJueCDOT9fH_XylwIe6KwQXNe2J7PGPP562A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=WW8oZWmjMUb3SU22RuU-tKKhIQWaaLQv79UX6poWl9CESmD-od4hpsoCPOsfwBnDWY-q7hZHO3P2_ZDeH8c92Dfm6im4tDLJ1Xl46x26vklo5IUM1SdSCg6TC5H-ac63OWonh3pMWrti6gGSL663Sv3IWRHA4Gpn7EJcxCTGvCiJFtYbz15b2_Ex9OtRtCmqe1QcWHF-H-peTKbdMqdmFqOyb5eODt1SHaC2JnGAGmzFVi2ve1DcEjUaQPjzMJ9uFsF160kLHoriojSOnk6wcWofl3LzOJwevSlNmvAJgd6NM0DkDWWUkIe1TCrSlFDgDt6n6E1JOdx9-bzpdW1wqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=WW8oZWmjMUb3SU22RuU-tKKhIQWaaLQv79UX6poWl9CESmD-od4hpsoCPOsfwBnDWY-q7hZHO3P2_ZDeH8c92Dfm6im4tDLJ1Xl46x26vklo5IUM1SdSCg6TC5H-ac63OWonh3pMWrti6gGSL663Sv3IWRHA4Gpn7EJcxCTGvCiJFtYbz15b2_Ex9OtRtCmqe1QcWHF-H-peTKbdMqdmFqOyb5eODt1SHaC2JnGAGmzFVi2ve1DcEjUaQPjzMJ9uFsF160kLHoriojSOnk6wcWofl3LzOJwevSlNmvAJgd6NM0DkDWWUkIe1TCrSlFDgDt6n6E1JOdx9-bzpdW1wqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3AF6AX4qTHjvA13qqj7k0-rAlY-CLoKU1nwib9CkdufYNNTjpv7mUIC-5c-uozmh2GEQ5-Xk_0Hv5twqtAqx3ovdw4TL6QWYPiy2eenFEiXck-5tzD6WVcntWyMyuTf6PMxwjDguHhLR4ujYnXOD9-uxrkSAx4ftmOn736d96ooDd3fwRFKmFz0Ocvvc-LOh9z-Y4dcZke6V7KbazBMA3gIKe7ZJjsSRBlgNaOf-LNEcvBLdtlrqyRh6j1hHHRg3eyQQd323IX_6s7vSWGN8uuTpD2l8mmniJtjRukdYxc606yZ2VugCOZueZB6roMSnZ-GnwUnOI3OQ4U-devCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfhoEE6OFJawxwS6iHy-bH0urEcEr_YUFsjW7xIlcyIm6h5aKkG3skP-1p5k_1lUoIQ5O5z7ySvqxNUHzNmW5aoMsgt8CPuHU9vCwhs-VmdQ_IGDnqz8MWsXCLXBS8rpxa287YKsEQ-0x9-OyhE7ltTq3ijNJZD5GaVW2wOBfsmy3IGQl1AJuFhjIJJxQD5vuTStELyrb8ZppVeD92eBEyL0rrDtWX7HdUby31pPNcYWvRZwsKClJojO9-8s0ztZXhajx5HVu-lahj5na69PnzZShwI2AFOe8QuOcbX4UqPlWgNQUgYSyCZEDoAh7mNbku7l25g-iRWSEtvPXAq4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYBGdXKtROP63cmmZTRsmpJxDLx3ZcyUpeI5vfoR2ijVrjGAHdDXZP_u-EWRB4WjwYJykEcuGKV8FQbaTyNvUhfevJOUntQtX_SjmBT8zwLmIb2AN5apZ7PSu98-HuArgOYyKpdrNtX-JtIgCerxwaCxUHza5xVRMRvVNCJBULTxGHP5IDeQA551c6c5PSWitNXNl-RTWFRosELuI-I0v85a-4Xi-HZZJi_kPKT7GwPulS6o3Lf_2f9-hrqC7hEzqH03kEt4RVsMFDDe0c-klUAHwzznBV5IuWTs3utqo5XHX6QsFFW_XcoeoXD_tZilncZpQoQXM4a0Hocbh3ODcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFrwbECOqEK5iiQEljCLRq3d3-ySvVSFfTt8GwXr5KUJvPKeYmdhw063lcd5MArweQScoNfVFR1MGJPaO1uJ0skRciTy3eibvIIeJ9pwMg-_gDOwWScesjh1nHxS4iUGaSfQLKOLhK0_Z1KwYpv-AHUBNq6zXQipcRpbjPdjhPwImdzjtkJof-kf4POACPdD1QrFOn4xJLKfYFjR7VaKdgwrzhh3X8BruzkPpzUWWOcsyf6RafTRCe46Nm5wYt7PwJFiRwv6gSxBKGc4AmFyA27Ctof6LiPRYIZ7oiYd3UsbXVYqLyNdJv941VUDcMTk1Sg76Y2brvPGQrbrNi6Bvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=VO4rYENiThH3uTH8L66ctsJTMYI0GcUyiZOjjogGSydXGoBqecePyHT2-eB1lBJ2_Y40sL_OxqAahrkF_-fJT8f5gd0k_Z0N1IYQvHAKxyLgeot-HOTIkQH_vq6IayqHW6pMiXQweOmx7ba1T8y5lA0Xe0ldd-57QoEgiv6uYAryKmM7ZlJRBEs9uqpm-WBpZMNxLtBzvoQ-KCymWuKdQT5PJrQC1M5sPZVk20BP0Vb3zB8P9ijHkxLjkewpqE1gZ6iqhCCIzqs4onrn_XlRfovPB1b-dAz20uN3c3m-WFjSfPZwSkE2w3DMx5Jd_agYxbSvpJ3CJMs85GOojngdPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=VO4rYENiThH3uTH8L66ctsJTMYI0GcUyiZOjjogGSydXGoBqecePyHT2-eB1lBJ2_Y40sL_OxqAahrkF_-fJT8f5gd0k_Z0N1IYQvHAKxyLgeot-HOTIkQH_vq6IayqHW6pMiXQweOmx7ba1T8y5lA0Xe0ldd-57QoEgiv6uYAryKmM7ZlJRBEs9uqpm-WBpZMNxLtBzvoQ-KCymWuKdQT5PJrQC1M5sPZVk20BP0Vb3zB8P9ijHkxLjkewpqE1gZ6iqhCCIzqs4onrn_XlRfovPB1b-dAz20uN3c3m-WFjSfPZwSkE2w3DMx5Jd_agYxbSvpJ3CJMs85GOojngdPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFq_7_07-8q-r0nZJNGjdOPlb4XPRMXgA0akmYIB2g1-rEFv3pNqpgfeCWda1Y3IX_zbw3NCiznwHDgduSKWw1i0s1KK4ubnQGeN3hqgrIRyEe_XJZ6591dB761nafsXajaSf58D20bBljBMKcopeG81JqMMz4fnD5uIplG9Kn3BCkAxisnSu1uNIcQpXUKiU-dQMRlQ7cgZxOnXlv7EjUc-di1I4ZB3yYf1xgQ7LeiH4tfPnVsBKrj_MlAiNDAHN4W7rhbt4Ab8Uu8mNJQ_JTrNEdltbDDrkde4uWQYNHmUQzk7_oaQWZjCc2Ufhs1NMrnhUTacBaLiCNHjvQa6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=NBkTKWlZ8ssm3ChAg5v6YACAKl6aXqOQODanJFqtuF0bPjmrSCpQieJuC0DOI1LhL57NLHZve-qGybKpQjZSG7R4RoHBhjvNCYYEgqNxyrSsaF8t_ZJwKlXB43zYFGK_2yM5A9brXAkNzSHwlCkghrrbso65uB8waZDCquSF5TbH_Jpizurk8ryQ4dfBHRiyJEBOHLOtgDSHO2hQ1HzAC0qoW4hGS98D1QZfgXYKbOKyA2A8siGEBl9uB10_tjBidlg7fO1lFFcEnKD7KVhVTiu9NW8CM2CX4qd7pVWnNcY-IPlRAHfYzV9jo5dB_bIZOlLjXnOnEoPGPfmuZWtnZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=NBkTKWlZ8ssm3ChAg5v6YACAKl6aXqOQODanJFqtuF0bPjmrSCpQieJuC0DOI1LhL57NLHZve-qGybKpQjZSG7R4RoHBhjvNCYYEgqNxyrSsaF8t_ZJwKlXB43zYFGK_2yM5A9brXAkNzSHwlCkghrrbso65uB8waZDCquSF5TbH_Jpizurk8ryQ4dfBHRiyJEBOHLOtgDSHO2hQ1HzAC0qoW4hGS98D1QZfgXYKbOKyA2A8siGEBl9uB10_tjBidlg7fO1lFFcEnKD7KVhVTiu9NW8CM2CX4qd7pVWnNcY-IPlRAHfYzV9jo5dB_bIZOlLjXnOnEoPGPfmuZWtnZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVqRIMheooyAWQHFiP9qIZa3_jbAHETES6_e1ZGmI0SVAxyM-VMmSr2VFL9LGcf4Q-Y16lgtgzTpzvByzo1WNEEGR6IW9_w664dIPaJHv64yUsNqT8TlJLWVdiPxwMmeHm5bf0BH9lVsSOxqgjp3Ag7SNmJ0LQBl8U2O4WH_fYotSesZZ0S0yXHQS4gvbEeTcARO3PFoKShBjJP_bE771hMO3dz2DNoTJ3tT0YNfEffEIWv4L97Y7fgaaP_gZ2ilPdxb1TE9iRif8GNQQ-oJLxE6uu8mBNYz46N5dbNICS53_BFJ209qUlMgQ3vx5nctk2VMzEkmU3t19qcYmxuF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIYfR2ghgfHFML9NsroMjh7GeT46YL4_1QDbemtFHqS0dmTpwkZ4-6aJdup6N-HUVeXKyxmuHMAZT7Vi5lDgvXVvUqd2eEz6MEJSlrsK3wBQS1Qw8z3IlmuMLptJsoxHlUDXnV2CPtW8uZMl-WNUc-6G1LE3PwQuVLmUoPL96cQ5CAZMylTBu0e_ca0K75CV-nv3DlYYcNYhOFBF5443WkxguP-mBAFLT7pYW1pHma1uzjX90dT4f_D1P7FxwkKXqjzpOH3u3sQLExgk6tUeh3mkj1lWQTCwpdnSSCL0BrEnaMKHxa1-FVLJU3VTOP1lX7bBG1GxpIOnb082oYTXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=PIaNMzLmthsrlnFTsHLFa9_7hqERBNKZYRp_ymKerC472YF5gCDoAupD8020QSic4n0v9hYKaKZnr9g6poOa5Jzr4VirTWfRN_eStxMuu1WvXcQRKb9okzI-D8MKOODq5tuPNtyQGIkqjY-MuB4TOmbC4oBHd2vW2-O4yU4rSrtGmso6cfxEndt7aJ7iW0iD2krWUCPMhbQ1KK8jxsfnREyWwmFxGEjVuF1mlr__6zyalnUAqXBMBob6NFWkHSPmXdVyU0UzBpuZ3e3jyMTmjD7iQZTv4DetGk5KAGJcVxmetCmuS2X3eIQOPSgO2I0ketgIEC_1sgUt0WegPoc7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=PIaNMzLmthsrlnFTsHLFa9_7hqERBNKZYRp_ymKerC472YF5gCDoAupD8020QSic4n0v9hYKaKZnr9g6poOa5Jzr4VirTWfRN_eStxMuu1WvXcQRKb9okzI-D8MKOODq5tuPNtyQGIkqjY-MuB4TOmbC4oBHd2vW2-O4yU4rSrtGmso6cfxEndt7aJ7iW0iD2krWUCPMhbQ1KK8jxsfnREyWwmFxGEjVuF1mlr__6zyalnUAqXBMBob6NFWkHSPmXdVyU0UzBpuZ3e3jyMTmjD7iQZTv4DetGk5KAGJcVxmetCmuS2X3eIQOPSgO2I0ketgIEC_1sgUt0WegPoc7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiCM1XT2y80yoAKpvTWjix_lUhRZxe9svAUDFfk2QgsLfOnXnxmfVqEOkAiwOY8t84YoXbnd-ReGX8oUtXN0Y_t59V7Qlgi8VcQzcMayuoHTULHX2W4-E6huUI1ZKsW0KVJyfvLMDMCt5cW0MN_tSw_1Hif0SpE4jpOAskAeRgaNb4iYb3rHHpcNTkLJN_H98VO8LS1DMy4Q2-mmNdQogClDhpDQ7B9LB4Tq4qyR5ekh939yS0kAsCn1oJu4bvVcqw5wa6XrgpW0gV8HhlbepkB9wcAwIJ027yYELnLcxPrWyJpl78QwP2bApxz-XW5WidOPU18P_NgnuBQWr26VFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=abz25dlQ-QWImR_NFqaW1KxaJawKLJJW1GhePKeDiT4qEvqkImM4B8mCG9_JqRI35q2Qp7a_ke3Ze7GA4oQvSedScfScm1g_DEix6mMgOsXFRaaex7fMCWvnGY6Yq9zvmrp1wNyp2su31Q8QHbhET9-bMfmAQboXdR29twdlIplf_9ax7OxF6jUIAcHBlOcvbsYJPskrkaoPCqdT8ZvoVBF3D1qvITRgjH47MdiRl9p2ZSsmWfi9cgzRtPvwfjrDCf99J_f0yFEIPJcfCdwXBCLIN-75bZKQBjpCxbI2jrJOPtnJbY9vtLIxxXC1zf3u8ZtAZ_G1uffZhUIBf7P1uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=abz25dlQ-QWImR_NFqaW1KxaJawKLJJW1GhePKeDiT4qEvqkImM4B8mCG9_JqRI35q2Qp7a_ke3Ze7GA4oQvSedScfScm1g_DEix6mMgOsXFRaaex7fMCWvnGY6Yq9zvmrp1wNyp2su31Q8QHbhET9-bMfmAQboXdR29twdlIplf_9ax7OxF6jUIAcHBlOcvbsYJPskrkaoPCqdT8ZvoVBF3D1qvITRgjH47MdiRl9p2ZSsmWfi9cgzRtPvwfjrDCf99J_f0yFEIPJcfCdwXBCLIN-75bZKQBjpCxbI2jrJOPtnJbY9vtLIxxXC1zf3u8ZtAZ_G1uffZhUIBf7P1uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl1MO48mmv6Bk_64sSA5icX47lxNzgXmQmjK3i57ErqhQHwb5-QIEdV6RqkObcMm5Wd4_Dc7iYINz_4oA56ClMziP6o6dpXx1EidafBCWaLJyzECliBOks0MafvWU1_8mMslcLzryYvn4aiEx9MZQj_Y_HQ9Kzy9LhM9lrDvhEFpVYwoTLKM6wvo4fp0FhZFG-Q5bP06LcWdu5KDqmBR9T5pfXyG6tzCBGq3GlVQxyw9o3BIKlkuF4kO6kOI5LktlCa_pCdoe7g2qYa1HaLa3p5b29haI7EN00xe6lHVT1F74A3hFVfg9r3HwmDFv0lgFPLM3oXtRmd6zWy1nDU0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChSsBgGNsYC4-gHgCr-YVcihb0v4w0sl3vDTIb_zZlOOaDddwxVrGCySWI7sFIiwEOlTzF-7gAuS4lOK-2f6HufomK1peu9VdResT4YZxRdbRyBjpNSV5jNszTZ3pxM0mRHNb_D_dVTJV56vZfAQuQEeGdLnvrA3KglLR52UP5ZUN-FU9pcvo1tuEoe7oK3MKeWVwYXVS21lA78rctNFv2wluO5bBKXdqmKYeQMXMrJ0Qmdq1ACQCOnTkCYyPN3HwjKFues09G9NqoraXyDUk_g0qrxFnKAIAFkDyVz_cCztZzPsSzXSOUzk-YrGy3gIW75UMmNFdlmrGg9sSizFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPfY1HhzJIMj865aYrQjA6-7eTua_CfSYpUaaD72ju98XKJXptlQiOmdGLbnycBn_-yWC8VR-MyMQXHsXTqDEAW12UugRcxu3PjdYhFbmc_eqMIiFLTx79fLLJohLVhbXGI8H9c0bGLMTw_rYCtUorLuFeW9xjY13gIbL2gV2vFXYwKoN8_EL8u7hSgURP7FVIncfDnjDMRLCBPG5nXZYgALFoQe6MKR4GcUa0RM7A3hnXBRs9IOBC17OIOgOWH8uUz_tBqO-A8OnmvRh7kNTPlCbT9Wm1GDo0KQfmJI41-LiYH7tVqCwdqLh5kSc1qDWJyEKK0Vio0jl0ovFPOefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=lOHjPcALiUexoB-XJ4bI75pERghebPQwwp0nwkjpDzgOir5Rb0JdUz62sv8Z6cP25b1JHn3mtGBpm4Yf3G9YR05Fri7c0Q-wnn9IF963JXwp70usxVG6nUUOaQ6OqbYkMrbHTAzClbAmshpgSib1jXDWzWBtMvu5QGVuFZ98y3YrVuE1sazSfQYIeLxHYU6OhEJBqxIYpNSULZ7h0I3IqUAyBRihC72KsCtBDHhOrRPTpF5UDUQd-8HVIdrE4A9sLzgNTJcC71V9dtSn3RGow4GgXEaCDGmzpFf5gEc7VZPNTTPmxwFR4kOz-o6jcFRl0QU-kfOKPZYtMZ6uQSbmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=lOHjPcALiUexoB-XJ4bI75pERghebPQwwp0nwkjpDzgOir5Rb0JdUz62sv8Z6cP25b1JHn3mtGBpm4Yf3G9YR05Fri7c0Q-wnn9IF963JXwp70usxVG6nUUOaQ6OqbYkMrbHTAzClbAmshpgSib1jXDWzWBtMvu5QGVuFZ98y3YrVuE1sazSfQYIeLxHYU6OhEJBqxIYpNSULZ7h0I3IqUAyBRihC72KsCtBDHhOrRPTpF5UDUQd-8HVIdrE4A9sLzgNTJcC71V9dtSn3RGow4GgXEaCDGmzpFf5gEc7VZPNTTPmxwFR4kOz-o6jcFRl0QU-kfOKPZYtMZ6uQSbmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=HJqaW3_ktbhL9HdhTQ8_iQ-kMYtNI8yFjX90xcFUJineq9o0KhwODxRAYX1EbIg7kMEL9qgZBw6gan5LcoVjz5cen30e1dZSy-uCCobwOeDw_vkQ_qwmaEQiE1mVEflGKk5UOR3lEEGQEJK2kz7UYHsTZeN6qzMi7zwLoZBPmpBb_AkFUl6zrgVP2i8EkGnllc_crZ3lIGBrXFsrcVCr7EyaxyYFpAKN7w8MxU_NDKpbAObTzeh4v7clzuhsTdHjn8sVhgsVmlGLWD7F21L48wNpbbW8zE9PozuwNYeP6yYMREbbY4HmhcD44qSegWtWlfOX7O8SLJ4TtAo5jSlSGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=HJqaW3_ktbhL9HdhTQ8_iQ-kMYtNI8yFjX90xcFUJineq9o0KhwODxRAYX1EbIg7kMEL9qgZBw6gan5LcoVjz5cen30e1dZSy-uCCobwOeDw_vkQ_qwmaEQiE1mVEflGKk5UOR3lEEGQEJK2kz7UYHsTZeN6qzMi7zwLoZBPmpBb_AkFUl6zrgVP2i8EkGnllc_crZ3lIGBrXFsrcVCr7EyaxyYFpAKN7w8MxU_NDKpbAObTzeh4v7clzuhsTdHjn8sVhgsVmlGLWD7F21L48wNpbbW8zE9PozuwNYeP6yYMREbbY4HmhcD44qSegWtWlfOX7O8SLJ4TtAo5jSlSGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=AYC7qADdhsTd_UHB0wNVeItDm3fR76Ld95gXkPbBj881NXWfxOfHACS9KrrDSYkDSbm-zRY8DR9UZv7PzfzWx_WQfkBwxYkMTOhAVCLs8mIg1ddmJg74pkSG81REvTuUR-9j3Snwq1Bqh-jZoeHx_XbjnMYwVdniAIVo4nzjDiaqcmokA2RCEg5_mKvm9PKDYuCgQsdvbfhtEQl8-_7-t2I8H8nJfnTJHzdAO7yfMiaOZthLYJTVo5qxlOLNLRvPw2PCh4LvV8d2OBm-m1bEOjOX8OOujjQ49iZe7HjTYrnNPi4nPTAMEQ_yYbp4ss7qwThi8qLTJH4fu9vVSZwPHgMaA2aTX7RrdXA5zOY6PG9-WcJyeJyhzIbBpMtYOy1GnGTnwlDcfY57hmYzt-th8ON9TL_oATNHYF5OUqQN7NhyIFB_y0VyaJjIJaAmUahLmfgRNk78pXd6-0i1b0i47BcM_MHIHPutXJWOZGSH-wmjk3Ul0Z0veNozPynGZuqCQUC-eXmQsI0EBPWl1-kX3lXHcZd5cbi_3S6wqpHyzgDrFW0O3bzGxwVpGFcIp3HJEBISCLQnsMocGjtY9J7UCwxpO40aQkCmqiJ1eQhb9zjYD_FHCjBHGb9k1AOrOwuqmUkSMZAXZJCtGF2F7YJoeMtzTgHITzS9F20-W2ml_vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=AYC7qADdhsTd_UHB0wNVeItDm3fR76Ld95gXkPbBj881NXWfxOfHACS9KrrDSYkDSbm-zRY8DR9UZv7PzfzWx_WQfkBwxYkMTOhAVCLs8mIg1ddmJg74pkSG81REvTuUR-9j3Snwq1Bqh-jZoeHx_XbjnMYwVdniAIVo4nzjDiaqcmokA2RCEg5_mKvm9PKDYuCgQsdvbfhtEQl8-_7-t2I8H8nJfnTJHzdAO7yfMiaOZthLYJTVo5qxlOLNLRvPw2PCh4LvV8d2OBm-m1bEOjOX8OOujjQ49iZe7HjTYrnNPi4nPTAMEQ_yYbp4ss7qwThi8qLTJH4fu9vVSZwPHgMaA2aTX7RrdXA5zOY6PG9-WcJyeJyhzIbBpMtYOy1GnGTnwlDcfY57hmYzt-th8ON9TL_oATNHYF5OUqQN7NhyIFB_y0VyaJjIJaAmUahLmfgRNk78pXd6-0i1b0i47BcM_MHIHPutXJWOZGSH-wmjk3Ul0Z0veNozPynGZuqCQUC-eXmQsI0EBPWl1-kX3lXHcZd5cbi_3S6wqpHyzgDrFW0O3bzGxwVpGFcIp3HJEBISCLQnsMocGjtY9J7UCwxpO40aQkCmqiJ1eQhb9zjYD_FHCjBHGb9k1AOrOwuqmUkSMZAXZJCtGF2F7YJoeMtzTgHITzS9F20-W2ml_vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyDYPJvH3e1C-_mzXHX6HubAj-gSrBt5jyZ2mIVxCRptcrowZIZ5CGRFlRsGEzmoutFZ0im2LGy_O4tqmA5AYdcWMzMEh8_EENxL6vOrfCaLA6Wb8SQebQjXklmRLFq883_Ot9c9pZp3rWF4c0Y4Kp3QTY3eGPIK6ox7YRqGRy2G8HJ-juBqHGO_0Zs04Kfd5eAycXnJbVJmAI2EjlJj083Kf2GGEsgMi7nF4R8YbPyIR52Huvs-uYREE4AWlj0tlVxMPdS6CKtbkqJ6wDKCN1aEHe96MJyw8xWcXwyDcOrScP957Cctwq91yGJDRv31pxbf5vQ9ncRFckTzHv1Xqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-XMz7qBGCMnUnPeYG4Eo72j7V0btz45e40kTPKSUznCJON1747Rk1jNziU3Tcx5j4IsK6VG2G3qxdi77Cw1eAAXEkjcgHoNrQQkzM8VbdR_gYndO04xWQTK9rRUFS6ForWXurChbsxCHsPYWTAWaCOZj9zWI51t2widXFszGcDCSbb2PTye1XIRteSLLxOt9vIUawmJ_QJYTA8PdA7dhrGsJiuAA1dgk2wS39qFj0BHbgdzJJT-boEK7T93pPtvouuzTW_kgAzgl79nyn25JtOrQSQ4SpJMOcAtLhYsoGneNwU_sxTc2Jon8OuieJeqYTrDPv1X4ivYFMrEfnrxtze4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-XMz7qBGCMnUnPeYG4Eo72j7V0btz45e40kTPKSUznCJON1747Rk1jNziU3Tcx5j4IsK6VG2G3qxdi77Cw1eAAXEkjcgHoNrQQkzM8VbdR_gYndO04xWQTK9rRUFS6ForWXurChbsxCHsPYWTAWaCOZj9zWI51t2widXFszGcDCSbb2PTye1XIRteSLLxOt9vIUawmJ_QJYTA8PdA7dhrGsJiuAA1dgk2wS39qFj0BHbgdzJJT-boEK7T93pPtvouuzTW_kgAzgl79nyn25JtOrQSQ4SpJMOcAtLhYsoGneNwU_sxTc2Jon8OuieJeqYTrDPv1X4ivYFMrEfnrxtze4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZGHTEahOs86-sKmO_gHAjaioiy_LQrgoE3_zU0VQssQ4LIqFb9T7p4Nlw4hl09yXQ9PwP2XCqFB9X73g1vAjaoiyrOO5hYFv8F3efZomLzBw5_ipDyU_7fZNDrm5vHdnKBDj7NcUZNwJHH0lh5mYwIHNkp0FP9j02hWAxBmk1oKCBRkHM5xr8i7ZwpJlZaSrCVCz3NgrcjTPdX6IgK5obbBTVO_zOFPmCkPcqgCG5949RCux_MDomMVmzgBEU6sE-z_Z-AhkVQWh8ytkHHUNB1K9ISkXz0bsnlLRO6UdxixNSZWVzPf4EdmpuF5T6__yOiDOILy2WjoSuqawL03fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6xJxxuVqb3HXYnFEA-2KroEb_jyhFMsOhrlZDEcawHWuXVgD97sAeyFzIWMqRj4umam0nweC5LtHiyUeSOWTwbl1eHWG7kDnfnrFKT4BK3oPhQjv092Pvz6zziUT9NABdAg0BLski4lbSQZbL0bkNzUwzJXqFpG8t99RF28ultYTq6XvJcY07AAZtgKVQlNryBNnKGCQ5nxZfWmTDlYEoINgqmm1qS86a9Vq9OmtcoreaLhqtyKnkFZ5mpI5IAxrRxE3IXeEzn8jfSCMrkpgEEQcukJqRAPxWsWteBWoN-bIgw5SwrwSr35KWaQkdLBQtYOXU27ESQ7aSiIZno8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fudyH6AarW2ALpbGS6Ae6aij7uECBUZpKEd9r0a1OO-0n2vHUokXSsoz-esGCqTjMucTPw2-EqTvHWApH04Y4YAuT2WOsUD-ae_SVIQ3-Z0xcBipNxM6XWf60YlgL20FRaG7AlXvwMkut2nJHIXBCTeZ_M3wTecw8hjEp3v-a_qFGOo0iuQHFftZ3voGebEqCUzLJqpE2u5TOuZEbR5m9sirVJ_adAu6vsmWcvl78CSjCgqqu_fW2hD7EFtdY8Aec3P8SOA4wMi_3rFHEAdp4fkQg9_aDzxgpyNOsjKQhzzevMazQEDcKbxrpqKErCamXE0cPTcVXJGkaArO9PJR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHL42SFQoXY4hh-7ibNhoc_GnpTROyQtuJAB4naylqw5hV8GUx8jhKBy8kKHvfBKZrCATdNN2j3b2dU1e1MbfzdORH30SzNQq4pPGm8pmIJl3T6-PWOx_7fbjHr8idyYS3DufGiwtwfwIsvidrQ_YKRgk0mh-pceyVyogVfwBnl51C8r14pFJm4vEQCL7JGeGdaT4sAja61W4l1rXr7kKm9uXSysDJakhHUc-xe_I_L4uKpnjrTp5f-ATiZiTTvj2kj7whAinFz0n1vvBR7g_HHwP-1MhHXvMOOgqhl4NkLpg2dVclMvcDfutigg6KC9tGIKWiG4oWhKRYrEPCpU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWDHKHN3CYjqj--WxQTMF236K6k4SPBwXnQ_a_J9A1F9ZqI9Y-Al2IMbAnzLfoaA8lOv_Qn53ab5V-n4fNu6uuKleocUO5xqI55UniM-gCLfITYI2vkiMzHk21J4eJHoS1HPPSvemnfy0ipanPkMbjAlYQQ2El_niGMWDvJbHVmJowE6li_bVV-GXXiTST6NJAmXFQZ9S0BU9qaTjC8fWSu3_6ag4lRbbEr6DVZqrITKlMiseYACAM8NvJ4enbNTRzdOuVp07UgSAoDV12Pgis8JAhOC_TCtXlHCHf33zjsF63ED2-qasq8BV2pDpUZqLoPupiVK2SnilcR3fIMWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sp7lk2OOYYYMp8N_WSJcBodSY7_CFmePYdwGIghry4dTM6u8WU_U4pUadfAPWFjgFqTR1RQma-ljC2YF9F2Xm6gZDZnkbQImvK9ee6SLgUNo6avdCzXDiGQoHgJ3zwFZrWMEz-oucUNJKfz9-UhdA4K56VolUeRcYT4bjGHH0iY2cBDH47YoFyAvJuPnl84d9OxIttNMv4UV_k5qrv-ERjI2yy9_yCeC9RVmv6XRxDS1FAY1liQRIMJVqLA7dSCx8NFvVyziX09oW9r37BPX3KyoZ_JEfxVn1oMYbbOh24-brgOEPRzCt2meekFv94Gm3RbMkqzFJj-OfkLtG4bRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=cnw7yV-2Or8EjyZB7JAq2p4NcIDFnwswTTsS68J3ZV117BvRr8d8vU9MwT-llTOaTurtkC6YsCRQUlIzc6OFXM6XhrgacP_vuXBeENIWTskIJGTxAO0y-MXRlNKlxIbjGmyt_DmITbemSqGYLoszVIf4C6HEKpLapePNeN1ukgkUFqDzC2Hy3xmuihQUo_ReEvtoQhpnQ8CKkOfiJI1aSNJHDaiM7786mEsLhPXDPk20F70Pa5OL4qsLke65gkHZKxl99NDU0HbkGawK5zL6dHKBBmpLrbrtxxUCPpV8nUmLNIzE05AwgL2hMgsixegFmFd-58_-GoDPAiAgnedlpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=cnw7yV-2Or8EjyZB7JAq2p4NcIDFnwswTTsS68J3ZV117BvRr8d8vU9MwT-llTOaTurtkC6YsCRQUlIzc6OFXM6XhrgacP_vuXBeENIWTskIJGTxAO0y-MXRlNKlxIbjGmyt_DmITbemSqGYLoszVIf4C6HEKpLapePNeN1ukgkUFqDzC2Hy3xmuihQUo_ReEvtoQhpnQ8CKkOfiJI1aSNJHDaiM7786mEsLhPXDPk20F70Pa5OL4qsLke65gkHZKxl99NDU0HbkGawK5zL6dHKBBmpLrbrtxxUCPpV8nUmLNIzE05AwgL2hMgsixegFmFd-58_-GoDPAiAgnedlpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdYtdVGEPl9JuBlMbUxv3Ybebw2o0atBEBB_TJEIVqmJQbcO79NNUINfJGZ3-cyfQkcKleirxSzTzKXvU5RKjo0v4b-PQ1L2V9TW9RTBdFvdwcAbMwXKz-UbEDwRp7PCtkY5H-BBEOsdyLXAHgVlETnL6x7dUi6bFHYil3upw1UF9L0hGA2bVwPyrm8ZxLmF6lQ6_rpkTuRrAQNQga6AUWRSXTvpeopOwakzaLe7-tVX39vFUJpnUnwdDDJeTQv1P89Bn8V7vR8DSv8BtZDG3sf_Kk3Iu2Yn0qoMkJQSjjAchIvCEU0Ja8dlYG-YghnQeVOegQs63xQLXemywJlDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz_ts1lm7i-mJU2HidiRFIRJk3dgOALrh4vL8qerFMPfOAZ5_zYbiMvZRC1VVIWnjCNCyxojzQjmP-5OJHXi4wWCEs1B0FnDIb5x22q_jeAfe657aOh_nsrqtPEA1mUGGhM01H7Ltnm3RaqSrwtMIIpdCQv7OohyfnL624gTUU97WweINyKOZUMJVnq5gG581zrEkiVshqHuAljd88gTtuBgjugf0yCX-K4a2evhTBptTu0t6h8bttIv7p3kNGqzOvHfxlr0Maxkq3jjrKDRDrjdO595CIq6lDU3kMAQBcTR2SM2dRG86M6nqJjtXrx-2vt8_Vk-qiemAk2kf2wa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrSDxCFw9tW0m-LRU0TiM0Qdl9Qog8bHE5TS165UuJ2Yu6pAveP0QZhO6Ps5frYIu90DErU1QukycPAURKMrr6S0CivlXuGu-zs29OL1MER_2X9UWUYVACfz16c5cP6PTCDn4093Q0qpQvdvWmHUPefENk6W_adA85ZWMv-zgrZHrpna3KfratpiMV8aw6QGlE9GLSeWgp17tr4L2qv0-RXRv8c2JNI_ORP8a_-zB2gV52C_OQIGLd9vOZ_cZw9J1CX_LUGi5r_DngMIQbNFPe9_rSK1N0ncH5ac4bjKBPdMvHw1Qb-DdLVG8y7AzsseNQBtny0_1JGCZYWDMZNoFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=BadPbMFZLwjI-wzMdgHQn5-6hctmaVP9Kdz4VTgi2quXqt7uSQmoyBZ0Pr5p6vLtRWgOVDhFoz73FsM8G2ErqNPhDiqUl5KDDl9s6nbGGds-BgI239v8Wmot1LkhIk5fG7PnsecF3uXWgubbKLvP_z6bGKTO9nxTGvrkQerf2_4spl7g0kgbhigsv1Q-1e0CTIzDjB89q9X4jtJqvUvfqeJFkS2PUZa_NFZDyaZAUHG_9m6sfL2IyjlRXhGlYJxsrN4RhM9y0vcnKlNZF3x9l5_hQCWmSytqDzhfWUeFQ8TlRD_rd3mTJdLgusnXqrAJbXfbQjhuuO-YJwKMSmpAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=BadPbMFZLwjI-wzMdgHQn5-6hctmaVP9Kdz4VTgi2quXqt7uSQmoyBZ0Pr5p6vLtRWgOVDhFoz73FsM8G2ErqNPhDiqUl5KDDl9s6nbGGds-BgI239v8Wmot1LkhIk5fG7PnsecF3uXWgubbKLvP_z6bGKTO9nxTGvrkQerf2_4spl7g0kgbhigsv1Q-1e0CTIzDjB89q9X4jtJqvUvfqeJFkS2PUZa_NFZDyaZAUHG_9m6sfL2IyjlRXhGlYJxsrN4RhM9y0vcnKlNZF3x9l5_hQCWmSytqDzhfWUeFQ8TlRD_rd3mTJdLgusnXqrAJbXfbQjhuuO-YJwKMSmpAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=cnIv5b-L8g8Pba3Y6QaoCoPaT8rNOEuvisfFKxnhl2Ni4v7YZ95z61l4y2bLk2WBdUAljs-Qw3LU1k9XsChwMgRctH31E8GKKsOAQ2C3xfWCtJOFWZYZHpOxAy3YK_2nYNJgpJAprTU5jcjnjM692NlsTAPjWUf4eMWvoLsHs5See6oWiP1t-qqcSsTATd8LfP2RReLHWgMlUbDneJAsbiiVrl5UHEd7lndQROR6_LMcSweDi0XAXBg6ZkeqE9qEgipygIx_G2v40Nmpic8T3CZkbLRsawdhV0kndH8ReIPrHboaxpJ4pLA5FvoPKOfps4O4CYrK5XxY-ovvWIeL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=cnIv5b-L8g8Pba3Y6QaoCoPaT8rNOEuvisfFKxnhl2Ni4v7YZ95z61l4y2bLk2WBdUAljs-Qw3LU1k9XsChwMgRctH31E8GKKsOAQ2C3xfWCtJOFWZYZHpOxAy3YK_2nYNJgpJAprTU5jcjnjM692NlsTAPjWUf4eMWvoLsHs5See6oWiP1t-qqcSsTATd8LfP2RReLHWgMlUbDneJAsbiiVrl5UHEd7lndQROR6_LMcSweDi0XAXBg6ZkeqE9qEgipygIx_G2v40Nmpic8T3CZkbLRsawdhV0kndH8ReIPrHboaxpJ4pLA5FvoPKOfps4O4CYrK5XxY-ovvWIeL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=evZ7gwP2lYVX_oMXJzNlzEOGJe7__UV0L-8NRooEtz8yVT0sKDLc16Yd80sDw-fAv5B0dtrmHaykj1W5MYJp0uS-EFu123DJOa4OFOVQzYCsOv0ECnz2LSwPkI4I9KjwI9Nh36tePS0X89woKLZ2wOFAOLTcBKkEluXYrCsdHtWeBNGnKIGMfxyhurqGCv9xQEJK3Y8WhroPtQ2l7ogjJDd0LL8gHKFcZ8aVwq2Vn6wa_VwREHJXtjB8wiU-zz6Tb9E2y5DbvyaEJD_NLA538Osp5H-HF1_FQdb3BBT7uSlTEGDKEQ1xLk1bMyy3_5ubnzrOwvf73mgTj9NoEaZzFSrxe1RPV2EbL9ULX4tktrWE1pRpfavMR3P0ygrqxJ_GkpeaRHOvwr7d4kHF7m_3Y3B22tY_1VEyG12Bv00kLWP6VRbFkDN_0fMRVCua92DQVuaOspedS-1fsecwh9A00o-ImTES21uPnD4aw-spmgNWpFRrQxtIypxwHihEKUeqX9YmydDjYvKXpaJPA05_zIUtqq0cbr4Czx_urntY12s7yIATHUGN48AptwqyNIdL-gzVokPoVFIYfAmHum9xWl7C_MV42XGaJ1-1iZbGeBaznBXxIw8BSCKmIsN-dyNqmR5aazPTC9_0nW1Ao6X0rhtzE80nb3CfdsN1atH0rFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=evZ7gwP2lYVX_oMXJzNlzEOGJe7__UV0L-8NRooEtz8yVT0sKDLc16Yd80sDw-fAv5B0dtrmHaykj1W5MYJp0uS-EFu123DJOa4OFOVQzYCsOv0ECnz2LSwPkI4I9KjwI9Nh36tePS0X89woKLZ2wOFAOLTcBKkEluXYrCsdHtWeBNGnKIGMfxyhurqGCv9xQEJK3Y8WhroPtQ2l7ogjJDd0LL8gHKFcZ8aVwq2Vn6wa_VwREHJXtjB8wiU-zz6Tb9E2y5DbvyaEJD_NLA538Osp5H-HF1_FQdb3BBT7uSlTEGDKEQ1xLk1bMyy3_5ubnzrOwvf73mgTj9NoEaZzFSrxe1RPV2EbL9ULX4tktrWE1pRpfavMR3P0ygrqxJ_GkpeaRHOvwr7d4kHF7m_3Y3B22tY_1VEyG12Bv00kLWP6VRbFkDN_0fMRVCua92DQVuaOspedS-1fsecwh9A00o-ImTES21uPnD4aw-spmgNWpFRrQxtIypxwHihEKUeqX9YmydDjYvKXpaJPA05_zIUtqq0cbr4Czx_urntY12s7yIATHUGN48AptwqyNIdL-gzVokPoVFIYfAmHum9xWl7C_MV42XGaJ1-1iZbGeBaznBXxIw8BSCKmIsN-dyNqmR5aazPTC9_0nW1Ao6X0rhtzE80nb3CfdsN1atH0rFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL4f81Jz4WDFE7-564KgOGLiREqik1m8YzgPtjil3uq9gQeWNdojkDDRBOsPhyehlcz2WjTVxK1KzmDr3kUVQn2ZlV5masXhgFLK-c84lnX9FgVmYCG27HomVg8ow_c9LyCq1G_bx8rzDsoE7JzHMb67cTRyBLc8sQbaAgr6wv5lUR478cijluSxcCwstGRk2zrz4t5rtWEhTIXEGz5APndmswMp31tEyYprVqKWiAz0p3JiB61Yxlq8bArjTVeKKp2C3exviy5Qy64TIqdtsiy5_8tr_9SgSotmYZ8NukpmHSrqrIJi_bwo7xneJ6w-kEh3Tv5S7NXsQm0MfDcsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa24BM12oE5r12KEC0vZIYsvPXMOMsWbADFegIdsgRwFE-iCH7S4JYk2ZK0o8FUtZxcekyqvCwtNSc9vMNYCe9UbiXczP3DdiMTYIwkvV8bMJTrvXk_eQuZXlHKsP3yammPL50z7iTHqGrV3n4fWG9PuRsMpdJD5pZRC2Qs3ar0LF6eq4lfcAlXmtDD77bI-OCQIGnj5Rq02xhh5I1ydT_-t-okSz_C0tAXz8pGTus8-h2GpHBClhTd643VMdhJnIh29jJSh5JgMik0mefuiQHPb9ScV_aqy9sBSlQ2QMsCuXGfapu5V-2bzELptLbXzHLSTzgLpeRidxOcqLV9WpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=BbONX0kHpMCEnxZtlj9Qq2naTS5gllO8tPzwyZsslRN_ih_f68DDmnDYND8ISKyUS-1aWwufjt8ryKct3NUn8jWVCdMzarLG9OJbS-VMnvIUnRKIQNPdzSsEa-m_XaHBjag3V5SF7S6UlgZmpDh2muNTkr00oUEfPNgjkE1-ZmFg3rOdj9v2P3dAXN7R1gxcYIxcXJJX3g-isSxG3jdoNM-c-X56nKz6XXC3qOI5LOHfxrXw4b-0Q_jUBo8Mrql9rg0aFFmN0cLw_SKkmLGDRa_r2e1km1whBWx3QBR3sVJiOpAcLgajVy8ugZKHpq5NCCt3Aoy03AkcD4y8V095kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=BbONX0kHpMCEnxZtlj9Qq2naTS5gllO8tPzwyZsslRN_ih_f68DDmnDYND8ISKyUS-1aWwufjt8ryKct3NUn8jWVCdMzarLG9OJbS-VMnvIUnRKIQNPdzSsEa-m_XaHBjag3V5SF7S6UlgZmpDh2muNTkr00oUEfPNgjkE1-ZmFg3rOdj9v2P3dAXN7R1gxcYIxcXJJX3g-isSxG3jdoNM-c-X56nKz6XXC3qOI5LOHfxrXw4b-0Q_jUBo8Mrql9rg0aFFmN0cLw_SKkmLGDRa_r2e1km1whBWx3QBR3sVJiOpAcLgajVy8ugZKHpq5NCCt3Aoy03AkcD4y8V095kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nur87x28vzA2pG3IzHyWpuDQUJOtonzg8dMkyjvOADWlowOA8ucKBOBktfV1f6442M08cpkwY183nD3AkAmNMTxi2nJ1zGV_C4oVxd933c52ZBy8C5bCff_tWqokSrHqKgniYshybbfYCTiHthGfl5ljYcyahIK24PRsYabak0Iy25R0jvbpFomZqkpDY_Vg9nZ9FZ3N-WeCO6kRbg57meT9RYDM_vtBVJ-iabuwxWnnZ8hi8iHMYsJ4uo70sF1dXB4DamGfFMZUT5Kgr4m7Sc2NSsa5G0z962krMt-d-DUPwoO8uuC0rioMNI_S0ed4hDdAx1troAkiJ5Hu8uZqlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=YpmhNZV8tB1d6a7XrB_HpPJVId0KgywJ8y3H102krVVFBzYvBIjSLoG3fRMewmyUz0uvI5sDf4RSANLKJld_zn4ZWSocqKC7lCJWA1E1YjPiIJ3yvPB6jPqKZQOAFlK6D3rnItnWHdVfGfxPrX6kGQx5ipNFL7krXO-y9U56fq1vvbDAqPuqtfxphzr8zK2uzmUj35vYx20o1Ru-fUGG9_k7ObujnqC4xStluh5h0TaFLL8tWz5fgear0fOg47GPj3peZHliTSDIqUAT_8o7Z0_iG0TEBmeBhZU-bqrBrCXC1yYU_CIfSnd2PdbFLkR5PRf6LQnM0_HJuo6oUxu1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=YpmhNZV8tB1d6a7XrB_HpPJVId0KgywJ8y3H102krVVFBzYvBIjSLoG3fRMewmyUz0uvI5sDf4RSANLKJld_zn4ZWSocqKC7lCJWA1E1YjPiIJ3yvPB6jPqKZQOAFlK6D3rnItnWHdVfGfxPrX6kGQx5ipNFL7krXO-y9U56fq1vvbDAqPuqtfxphzr8zK2uzmUj35vYx20o1Ru-fUGG9_k7ObujnqC4xStluh5h0TaFLL8tWz5fgear0fOg47GPj3peZHliTSDIqUAT_8o7Z0_iG0TEBmeBhZU-bqrBrCXC1yYU_CIfSnd2PdbFLkR5PRf6LQnM0_HJuo6oUxu1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
