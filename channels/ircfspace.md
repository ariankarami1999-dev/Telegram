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
<img src="https://cdn1.telesco.pe/file/W_sX0Gr_WLdURB3NqjvyIR4_E4rhfkkkNc8PZYiBgXgYtwsd1E6ed23MG3sLkHIU57mOfR8mRP4dt-ueUjPjVjVj6sdEjMd3kj3WSQkjOighPf0QWAOSiwu4P97KDxkJ0573iU6hm7ly9WuBh3mdlJ6hnIQ6dvCc235xncqtGaGtfl_F36RHvEgjEI4yjLxWAnZApZqdvg-qJZWO8v8ltNvHhiKcN-J2iFT3HCJW5rmr8Sn1wpbuiHVq2npaItDGQqzos44V7h9OhOH2HaeFhnAhN0Goz0ahLtrxeT2VHCv6SSMSbmDfjgBy0P19xVF5TbtoSIb9PkuiH8dHHuqjyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.2K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 19:54:24</div>
<hr>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=FiNysANOqysbbXDQE2OTpTJfgsw4S45sj2HOGM1K-a-8crZFt75qNh8b8DKsocoKfHfIm8vnpG6VlAI61HdjTnZhJQpH5eeBS977Lv5_u66bQw0jbjumx_NxZuiNszSYevtjgT4QQlsRWHMxVRTLOWi_MlQOyf9j8gBDS1K-76hNjJaxmJCzN2JdnQs2wQTHYvngg0kqe1icwyGL5IQpJ6zKKv3ik0dSsmW7_tfvBVEh6MjvHLYmBNeOh4CmuEKylQxC3VHRV3SYzl8hS1Y2D-E66iBkJwX-JK0Vyhz4x9HFtjhDLVgB3TPTdbX-2bsq7Rq1hdxVaEv4zSHCUYUVWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=FiNysANOqysbbXDQE2OTpTJfgsw4S45sj2HOGM1K-a-8crZFt75qNh8b8DKsocoKfHfIm8vnpG6VlAI61HdjTnZhJQpH5eeBS977Lv5_u66bQw0jbjumx_NxZuiNszSYevtjgT4QQlsRWHMxVRTLOWi_MlQOyf9j8gBDS1K-76hNjJaxmJCzN2JdnQs2wQTHYvngg0kqe1icwyGL5IQpJ6zKKv3ik0dSsmW7_tfvBVEh6MjvHLYmBNeOh4CmuEKylQxC3VHRV3SYzl8hS1Y2D-E66iBkJwX-JK0Vyhz4x9HFtjhDLVgB3TPTdbX-2bsq7Rq1hdxVaEv4zSHCUYUVWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WnTe88jsXlDJX9wraW15_J2d7QbimMxfnQ-n9ZIS_OuhkLPa0H5njCIfDGpwEPmUp47obK6Z5dzZRkbmruc8HBBh3TR2yUVrRiKfiXMnUiZylJR6cLyVIuPbTvp2N0oJrDZRbiGqektfPLEaMky9_iunhTBtSXZz_4A2W9L0B-SRrdw3ghaBnX8lEvTkfzysuIoKcrh6_dmu444nw-dk0D11KOkWG-ZZzhYhAonOIFSEEjAVkCmag7a3izMlewX6yxLHgqWxyUpCZNKU-jWL1kJmq3mHHiXvoMsn-0_BwEkog9XIiC7E4wWQuKzJTOn3Kt48KNourLmreZQnrkxZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H4GKiPBZbpnXQRokAhxvg1FNE1rXIyOe7RHEW5RR9X4eCy7Gxsta7e542V8fwWyWiZTaJdmZe4miqW_pkvZiOsF0gUVzvKf--nqTnKcu6iYLo4iF9eE2LeM2Ybu4X_Zypo6veLX152vl_VJQWOFMqAuwlcT-pkkoeIUnFl77lu8qW63jkcLI2raPOZhgLa3mIO86etT-dPks3qHmXzfHLEEFVNg-O8IPLwXmEfeCUqVWIpG-SbQ5_7Vu-dZKwkNSBVbmG35tE4XIEJ9DN2IQDfTdrEdMV0iZ6cSnYByIAjITygZ4PlDOxPQGm-WlK09ElQNd0fzOHPJN0gi1CyLT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SGC5sC9luZKAatQLd8mJ444_NaPnb-YCri1dZq_2QIRSG-p3e4KYpyFk87uY2xsoAmb0_4kmSbHuKSqmp_Hd-TZR74Agp42qrvmdS2garR2KlYA5IiWxKPJVboyaloosX0-ex8ON76PTso407E8HSfhOAf_M33BdQIcr7aLElQBHTBM7nTFYz5FcPPZRU_hnlAQPFd-S26GPOkM88InjVJaN1I4aw-56P60zLLJJOD164j-HplvT8ezpCduMQFqBBj7YU3l0KvlmDcJX57_auFCzCpXL2niLB9Qgp-qJ0FBwSt5F1vLaSD8UsQddDuZEL65XS5nsQsXeAU6S5veyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJksTwXJ4x0Tvn8heJrB42CJhBNBMCk3yCKPyDAetwpKkJAGjsAWNRL8CI-SiyuAdAJ_8N_MZgrEbUlLLHdDblNEqd3bXtOrFdtwf1Q5YT3fNXGQ50SsLkPFBWbED1ihqMPtXN9ZsCnhQz5fknkJ-8lTa7qe4BeZnOGLIhmPcjG2zX-s9hxbnvOS8eAwooJrAak4AM3nA5Afz6xLesO4oEQptbuavkMyKcIVjrZ2qzgcbqkiuFujln6X96rWoRso2i1d9z1hricA9mHQnFjPxV_6iP8hD9FPv2NQRMfFhIzQ-j94n3zd7eE6PBTE1N5Md12fglMWv3D1esDUyinPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kwVda6DbKUuzoeqeDvSK1elVtWH4Z6PJI8lKM5eZ66YhHCHwilVKs6fJ7E1Lngxv144Kq6y2LaUt5B2DPi0SEKbKXQsJNfanUxPK22dnmeJeACLTqXGfhLleDqpW4mLqyZJFzhIr5zwqSmHUe5xlr49Vp-d2Lt9h1euWh7YDq2RPu9lxV40OMXbvnzt2BZ-n54uPB0ph5LRGNZow2jNAu3oFWm8dr8qpj5jvA6XK49tocqSf9UJpTE5lOsBTePIFMezKp6FZKqQLFCWcewOENDRyJfbadVX5BlKqajKBlvqd_c19D8d3WZcABxDn6HFDssQN1VVgpxi8TYIMItM2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iU4f8tl-uAg1LP9JjcnJ8fYdXMIiAQlQbO1-JHLSIFgSlA-UgLcDhJ_fyu1dQzUoOb4oKFAP96sZf2dyp_JOzcrgZ8CGs_XjqHJrSX0mmgYdZ1H9y61uiSZ21bRyznpo_oaHws9suebILhJQREfIGTk8ZWbppbiFrg3nUlGJdG9L5JpDW62nvsqSXiZWk3ZLC4KqhVMn1l6R-_6IYCvcoFmQfAQi4ZMq7foyi4I5Hvr_JbjGRTaryS-rPOIwnsxu8ve5e33oQ5-LWVjQDzRNdBsJLGM9KMpU0BeXhNwPfyg7eLRB3TIHzjjbX5snp0zb_WD22S9AwD_Jv_pC44xt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wB9coBKpGGn_6eRqowRj0Z8ZZDZTtbIL2XxohJ5gopt0EE8n61gtust0nXUrOx9AR2ov-ZgRRDqq_fosPotfgonBbemdp250-vrEPdc-46u5Rz2CvxgA_HKvx06h1h8hjQ4Z64ryzVttWM0MOVkWhDZUehZCbHZaOC65rWw32zqLZu8dBLUeVR-x3H9zO4DntqJqpFf5hvD77jHpvjLOt3A00Sy-v6OCW9_8VnVwNf7r9rJBro-FnAi-C1WkdCbEsJSzqcuF1nwQki-PaXeuXeMOFfq8cPUKNOxPDou2sj9ZrdO4oLOlzQQZZXOVQiVPvueobNQh_W7dH-cYNLnkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oyi1YX4ISbU2jduUae-Cre3Ie0qjoD_FJ5Xt52EGxC-PxChyrmb6DZN77KjAnsItBz5tQf0lDjwTWDpcvPSygjBMF1oTGBRNg1yu3zInHl41cx_orS5TzWXaWE4l8QNdg_y0i73Vd3ORcEI5UXkCsK8N9Q90yc6MezhSoXhKdVx8x85ZqeAEyvkNBjCy9136qbKi5ekMy0dE8YQe41KFpagn_aJo1mpoinnib3DVM7djCXKnzgtUYspNEXDP6GL6_Mo1ZdVQ6eV3wVhXOSFIFPj7IOPt2cK0in_3aG_ixnOycLAjQosMjNA2oEGHwEccINFj-UyvRLn4rcVLzNfWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lUIE8I3rMxjGEUz2vtLr-2ykVI1na-fS4cC1e3_8nxS7TdYXnme6MK2IH79hIfcpl7PIWwHDOE4aKGlZHKx70_uqvB-Umtvm7LXwdJXi1ISIZ8gXyW0vU3cSjKPrvBtzu0g3BCZ-X7sp88jrNZvpstNyzS0pj4bQ_cCpnJQHeVU6uwQRwzSUX9AA4seyG0m43NCW3eqZs1RKqklmVHmE1E5nfxg2OUophN2U8d1ULfbZcDVSJYpndMP3ZUzS1Ko6SyxfTGKxrmsCjkApoPZnL_sW9DrTuUcCSKyaEilolUxG-rXhNln8BEM8NwMTa3Rw-Nkh-k-Arj4b7UhmzhiZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ve4HpUCbHkEsyRfnis8cwEu5IXzXy19vkc3i0UwZg-KrOff7D8pVrNBUUYPJw18teYFUNAN6OM6T7zECpFwMf4WZmWUBl_4ZvdEpl1nhwOJOeKcdSNlwVuA2yOcvnr_7TOu_BrinaxPTuD5OtWVFP7IwYbsz2YP9amRHuaZBZ7raR_LkJTkm4wN5MwFSeaCgC9CXXUmq7Q12e8OEvqDWHZXxeWk82Jx-NjX1bIenNx86CFTecMzhaO__hapRgN7xQqXQHJdastyXn3Ah9S2peSfxOjjRfx5uoZ3WcSJXDNOJYWbITRnrh-qXwnLDHDGirpxZbELOxHQjMfADDG87oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fe7iucmnHqDOvZgypcNTENtsgEH7YtXTq10VcVnzIpuvDDjS93uU9EqCUnOFlJyiU3HqdzuWG6JVe-T7K03zwntwojNrh2mnyYURkTYJeLR-xsc-VSwqYJul4Kv3J85RXXRz9el-VtgaQyib3_iNryRLm8p-54NZbqRA7ptycFTTjYjePaceSOyk3tRRyCxQBdbdKaiB-HsNKrNTFtjfHM39sHObJ2S1fYCf0wewjLHhOvVpre5hiHMIdcwXotmBGuEsYM3P7dsyv73LrjW_Cnmw4LqsPUciyuOb5txAkYvPtiDNpBWzM1Zxmq24Mr2GheKIi2hSx74RBHk-R_SsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ddqtZj_BmV6Ajk4Met835fu9iKMjKaZ7TA-gkfvXcJHtErC2zA7LxpRUaNXSsOEgSTszhX-8bq8BZWKvKjsDRHAg1-b3zDP9iPx5lfLIjg9siDmfueDFxULVUgY895fpocS-SmKDjokZ41Ryw4gz4rxMWgEy2dobZAWSEtQ0ZvyfXDERAkKMlz5T9AiVQdxt9Q4t1R86Ls5URuwKJK_iiEEO3GSOwd_s1WcqYLCTc0VwYacjaAhepwsymyEU2rqUQ8VNGS_227w8tGDuvXkl2h_4hb7beylgOk6pn02-FC6_B6--DNu2UggnA9YUsjoxM3ejMz5TjYAeYNoa1RRh6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LYjuxDvje67d6IeYbpyWn9TsTh3acZUtbyEDRDzkC2RUR2-ME-jcZ615_SpyCywP24Zi2V80bgxa6ZeCvVr3bowWE-zUi8dR0jaC6J6bc50GZHzPiG7mWeDqqymbR8PIx4-8yrkbeA13AcWiM9sWru8TK6DXOEyo4x6cY6GG9UdAY7kJyKimEtesBLJgtf5dblZkkpGI3C5r23dBNrq35nUQlV2fLU6ujdygEk-m5hVwsdCl0ByFlZc3zxD5a2lJRNs22WrsrQDO1jWk9y3IpJTCQvJyupA21J35H--4t7zHY3d1Pn9BYfw87n6b_hQGS4DO1tnyJRGr1-I4x9-SUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BLcf8b1RxJ26ovX8aId_mLxcEwtK1-lFovvXUR4QbCd06eN_j4FQwBhCjHcvAZ58Dz0bCiWzv5MaCbQ36lJb4iOqSbchDkz1z9t6VvNUGcKqYOZFSwglgFMUoiYjq96cqwOA3eYVqcabgFeP4d9xXnbV0kVg8x4NM06s_UMb3eTvJyb4m9iGDzMm8zdb0AKiKBAsYEmm69hJ1wXJr5ZRpSqjgIuzzmESD1JvH03KeRagkKUg2XAHAeeEKUVV04SZsHaelBr0m-jga-ZjKPLWchtl_TRgrEBBpjeafzwXXICw4ITIuEshaOrIbjS7nHoxH-0CvvWGFVjWHFJl2sWfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jv0ocn79gqxnH31P01kUlNR88dV_KIMrVez26Jvf856nkX1R_n0pvbyGopzOoIagV3DJ5Z5TuE0WT7cU7eShEPoDlTkqeYz7gB5Xc0jCT-dH0TwW43U1u_KCcRbbV9_spetFaU0qcF_SCoRxxdb5yNSq8JjHItREjhU5G1SUdSlvt3oa7WlxzaIfSTplZEjWvltZ91ixoBn6y3_TsybQ9EVKx00QthRCdlex9-5MjQoInnlORyUJIEX0rRBvBZuBkmA_R89u3jHgwt6nMdo_7J7oXEHVROz8BafpJnFPe7xL1N_SeZ_5EqCBuyD8435xCBOv7PvgAYX4g92gTw741w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qRWh26psaubVytRFxJUNDXS0A1Wmt9fBqZghICf8v-AuzZQXokQLls7YYEH1_i-2rbVKnDNaIAr7SWNzAcmE7OzYU8W0xAI8gnxvx8nwelflgrXmiP_UQ7G7lqTPEnu_UxXczcgJG_anwj4r8mtUiL95-ogZyZlTM-MaszhOLI6FoT7B5P2H4gpX_xmphun9ie5MKtVJLP8LJbrHyY4k5ZnulQ3A3kJ3kPpl4NpfuUp-xXa3ZbYWdhVbOPNW2uDI2psxyuG09NnmEx4QgRNfR9sXIdh8e91fJRh5RPm1Jyvg8kcOQZeaW4pz0MJcOZXuK7UKG86rQBF_nvHkoTkLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KhO8b7BcqxrlzgL4hgn_SuJLDD58BOApGH0CeSg356lja4jWCj2m6x3D9oAzmZVGZYdBxQw_eTrlGd67jw5aXzeOjiiaBxMaVF-0pdvG1-k0ixFkNowUvqLq8Pd59-K-o4HbqQ388YE1zW-fRFtJRfE36VdjPtXKzQgYACH8bPwSwBODsGgfo7mfZ4Nu9-QHt-ppqoEn7No9LwqU-DkFF5h3_i95Diud47YXVYa1MoQTqJc3OC7pFlKPLB7QEwDv-nkxEq9mcaU9-vWELHCf1LYD7e6plsVXlv6IYAPRJ5wQ-OEhb3SZUf28GUEc4irHi62dEGrhduugxoUueprrUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N1-qKus04fJNkdbFOS1_egqPiecqQ1NaVzF8YdK4oWc1FOuTDZHsBrXmk_0uJITre59vPM2xByjWGw9KUKyAajNzIsbmelSBQK0LW_eraS5FiJppBuCTc2MUloRHYl4VVUiXoPYQx1xjm4ZNLSt4Mj-uJOujFjYTG60F9ywZEYYOIPm9uZj9cRdPeo3wS6d1o7uY06Jdhl_FjdQaW9O8W3ag2PuvsUZu0W__xSr6MK5N_sK8tTybHsAUTPqUxmmOAK_mgwSTvXLs9-61ZOkf6gL1tg-7HzOg_in-knXNfkbj6ndyLIpiRiGJkVYSZ9Mz7K20XbDJxewf8FKCZyoV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IAdDsRGMNgdd9uJYWYjRXOAVulwuYnSexslbX0MJtBOeyI0gwQBR_xTG9yaaqvauxEgoDi_VrHVKWKquYQc1dVcykKXkbS9tvADTJ7ACFGatSao6BSchTJWI1BigxAH4WZYixw_ze6NM95DV002ip3cWUw72F2Sn3P-Z7EMEuur4RDUIqyTdJaXybLWksWK_WM9mewkvHseoNTbMOQbml5GbeIYWg3wZ_ihi5K8CJaUdZrcRWAgzwbMg4qtTKXk86nmGXs_7xv96PngaL99cp6i13t2dWhJRMP_BXKC7EaF47PbU0gljiYVBIGE0v5xW9GIL9QoMlTmsOpRflPPAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nBstUI2GPo95p3pLWT7nTz4ZHF65HloMjr4PTN8bPWvC671cWScpAFA1Qtgqq6r2lk_MyPeqRfg8QryE_OOMwAnnpGfZlYRco12IPolLdpvoEiB8xmpQDf1UP7YTdudHi8Fqskep7yRd4XCp9OAUuRwXpGAW4358Ir_RzWJgdPCvOdR0jhBYBC-oo6qVHn2aoDGLufrWUCleXVuXfhui1sYV21sltuVMM66WXUjsxOsMAVWpOSYHDp28h2AYWHuU7Xcp0cArHtWkY9kSPN2Dw__gw3so6bcHQxyqiTmU2xs4_xgT-PjOF0OCguVmgxuTj3ITlwXIe_qIoDOKKagZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t2LniTnPGCi-ptanQQtiky4N2-90nkguL_n777Yg5og8ofSE6bpfMTWqWmS7aOTAai82I8eIMOwIZPwaL-KR7KqfQF0OftBDFKe-41HxWDYS6MJTDQYxZi1WJ-Bk9u-djk4c8Z257I-JF2kv3Qi9-viazo3EdU3IAx1HQLGC9s6ppN-rCGCdqczj2XsRchwN6tP8PNjBCFOUs7TCiNBV_Y2BUpqi0BmPwP6d04kv8ChOQEevWa4Lbcf0DxLrmnUMt-6rL6K6duO3z-uBoMlqP3v8MWLeGj2Jn190NfG0SWrKIfQ0jZ-NzE9XaNhc0ZHlAY8G5OOYe9IO4SX3925t3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8Dzu5l4YqF6dHNCARggiv5ya3tt3puyerwucwTupcCq4YTdK0kIYGUxoX_GOt1jqlphICruzyhK1R84EH-72b6pYbHvMDSsqTIOImX3RsDxvh_zgEfqRC1cwLy5-NhL8RvfkyVWmFIBmpa-Tt0fbiMItcgLj2gf9PmFrjT2QxyAqgm66WUr8cGwQ0YmGIFG2tpgWArJW3v0KqoVDNVIKLD-DA7PpPJRSYLtyhATo3_LtVSNSGDHMOnh0n-onm22z2KSjV_5HittVG2-niT4Ia2TFK29rMAGN4BZqKBKJFRzjsGmHUd-7KitEwyy25BDTy8qarYVhW1V3VEDgZSXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGc3zkcJgRR1IGhHJB1Z6g0BcCxaYF9bZr6SvMJ4u0m265hRvKu1l9eQvMBIuISBOIsiH4tvw8DctIgXg9_jyFv9pQRHETLHsJ_2Kr1oLqNWMpk2ZVU2qUO8go1XA_nWxwseqYvgF9uV7GwMwv3uk-9Dby8plrOLdl4zTl04Uy0Vp27YDgPb0-lGG9P2g2yG2B61IPGrc_-0nNPeM4mgoAS1sgsVLjQfsofHodStHjmp4zburvL_0brLyW2YU0x3IqIJumxHeAcbYnZNlI0a2DYdw3Pst3W487OTXkQxpP-c7b2P3_KBFA9WV_AxfOCRYZWPuMpZUJuNI3T4vHms3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hnL9XekpgdtKUo_xF1SuUSjluZR2431HSJgkYAKNekuFUt3M-u3s5WeC5fClMe_56No5ihqCAmGswqtTmlmxmY4jloFBnfIyr_pdcjVfbtO-HAnqpRDhpaTZrU2aTOIZQGNPLRekPggqkjl7fttZLjxC04eFZLXBFVFTpnJKVCQB4hsSZUOb2GO6ZzSMmCNXH2oiYy_ib91TD_EDN9SCKqm0MzCjWKka9shrJ8djtXPge6qH7tMUNbX4QepomV_-m4245Xqz4mMQB1iCWFrQkrNvRHowSntXw2PZFwZyQkuPPm5VZtKTJBVya7I-6dCRJnmMRtZc32ZyHzn2XXKgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZPnJiiL8QqW1TUHU0s7iAHLu90RF9cMPs9Zctd-IHI6ShA7SRbMZ5URDms1fkzL3rT7F0sZZiNcBH7qqql991yqLSnZeoxRmnso6lwwPAjzfW76pQZjKhJO3OJQtMawdw_c5Bv876sgVmnQ9KcrO3VmdaePLNvUjdpkrfbFOHaJRTSKhLbSuPvM43ZJZ7sppGkcFeuG6yhvFUL7YiUMwnkExVQEtsVSaL95wT5AlYiBHDLm-sHB2DKYMdGsU5NuBtXt0SrDCtRgaVYt51pm5lUR1sXZcN620MnUKjyfKn0WmvlpV8BKl4b0y_szQaAdP8H4aMyg358vD3g8pnPpABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ctGBYeWzcXQQYSy3R53vhudlMC5PliM2bZH0bY1FFutJuGydCFpII8Ufli-ox_IIP-tf4xf3mwDvWZ-WVzz22U_mlAwXe4yfMattFX-nil1fXDei7SLwda7JfGgYUdmKlhI-ndgAF8ZXtOyBd_AMX9jfBQYAzNVC3e8qw9lHGyuy4g3_AIlDX7CVj2RFU4VWn11Pj0T4LYRF6JfdAm0f3YBaJYAIpuXNL5MekBHvK_bd9v6n7DGlj3n63IZpmnELy4kAYLKj3hrbC9M_DarjqR3KhIzNuTznMMRlUPAVB9Lbyklxwr08oeH3SDeQ8u9mdOgRdFrHRaREcgOxmJGIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qpDKROoX6Y4dj7ciiaN7bW0do1DVTLXmJbXXHp2vec32LYeyk-jgl6TnuyW-nL9WtoxRiJvgGq52sI1q2Pzof4Xjhb3s5h1XtpuOzLJmZF5lfJjkgcvnLM74WQSNSGzEscvh05TMephDvVTxZoUipuuAxG78LfIfYgNDWLqJ-LHMPtvX7ovDHl0SlLdTtnePustYe5UekHwSz6LFmJHSpItGLDte688Y3q5_6WIR4FlO2BhA3y17G8DZY-jh0VSAA60PE1QRSRT85yqaKTQ5Ti7orl3nL4HCNSo2W5-Y2ObtUIUOQOhMueV5_1Q5B12pVboCdFaujK_hZwPURqvy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QCtejEicm1MstQcpG4nCdyZEGdKClDG15Gk2ToiX1a0EX_axTYjEx8ItzXZ05nXY8XVR-SeeTUvu-FrkioJvCmF5BE2MdKiwSPB9_dvesLv295no1jvK9WVQZkUdjmQGpSLtHfS9V56dfNQ5G0XeLqnKcxQ-aRO2oi5eObI47lc88o5q_Jg_1KjLudwebQxY71njZJPzkHpN-f1_1Cx5pQFKTeYMGTQWEN22zqcQga_KE-KosFAXHei2F85-DRsZ3zTlBnIXyqfbbw6aO-F0f2K1KRgZ2ZmOUsfoL3Pq14XZbXc0oMC67oB3hLtIqxtSgTh5XBgnbt9yUVm2Uc4Zww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Efbh_H2ylODiWEPRatNZyX3gmPMvvu7-Hl-RL1SEOaPwt-TYvoIJntIsQ-4YXSYbIH4JUkEQKOaWFvOU_8IGZ7dA3Im4ltU4iKC8T7aw7y44SDaLTgbfjgzmbjgeYwypuDYS6i-qdmUJj5ARA6wfnmwz-7OPd-QSQEO4VU_UsQB-nnmqAwuDnBXPMoVHg4hIJ8dvnMQYB2rti4MQmSB5Twb-wsKqkkBpu3ISpOCkg0rQmfmmLyTlyx9RYSykYoIroW3T89U2MT4x8r87z1RSTCaAul4UNz8dwcAAzcMA48EBB8dwzQWVYqRrcA_pXApHo3jkfwmLPCtuSA5x5i_ZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KvEugHGAWS9PdhfGkWTZfywTCX4HymWYfgHT-JQCuu5K9yNQLRRLeQIJUakvz6El1nxw1omXgUfzRanE_xpUbXv10GKkrS85Ow8l7ovB9ENIQ2-0djz4LD9wHEi8ENaf8bpm5ZRjQW3Y56B8llrJmHpip5zS7SbAtqWYXs4mrNQY51Egn7myB1KL2fYWlor25GBcQ5rMA0Dimw7f6oplNXWrkVPmfHQfPu_Z3ayweO9kPeRDs1IbEOoVxH_xWOl8AN6aYc9TrODiVscGeRPUVD8wjS6LRaKdRAUVz3ZsaTpiI7N82vXMhtwzFO1hjr8G9Ute5O0l1SWzWzOo5f8pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qs7AVL-tQ6EHt4DFVKitv2hhLMP1VysvUrODkdOlz4jPZS5Mz_y5Ta1h5bEhFINvEIfc1apqGPXTsKlYuI3YJnSZTj9EC201vhXRILYFkJ_qGB-MVJIBJoGg914yk9tbiHnYQVu0U_DmU7JoX3qVQzz4jJ2fN9-_4BGqk0czl3YtkLoOhQKB9z9wSOAwrysng57kS9h0BBtVnB1WdE9ByXtfvgxvbAMbR-13eXziU1LXwiiWt8cTv2wnw3mY7jfoFtb0ak0Q542PyQLOKU_Kzkoj4mfQtF7XRb8x_5u5hjgsmjAjx-5yexkHm2CoNohoyh1K0WrnCnT0O6mVBe4IKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_Kd1zEyf6UzAl9rTxxXVRv75LeKG2OvG8pwfjJgm3uSJooTld8uB8BwzDMGy8zz6-UajlYmz44sX6DV0Z6QkvEdWkaMxfcpobDuHKLOQRep2wgthLWaGHAqlMBIMykR9A4SrL2MBOF56WFU6TMiPKsceGeH4Z83QtOF3rW6vGzMYzyLg1eDTjKc9oK-ZGB39prCmd7Gv7VifZlc4XjPAAASf9llaoBji547DYShuvUtc1DMHrPfHLAIHd4T3a0T373HqeyLPDFZfsGqmV8jThDwqVRUI7BY03RwtatyI9WwD8exT9s4TfuXWRnjsOIJjbMgbdhkTEyXnWilmlpZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZnEUiWDFi16aKIoqpHBVy7AVcb3GpQG4h4QKh20GY4RkONf5NWQsmeagAf6ArfW8R-Pume2biWcoGV4CQ48w01HYv_i8WUdPVNiNFLgZS15vb1BmQY0xhnwo03kj0UXYDCBi2Fq9omMpRzB5SL07KjOzr7207t2tb0q317sa8H9_AEh9qrcQ8V7rJEuGn2tVumgtBL6zjBRfx1UcG6ySuJn4n0dXFXXLqmqSgz8UoK1IfViBZoT5LTRtCtpLHjI0-ci6LW9rR8-C33l8fp7boBX1fVG1rV-iArgiISHqvmWER4EV1_TuLgvcZzad2w1jerwu6ERMQ9cBtKJPcYBwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PeZacs0wzlxMLJ1dnSGjQzNILd-zOBKw4ZmwO9ztAOVloKLGrNkuQ59jgAcefKFv-xabLYkNAub3JM2QtKw-I73G3fAPKZHWPqs4g2_wBdXes1TN7fq42VzSNhIyn_XfUd4ewBBjJqKdemmsLysxZrRIvVpxn4UKcyhilafSKgtRr939IYvybSknEEZ3wKyzfGcXafms9rdwOSxN9-qdT3YRQdznPgMEQdzK3Qd1PQPDID_3Bu9vr_rVElZ6aFobeSYIcohIzY4IqqJL4ieVRykC4f1S2CABne3lvXpLQNftBMkoRVoJX9bSjtcXw1F33dtgm97lZOQUWhsqvWd_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J-PXOn8nyKGmSRHqxkmr8inOrymG7Egedfu69EmAwHharB55j-N7VOZDZGtAx0q19mQsSECWiqfnEPX9-6KHAf4FtLCv6z6z85tqZs7DuY_M85P7AteN7teXUkIGag3oI0ABAafwE0DtLPILSDjsC-EzMveby8lWzpB4LQu8U9QIGYqpinum4LbGOLZtqD2rHRO2kl86morwnr19ZmfjdijBxqPaq9UgfgsRicx0Hb1eaIFaTJIXlUL_9_NMYDZ67reDQcNTQHeUp4lf7rxnsuAT4Mvcguwi3TK1qM8qd3V6hjoqUY2rFokDJe6O9dSzAzk_OFIJXv8l6gFvMDdv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lFOLSdUqfBHxtpaZ3oIdA96AvHyR1WkPq14M9_hulKtZv1yPkZUaPg-dHFHfxERmvgsv_ZYZAGX1SaN6A2NvFbF-A4hmFRE7mIqm2MvxuEJ1trzXIV84gRUXsC-6XA7RY2h-XtA6wnU_VgP3KofR99u1SsrtR0sVRqeARALn4QbVuX6sBuJbz6tqUk1eXZPdXd6qiokFxVJEL3IIB_C6gix5Qb9Px1_HYWhx6Z2Lp00kXLAL5PHHK8mhRTYw7gs7Cu79x0SXlRIzGMu67NVuqehWa4BLvbImvuOm26Bhuhwe1XwaZ9G7S9PYIzC8AH15ARI3zFqNpGV5CWAvgES6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vBBke_bDqZakEoIbXtN3uVxjb77FOA2tz2_D2ev_o-jMxhXuhem_apLzyTiWWc4i17zCZhUi86Tjmbx4Vc0kXc45vT9arZU3Es1ABl1oc5-kasAlsWlxAusBl2sgi7f8WlvTREJn0IF92hB352yTHIo0FH21gcWlGzu0wHP72wDOF6xeYrWDH250cOp30vAS24pXW83FQY6ToJPnvWfVwYehVw2Bv5WG93T30sIFUqDyXIDEpNTBBruDxlv5EPhyoPNNRwgDVJzS9vkmugvLogxxpB4N4rdmgd08ATFa8fGjBpwUFE3pDjoQQYFG8HS1RhDuDRdsmSsp5r7zmw2p1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csv-qimvUtms0mZUWGh27_lzYCD5wLccqyufeRkZR9CHlUBwUpyoPgOYCfIkQlPsqBUtVVGG_Zl6Yzugt3CdHtJFnvataTf1XZNB-VzYwrcaJp3rAp1cJXkRXXM42sHeipZjqQNW4BnxibidoyxtOgN8men2_-fA8lxEfXPpvJs9TsFacEmL5px5Ox8VxRE7OU1PZ5pOSq2-NtnVpzNllbENvqE1ozE6TBtpYm7eJ0Ah5atnDAxaeAF8wU3z--YsQmLi8ygoeA6DMRwNiNFe4GMn82w75unpeygyZGjyC8Po0HpGsTF09AYeRfzeOoFgtFn6NKYkaRlprojf0e9fJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GMmsUkmamtNHUmDNqPD3rcOAaGarrGNAD4hqJIQ0jDDf28T9YKLEKQBMaVxlN1XIIg9Qo45v6iFBxNIumahx4yRHL53nZ6dJCbHHdlvQy8QOdoxj8XI-i22WBXF8DaXMWxp_iw8JKJYyDYS_tKcqSzmXZ5AOS2ppIAsTuXpkPkb__vhsgIEneC-4NhMmXhumj2xvbFtyNaqMXjLfMDuLGKTtC16zixXm7IFbtXEkixVsKU3gt7X-rbaCGXnfjKlzxitMN0rK8o8FKAThilOpF-faYJXKVKoI8uDa1ttLaCZzpH4dgS0gqg4rMcisVUxYz6z1KvkfhkoQQx2b5cctFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mJHRuFMj-FA8ZvcmiR7HZ26-ZtXHtJ3qJQdZj8U4EilPY06h4moaFigv_q9AMQ2uaQxaGrV3_tjzw4Z6HKGZbCxQPl0kZDpkOMaUrZpf9Ed8PvjzGUlC-lzjo3KL22ye7r7GmzaCElr6_hRDY1-9eMAGuvccQhT8550OeMYNZ7jKQvR0jG2QrV_e8moQfA6w4Y5TMuvjxhIO22tHke12AL8RcyG7aaFYVjuiZHeD02OHB28gT-iIZcL-dv3oE0PRsRSvRqkeA6jkJ2fF20B_ctrzqgJ94Qo3w2XiBrMadsL84GGxO5y0r0fwf3Ee-824VLF8ridmmiAbFyssc9mTnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JjGD94IlIvAw9wX6sHBL2WkJvgkULM5qW-Mhs8eFFWKA4ViLxuYsPFwMZkCKuFzHJyPhakaWi3O1hU8324_8fYms0JdM60n51rnP8PM0OqSvRcsILWb6eiNnUZWmLWqdQhaHArN3me1ypRcH4tGtUoiie-Unh2dU8TdneWgUH1x0NJ-yAHAaRu9yNscUeEWNOqIX_deXcEq59kl9vL_P99Ck1QTVYAeyxKzXrIVnfQjnguq7b9V7D1plJEaiq79KaqJeO4AgGUu4V61aOkTdw9qaUm3x7Cm6oZ4EskIalzfgWxAyDAK3k5vCYi0Qmwd5eGS5HkIi7LZxOux_btHOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwcWBSMp31bj5p102rsODRYpKbc3m1Ig2fJfqnxDov3Y3EldssPnD2nogFj5wJG92RwxE1WU08pbqUY6wxYX_u-paOYfgMEAP2DjYBj-c2ne46lmXBFEaNlnPMwa9vsaWa7ieqwKbReTWpqWrrFlE7vJOiVs6EIcYBJ1mKlxt4g03HDP6xTYRZ4c0Jq8eMKWxicQz2izXHp4VMuU7tFynCy2-jPopA7cr3azhYkXaAuRKW4LhRPOVLEvlmqfyveH3jotplGminnPce4W4qINHcBwnvAbrLwjeKBZz2QV1o9tM3ENUbJTmY7MTFkbldL3lDogGI3DigNmle9lgQvF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vYaH-xxpZHHCDvQf0BBCwVcvywNAVFSG7ws4KRzo87YFtzxCmRfD-hLEVqhdpeicB1CQu0cPyQYFoLnPweCkjnD9uSPOko9EuDISqUNI0QHcVC7s6qA_O70ssGhl_eo9CLYrFphHj3swSx-7PZ4nzls6Zdu7kYMrlvi0yVOt64r8cIfYRt9nYlq_w0cTyWb_DklqaWsOC9_YDQV0AG2zv63lJ4Nu50gA16NYH3boYnnPCTneQYCA_avsOoD-a06mfSwUWI25x_DLXz5yAHghQRfDvsdOKQRGNWnmQ_4owBlhzePZpHZfBzcyqPL3Vcr1xRI0qH_kXlqU4UYUmaSTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AoaEfVBj7KFCUtD1nhfmgyda9OQA8bSWCh9fvRm_mbigosI5IkxKBILqtoN0h4nv8H1Q3hxbvvQv46mNjb9JEzqLNw6LOb7BRg0vhTCJtGm6s_Dy0aIR0stnAADKbWESdfu_FgCAVpmuSsfiCIpU67ozKthzivXwJFMVZ7MuI_sK3C9bM8-KjJC8h28zpceBF70SNLTwLnH0ZHW9mdgLlCtOJlktPqVejdABlFyvhVoXuG4l7SYtgO9FT8NiDydGHR_NGh9bc7slz5Hs9frmt95eaRkSm5h_OrPsVrQF1oqHIPvdDFvllHSMxpMOa6I_84_A4-E9FLwy1Rsue8jOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IoZXXGfM1gE-u3ZZTZOyPV5RvezYx2f6rvbxhbEalCr1J_kKFZpAEhLQWzjQxumHu-wmk12xQgiAzjNKJi8KOPtjmjhFP1EtnkAtVnWndu16Mpv7sOYNNAP5RoSk5_2E1mPqTE19GCe8J-DFA3Y1wn8utgFCfso7L8o8nJCeLbwkJ6Wjb6Z-iP1c4OawBwsBN0GxYnm1czX8B_XkSmHbpCNy3UEgsW7uUapa3MO_4eeE2RzkI_O8q2lZNowLfP0bLuJcQnEdWkOb20MuGvDrU4oM6lkUDlMhufNEdNnx4PTbSD0pxNcABWFvf6DK0OZcOjEEgeRqGJAWNu0zYQb0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WzDK80Or690UiYecu6GG3e6_1MeapW3wzKCh71POGKqToawJ_BW3ohyfWKL-3NUhsdxOUO7HqJYJOCOfHNWdzxdxhzOJA32WeNweXrrhnvuA7UMfjTRWyrYqahhKy8Gg--ZFMe_hQmnGhxvkrIL5kKn9HX0K_skMs81di68UM2boQKhLijNMCqHX0hIb4v8d3zNIMHxh1yrAYCt-58AzZZWGQOgqJWaMbNxMp9LoNAvcAd2DFqXX3hNp4_PgN89Z-jZyPyiXH2NhAnhYiv_Sr7WaG_o29k6eGplUwVgjhNrHm0afTMr4S3jC3PiGaxZ0GqSD7P2pUV1vLV25va9TTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5WQoW53sjJ0w_pN-gE-16bOzWI95dn2yIPrhUroGlc_LRnu-GZqRMFEbvw6VktfDDSQbTDmzFeAX_lBg01DxTIi_PqDCi-UpfVLGtcWAyE02h83wa-zUXYwrVvl6l59rXdRVVkvg54o2jLCGSHQ8od41YQ5kQcV6PLiWnY7ZMI3a39r31tGIP6epGr_ifigeQBdSX1T4qWA6bIFGlrfFfSHer7Pp4H2gUW5yukuVWT6keJ-ffhYpO_rs655l1s83I1c6o9JndEDZ0GDXNfaLzX9Nr3MMVPCuCwEUq3D43fM0WymXTq3vrxOn8WO_S0BD5D3SSlni2i6SfVcalwjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q_lpmfN-KwtSbr51WJv3qXgRREHEhpYAJFai8CML_505FCebWjGaQpyysCB4Vn4n3UB1BrK-uXqB0aFH-cGyJ44IEAt1-A3bzPQ03ilBhygnhuVfq4C2AQ0qdYF1hZbHDB4-1RDDFKuqisw-eSlJPyiPfolwVYH0cbw750XPexgipNcdisHpeF81o5bPZSuKoyuWzeXcC1sDmleCV0MeNxCOOnG_Z-KIOITmavShdLDOIS_1RPZU-igqZcFMjIlPGn6dUphb00D74CFb-qO65HPbu5JFuSiZJ51HfeJAYo6J39-dcrHt3-dr8S41ngr5NONTIab40Igo7NMYTeD16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmY0vXfMKX7NViWpmzWf5zGkfYG0iUXEvkE3tR8NayTxLRhTznZxZIob2Wexqfsulc7j6A-_2F1Ru-EkS7d4QNMQXvBQdkzVF60EyZ6QlXAIiTyV2GOpotUqYYN5BoXGGgCnts6B0z4xljdkBpOPwkwBj0AbiZ8kT7VbFVe5h-qTGX_UhI2xOkob9CrzWYxfcik8OS1YwR0DXcISiiiA8WMaisVkNSgkOKTeYF9RKyjtBk-2A4x2qeqBQZhynDXx8xR2dJYJB-fHZ2GTTg0GEqn5Gf9ZaQ1XGPd8QdlikG8YkI9L95CUVds-lQTc4yErdnAEUdi4a2RRAHOehPIXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UFDIUlwhTIyMRzG62hwWmf7-_QVXAz6I0XG5acO43qXHpjW0JURwQ7n9yjVG3AlqIcV3y07qi-MClGMZK1EnM83GeslQuSTHLE3ckTTQr5EVCdgdQJS6d03c-ZIDAR0Pg-ew3ygIhxFP0xhbGijySkq_t1i1EB35azbTuzN5fdrHCV8nZfwUU0AYMLtjPj9wBUIFb-j5ZEuUiOcS6NDpsVFV8zRTa3Gky3oHO-rHzOJ9b7S5EuIXmKNW92IQzd3TDaVuaDRWlkx6_YO34XkmXSqstkel4UB5HK87MSCogty2G64lqyQIdfu5tYAo47JgKnzaN6a-3e5m-hmhYJrMZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8cgiDwfaqlIEjlrkBo4YSNC4Ror-4JU-U8MV4cUdVCZ-EEA2tQJQziD1lXk0ScnK_315WcOzXKXXF61w0-tOKAN4NimSICYyera0AQTfxOba5yC_6bpJOM1L4a1m873MPmBa0Tn1A6Vn44LCJ4yPwRMONIy3OyqfQKf4B3D6DOp6WLFN7QyzeKwYFRLloFdXWapacl4_nD80Ez0Cy4wT2pCjyUz4wcp0vu_a8NECJDrOYnn3oQWRqxhBwUz0mLIwDEXtI16q0sejwMuknefTSH0eMNdfmaiTMmawofUqdgpWxl-8pDtitJ2ukM2MMMc8PiT2mQIpMhusv7l-NsBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HzMacfvdbu-Oow72UEXA3rpaHBqsgelMcM2yCqInmIzWqtIflmCCHi5InNiOW-y4QVsVUBH8QwJMm-WCJhnwpp3x2dVVv_DAowxpXp6bj-wFeMMJnZKr_nCsChzS7d-t1O3v5YQTVQgJq2ExwlGBNJ2ksGzlntaamQid_TjXOf8ymU-q3IoWEJG8rLWtXSdoz6mzi0X_k3Y43jgCaCJwpw54Yb9ju34tZ8tlP-RxZwcUK_hkGStIqOsk1A18jeDrJjnPmaIaFP8_2nCmv8uvCxPOJQibX43PoQRSQBm8Ra9u9G8HHqAbuZyj5k1ne_hXmEFP6bDC3mIaEI9PZpoHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W9kFNkjSX5VOT_3asV6gHe3aZKbCShG2ztYHmvh4nDu4u5xZbjKwnZ3xpdo7SKISVWoZXRnvcAOkGkc6EhvauIysryf4lrofpx2ENpSL6MISRP6rLjJrtVypg9Z4KvorR6d1nWOGoBoieboHQyv8LZaXpq_jg3EXZ7we_GL-j0pXrUMkvtNFjGzkPMX1LSTsS9T9QQO0B6T70NgTEnOSbZeN-PYujjWIw2DlgCJNFv1RDDQhjc-7xsaMyb2KNFnhnKWl-5EkyyUF9CmlMgU0mS2mHAjCIYqQc9KgdYSc6tt5Jh0rMXg24BkIGoljm-_VG_DlOaL7ATUSH29g_qzlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PFaWojq7AGpVLONEYRurk-amrOVgepf2xKUWGRnJevmRArti6AhL1LAkSBi_osKuQPVtbrMImXiBKh0noZd5OB2298Zd8_bBXFKnxM07EXMbKkSeOZ3xCHIar8XG-V-LxSLRLiys4gsLsxwV4aBakuy7v36UWwLjva_Bx1qYoTHjaZCLIwNVLi5RcJuz5ZFyWJjHC7HxLgi2ya66_7GXCEKSC-RB54W3ehbKmFgVCbqNWiMuOiykA73-cfsHHeVAHX8ilgHPOb0RlaAjCmBwdioUK6sxiLo5DqauJWeLJBqHfYr8B96XbYu-Ae48KZ3qK48D-thp3v9FM65lCQxwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sO7AIBSZC2vnM2vGx8ESM8-jtd2XTUtEj59Md2oQtQu1xnj7k92BpDzW2YS5noQqTV0yq_Kuk_nR81Kin_RLnFJdkqkj4fip47xwyYoO3eap4UnOaABFuUURWR521D0pacgKRT1bdThFe1WtnWoH95VWZXVB00TTqQ968Jap-zAbhCd9ffa8Ud_cEMP1BE3xrmsNvP2ab6Mgsmu9RY0RpLWqpb3x0Nyj7olR6iN5ei1kcuxQ2Iqy7NaIoodMd6xxBKOexI2d3tI4Fu4TBTlqfiDvfkMJg-pVeGG_0uiL_EHi6RkdEKUwcv8np8o3NMl9ngYKA84kIPHVEwjt4V3jzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P6XD1IYwcMYRlkENxg9NffElfbXH4vh9VhddNjBwNT9JTCfmnNdi53hJ6QqCw1DRfuoduxottqzyQHUW3pZXTAXQ2g67PubK13JTzX0HSfqxk5wAIEJigsLyPcx2t7cMhj7eqpR69XtCwbjvMGdx_DhvXVFTHJhzM_XHkP8pfNVnNcWhEiXMOR4_0BzM7oKJuw9kZNHf7d2Z94-1cHBSinba8zOTN5cPYjCpyDqLkhk_EbioJLCihHvNpR-rGCIM3Xm8jCAzNv6CjrROaK0DjStu7ZmX9aiWQpdF7O0Lwr7r1-az2PeoE4j3AKzOupgl3wTbe8fV4hTqPS1llpt6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jS7T7uaxIxYs4-zIyF8YxGWL9ZOvxpn6b5eD9WZA6vkk2ZtyRfU26ql05ht9huADpJMt6EbOPcYfkq8J_K-x053C1VqJArbqLJbSTrQWR4iy3qMghhYkreU6sK2x0XyLYVpEy1bvKJf2TYeMvu1dp9ERqgCDLdU3K2_uqkgQhXS13wYmGzdqJkAvacyQ8qKaN9ZQuW12urZ1kT32yFi1wg22pJ9rnaFJxqfkHpfM0Un6q5FDFYUEqn6UDdwasf1tOlSoFUvh2HJE38N54jxUpqrsGvu9Xz_8q6qQ2BGaGhAN0mP7yA2ybM2bGI_fzsR5b055HSAI47ce4tLWifckLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uFcAPE7KbWA7_nYMevu5vKw2THaag4m6qAB8PP8g1pA_l5KmtR9CaXbYS8DqnBiasScma9d_HOt1GMC3J7HtG3SuprqeGw37A_9COKXYBmsTCf-OoKxjfgwWZ431oFYUZTU5yYNDblVWtfNyt2lr-Ld3-JRUeXgL0y6smwi-9rwDK7ntyXNadV3jpEQACozXEqk76_pscJ28PmBWxIP9y-5_dD450POECrkJrg0-6kK_VNy6H4aDq5AoZb39mpG3vB52-3ULdRoiffzkJEmrNjVmhu1JGebwAejg5gNNSW0d0M_JOuzURQqzwspWjQiHUuDABaAbsG6oRg1-mwQemA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MU6Ks5zh8qi1k2aEiM5upn_A1YgONBJiPQu9QJCCaeW3sXw9WEMvrxFxyU2OwDHR_rnGrUdIJPerUdCMDFNorEBq6u09NGqPOKvU9nNdlBP0B75smZa56D4O7wdRXCg41ac_VdsPSAp4RCeUZ_xm32wDIMf8Q6TqX-Dp8h4y2QhtWEY5Ib0sSKC5km4O5RCNahyY6jKBe04Qy1jZ9AP0eGpMKFCDzZvgpHYZz9JvJrEbYXuuU-TtbLmAlVc5mdZbV9FVGHW5_65hOlNZIW-vQeznmQnx0ABbhXyh5hj3mBJV9cNDU8MVHdmEtR2I0vBfk6VNkqTKgIfwgpSgIjLdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LbBCA24d4kzFinw7lbMieYAmPXyM8ZgK11TjLEvWijXNmPQSldXT0GfBL31U4h2mUV7aX9UV7d7CHzsqCM7HadX6wlbGeDSQcLTSnOJnO_3sBIFx2yqdwqAHWfEh3tHKYtwd_HfkOPrNJsSLrbB-Iyr61_cVkFSitaCfuto9YtbEneIo5trVld-2NeSRqYP9J_DRXRflXG0cqC-A8gswbfigaxOeKfhsK51tJbeS0y2pGh1sXVpkzO-qjbTf1qg3zXQMnEFycNCFdlFdrYyWLRYePpga6NAAUag05p4MdlcuyTrok0556zXYC0a472eI_59SSa1Yl9427pd5EUl-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6H5a1HjZNVJhuqD3IkZ9HHHJubFjWL4OatJmywC1_nyM0561iWc5vIHyLPkqD37cb8zqxwYKGB5C0YrM-lUShhlTtsRw4n6W9OueAkaOWb-gSI6NFOlWJnlB7PGYRpVgidm5EgXwv_z1E0JgI-NVB71To5hJH-mnog2jShzy-QBNblYSX07UpOVQjj-hiYjpVXf2jPxA1MVNPoV_3flBvslYjedCL5tlwB6ZAw5IcQd-TlkM-gz5LPzFUKtUbtDseMd8WEdse-ncW1Ity_1OvoQyJVQ7p13DRIZL7J9MpxwFoeAhOzIw_7XvZ2IYS_1D_dq7xP49GojM_Ix6O9IgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vRRP3a64DCrlMyj-8TnQjvpOASYoW5UHailSA-28eTdcN1bL1wtU4P4Vi8JAcOP3DeMVOCxDajHLNJ1RvZac9Ix78jAf2pjgAALpqbtGopWgRpxzMUzqsNpbMV6UUjcbZi711niSqzlJK7YubKsTDvNH6ckpos5oWlXcWcvgCdR2UEeAYkJWuoAePrR0IZhD9uy000gIYNxKHinQO1BCihvhNJ2lgL0cw10Dz24uCIu2TYVopJ8QZxEepOVc-kS6BMvFZBbvcRnfrMIjqY2ugtWkCto-2t5yx9ZqYtuZAyD-slNVbjATQN2hPLwkY7pWRtX4P95CYIBi3fQKzepNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4shJFM_7t3R4-6538h87obr1ub2FqoOm8XrSN6OwVwW79rOHrvyJjZIsq1-EfBCmt0br32WSjr-gjjnmUHWKfemWWEIpx95X8tXoeTr1E9UHzkZgCMqRGvp1XYZjbHiYAknaFB_RqRcC7HZRVetytafB2cDxc16idTg1RsF6rk3q1tyMPdARXYpoLIuGEt5GpoVlXWGLo_OHEFGM4XxaZ85_soy9ecsij7uPyfbhZKpzIPg0S8FyldwioDV0YhUSGdujFf_OptTEHyEC1XVm3XBmYHbFyJCdx40YwI8NSxx810ABJQ6o8dMNNi_TNUdyzos10Vi5uPdFLof5yLjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iogBEIYi4jRhOK9BTbz2Er8DzxtgCgkOGuPekkhjbC7LaqrupgEhfBzLcT38gKypa5ltVhfaiy1feFP8hJ5BDCfHrDsJqwdHb0aM-03AlJbee5Lq56_1_Yr3uGPX6TSZRfRXGhD4teQ5A0VijAgJDoukO-EmgDHEkuS5dp16t8HkYHeMj1gIwt5uFtNKrB5Ub9WUHujPxSIQGkwAmM8CnfBbDld2pdnCL_f8y9wgC5GHy8GPpz4k1UTGdUPJDWikEbQnPlyfvniy5RM_6ji9ibZsIhKFcRQYHtf0VYOfWXly-lnIeQp8SSKsht3yUhGSHCuPfMSgmfrp6MwCJfjMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CVNs6e4hcjOXbzcZwSLpot8F2SAcev_-v1cVHe9Ti5jgQbW8Ciw3sUQ30izLD7FBYFdIWdGihdvaqYoZy-Hl94j77gGTxJWPLJNHjw-ReWZpH2s1p9UduTfI3My7unDYyrmdy9Pq6M_gXEMS4DtZD0MZhPzo8FnVpsWK7c6OgE04Jkr_vcvyAdfZLFpXTIQwEEQkn8fxiYW2O0U6OR0CHuxLqCwnJremUDQ5Z00Mb7p7q2VqjJNVqKZomxWuVFClihm504U_E2owri9_c2riHo4Y0Em1wG1PQHDmYDptkZcrZ4wOKo2H3RAfXf63-0LWTLg52M-Uk2s6-B_evp-BDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Srr9Zs4lmKD63gS-gKgajTuvibM9cKovoVBKbsZ8KvQYwZMqq0jyz7ejGkeVsPkuj5pNfSnq7T63Fr2ZS5DaIi98te7qFsnxK7nrw0EpwZtUlDVmsp61PCLw5YvDOCrVvZtoWmxUDomjpYoDiNhBZ3ZYH_w9jpIEMxRcAuOOg3WM_N8q0OF9bx1X_uCByLSC8h6plcv9NDNH6soFsP5pvicjFvL2EdZVBrKbNlS2WvPNmrXs0fYyLKSUHOHXHu61Hnbtqr58JXDDCphD_pbIOPEwehBO9zgROjw7S2wdpJWvWwfS2abJ8F-qmHNf9695YVfmamNW5cVJMBBJOB0nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lRAEIQ9Kzc88t6vqlJva-HjWqdyrfP8qSCXNvPIyz-IQzJqA_JESs9GoiDJ3nq08VQlQR8XQHA6fbQgkwNveN7v_FyMgOm-HdTpknWYNtmA7hZjmHO3O_DP02QMSdlQfAFzMhZFkskP33fVXCXflRCDweabi8VUy8hTQMAxbz57Hqel5bALCPOoWBUj2daaFcx9CtqW5tCMC6xeid13zctrtHJh6Cvbxt_sg2AAMjOv5aBQW_7Ap7ThkMbtHdeHbQle9toLye-goVY27hRGX2XYQe_jjlVAuQpTRAu7G-rnb0E_S7Rw_QEjlNcPmiwnJy_ec29Ofd5uMpl23OIwjbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XnjV9Jk0OhDZ1waBYX790QY4r4xSQXyZcY4YAdtVl7SBO2tjG8mHoaQBNkHqoLyQPIn7kbrKpcByiXUgUsCLs3IekFaNRWZPv0elCZsV5jFgZXpCPfgmzDbnvjzo8N_Bi_p3iXXTLv9COL64W5B5xG2H4oI88baVM7cL8yOh-R852N5_y5AFrQNhsUvk0rQuz9v9NnzyP4UZTjaSDN27ZCvifNDoQKTz1kYVp_-tK9_6NEdccF3r3bPlnOShi08GVtfpqRqQFtsS2lDE5zBI_JimOWpIZN3I5kajE0-iKVkf06BMSFLupsWgErtgdgbPa-VUDnzT1gxEuZMHgeWzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sEKLzGMTkUMn1CCwoB7jGRO3xKKWnm3gLBFJ7vMAmrWLyqYDooDEF9JKLO05D_xW2xh2ix9BMsLd5O2XsVd6sCcz0eIuT7DZlrwyL-u2qtvXQ5zj7ZdnFa-Qr15EV86J0ASgKXvayVGup-L2A862sDt9w2iZ1FPd8DpoD7uV9TfDbnMjf_kVSqt00E5qhyRFmVYfXmmKS--1h1xI2PRq7RCV8YRSVcFKM5fWVburZ2Z8b0nwR5diqNaQU01P9RV8fO3gKsvFkPRTMBhLdLY3sRsaJRmo_Kp4RAVzWJfk6yT_QrLL4KtwHAoA2qfYAoGHqWWnMOiKUqoOFOb2u2RCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکت اندروید F-Droid (که کاربران میتونن بدون وابستگی به گوگل‌پلی، اپلیکیشن‌های آزاد و متن‌باز رو ازش دریافت و نصب کنن) هشدار داده که گوگل قراره از سپتامبر ۲۰۲۶ قوانین جدیدی رو روی اندروید اعمال کنه.
طبق این ادعا، توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.
منتقدان میگن این تغییر میتونه نصب برنامه‌های مستقل، پروژه‌های متن‌باز، نرم‌افزارهای شخصی و حتی برنامه‌هایی که خارج از گوگل‌پلی منتشر میشن رو با محدودیت جدی روبرو کنه. به همین دلیل F-Droid و برخی فعالان حوزه آزادی نرم‌افزار معتقدن اندروید بتدریج از یک پلتفرم باز فاصله میگیره و کنترل بیشتری روی اینکه چه نرم‌افزاری روی گوشی کاربران نصب بشه، در اختیار گوگل قرار میگیره. به همین خاطر کمپینی با عنوان Keep Android Open راه افتاده تا کاربران و توسعه‌دهندگان نسبت به این تغییرات آگاه بشن و به اون اعتراض کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2452" target="_blank">📅 08:48 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
