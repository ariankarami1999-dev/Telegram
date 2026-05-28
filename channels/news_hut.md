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
<img src="https://cdn4.telesco.pe/file/DU2-na1WjWUc_h5KyPaiN5CZV4lQ2Xs6FneOJHQALp1Yn3RPFgJwfuziGqRfzEWKEty_iKoRFU_PtqFR-BknLcuNY11FstUuuMZvSM-szLVy8oPHYf0Gro6sAMro30qREdZ8dCNIIogTr-iARYUCg4FCbac21dDsfj9pG4HTaDI-5u1WHjAGgPvBod_rj6MdGJzEN8Nyx1s3yEsusTkNkV95YfscocmpwOtrhR9wPiqzVEHFc5EMJQl_g54o_jXXCybr5pn1lGRUmdBnDYVpsWxhZi8q8vvvlzH2HNQYnNQzBnQjov0QRYvB1jvJTKb5imHfnr6H36YL0G_Aa6aP0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 132K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 03:17:43</div>
<hr>

<div class="tg-post" id="msg-65129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/news_hut/65129" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvsP9UQP6Dx-u454D3kKAMIuj1rhGJHE_xjlGbtyLHYueI5FtseIWzxQVLiSTwRFDC4fPc7ghCA_cGx4LMq4kwUeBIQdVkU9JsZchhGRILWY_Dp3hRxmlI8L-BJL7K9uV3M6ZZaTp7foJgZkDAy_VScEfKacQYBwbjtaIBrJ54oRxuM04X1YgAGS32rDLIe7-IsgGUPz1BfugawNVf5E6l74zVHFu4SCZhDWozvGPG9KX1sbtXl5GM0hQgweFt6s2Q3OnAxiheQ4NkD-OCWEGs1WlPq1j0mOOQJKuQaTim2V0vrr9xsZ5HJyydVwB_omrPlxfQPYI7-BPz6QU1iT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a7
📱
@winro_io</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/news_hut/65128" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=HpV02fZ3KfxBeTGUXBRfeofCG8swHQeGFa2OWc7BzjU3tQSLV-SsczlzMAThjo5QHfdIqThwNkH1Z1PvtHdpDNni_gQDhDv0KcaY7vziCk7bBHvh3PlefEvxn1nglm_nQlYH-YPPobg5pGk3LWR4LbAyg9kqDwKDgJqM5lex74IxhnXYg8T-uz7Jncy3GWJvzTCa_WE8uK8HQRU_Lm4j5S3Sq6QKCjiVmQVCFxSBLvBZ752iucyUZKAkwxDhP_nd88JLqpLCQkWQexInk6_6XP9VE44NKUfK4OXBKoptUKJxPDUaBpYsURJd_fpTz7ZqeRuAjiPHKfTv-4T4v2r7Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=HpV02fZ3KfxBeTGUXBRfeofCG8swHQeGFa2OWc7BzjU3tQSLV-SsczlzMAThjo5QHfdIqThwNkH1Z1PvtHdpDNni_gQDhDv0KcaY7vziCk7bBHvh3PlefEvxn1nglm_nQlYH-YPPobg5pGk3LWR4LbAyg9kqDwKDgJqM5lex74IxhnXYg8T-uz7Jncy3GWJvzTCa_WE8uK8HQRU_Lm4j5S3Sq6QKCjiVmQVCFxSBLvBZ752iucyUZKAkwxDhP_nd88JLqpLCQkWQexInk6_6XP9VE44NKUfK4OXBKoptUKJxPDUaBpYsURJd_fpTz7ZqeRuAjiPHKfTv-4T4v2r7Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNoGNXmFKacu1SqPGVM5pI76dVNOKBIBJvuoujFHnGhI6MIqiQHVdvtOcyH2Sr0R5IYBWeW8YmDw51pbV-aZ-inhYMGNq6QfpNeCQ7Ls-oO3IVnMYCvgVdZUVsGaNxWl7mFTDkAGzMn6FZ0UNEOfE2fLCK1hbz6DDOZjwVkiF77f4-EpG53aB3q8VgHs4zdt7dq18oi3IznZqbRVPyO1CIL0SxhaKnA-lAAD7wDviGAdCsJfMWfzyvx1ZsXCI9mSHNFhJi957LJyL8TORHkTaXhiEIq2dGmamuqw3D7MpcXjNRpnel68dkJ8dowwCr67CM1eB76xRGVxjMTjsRy0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65125" target="_blank">📅 23:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=YIYEI4sua1fPXWSWmv07O-URVkU6H_Jc-dHidz0QDJaKhAxzoUG0wwgWdRLIwV6eqoBXSu7ejs7fHJfjaEsZi_FcR4HLNpsu8y3SXZhiJnyRXaMH73l5dUFegIYEFW0im6_G-4GnyFCLFXJxgG3KnHj9X39tO85xmgbRoTZarJOBYmG96fqrswrYfRjzQOnj55z93329lN8MYcFjAgVQZAYV6ezH9FGs_KkP8iW5FSYZkKlp5Qi4V11Pt0u7-3w-V89YZTFBsBgLjSh0qqk_aq48Nio9vkK7nPG3OECl4956VDyZoC0y0CPQvDu57v-wVh1OQBfILYFW7vmAO8ULIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=YIYEI4sua1fPXWSWmv07O-URVkU6H_Jc-dHidz0QDJaKhAxzoUG0wwgWdRLIwV6eqoBXSu7ejs7fHJfjaEsZi_FcR4HLNpsu8y3SXZhiJnyRXaMH73l5dUFegIYEFW0im6_G-4GnyFCLFXJxgG3KnHj9X39tO85xmgbRoTZarJOBYmG96fqrswrYfRjzQOnj55z93329lN8MYcFjAgVQZAYV6ezH9FGs_KkP8iW5FSYZkKlp5Qi4V11Pt0u7-3w-V89YZTFBsBgLjSh0qqk_aq48Nio9vkK7nPG3OECl4956VDyZoC0y0CPQvDu57v-wVh1OQBfILYFW7vmAO8ULIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65118" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2tQV-lgxsA2oY2yJ_D_r-did-9be8VQFHBWxbx_qX-BjAe--TvujKaPYUhxrNGmaQuBk11ooZnYHqXHIW0snH4KhYFqWQGsAPi0DJ7GdKr2By3VOeQ5gUrN5vm2FSdAx8Ka22h_ji5b8xIjmEnNpogZeiDdxG2WO1omkkAyx46An95Pip2YgvTyp3aNJ84dLTDD069zWXhAJ7V38QGa0uICmX5pExKltmtntfUdZHRd8pIvl2zyn-Ob84gQLhJeiI20WOgLMhp03DY1xcKFCI0SgdNqoHuzAAR2rzBVucjiLIhdX8t9DdT99IddHLMauwViFh02EZqwsxrkdUtj5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65117" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhvUhalEbSzvEkA92yYm_59-vnWPnL-iylKamg-dSPifr4MGj5OEX2JSE-ZBM2ezKVw3i6GkQ7ccLU3ydeQrxbUUdd_mexQgTa5HdmfPQKmuZP3L6IDkPBz6okw2AtUW99SfBh_eytLonqI3c28bzssRAiVSj22KbQvobreCrRlIy5ovLTI5N41QgPS4izIiaPiijhGyhyrbo2liUCw5dy2zkHC072g45ZNiv2_3NEtSKC8vjhPAUyLVuKIE_PiIZXd20GyXdEkbHZPZFoH6w8dcMUFi0fprSnLIOp2Qxpq2gZy6U_8Ek2N1EugeKWtF4kKSG-dDs6-5MjAVWYIXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbGAXzDzNqJhpVmjsKH-nEbvcw7tVx7tIjPqajVVhw5_uURbRYaSplgkoH_YdyHL-Smar4bB12J7yWane_WwTjkj-pze5W_TSFsDBF0dfhwRt5yH1yFeNAAWifngBohokcugdVsc9h6bsDXmnG8NFzi0I9BONWce8SKvJOWA-BKc_xT87ggKYS5vVGKzB2lPbPJV1CjaVOOU84KvjJSPHzp1h2AaQT2ZeGCSXsf1AFzODoVvv6jmfAqsyFYzksrNps556cYHHVsfKuDNGCMELbuEAwd_HMqw4_aMBtHbFzo0Pz7iJlgwTo8E5HtyBuOpnKDyW4DHs8eOMpwFfhcSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fKaBv1jxVmO4oNYsfVUaCRP0jwUIGcc17LWpqAY4hkeMcsPqIiJ1fgugG1SX3ddQuOs3fSbGWmgwF5Jyu3mNXBdM301lAmk_-jPrzywuHXetY6jPBhwWhLoP7ON2N7Rs1ngUlDQGcod6rjmy4pGU4-X1VpLHxzzvIGMv0mqhFkhv7N_lB5146bQYxy5af60LP7bk5Wy0rvjqOMlSwwtK71KHrY1oQEqn0PMeLGm7YAavz3iEKGw-8GZuuS3BVgVT2QtdTW-KOuHnxFkAe42c0AWQU_LJ20hchjfYOCJcxsrBuwN9MZXbuY_r99fR8cxhkA5KQH-uZz6O-ak-7-mISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا پشمامم حقیقتا ریخت
✔️
➡️
تبانی نتیجه دقیق ضریب 15.00 رایگان
😳
10 میلیون ببند 150 میلیون ببر تضمینی
💸
فرمای تضمینی و صدرصد رایگان
⚜️
🌟
https://t.me/+BDjkK6j2gcQ3MGFk</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65114" target="_blank">📅 16:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR15UxL4V-kYmpr-sXQs0Bg-uSh6QpfJ0ygnS_eBTROcKu1835FLlvFZitYM5AtWzw8iLw182epx5RthX2qIF3Qi9HdCf_LhLa0vDgnEuBAPnLx5IUEjb4d_wYbv0dLmSycEWVHrVVLMldFKqijBlwmg6ZCkcdQTpEakj53-iDX4aQ3PeGzq_imoIczdvsxrQA9JobE5aDO__LQnHYTf2D-8nT1sa9yeatT9AxeQqoTwshect_XiQ_qLD6-dg5wEmxn6BaIZFHdjlE0U-ntiZ6asGosmjd8uJcnIG7jre32EQgnQqoYgRKdy3ygett7Vl1tC-hdAcP0E1V1oEt6bFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👍
👍
#اختصاصی #وینرو :
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65111" target="_blank">📅 13:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw8ni44abXblgwQAjbVFIBy_RQ-GCks9OdcxG8lOwPrWAFxw6e0GzLPukuYJg8Z1oTg2Xf6Hb6LL8lJiRaUzOJ99xLukZ8sYd99osKYV2zxqClfAx_lWh2JF8zzM7gxEjn-CWyPysP_jjzPQbwCCKIEcNROcZyKNs_0EBc-XES8dit4jLVvUR5_T2a3S0TksAzx5vxrm0hUErG4dKyMBAaZlCJGKTKV5QQQf6BBGq3cO5u9qzSz5Qvo4WSXMh0Sfvosq0xOvFlDa4Yxk1RHbTZf5aj5ccM5VgtIYKLPYYOFVBoh4mN2XNyu0vdHvlH7d1ld-CHEDArbjazocZqjUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65110" target="_blank">📅 13:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsVQpwxkSeoN-mkU4jS6q2D_UIGaZyxjgFZoWbE_Y7CiVRCm0FCmf8MBic3d9CsUWtFIHSf-7XEs7lzmHn2-JPHSyvukYGgBMy5XDe4MlyXpnJqeVFfwurY07UwYEjOFrbbdlA9r1rQ6fKRwpVaOjDhfIhMJOL9ilhSwNVZLCkrXclZTEKtPYIIjALJHXfBdEn0GjYLNh41hW2_7_lt17OLaD1eDWSuyXgHiczwTpjcA9zvnmvLNT7ha-yCv2r2beSIAAsYIk3jkGJXsCgUdKxKlzYA6tPpXaybHmC9KTaHIUHIx7b0o9OtorCswAZ_aqZfET1iTLBFaAU5zGQoebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF3LqSucpx2pnQiXWpHlEOM97g4hVRT9r0rCAM-Rh_Kyx0-kSoXM2T6GSP1WpOtN082cJcVZmRl9IQTF5j-BKa5FLYiM8WtpYtaTX-VZeai1Hh8usdPuZC8HE5mrXeV_PfLNQhLTq5QpVquUtTI-2kFPB4RyRrCb_HPNt72p1Q_Z62f5xOMT0lAgIlIjU38EC3yy0zHcEU1IlsVkZ0Y5W-j32DsHAixjvdkl5fIY7ASunvEykljKpghEfrzH0Vtn602liTQUXa0GRvHMz1jUyc2nwFfzbqCOroOwzedzbVTGpzzlheBdKrkePI6zuifOXFBKIegdmQl1-THhiDFVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYWT4w_RoMJGBU8KgFHZjY3vUzt7TtIjxYAOeBT6sOgHqkcEhRIohGVRqNs6OA4M9XTGOoFXsjd8AvKUwe38H4Z291N6AYZuCPWl44X8kKK4q-sKy097LtSIdgC88IAavT4BzdDifyTmZ59vo3YcBnPtEn5aHA83nvblJ_gwoU2_mGNhSpS498fqWNuNKjsQh-p22Cy9OT_hqF_LD5I9OHJdzd8UjOKs7nwAu9atEahjCYnHdVMWsG4d_brXpqoPJFwBdXh9rfiygFfTlz1dKoXsyDj4Xt9U9z7Q_nr6lIiDgbHkCUEVXPAu09WohhaTewSvJhOIFOL7S_zweaoDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBbRCf2u6u5-m7pYiNCR3PlG4yEbIRuxQSX14O94NghS2-mbUgDRXGLLPXgGtyd1xDc4UwhKqof4wNJBLKMWAhKF3OlypeZkOUnojdxZA3QgArndfC5ejYIsL8mqVXmn5qB8QhmU3U1zh1n0B9WXKMCJJu-AZNKpu0Fs6D8K3ELgaNrJz0ukLkCmZWOu-S8_PGUIbM-D-a-_Q1YDNX1kzn7-3flnpjrAl1p-ZxrblpDUgyF0uID3MAvox91xGOF2wshrBtENPV68CXLdBumWMD3N0Im3xBd_O03GurG_Evq45-9VE9d-esdIYa6xFrs9I3ylDj0vqS5UoH7D_TD_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2JtiYE50QE-kFXQXaFrw-Tictnqv_TR23lWOy9YnoXbKAw0GAhGgFbaf7na4vZT-zLqViqYV-PJC5b2PX5PR5SfwAQMadYGE5yHMaaMG3IJ4F_VAjqsMGNWoohzsdpuuacKBdxntqxRbsOR4BHGeu70knENZ8o-tbGVYj6g1UpNNLNy34Lb91XDeTWQu7qPVkAj4Qscz4HdVChke08zEgZZFLWVtYE4vJRYXRhV5f2KRkjGfrX7wOtSlcNoopr97gffVRWfuR3s5YfsKNIM1daMS3BuYBN8RQ6pJmy-fqoQAuerrD4cIxzj1nErEgEsixdt5zu8WOY0PvDkRcpCPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-text">Barko VPN_v2.0.apk</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65087" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65086" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=sNVDkU_d2J8WWkKrxnTnLxsIRDK8ClklPDyZrsKYqiJkTXHzH9tSeq0VhZy-qfrfJl36zWyQRdr5-IdQpX0KtLUUTWrABtB11z1VBWcOdtaLyTcwOWXLjRsePOWTKrKeptPptedLXgwZxzO6ohsDSlKi6An_GCMSW_ROYRzGGUSEmyylFqrqQZSjQkvnwyk3jZE4y-CdNefzLJvfNWSu93xLFRD_GvTBU4NyX1LKSAhkPtMVlkgI19Zd_0iNN2nsz8jCxh7-_WmKxDpvigmhuulcR0bDhRS_edchR6FncUgfv74tt5h_C0Qc_Y0teqc-NKCHxfobGPMlt-Ny9lZWvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=sNVDkU_d2J8WWkKrxnTnLxsIRDK8ClklPDyZrsKYqiJkTXHzH9tSeq0VhZy-qfrfJl36zWyQRdr5-IdQpX0KtLUUTWrABtB11z1VBWcOdtaLyTcwOWXLjRsePOWTKrKeptPptedLXgwZxzO6ohsDSlKi6An_GCMSW_ROYRzGGUSEmyylFqrqQZSjQkvnwyk3jZE4y-CdNefzLJvfNWSu93xLFRD_GvTBU4NyX1LKSAhkPtMVlkgI19Zd_0iNN2nsz8jCxh7-_WmKxDpvigmhuulcR0bDhRS_edchR6FncUgfv74tt5h_C0Qc_Y0teqc-NKCHxfobGPMlt-Ny9lZWvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbuCOetczu70Xdf3SXaBleu7Yw0FNfBqHLewg3Kc7xECFwQNcikjT8vR589vfI9QqbCQ3bWEQz4H1uOJdrercKiHyNQCgglIEw8KxGKH9SV1vOhFIdcdME2UkmxUdnEeV2rhsEmXI53-sq0TvGwEtLVzuhPJhrLf06f8BWKZiCNN8v2sPJDoKII-xcQvmD5XKZKt40PffjwzPS387F2ohnb4QgIjnEHBeeyfhsxUFi1EY_ODItLfOwgDMj4j_kiOciwHw76UpeBK4v7USRfXK8S1smTskl3TRFiGfQMpnTxkfa2WyfgqfdMhOEU70TnVRsCmRDA-ReM_5QW3JEcv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGfM_EPZT2PUrgVrYXJhXhUnTz-XoXCBh34EqElcO0XgDti1UGer9kmQVL2Ie2Aj9Ib4A4lv7gBBkQhW61jFsVfd8l1bnNArUyvZKRp360akDlizXAnejLLF-6pW4iUXat-0C8FxivGFWez9Cau5-rhDb-zrNhKCExhSPmIYT5oKT_A3CYxEYupMlPHjOY8VGmCDSMSkOVlEhzx7Cr9N8OPuh5jx0lDzMGE3unWcol_dk6oG0IPyTO2joadEP9oI2clBDNsVjQi221_vAE_f-UmAtgVDDPHwGWIA8JDQrhft6miVVmWyf8VNaEGx4y6rpW-89DQ_xaD2F-e7qDlUnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBzJBN0lTXeRr4K_HFOKxL0TuP_0XdBOLfhjnNIb8dwoGfF9RoeSdodukR7F_e4kFVf6dhc4chmtOvuLPZjzLgzmqVwFMdWx88aGPzBCig-o7aL1aYzqqEAzOadv7w0ZrVAO7HrzM4eb2UsU_W3tuYRs4HumgvUffkdRx0Yq96AwPbO2yVbwGNea3A1V-8u1sdFoLg6rb-ihzSFP4OAs1Aiudqa91wjfusG4e3bCuDZs-OjesF0lDngrHLwxnnyPx3nKet36dY4wqWelINX3_sWL1wBdY0KQ3-rHciV2tdTnA_55JSZxvMYo9pY1ZLRy-cl5ciodGL9ByJ0jf3yFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65074">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65074" target="_blank">📅 12:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65073">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=cmhfYT-6ZzPa2728FG_UBshzX3q6I6CFK2UirWxWvtYPgLQpENxi3f3dC6M0Vt7y_8sPY0Q_8bxRlWg8JhSpgCkWgB83ciGdFGF7y_f84u1-1OIlNM4BcC10252u3wYL1vFG21TDwvuBUs6TJ5aXMRcHNUbbmmtfBAh_VpcDleUk87RSdpxIHT5H4EWchhbnA58idKA9PJhUayti6qkgZIV-WMGlUXMum2w4AKVkBpbqhovYa5ihBOmi2KTUSCHl6E4F-8gEVUyRg3YqwLh5PefQ4RsdIG-UeYcs_w3CqHaZe4tv09ZPqvjuG64R08VDa4_RsQ5JItUzaZslkQtjFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=cmhfYT-6ZzPa2728FG_UBshzX3q6I6CFK2UirWxWvtYPgLQpENxi3f3dC6M0Vt7y_8sPY0Q_8bxRlWg8JhSpgCkWgB83ciGdFGF7y_f84u1-1OIlNM4BcC10252u3wYL1vFG21TDwvuBUs6TJ5aXMRcHNUbbmmtfBAh_VpcDleUk87RSdpxIHT5H4EWchhbnA58idKA9PJhUayti6qkgZIV-WMGlUXMum2w4AKVkBpbqhovYa5ihBOmi2KTUSCHl6E4F-8gEVUyRg3YqwLh5PefQ4RsdIG-UeYcs_w3CqHaZe4tv09ZPqvjuG64R08VDa4_RsQ5JItUzaZslkQtjFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65073" target="_blank">📅 11:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65072">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رهبر سوم جمهوری اسلامی: سه چارتا جنگ کردیم همه دشمنان‌مون رو تا ناموس شکست دادیم جوری که ویران و حیران شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65072" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65071">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
رهبر سوم جمهوری اسلامی: پدرم، علی خامنه‌ای خلف پیامبر بود و بعثت الهی یافته بود(از طرف خدا مبعوث شده)  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65071" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65070" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65069">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D1LGSbhQ-P4a1ajcUZnDZoWBQKwgU4TjCym1SBquagytEHL0SgflEmS5fQhz9Vc82GbFni5BRZG1xPZF8Sc91Lal-sOAZ_5BRupSG325dbv3U32xRORYOWqeaSWrSWzPeh6MetmBvJXUJI7Ar44nkb8pot_GYFxMIl6UndzjYy-VhPbHJSij2ipqAx8NxFVmq1c5gQLvLFK8xlHp7ovFWKy94OlAAiYE5FWMuvn0RBO-k9QiReCIsg7gcwJ85VPGujraYPErKnzfvh10qYycUULUa-jmjmzoEjqCOWkuomBd3PHImAVEtODUaPoTzGjfoRSXkMbaf1wtbpwGS_cd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65069" target="_blank">📅 10:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65068">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jy0yADTAgMHcMWCFYIHUQnNaHkhfEzuuMkeFGGXTlG2cHkNTuV5uFWDaUr6ZQ-4oEIXVt9tLGWucd67qHUH2JYnoQhnLQlB7BQk8F-ozF4CA_nCr5SQXnsDq4Dwf0XAU1ZXbSxfIyw-s9U5Uz1OL-xmOhPqUHeoxSv9a6w7Jh9mFnMl31ddoiyiXt-pnEjwDpIaSK8b-LFDSMYE9IpQCp2RtoUlLrcAkO4co0AH8gL3AqRpxsrbHTHmLynd4ndecbpiWXlnjlCS5e6PLmifROU_KfxzVteXwrwWPaW9S_OQDaWLzHeg7bP10tnvMbSWxx8dCflifLna-BxOHqM2m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65068" target="_blank">📅 08:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65067">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QYkg7P9ZZDJOnQgwzcz53gkfKJwOIjNcX-ERW8XRLkw2nTPVsilRVm1ayEtrBXvRekA417m-CZUSd6mAXLU9EEqOddsqD2iEGoRQEFq1cFN9HCRAHY1EY5c9Qha8CYkZWSWn1U-wx6pNQSaMePRS7BgV3JyJZcqpognHYDDgwn7Nv-n-0RYNwM2KlPtMIjJYPPPSV2jkpZxnK7OXqZGQ0UH5TqtiUuV2nZ1PrLN7b0r9f3k-DXErgcFdEz6NkbDdqBcKbhHMWldUwC_Fn5w8lSV77Zo6-GnmGahRfK6OYii61vERU3KTbSD0oP25G3pJPYHwb0IPsVl5Z0R3EJfpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65067" target="_blank">📅 01:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65066">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صابرین‌نیوز: امریکا دو قایق تندرو سپاه رو با جنگنده زده و ۴ نفر هم کشته شدن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65066" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65065">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPMBePeICv3H3OR4TKXDhfgtCw7K-blfi3y8pX_AohqvTxc2dFLRv2ep9sefHt7qKyWftHnWiXjREJWGAwxSeBbKuK0LyGmey6Io4uAJrYchaQIs64oJJX9cS44yoTlcaYmc6iw4WtsrsQjHlz9hCxX52_1IM-eJ4n0PzX1ezN4Mr4l2jlOJEj70oadnNW5QvAjc7L_7Ca-2f6FH9DUBJSldeef8zx1FTnY5JmPki5n9eeWZeRuBndnUZRvyQ9j5OKf8bCAWZ4AQGUkrkl9PAGTBg_tnhQfFy7l3f73nc4p0fA1Qx7XCcfifcpboq2If3dZ-eYIuT5Q5ZYYIsgyeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود.
یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد نابود شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65065" target="_blank">📅 01:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65064">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65064" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65063">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ5rXl82_ZEImX5c5UGYKbInTKjAvhQpdQQx-370neRw_Jgbo8SG_q1sSng1PdJC9BSVCJbPC_w7IT_wjY7-kmJwwVuAWFRodwCC2EPUW5OLHnqG-M0SxU1dmXoKLc02fwm7e9Jj3cULuhwUWdMgeS3SrgZoNf_AY3ip-20AyAaLrCncLSLcSSZOmo1zYwz6kF85AkgcxSJDboqBtQnbGMtPk6aZPbvQRJ5wmKuExEVwAKc4As5Yv_hbTmYfa1UDSfg-oQLGu2resZQwcuMLvqDf19XFWB5RDWldCEB6tVMTKv9yP8U2gzyYmMQKrVTiTSXXqEgPVTMCcrjhSV2r4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری تایید نشده مربوط به انفجار لحظاتی پیش در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65063" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65062">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65062" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65061">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
📰
آمیت سگال، خبرنگار شبکه 12 اسرائیل:  ایران در حال حاضر فقط حاضر شده به توسعه سلاح‌های هسته‌ای رو متوقف کنه، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65061" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65060">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به صورت قانونی، ما یه "شورای عالی امنیت ملی" داریم که به "شورای عالی فضای مجازی" دستور میده که به بقیه اپراتورها بگه که اینترنت رو ببندن. به صورت غیرقانونی هم سپاه رو داریم که زنگ میزنه میگه اینترنت رو ببندن. زورش میرسه، میکنه! حالا دولت رفته یه "ستاد راهبری…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65060" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65059">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترامپ: من به صورت الزامی از کشورهای خاورمیانه درخواست کردم که پیمان ابراهیم را سریعا اما کنند تا «جمهوری اسلامی ایران» را در ازای بخشی از توافق پیمان ابراهیم داشته باشند  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65059" target="_blank">📅 19:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65058">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ترامپ: توافق با جمهوری اسلامی ایران!! به خوبی درحال پیشرفته این یا توافقی بزرگ برای همه هست یا بازگشت به جنگ بسیار بزرگتر.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65058" target="_blank">📅 19:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65057">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇺🇸
تروث طولانی و مفصل ترامپ درباره توافق با ج‌ا و پیمان ابراهیم:  مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است! این موضوع تنها یک توافق بزرگ برای همه خواهد بود یا اصلا توافقی صورت نخواهد گرفت؛ بازگشت به میدان نبرد و شلیک، اما بزرگتر از قبل و هیچکس…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65057" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65056">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65056" target="_blank">📅 19:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxKkjhkzKJVI8z8bFBz-gTmAR9QtfrL_WJdLOU1vM9C_DKlMMRL2Fd2RPFslrNkRtdbiM6V3-974-ztKMHmk2CqrDNHqWz0zuBl7afOHuB6x69oleBhJ26y4BniPEO5j6j_5dL2wFPY2j7ySm4VM7Suj0RsnKkj4qdQdfgE66u5kmc5AV69V-TVprErVnDRZE509yYhV80Wmy30In79OJL0YQjCY74AP8eonUw5-ZSgfTKPjrRQIYc-icUJvtW-NLI01mnkJ0x5IqwCxrq6URrenhyLiNN8zDvzQ_apb9Lv_TZTeWuBFGPygKIR-vb0c9vgssa6w4feNJ_TrDgV57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم  در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟! #hjAly  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65055" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65054">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم
در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65054" target="_blank">📅 17:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65053">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چه افتخاری هم می‌کنند حیوون های حرومزاده...  سه ماهه حق طبیعی مردم رو ازشون گرفتین و الان از بازگردوندش، دستاور می‌سازین؟ باید رید به سر تا پای دولت حقیر پزشکیان و امثالهم #hjAly</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65053" target="_blank">📅 17:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65052">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65052" target="_blank">📅 15:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65051">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65051" target="_blank">📅 14:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65050">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJLwzElUS29d6uoEkJlKuxMYVlMIKj1TaKGeNHcvYX6bRmMwoo0EFKruWvzWXcx6TyCvTBMr6S04_WDpF52yDF6cFj-xX-qoFoUPNXcbWxuq7S_airPvhr9W0caKIwIf0SjHAdiGWRv0YUse0_WAO5fHuBQPVVKQTQzofk5CKE36_d1aePmXKqvmrHux7RIDWw_CGrVZwKt-36mV9DwlXDm0XWQIsYgF9UyPH3E7-jMkuqGxQTsRBC8na6F3BtUORsWF14-ybu_MjzRs2xxhKXxFtrRg3N6OjNOQVWGI7weuRZ5EDC7dlrgD0XRnOjvTQuyyRzG6nSKfGCUass7Feg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65050" target="_blank">📅 14:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65049">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=iLMODrjE3d3eulJVDmPe7iWEh7qUu1dUVwICxTrFw3tG6O8og5tE9nlZDhiS9SOl6-orHbNeWGGmhlYzf1NXEZUOVFJ6eElpwaBUjGk7GJXoDeAFmu5n1nVzeaRi4Xk01ckepYIT00FJs0JEOpHw7l7ffvwHhQwjkcsEckGwtw74TYdNH5e8wD1WkaWt53dZytY4tFOjZ8YLmxr2yNDBdV27vCALepVxOJsrlFthhBhD_rmJGS5mj2hMTflTeW9VXA-TJOY_dZPB2mwkjagAukIP3EkL4zSMHyMG54BePJxt77QdHU1No_C5Sw4BtHZNdkVwNEtKPBAwRhsfMnLCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=iLMODrjE3d3eulJVDmPe7iWEh7qUu1dUVwICxTrFw3tG6O8og5tE9nlZDhiS9SOl6-orHbNeWGGmhlYzf1NXEZUOVFJ6eElpwaBUjGk7GJXoDeAFmu5n1nVzeaRi4Xk01ckepYIT00FJs0JEOpHw7l7ffvwHhQwjkcsEckGwtw74TYdNH5e8wD1WkaWt53dZytY4tFOjZ8YLmxr2yNDBdV27vCALepVxOJsrlFthhBhD_rmJGS5mj2hMTflTeW9VXA-TJOY_dZPB2mwkjagAukIP3EkL4zSMHyMG54BePJxt77QdHU1No_C5Sw4BtHZNdkVwNEtKPBAwRhsfMnLCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد نگینی‌پور، مستندساز حکومتی مستندی ۴ دقیقه‌ای از حضورش تو پزشکی قانونی کهریزک منتشر کرده از اعتراضات ۱۸ و ۱۹ دیماه‌،
تو خود مستند حکومتی که منتشر شده تعداد بالای کشته‌شده‌ها و کانتینتر های حمل جسد دیده میشه که جنایت خودشون رو به کار دشمن ربط میدن و ابعاد بزرگ این جنایت مشخصه!!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65049" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65048">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65048" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65047">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=MrZfBi4n_aKx9kXcYMaJs9ahCRk-4DV8jg7K5lsn9iYNUItnEjGjNrxLCWgxltGkAOAeEpL3vjosnCx9SXo0H23RnD2CZz1zLODRQ9nDffLHO024qb-sRWXV4qfM9bwbTO93KvYPnyuDJtAvakx8gzBEiL2xMzVJNerjR-iEEEG7UclUoPmI6cXs5IF9TEhvZ8Z65Vi2owwSan9FPRMapFfL-BZFYuwyMKuyOZAL_X6vYTV3L_nAmSjtLbVGQtNlZMip_1tdPXJ3lq3NNr8CwU2ahVuc_hnmh6ejGQReanuDFmHw6_3AToao3qj7IAvlSQ0ohBnNIg7XLL8fLppYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=MrZfBi4n_aKx9kXcYMaJs9ahCRk-4DV8jg7K5lsn9iYNUItnEjGjNrxLCWgxltGkAOAeEpL3vjosnCx9SXo0H23RnD2CZz1zLODRQ9nDffLHO024qb-sRWXV4qfM9bwbTO93KvYPnyuDJtAvakx8gzBEiL2xMzVJNerjR-iEEEG7UclUoPmI6cXs5IF9TEhvZ8Z65Vi2owwSan9FPRMapFfL-BZFYuwyMKuyOZAL_X6vYTV3L_nAmSjtLbVGQtNlZMip_1tdPXJ3lq3NNr8CwU2ahVuc_hnmh6ejGQReanuDFmHw6_3AToao3qj7IAvlSQ0ohBnNIg7XLL8fLppYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم.
ولی ترجیح ما توافق خوبه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65047" target="_blank">📅 13:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65046">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قالیباف دوباره به عنوان رئیس مجلس انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65046" target="_blank">📅 11:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65045">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akSaipjkhYi52-kta1hUZA3FhfBg1hGuoXFrD211WJsCoYjw_Ez18RhxhM5dIavmIdE6Kgzas8AKh6HrxWR1inYNBFKN4ySEjoEvwYh5M8_YqjuslEqt7BfpjcKY5MuLi_ABw6Qqt1V_qwYGSxFmAs8yK-PWmXme5JSRjinYwutfWtqidywBuFSDwzB4ferPkaVAUX8gT2pEqJ8mHc7ovu782gC4n08w3RRtvd_3pGL-H2VeCFaCGpm4VIeKkFqHlPrxOvdB8Ar9iYKIf5jlOf9WoqwrJJqo_DJvM4D4TdkUvDsoFCkelGsmBPeV_3-0pY9WFJdXC1iaOo3hmRmu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج حقارت ارتش
ایران
به روایت تصویر:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65045" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65044">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: توافقی برای پایان دادن به جنگ علیه جمهوری اسلامی ممکن است «امروز» حاصل شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65044" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65043">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام: اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.  پیوستن…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65043" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65042">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYv-9cmMZhL1z4mdnvxLA4a2m6-oHfdPj7StpO1ZGLkWY5wF3cDD6T0rZuKNxIvlBFmNJ-fSE_58wytvjJF6KStnC6QuuwiuksLmv_5pin1OMsuizYse8x38QSugqxor3WPcReyPr-ingWlEET3LA2wwZKaSaL3vy3eIRIKBo-_y1BZW6S3A-HRB2LgFMco0mqUS25FVF5AV7tOZtJ8LSD2BM_jdp5gl5zYngZlT4evRVEZh_9ktkrfjTgAd3tY7u_F2ikgd9Z1IXXJztaSL8NKsWeNC310_6mXyZs-YMIVx-vFoK2AWBiWoT0yeu0juFl0IA3prUhN4HQ797d0zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.
پیوستن عربستان سعودی، قطر و پاکستان به توافق‌نامه‌های ابراهیم فراتر از تحول‌آفرین برای منطقه و جهان خواهد بود. این یک حرکت درخشان از سوی رئیس‌جمهور ترامپ است.
به عربستان سعودی و دیگران: اکنون زمان جسارت برای آینده‌ای جدید در خاورمیانه است. من انتظار دارم، همان‌طور که رئیس‌جمهور ترامپ پیشنهاد کرده است، شما در واقع به توافق‌نامه‌های ابراهیم بپیوندید و به طور موثر درگیری عرب-اسرائیلی را پایان دهید. اگر از رفتن به این مسیر که توسط رئیس‌جمهور ترامپ پیشنهاد شده است خودداری کنید، این موضوع عواقب شدیدی برای روابط آینده ما خواهد داشت و این پیشنهاد صلح را غیرقابل قبول می‌کند. علاوه بر این، این موضوع توسط تاریخ به عنوان یک محاسبه‌گری بزرگ دیده خواهد شد.
رئیس‌جمهور ترامپ: در گرفتن یک معامله خوب با ایران بر موضع خود بایستید. به همان اندازه مهم است که بر موضع خود در اصرار بر پیوستن عربستان سعودی و دیگران به توافق‌نامه‌های ابراهیم به عنوان بخشی از این مذاکرات بایستید.
دوباره، این یک پیشنهاد درخشان از سوی رئیس‌جمهور ترامپ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65042" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آیا دونالد ترامپ، باراک حسین اوبامای دوم خواهد شد و دستور آزادسازی ۲۵میلیارد دلارِ جمهوری اسلامی را می‌دهد یا خیر؟!  بزودی خواهیم دید! @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65041" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwr8pTKTWaLEKuB9UAf-3BsBtRwyPFDmrFTJ2XcZR1vxZCyrC3f2cGuTBePAGVSsv_PrONGevFyck7oIyWmT2b0ZfsBdT90TlTC65PfAH2qQd9OTDGzz5_vhg5JinTIcDgkJiQq9QL9Jv44CMvkURVAsSdiyb1dE1vDeUFxtJ2PPDuLbmecAa0yuaF-w08mxz912qtGXx0aW6WGoK2ijevYBb7ScuDxTlvCZ7-jiOT0wV2Pawidn4bQzlDRTl0nI-pCtdhH4ClUYuVUyJooBv-Ud9sqjNmh4Rf29kgJJJINZtJRAi5LyHayLyE8WsBB6ggeB5FNrFdD22ddnQ4nydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65040" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM0OCKM7z8xHNnC7uw6RPOrbP24J_xbpQqiYcsr_EmDUiGbrADpHyW76UaxPkdD1vmmb44x4xDm61oUExLjd-YsIwytRx84hJ2TKqBZEHmWyGXXYbpqkwpGRZk6e00QChb6lnoHps_iqCk2ptVngUWBKbHUpWYc4TufzWgnaVdMWK0-OSQ9oeoj9lN4xBWAlmjqanoz1X8LgnL2-MQbK4GItd_J3AADeQ5jlrObfBxa5jMrxhFIOl_0MTQ2o55skFAoKrLMcGDQpbyWO5sAKWEpbW--D8qGokbiIHTnEUz45QO9ylMjZjveCMg4HYc4xvzDk66T9Ptg-a34Y1Mje7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز حتی به طور کامل مذاکره نشده است.
بنابراین به بازندگان گوش ندهید که از چیزی که هیچ چیز در مورد آن نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بدی انجام نمی‌دهم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65039" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است. من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد. این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65038" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من معامله بد انجام نمی‌دهم؛ در مورد جزئیات توافق فعلا حرف نمی‌زنم، صحبت های خوبی در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65037" target="_blank">📅 17:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65036">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تنها چیزی که ترامپ تغییر داد رژیم غذایی مردم ایران بود
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65036" target="_blank">📅 15:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=UeUktsQ5ZZWO5AxjmYYWrrqWCx_200WOYly6IsOtMHXyZ8dRtcjCBvtu3Bdl6v1IIWd7sPkrDFnvqyLaynJAfeqGK_WDm7W5HOoTlD8Ck_QY7OAAsHk89n7L2IubXPY9wqlkEjcAp6PFqNJJDQKv-dSISIDjhNRz9Ac21YW1vzAsU_efPVZe0nF8iaxyZYToC_kF8U8VL3L3l1Ka6awsbmzu1PMRn8aIo8JQlzgmKJkNX6zhffuW6HJbVfSMh9Eiel1ulkZJW_f6HExuZx6m-YNcdfaxLQ0AOnf_hdmId3W72gz-SiwFF2_iQqzVDJUKZTYc7dg7VxpKV9wqvaqW2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=UeUktsQ5ZZWO5AxjmYYWrrqWCx_200WOYly6IsOtMHXyZ8dRtcjCBvtu3Bdl6v1IIWd7sPkrDFnvqyLaynJAfeqGK_WDm7W5HOoTlD8Ck_QY7OAAsHk89n7L2IubXPY9wqlkEjcAp6PFqNJJDQKv-dSISIDjhNRz9Ac21YW1vzAsU_efPVZe0nF8iaxyZYToC_kF8U8VL3L3l1Ka6awsbmzu1PMRn8aIo8JQlzgmKJkNX6zhffuW6HJbVfSMh9Eiel1ulkZJW_f6HExuZx6m-YNcdfaxLQ0AOnf_hdmId3W72gz-SiwFF2_iQqzVDJUKZTYc7dg7VxpKV9wqvaqW2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz6Hc0N2BOtcu20DnuGstF1oxZ4krKUILovmCRVbbHY8xxo0CmXWpt9SPfecAiB8c-Du8u2cq5jgxj0jEbPTLVj7ArugnaTXTFnq-W1lBlvEU770vrI5xrjiS77scCl6sMr6zKfhTUJfjUz6pb61RX61Bv48f9pxhnxQjDE65sN5xqRaJuWQ5Z_FJH0H_HhZo1yaUFwJX2gpFIVJrWireMwWEHCSJE0o5E2K-3-rSGTsJRRxfyar2eOZyPoFXgFPThBjO_Tct-ZFAggdDTLLpQ69wcr9_2ZlbAcowLx-y1Oyk697CypzE7stOLTBAlgGh2xz8Jg13wqPGf1PEhDljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J7mgjmZ3qBoTRSRHYLk36KXqyRT3yG8A0e6cnNzM9z-KAKfeuugOnTV7512caWcqm10Z1i-6ahq44xt1_ORIdZmcVytu2JVgv4NDlbP5RXncw_JTsbz_jY4fh28rPLE39Lh24Dh_1O2zzMpg31RSQQ813kMiERXSBLicyxp23gBrIbpCCmxdT1kySr9hCBdX4mgoEzPGkaIxyiynyx0k34E86cQEZLte_RBQUCRQnVdZXbU__VkDRVn30VH7mGKwyG-jV35kvOsYtdcm21ys3n__nw2gxP657hwiLKORAahuO8CctiYsZjw1qEAq7TSVZyV7kHs4cUkw0aDcxER7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=ZM2b0UIpScYn6RO-AP-mTkUmst_dD65RwB5vQDy8Wx6-XhzHv4R0-DavEkRCV08oX1jvHW_HqVN6BHgIvgEViLJo5Rm7tTaAD1k6RnFO88aHQvct295SKm2efvvsWFRCOEx9rjd3wHU3TrWtqoBR2K5nzor_uS90irdfgMTkI5yCtSCsunTG04rFL16dNKPQODDVj-vQP_qtNV2OFeRUwq6BBDpbrk5Dq9DOSINnrCrvxvLY-CHPlzpECU9cccXNcJUMjbC1gmCoWtohfFsSM3BJZjop1WfGRJTIA3V2ON9PWF6hvs8lXI3Jdh2Y1mwhQ48E5HXNGSudUbvro7i8YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=ZM2b0UIpScYn6RO-AP-mTkUmst_dD65RwB5vQDy8Wx6-XhzHv4R0-DavEkRCV08oX1jvHW_HqVN6BHgIvgEViLJo5Rm7tTaAD1k6RnFO88aHQvct295SKm2efvvsWFRCOEx9rjd3wHU3TrWtqoBR2K5nzor_uS90irdfgMTkI5yCtSCsunTG04rFL16dNKPQODDVj-vQP_qtNV2OFeRUwq6BBDpbrk5Dq9DOSINnrCrvxvLY-CHPlzpECU9cccXNcJUMjbC1gmCoWtohfFsSM3BJZjop1WfGRJTIA3V2ON9PWF6hvs8lXI3Jdh2Y1mwhQ48E5HXNGSudUbvro7i8YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=QdgLJHytal9mcIiyfu8TGNFCDKbuEJX3HhSaHoDnnJyWKB5eIs2C0dUixt4WlN5WqPQ68waFD8uw4xelGIG2XNQMNhLq1Eob4lksuWOifi3ax3oKO9V39JJfZxKM-Dhfq5zljVA6-HYG68QfWG-Tn2YMLRO0LKuEPkTNq-wvPL_76opxPxnXVjU7BCG7OnMG-h9ycBm7wlnDhNx5hCaIOLosv3-MWSU1uuZ5gwkoynSXU-HV3FDCePMz8KKDXXP3YXNg0gFYho9qjsolXkgWRd2s4X5s1Mtce4VR_aglsu4tWTq2SK-aKY5RDvt_K9NcWHDcyHa_riVg255KsRf_aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=QdgLJHytal9mcIiyfu8TGNFCDKbuEJX3HhSaHoDnnJyWKB5eIs2C0dUixt4WlN5WqPQ68waFD8uw4xelGIG2XNQMNhLq1Eob4lksuWOifi3ax3oKO9V39JJfZxKM-Dhfq5zljVA6-HYG68QfWG-Tn2YMLRO0LKuEPkTNq-wvPL_76opxPxnXVjU7BCG7OnMG-h9ycBm7wlnDhNx5hCaIOLosv3-MWSU1uuZ5gwkoynSXU-HV3FDCePMz8KKDXXP3YXNg0gFYho9qjsolXkgWRd2s4X5s1Mtce4VR_aglsu4tWTq2SK-aKY5RDvt_K9NcWHDcyHa_riVg255KsRf_aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aZFiGm_Yj7NkGT3x-0Nsx6pRW6S6F4zyOSr41Y-xvVA62IKqiqieBduCW9TTVcUAyRxmKva6XXKC5C9ewHu6MRTMVTsSibRGxcK9o9vIgVLZTjFEzkZeL3pOVY6vB9OdojXNkeJ9jCjmxJdb6mmBVn8OJ3X799Rstq_2_p7-hpGQ9W_COIbZURPVbv1yFdZOtq0uM1zcpqL4vO03tsRwloFsaeogf4gdSGh0fYz9jOjLoIn-zdarxzheJYQQ0IyzO6CQcb03O78D6QSfEE5zcOpBd_KHTWFWW5ICEQmi33WL0JKoIB8mTBgnAus7mmMw1pzbzPxLPZIFxLX5fyMUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
